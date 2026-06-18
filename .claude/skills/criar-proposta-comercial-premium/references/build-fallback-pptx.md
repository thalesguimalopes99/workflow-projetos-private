# Build fallback (sem Gamma)

Quando: API fora, `failed`, timeout, ou quota estourada.

## Passos
1. Usar a skill `pptx` para montar o deck com as 11 seções (copy já pronta).
2. Aplicar a marca do Thales via skill `design` (cores/tipo/logo de `marca-thales.md`).
3. Exportar PDF: skill `pdf` (ou `soffice --headless --convert-to pdf`).
4. Mesmo quality gate (`quality-gate.md`).

## Regra
Fallback não pode travar a entrega: se Gamma falhar, avisar o Thales e seguir por aqui.
