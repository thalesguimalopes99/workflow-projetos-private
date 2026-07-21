# -*- coding: utf-8 -*-
"""
batch_download.py — downloader em lote reusável do curso-ripper.

Lê um manifest.json e baixa cada aula, escolhendo a receita pelo campo `source_type`.
Generaliza os dois casos já feitos (HTClube = MP4/áudio; Supabase = Panda HLS).
Rode assim:  set PYTHONIOENCODING=utf-8 && py batch_download.py

O manifesto é um JSON: {"items": [ ... ]}, cada item:
  {
    "source_type": "hls" | "mp4" | "audio",   # hls=yt-dlp; mp4=vídeo direto; audio=extrai áudio
    "url":      "<URL do vídeo (m3u8 ou mp4)>",
    "dir":      "Módulo/Seção",                # relativo a DEST; espelha o curso
    "filename": "01 - Nome da aula",           # SEM extensão
    "extras":   [{"title":"slides.pptx","url":"https://..."}]  # opcional (materiais)
  }
Monte o manifesto na fase de enumeração (browser_evaluate no playwright) — ver SKILL.md.
"""
import json, subprocess, time, urllib.request, shutil, uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ============================ CONFIG (ajuste por curso) ============================
MANIFEST = Path(__file__).with_name("manifest.json")
DEST     = Path(r"C:\Users\Thales Lopes\Documents\Cursos\CursoX")   # <-- ajustar por curso
FFMPEG   = "ffmpeg"   # está no PATH nesta máquina (winget Gyan.FFmpeg v8.1)
# Dir CURTO p/ os fragmentos temporários do yt-dlp (evita estourar MAX_PATH 260 do Windows):
TMP      = Path(r"C:\Users\Thales Lopes\AppData\Local\Temp\crip")
# Header exigido por alguns players (Panda: o Referer do player). Vazio = não manda.
REFERER  = ""   # ex: "Referer:https://player-vz-5d8b4169-07f.tv.pandavideo.com.br/"
WORKERS  = 4
# ==================================================================================

LOG = Path(__file__).with_name("batch_download.log")
TMP.mkdir(parents=True, exist_ok=True)
items = json.loads(MANIFEST.read_text(encoding="utf-8"))["items"]

def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def fetch_extras(d, extras):
    for c in (extras or []):
        out = d / c["title"]
        if out.exists() and out.stat().st_size > 5000:
            continue
        try:
            req = urllib.request.Request(c["url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
                f.write(r.read())
        except Exception as e:
            log(f"  EXTRA-FAIL: {out.name} :: {str(e)[:150]}")

def run_hls(url, out):
    """HLS (Panda/genérico) via yt-dlp. Baixa num path CURTO (TMP) e MOVE pro
    destino. Motivo: `-P temp:` NÃO protege os fragmentos `.mp4.part-FragN.part`
    em caminhos de 4 níveis (trilha/módulo/seção/aula) — eles estouram o MAX_PATH
    260 do Windows e o vídeo sai vazio. Baixar curto + mover é o robusto."""
    short = TMP / ("dl_" + uuid.uuid4().hex[:12] + ".mp4")
    tmpl = str(short.with_suffix("")) + ".%(ext)s"
    cmd = ["py", "-m", "yt_dlp", "--no-warnings", "--no-progress",
           "--retries", "5", "--fragment-retries", "10",
           "-f", "b[height<=1080]/bv*+ba/b", "--merge-output-format", "mp4",
           "-o", tmpl, url]
    if REFERER:
        cmd[4:4] = ["--add-header", REFERER]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if short.exists() and short.stat().st_size > 1_000_000:
        shutil.move(str(short), str(out))   # destino ≤259 é OK criar; só os fragmentos estouravam
    return p

def run_mp4(url, out):
    """MP4 direto (ex: Google Storage) — remux sem re-encode."""
    return subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                           "-i", url, "-c", "copy", str(out)], capture_output=True, text=True)

def run_audio(url, out):
    """Extrai só o áudio (stream-copy AAC; fallback re-encode)."""
    for a in (["-vn", "-c:a", "copy"], ["-vn", "-c:a", "aac", "-b:a", "128k"]):
        p = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                            "-i", url, *a, str(out)], capture_output=True, text=True)
        if out.exists() and out.stat().st_size > 100_000:
            return p
    return p

EXT   = {"hls": ".mp4", "mp4": ".mp4", "audio": ".m4a"}
RUN   = {"hls": run_hls, "mp4": run_mp4, "audio": run_audio}
FLOOR = {"hls": 1_000_000, "mp4": 1_000_000, "audio": 100_000}  # tamanho mínimo p/ considerar OK

def work(e):
    st = e["source_type"]
    d = DEST / e["dir"]
    d.mkdir(parents=True, exist_ok=True)
    fetch_extras(d, e.get("extras"))
    out = d / (e["filename"] + EXT[st])
    name = e["dir"] + "/" + e["filename"]
    if out.exists() and out.stat().st_size > FLOOR[st]:
        return ("skip", name)
    p = RUN[st](e["url"], out)
    if out.exists() and out.stat().st_size > FLOOR[st]:
        return ("ok", name)
    return ("FAIL", name + " :: " + (p.stderr or "")[-250:])

open(LOG, "w", encoding="utf-8").close()
total = len(items); done = ok = skip = fail = 0
log(f"START {total} @ {time.strftime('%H:%M:%S')}")
with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    futs = {ex.submit(work, e): e for e in items}
    for fut in as_completed(futs):
        stt, name = fut.result(); done += 1
        if stt == "ok": ok += 1
        elif stt == "skip": skip += 1
        else: fail += 1; log(f"  {stt}: {name}")
        if done % 3 == 0 or done == total:
            log(f"PROGRESS {done}/{total}  ok={ok} skip={skip} fail={fail}  @ {time.strftime('%H:%M:%S')}")
msg = f"DONE ok={ok} skip={skip} fail={fail} / {total} @ {time.strftime('%H:%M:%S')}"
log(msg); print(msg)
