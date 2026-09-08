#!/usr/bin/env python3
"""vtt2ts.py — converte legenda .vtt (YouTube auto/manual) em texto limpo COM marcadores de tempo.

Diferente do vtt2txt.py (skill pica), preserva rastreabilidade: cada bloco de ~N segundos
recebe um marcador [mm:ss] pra que teses extraídas apontem pro momento exato do vídeo.

Uso:
    python vtt2ts.py <arquivo.vtt> [--chunk 30] [--out <arquivo.txt>]
    python vtt2ts.py <pasta/>     # converte todos os .vtt da pasta

Saída: <mesmo-nome>.txt ao lado do .vtt (ou --out). Imprime o caminho gerado.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

TAG_RE = re.compile(r"<[^>]+>")
TS_RE = re.compile(r"(\d+):(\d\d):(\d\d)\.(\d\d\d)\s+-->\s+(\d+):(\d\d):(\d\d)\.(\d\d\d)")


def _secs(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_vtt(path: Path):
    """Retorna lista de (start_seconds, texto) já deduplicada (ASR do YouTube repete linhas)."""
    cues = []
    start = None
    buf = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        m = TS_RE.search(line)
        if m:
            if start is not None and buf:
                cues.append((start, buf))
            start = _secs(*m.groups()[:4])
            buf = []
            continue
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if start is None:
            continue
        text = html.unescape(TAG_RE.sub("", line)).replace("\xa0", " ")
        # ">>" = troca de falante no ASR do YouTube → marcador legível
        text = text.replace(">>", " ¶ ").strip()
        if text:
            buf.append(text)
    if start is not None and buf:
        cues.append((start, buf))

    out = []
    last = None
    for st, lines in cues:
        for t in lines:
            if t == last:
                continue
            out.append((st, t))
            last = t
    return out


def fmt(sec: float) -> str:
    sec = int(sec)
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def header_for(vtt: Path) -> str:
    """Cabeçalho com metadata do .info.json se existir ao lado."""
    stem = vtt.name.split(".")[0]
    info = vtt.with_name(f"{stem}.info.json")
    if not info.exists():
        return f"# {stem}\n\n"
    try:
        d = json.loads(info.read_text(encoding="utf-8"))
    except Exception:
        return f"# {stem}\n\n"
    dur = d.get("duration") or 0
    return (
        f"# {d.get('title', stem)}\n"
        f"video_id: {d.get('id', stem)}\n"
        f"url: https://youtu.be/{d.get('id', stem)}\n"
        f"upload_date: {d.get('upload_date', 'NA')}\n"
        f"duration: {fmt(dur)}\n"
        f"views: {d.get('view_count', 'NA')}\n\n"
    )


def convert(vtt: Path, chunk: int, out: Path | None = None) -> Path:
    items = parse_vtt(vtt)
    lines = [header_for(vtt)]
    bucket_start = None
    bucket = []
    for st, t in items:
        if bucket_start is None:
            bucket_start = st
        if st - bucket_start >= chunk and bucket:
            lines.append(f"[{fmt(bucket_start)}] " + " ".join(bucket))
            bucket_start = st
            bucket = []
        bucket.append(t)
    if bucket:
        lines.append(f"[{fmt(bucket_start)}] " + " ".join(bucket))
    stem = vtt.name.split(".")[0]
    target = out or vtt.with_name(f"{stem}.txt")
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--chunk", type=int, default=30, help="segundos por marcador de tempo")
    ap.add_argument("--out")
    a = ap.parse_args()
    p = Path(a.path)
    if p.is_dir():
        n = 0
        for vtt in sorted(p.glob("*.vtt")):
            convert(vtt, a.chunk)
            n += 1
        print(f"convertidos: {n}")
    else:
        print(convert(p, a.chunk, Path(a.out) if a.out else None))


if __name__ == "__main__":
    sys.exit(main())
