#!/usr/bin/env python3
"""extract_sections.py — concatena UMA seção de todas as fichas em references/videos/ num arquivo só.

Serve pra síntese: um agente lê só "Teses" de 86 vídeos (≈40k palavras) em vez das fichas inteiras (≈200k).

Uso:
    python extract_sections.py <out_dir>            # gera um .md por seção conhecida
    python extract_sections.py <out_dir> Teses Voz  # só essas seções
"""
import re
import sys
import unicodedata
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
VIDEOS = SKILL / "references" / "videos"
SECTIONS = [
    "Resumo", "Teses", "Frameworks / métodos", "Histórias / casos", "Números / claims",
    "Posições", "Voz", "Cacoetes observados", "Perguntas que ele faria", "Conexões",
]


def split_sections(text: str):
    parts = re.split(r"^## +", text, flags=re.M)
    head = parts[0]
    out = {}
    for p in parts[1:]:
        name, _, body = p.partition("\n")
        out[name.strip()] = body.strip()
    return head, out


def main():
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    wanted = sys.argv[2:] or SECTIONS
    files = sorted(VIDEOS.glob("*.md"))
    for sec in wanted:
        chunks = []
        for f in files:
            head, secs = split_sections(f.read_text(encoding="utf-8"))
            title = head.splitlines()[0].lstrip("# ").strip() if head else f.stem
            meta = next((l for l in head.splitlines() if "video_id" in l), "")
            fmt = next((l for l in head.splitlines() if l.startswith("formato:")), "")
            body = next((v for k, v in secs.items() if k.lower().startswith(sec.lower().split(" ")[0])), "")
            if not body or body == "—":
                continue
            chunks.append(f"### {f.stem} — {title}\n{meta}\n{fmt}\n\n{body}\n")
        ascii_sec = unicodedata.normalize("NFKD", sec).encode("ascii", "ignore").decode()
        slug = re.sub(r"[^a-z0-9]+", "-", ascii_sec.lower()).strip("-")
        target = out_dir / f"{slug}.md"
        target.write_text(f"# Seção «{sec}» de {len(chunks)} fichas\n\n" + "\n".join(chunks), encoding="utf-8")
        print(f"{target.name}: {len(chunks)} fichas, {sum(len(c.split()) for c in chunks)} palavras")


if __name__ == "__main__":
    main()
