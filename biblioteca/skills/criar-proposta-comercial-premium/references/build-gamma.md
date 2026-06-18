# Build via Gamma (Fase 4)

Pré: `GAMMA_API_KEY` no ambiente. Copy final das 11 seções salva em `outline.md`
(markdown: um H1 de tese + um H2 por seção com a copy pronta).

## Passos
1. Gerar o PPTX (fonte editável):
   `node scripts/gamma-generate.mjs --input outline.md --export pptx --out <projeto>/proposta.pptx --textMode preserve --numCards 11 --theme "<tema do Thales>"`
2. Derivar o PDF mantendo o MESMO deck:
   - Se LibreOffice instalado: `soffice --headless --convert-to pdf --outdir <projeto> <projeto>/proposta.pptx`
   - Senão: 2ª chamada do helper com `--export pdf` (aceitar leve variação visual).
3. Guardar `gammaUrl` e `gammaId` (log) para editar/arquivar depois.

## Regras
- SEMPRE `--textMode preserve` — Gamma diagrama, não reescreve nossa copy.
- `numCards` ≈ nº de seções (11). Ajustar se alguma seção virar 2 cards.
- Erro/timeout/quota → seguir `build-fallback-pptx.md`.
