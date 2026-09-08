"""Converte legenda .vtt (yt-dlp) em texto puro, sem timestamps e sem duplicatas.

Uso:
    py vtt2txt.py legenda.vtt              # escreve legenda.txt ao lado
    py vtt2txt.py legenda.vtt saida.txt    # destino explícito

Lida com os dois formatos do YouTube:
- legendas manuais (cues simples)
- legendas automáticas/ASR (tags inline <c>/<00:00:01.234> e janela rolante
  que repete cada linha em cues consecutivos)
"""
import html
import re
import sys
from pathlib import Path

TAG_RE = re.compile(r"<[^>]+>")
HEADER_PREFIXES = ("WEBVTT", "Kind:", "Language:", "NOTE", "STYLE", "REGION")


def vtt_to_text(vtt: str) -> str:
    lines: list[str] = []
    for raw in vtt.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith(HEADER_PREFIXES):
            continue
        if "-->" in line:
            continue
        if line.isdigit():  # número de cue
            continue
        line = html.unescape(TAG_RE.sub("", line)).strip()
        if not line:
            continue
        if lines and lines[-1] == line:  # janela rolante do ASR
            continue
        lines.append(line)
    return "\n".join(lines) + "\n"


def main() -> int:
    # console Windows (cp1252) quebra com fullwidth chars que o yt-dlp usa
    # ao sanitizar nomes de arquivo (? -> U+FF1F etc.)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1])
    if not src.exists():
        print(f"arquivo nao encontrado: {src}")
        return 1
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".txt")
    text = vtt_to_text(src.read_text(encoding="utf-8"))
    dst.write_text(text, encoding="utf-8")
    print(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
