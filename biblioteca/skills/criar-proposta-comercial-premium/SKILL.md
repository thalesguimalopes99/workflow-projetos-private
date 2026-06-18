---
name: criar-proposta-comercial-premium
description: Use quando o Thales quer ofertar/vender serviços a um cliente e precisa de uma proposta comercial premium que FECHA high-ticket. Gatilhos "criar proposta comercial", "proposta pra cliente", "ofertar meus serviços", "deck de venda", "proposta high-ticket", "/proposta". Também ativa pelo roteamento da skill workflow quando o entregável é proposta de venda. Produz PPTX editável + PDF desenhado + pitch-kit (talking points, objeções, follow-up). NÃO use para brand book, site, conteúdo de IG ou campanha de tráfego — há pipelines próprios.
---

# criar-proposta-comercial-premium

Pipeline de 7 fases. Regra-mãe: o valor está nas fases 0-3 (estratégia, copy, ROI). O Gamma só renderiza. Nada de proposta genérica — se o quality gate < 9, refatora.

## Fase 0 — Brief + Discovery
Coletar inputs core. Se faltar algum, BLOQUEAR e oferecer minerar o prospect.
→ ver `references/discovery-qualificacao.md`. Use a skill `briefing` (lente venda/oferta).

## Fase 1 — Análise estratégica
Convocar especialistas (escala com o tier do deal):
- `hormozi-offers` + `hormozi-pricing` → oferta + modelo de preço (ver `references/modelos-preco.md`)
- `copy-master:copy-chief` → ângulo de copy
- `advisory-board` → só se high-ticket / decisão estratégica
- pesquisa de mercado do nicho (inline via firecrawl até a skill `pesquisa-mercado` existir)
Definir: ângulo, modelo de preço, custo de não-agir + ROI (ver `references/roi-custo-inacao.md`), "por que agora", objeções.

## Fase 2 — Minerar
(a) O PRÓPRIO prospect: site, números públicos, concorrentes, linguagem (firecrawl, `site-teardown`).
(b) Decks/propostas que fecham high-ticket.
→ ver `references/fontes-mineracao.md`.

## Fase 3 — Direção
Montar a narrativa nas 11 seções com COPY FINAL (não rascunho): diagnóstico→custo→mecanismo→oferta→prova→preço/ROI→por que agora→CTA. Gerar 2-3 ângulos, escolher 1.
→ ver `references/anatomia-proposta.md`. Use `storytelling:story-chief` + `copy-master`.

## Fase 4 — Build
1. Salvar a copy final das 11 seções em `outline.md`.
2. Rodar `scripts/gamma-generate.mjs` com `--textMode preserve` e o tema da marca do Thales.
3. Exportar `.pptx` (fonte) e derivar `.pdf`. → ver `references/build-gamma.md`.
4. Aplicar identidade do Thales → ver `references/marca-thales.md`.
5. Gerar `pitch-kit.md` → ver `references/pitch-kit-followup.md` (usa `copy-squad`).
Fallback se Gamma falhar/quota → `references/build-fallback-pptx.md`.

## Fase 5 — Quality gate
Rodar o checklist "fecharia?" (`references/quality-gate.md`). Score < 9 em qualquer item → refatora a fase responsável e re-renderiza.

## Fase 6 — Ship
Salvar `proposta.pptx` + `proposta.pdf` + `pitch-kit.md` na pasta do PROJETO ATIVO do cliente (NUNCA na biblioteca). Entregar resumo + próximos passos.
