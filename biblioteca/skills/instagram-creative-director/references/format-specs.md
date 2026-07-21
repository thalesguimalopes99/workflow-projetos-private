# Specs de formato, pipeline de produção e brief de entrega

## Dimensões e safe zones

| Formato | Dimensão (px) | Proporção | Observações |
|---|---|---|---|
| Feed quadrado | 1080×1080 | 1:1 | Seguro, mas ocupa menos tela |
| Feed retrato | 1080×1350 | 4:5 | **Preferido** — mais tela no scroll |
| Story / Reel | 1080×1920 | 9:16 | Pleno-tela vertical |
| Capa de Reel | 1080×1920 | 9:16 | No grid aparece recortado ~1:1 central |

**Safe zones (Story / Reel 9:16):** a UI do Instagram cobre topo e base. Mantenha texto
e elementos críticos na **faixa central segura**: ~250px do topo e ~320px da base livres
de conteúdo essencial (avatar/nome no topo; legenda, CTA do sistema, barra de progresso
na base). CTA e stickers interativos perto do centro-baixo, fora da zona de corte.

**Capa de Reel:** o thumbnail no grid recorta pra ~1:1 centralizado. Garanta que o hook
visual e o texto-chave sobrevivam a esse recorte — não jogue texto importante nas bordas
verticais.

## Pipeline de produção (quando renderizar)

Ferramentas primárias de imagem do projeto: **Higgsfield + Canva** (ver memória).
Escolha o caminho pela natureza do trabalho — não por hábito.

### Caminho A — Higgsfield → Canva (peça social pronta, on-brand)
1. **Higgsfield** (`mcp__higgsfield__*`): gere/ajuste o visual base.
   - `generate_image` (dirija o prompt: luz, lente, mood, composição — específico)
   - `upscale_image`, `remove_background`, `outpaint_image` / `reframe` (ajuste de proporção)
   - Local: `media_upload_widget`. URL web: `media_import_url` → use o `media_id`
     retornado (nunca a URL crua).
2. **Canva** (`mcp__canva__*`): componha tipografia + copy sobre o visual.
   - `list-brand-kits` (ficar on-brand), `generate-design` /
     `create-design-from-brand-template`, `perform-editing-operations`, `export-design`

### Caminho B — HTML/CSS + screenshot (tipografia/layout de precisão)
Render via HTML/CSS, captura com Playwright. Controle tipográfico total. Bom pra peças
type-driven, carrosséis com sistema rígido.

### Caminho C — Figma (handoff / design system)
Quando o entregável precisa virar fonte editável ou parte de um design system.

### ⛔ Regra de arquivo (CLAUDE.md do projeto)
Salve/exporte SEMPRE com **caminho ABSOLUTO dentro da pasta do projeto ativo**
(ex.: `C:\...\Projeto X\entregaveis\post.png`). NUNCA caminho relativo — cai no cwd da
biblioteca. Temporários de conferência em `<projeto>\.tmp\` e apague ao terminar.

## Brief de entrega (quando NÃO renderizar)

Quando não há ferramenta de render ou o usuário só quer a estratégia, entregue um brief
que qualquer designer/ferramenta executa sem te perguntar nada:

```
# Criativo: [nome] — [formato + dimensão]

## Insight estratégico
DOR / DESEJO / ÂNGULO / PROMESSA / POSICIONAMENTO  (do market-research)

## Copy (idioma do brief)
- Hook: [texto exato]
- Corpo / cards: [texto exato, card a card se carrossel]
- CTA: [texto exato]
- Legenda + hashtags: [se pedido]

## Direção de arte
- Conceito visual: [a big idea visual em 1 frase]
- Layout: [composição, ponto focal, hierarquia — descreva o que vai onde]
- Tipografia: [famílias, pesos, escala]
- Paleta: [cores com hex + razão]
- Imagem/elementos: [o que gerar/usar, com prompt de geração se aplicável]
- Referência de mood: [se houver]

## Specs
- Dimensão, safe zones, nº de cards (carrossel)

## Rationale
[por que essa dor, esse hook, essa direção — a decisão estratégica]
```
