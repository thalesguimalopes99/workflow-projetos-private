#!/usr/bin/env python3
"""build_index.py — gera references/indice-videos.md a partir das fichas em references/videos/.

Lê de cada ficha: título (linha 1), video_id/data/duração/views (linha 2), formato, tema.
Saída: tabela cronológica + agrupamento por formato. Rodar depois de destilar vídeos novos.
"""
import re
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
VIDEOS = SKILL / "references" / "videos"
OUT = SKILL / "references" / "indice-videos.md"


def parse(p: Path):
    lines = p.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip() if lines else p.stem
    meta = " ".join(lines[1:6])
    g = lambda k: (re.search(rf"{k}:\s*([^·\n]+)", meta) or [None, ""])[1].strip()
    fmt = next((l.split(":", 1)[1].strip() for l in lines[:12] if l.startswith("formato:")), "")
    tema = next((l.split(":", 1)[1].strip() for l in lines[:12] if l.startswith("tema:")), "")
    return {
        "id": p.stem, "title": title, "date": g("data"), "dur": g("duração"),
        "views": g("views").replace(".", "").replace(",", ""), "fmt": fmt, "tema": tema,
    }


def main():
    rows = [parse(p) for p in sorted(VIDEOS.glob("*.md"))]
    rows.sort(key=lambda r: r["date"], reverse=True)
    out = [
        "# Índice de vídeos — Alfredo Soares",
        f"_{len(rows)} fichas em `references/videos/<id>.md`. Cada ficha tem teses, frameworks, histórias, posições e voz com timestamps. Gerado por `scripts/build_index.py`._",
        "",
        "Como usar: ache o tema na coluna **tema**, abra a ficha do id, cite como `[<id> @ mm:ss]`.",
        "",
        "| data | id | título | formato | tema | dur | views |",
        "|---|---|---|---|---|---|---|",
    ]
    cut = lambda s, n: (s[: n - 1] + "…") if len(s) > n else s
    for r in rows:
        r["fmt"], r["tema"] = cut(r["fmt"], 70), cut(r["tema"], 140)
        out.append(f"| {r['date']} | `{r['id']}` | {r['title']} | {r['fmt']} | {r['tema']} | {r['dur']} | {r['views']} |")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{OUT} <- {len(rows)} videos")


if __name__ == "__main__":
    main()
