#!/usr/bin/env python3
"""update.py -- pipeline de atualizacao da base do mentor Alfredo Soares.

Baixa legendas PT (auto) + metadata dos vídeos NOVOS do canal (ou de uma URL avulsa),
converte pra texto com timestamps e lista o que falta destilar em references/videos/.

"Novo" e decidido por presenca de arquivo, nao por --download-archive: um id conta como
baixado quando existe <id>.info.json E <id>.pt-orig.vtt em raw/<sub>/. Um .info.json sem
.vtt correspondente (download parcial anterior) conta como pendente e e retentado.
A enumeracao dos ids do canal vem de check_new.list_channel_ids() -- nao duplicada aqui.

Uso:
    python update.py                     # so os ids novos da aba /videos
    python update.py <url-do-video>      # 1 vídeo avulso (ex.: aparicao em outro canal -> raw/extra)
    python update.py --shorts            # inclui a aba de shorts (so voz)
    python update.py --status            # so mostra o que esta baixado vs. destilado
    python update.py --retentar-falhos   # limpa raw/no-captions.json e retenta os desistidos

Id que falha 3x entra em raw/no-captions.json e sai da fila (tipicamente vídeo sem legenda
PT no YouTube). Sem isso a tarefa semanal retentaria os mesmos ids pra sempre.

Sempre enumera os ids do canal (--flat-playlist, chamada barata). So invoca o yt-dlp de
download de legenda quando ha id faltando; se nao houver id novo em nenhuma aba checada,
imprime "nada novo" e sai sem baixar nada.

Depois de rodar, destile cada .txt novo com o prompt em scripts/prompt-extracao.md
(1 subagent por lote de ~6 vídeos) e atualize references/indice-videos.md + os arquivos de síntese.

Requisitos: python -m yt_dlp (com --js-runtimes node --remote-components ejs:github), Node.
Dados brutos ficam FORA da skill: RAW_DIR (ver check_new.py).

Rodado sozinho toda semana pela tarefa agendada do Windows "AlfredoSoaresCaptions" via
scripts/baixar-legendas.cmd (raw/../scripts, fora da skill) -- log em raw/../logs/agendado.log.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_new  # noqa: E402  (mesma pasta; reaproveita list_channel_ids em vez de duplicar)

SKILL_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = check_new.RAW_DIR
VIDEOS_REF = SKILL_DIR / "references" / "videos"
VTT2TS = SKILL_DIR / "scripts" / "vtt2ts.py"

YTDLP = check_new.YTDLP
SUB_ARGS = [
    "--skip-download", "--write-auto-subs", "--write-subs", "--sub-langs", "pt-orig",
    "--sub-format", "vtt", "--sleep-subtitles", "3", "--write-info-json",
    "--no-write-playlist-metafiles", "--ignore-errors",
]


def run(cmd, log):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    with open(log, "a", encoding="utf-8") as f:
        return subprocess.call(cmd, stdout=f, stderr=subprocess.STDOUT, env=env)


SKIP_FILE = "no-captions.json"
MAX_TRIES = 3


def load_skips() -> dict:
    """Ids que falharam repetidamente (tipicamente vídeo sem legenda PT no YouTube).

    Sem isso, um id sem legenda fica pendente pra sempre e a tarefa agendada semanal
    retenta ele toda semana, de graca. Depois de MAX_TRIES tentativas o id sai da fila.
    """
    p = RAW_DIR / SKIP_FILE
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_skips(data: dict):
    (RAW_DIR / SKIP_FILE).write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")


def bump_skips(sub: str, failed: list[str]):
    data = load_skips()
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for i in failed:
        e = data.setdefault(i, {"tab": sub, "tentativas": 0, "primeira": now})
        e["tentativas"] += 1
        e["ultima"] = now
    save_skips(data)
    done = [i for i in failed if data[i]["tentativas"] >= MAX_TRIES]
    if done:
        print(f"[{sub}] desistindo apos {MAX_TRIES} tentativas (provavel sem legenda PT): " + ",".join(done))


def skipped_ids() -> set[str]:
    return {i for i, e in load_skips().items() if e.get("tentativas", 0) >= MAX_TRIES}


def have_captions(sub: str) -> set[str]:
    """Ids com legenda de fato completa (info.json + vtt) em raw/<sub>/."""
    folder = RAW_DIR / sub
    if not folder.exists():
        return set()
    info_ids = {p.name.split(".")[0] for p in folder.glob("*.info.json")}
    vtt_ids = {p.name.split(".")[0] for p in folder.glob("*.vtt")}
    return info_ids & vtt_ids


def fetch_new(tab: str, out_sub: str, ids: list[str]):
    """Baixa legenda so dos ids novos, passando URLs explicitas (nao a URL do canal inteiro)."""
    out = RAW_DIR / out_sub
    out.mkdir(parents=True, exist_ok=True)
    urls = [f"https://youtu.be/{i}" for i in ids]
    cmd = YTDLP + SUB_ARGS + ["-o", str(out / "%(id)s.%(ext)s")] + urls
    code = run(cmd, RAW_DIR.parent / "logs" / f"update-{out_sub}.log")
    done = have_captions(out_sub)
    ok = [i for i in ids if i in done]
    failed = [i for i in ids if i not in done]
    print(f"[{out_sub}] yt-dlp exit={code} pedidos={len(ids)} ok={len(ok)} falharam={len(failed)}")
    if failed:
        print(f"[{out_sub}] falharam (retentado na proxima execucao): " + ",".join(failed))
    return code, failed


def fetch_one(url: str):
    out = RAW_DIR / "extra"
    out.mkdir(parents=True, exist_ok=True)
    cmd = YTDLP + SUB_ARGS + ["-o", str(out / "%(id)s.%(ext)s"), url]
    code = run(cmd, RAW_DIR.parent / "logs" / "update-extra.log")
    print(f"[extra] yt-dlp exit={code}")
    return out


def convert(folder: Path):
    n = 0
    for vtt in folder.glob("*.vtt"):
        stem = vtt.name.split(".")[0]
        txt = folder / f"{stem}.txt"
        if txt.exists() and txt.stat().st_mtime >= vtt.stat().st_mtime:
            continue
        subprocess.call([sys.executable, str(VTT2TS), str(vtt)], stdout=subprocess.DEVNULL)
        n += 1
    print(f"[{folder.name}] convertidos: {n}")


def status():
    done = {p.stem for p in VIDEOS_REF.glob("*.md")} if VIDEOS_REF.exists() else set()
    for sub in ("long", "extra"):
        folder = RAW_DIR / sub
        if not folder.exists():
            continue
        ids = sorted({p.name.split(".")[0] for p in folder.glob("*.txt")})
        missing = [i for i in ids if i not in done]
        print(f"[{sub}] baixados={len(ids)} destilados={len(ids) - len(missing)} faltam={len(missing)}")
        for i in missing:
            print(f"   - {folder / (i + '.txt')}")
    shorts = RAW_DIR / "shorts"
    if shorts.exists():
        print(f"[shorts] txt={len(list(shorts.glob('*.txt')))} (so alimentam references/voz.md)")
    skips = load_skips()
    if skips:
        desistidos = [i for i, e in skips.items() if e.get("tentativas", 0) >= MAX_TRIES]
        print(f"[falhos] em observacao={len(skips) - len(desistidos)} desistidos={len(desistidos)}"
              " (--retentar-falhos pra voltar pra fila)")


def sync_tab(tab: str, out_sub: str) -> tuple[list[str], bool]:
    """Retorna (ids_baixados_com_sucesso, houve_erro_de_listagem)."""
    try:
        remote = check_new.list_channel_ids(tab)
    except RuntimeError as e:
        print(f"[{out_sub}] erro ao listar canal: {e}")
        return [], True
    ignorar = have_captions(out_sub) | skipped_ids()
    todo = [i for i in remote if i not in ignorar]
    if not todo:
        print(f"[{out_sub}] nada novo")
        return [], False
    _code, failed = fetch_new(tab, out_sub, todo)
    if failed:
        bump_skips(out_sub, failed)
    convert(RAW_DIR / out_sub)
    return [i for i in todo if i not in failed], False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", nargs="?")
    ap.add_argument("--shorts", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--retentar-falhos", dest="retentar", action="store_true")
    a = ap.parse_args()
    (RAW_DIR.parent / "logs").mkdir(parents=True, exist_ok=True)

    if a.retentar:
        n = len(load_skips())
        save_skips({})
        print(f"fila de falhos limpa ({n} ids voltam pra fila)")

    if a.status:
        return status()

    if a.url:
        convert(fetch_one(a.url))
        return status()

    tabs = [("videos", "long")]
    if a.shorts:
        tabs.append(("shorts", "shorts"))

    any_downloaded = False
    any_error = False
    for tab, out_sub in tabs:
        got, err = sync_tab(tab, out_sub)
        any_downloaded = any_downloaded or bool(got)
        any_error = any_error or err

    if not any_downloaded and not any_error:
        print("nada novo")

    status()
    if any_downloaded:
        print("\nProximo passo: destilar os .txt novos com scripts/prompt-extracao.md -> references/videos/<id>.md")


if __name__ == "__main__":
    main()
