# Roteamento e produção (Fase 4)

Você fez o cérebro (intake + nicho + estratégia + copy). Agora entregue isso pro
**produtor especialista** que faz as mãos. Regra de ouro: o produtor **não repesquisa nem
reentrevista** — você passa o pacote pronto.

## Tabela de roteamento

| Tipo de peça | Produtor | Como acionar |
|---|---|---|
| Social orgânico: feed, carrossel, story, capa de reel, legenda | skill `instagram-creative-director` | `Skill` → `instagram-creative-director` |
| Ad pago: Meta/Google, campanha de mídia, criativo de anúncio | squad `traffic-masters` | `Skill` → `traffic-masters:agents:traffic-chief` |
| Banner: social, web, print, display | skill `banner-design` | `Skill` → `banner-design` |
| Site, landing page, experiência web | skill `criar-site-premium` | `Skill` → `criar-site-premium` |
| Só copy longa: VSL, sales letter, sequência de e-mail | squad `copy-master` | `Skill` → `copy-master:agents:copy-master-chief` |
| Marca/identidade do zero (não é criativo avulso) | squad `brand-squad` | `Skill` → `brand-squad:agents:brand-chief` |

Dúvida entre social orgânico e ad pago? Pergunte o objetivo: se há verba de mídia e
otimização de conversão paga → `traffic-masters`. Se é post pra perfil/alcance orgânico →
`instagram-creative-director`.

## O handoff — o que passar pro produtor

Monte um bloco de contexto e entregue junto ao acionar:

```
CLIENTE: <nome + nicho exato>
OBJETIVO DA PEÇA: <autoridade/alcance/lead/venda/nutrição>
FORMATO: <feed/carrossel/story/etc>
INSIGHT ESTRATÉGICO: <a dor, desejo, ângulo, promessa — do dossiê>
PÚBLICO: <quem + momento de consciência>
COPY APROVADA:
  - Hook: <...>
  - Corpo: <...>
  - CTA: <...>
  - Legenda: <...>
BRAND KIT: <cores, fontes, logo, tom — ou nome do brand kit no Canva>
RESTRIÇÕES: <o que o cliente não quer>
```

Isso elimina retrabalho: o produtor já entra direto na direção de arte e render.

## Pipeline de render (quando o produtor produzir a peça)

Ferramentas principais de imagem do projeto: **Higgsfield + Canva**.

1. **Higgsfield** (`mcp__higgsfield__*`) — gera o visual base AI (cinematográfico,
   photoreal, styled): `generate_image`, `upscale_image`, `remove_background`,
   `outpaint_image`/`reframe` pra proporção.
   - Local file → `media_upload_widget`. URL web → `media_import_url` → usa o `media_id`
     retornado (nunca URL crua em `medias[]`).
2. **Canva** (`mcp__canva__*`) — importa o visual, compõe tipografia/copy, aplica brand
   kit (`list-brand-kits`), exporta (`export-design`).
3. Alternativas quando precisar de controle tipográfico cirúrgico: **HTML/CSS +
   screenshot Playwright**, ou **Figma** pra handoff/design system.

⚠️ **Salve sempre em caminho ABSOLUTO dentro da pasta do projeto do cliente** (ex.:
`C:\...\<Cliente>\criativos\peça.png`). Nunca no cwd da biblioteca. Temporários em
`<cliente>/.tmp/` e apague ao terminar. Ver CLAUDE.md do projeto.

## Se não há render disponível

Entregue um **brief de produção executável** — qualquer designer ou ferramenta produz a
partir dele: conceito visual, hierarquia, paleta, tipografia, copy posicionada, specs de
formato. A `instagram-creative-director` traz a estrutura desse brief em
`references/format-specs.md`.
