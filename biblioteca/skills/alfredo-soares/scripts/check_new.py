#!/usr/bin/env python3
"""check_new.py -- checagem barata (sem baixar legenda) de quantos videos novos existem no canal.

Roda "yt-dlp --flat-playlist" (so enumera ids, nao baixa nada) e compara com os ids ja
presentes em raw/long/*.info.json (e raw/shorts/*.info.json quando --shorts). Grava
raw/last-check.json com timestamp ISO + resultado, pra a skill saber quando foi a ultima
checagem e nao checar duas vezes no mesmo dia.

Uso:
    python check_new.py              # checa a aba /videos
    python check_new.py --shorts     # inclui a aba /shorts tambem
    python check_new.py --json       # saida em JSON em vez de linha unica

Saida (stdout, sempre uma linha se nao for --json):
    novos=3 ids=abc,def,ghi
    novos=0
    novos=? erro=<msg curta>          (rede fora -- nunca falha a sessao; exit sempre 0)

update.py importa list_channel_ids() daqui em vez de duplicar a logica de enumeracao.
Requisitos: python -m yt_dlp (com --js-runtimes node --remote-components ejs:github).
Dados brutos ficam FORA da skill: RAW_DIR abaixo.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAW_DIR = Path(os.environ.get("ALFREDO_RAW_DIR", Path.home() / "Documents/wtf/mentor-alfredo-soares/raw"))
CHANNEL = "https://www.youtube.com/@canaldoalfredosoares"
YTDLP = [sys.executable, "-m", "yt_dlp", "--js-runtimes", "node", "--remote-components", "ejs:github"]
LAST_CHECK = RAW_DIR / "last-check.json"


def existing_ids(sub: str) -> set[str]:
    """Ids ja conhecidos em raw/<sub>/, pela presenca de <id>.info.json."""
    folder = RAW_DIR / sub
    if not folder.exists():
        return set()
    return {p.name.split(".")[0] for p in folder.glob("*.info.json")}


def list_channel_ids(tab: str = "videos", timeout: int = 60) -> list[str]:
    """Enumera ids do canal via --flat-playlist (rapido, nao baixa nada).

    Lanca RuntimeError com mensagem curta em caso de falha (rede, extrator, timeout).
    Reaproveitada por update.py -- nao duplicar essa logica la.
    """
    cmd = YTDLP + ["--flat-playlist", "--print", "%(id)s", f"{CHANNEL}/{tab}"]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        r = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", env=env, timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        raise RuntimeError(f"timeout apos {timeout}s") from e
    except OSError as e:
        raise RuntimeError(str(e)) from e
    ids = [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
    if not ids and r.returncode != 0:
        last = (r.stderr.strip().splitlines() or ["yt-dlp falhou sem stderr"])[-1]
        raise RuntimeError(last[:120])
    return ids


def check(shorts: bool = False) -> dict:
    """Roda a checagem completa. Nunca lanca -- falha vira campo 'erro' no dict."""
    try:
        remote = list(dict.fromkeys(list_channel_ids("videos")))
        have = existing_ids("long")
        if shorts:
            remote += [i for i in list_channel_ids("shorts") if i not in remote]
            have = have | existing_ids("shorts")
        novos = [i for i in remote if i not in have]
        return {
            "ok": True, "novos": len(novos), "ids": novos,
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }
    except RuntimeError as e:
        return {"ok": False, "erro": str(e), "checked_at": datetime.now(timezone.utc).isoformat()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shorts", action="store_true", help="inclui a aba /shorts na checagem")
    ap.add_argument("--json", action="store_true", help="saida em JSON em vez de linha unica")
    a = ap.parse_args()

    result = check(shorts=a.shorts)

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    LAST_CHECK.write_text(json.dumps(result, ensure_ascii=True, indent=2), encoding="utf-8")

    if a.json:
        print(json.dumps(result, ensure_ascii=True))
    elif result["ok"]:
        if result["novos"]:
            print(f"novos={result['novos']} ids=" + ",".join(result["ids"]))
        else:
            print("novos=0")
    else:
        print(f"novos=? erro={result['erro']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
