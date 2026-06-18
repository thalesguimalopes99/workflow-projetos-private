# Marca do Thales → tema do Gamma

Objetivo: o deck sai com a identidade do Thales, não "premium genérico".

## Onde estão os tokens
Procurar em `biblioteca/config/` por um arquivo de marca do Thales (cores, tipografia, logo, voz).
- Existe → usar como `--theme` (tema custom do Gamma) e na camada visual.
- NÃO existe → mini-intake na 1ª run: perguntar cor primária, tipografia, logo, tom de voz;
  salvar em `biblioteca/config/marca-thales.json` para reuso (não re-perguntar depois).

## Mapear para o Gamma
- Criar/selecionar um tema no Gamma com as cores/fontes do Thales; passar `--theme "<nome>"`.
- Logo: inserir na capa e rodapé.
- Voz: refletida na copy (Fases 0-3), não no tema.

## Fallback (sem Gamma)
Aplicar os mesmos tokens via skills `design`/`pptx`.
