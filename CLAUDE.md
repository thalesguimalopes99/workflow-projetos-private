# CLAUDE.md — Roteamento de recursos (Workflow Projetos)

Este projeto é a **biblioteca central** de skills, squads e agents do Thales. Tudo
está instalado **global** (`~/.claude/`) E **local** (`.claude/` deste projeto):
135 skills (das quais 67 GSD) · 14 squads · 33 agents. Índice exaustivo: INVENTARIO.md (gerado).

## ⛔ REGRA CRÍTICA — arquivos vão na pasta do PROJETO ATIVO, nunca nesta biblioteca

Esta pasta (`Workflow Projetos`) é **só a biblioteca** de skills/squads/agents. Quando
você trabalha num projeto específico (ex.: `Projeto Ingrid`, em pasta irmã ou em
qualquer caminho), **TODO arquivo gerado vai na pasta DAQUELE projeto** — código,
assets, screenshots, renders, PDFs, temporários, saída de qualquer ferramenta. **Nada
de output de projeto aqui.**

- **Playwright / screenshots / renders:** SEMPRE passe caminho **ABSOLUTO** dentro da
  pasta do projeto ativo (ex.: `C:\...\Projeto Ingrid\.tmp\shot.jpeg`). Nunca use nome
  relativo (`shot.jpeg`) — cai no `cwd`, que é esta biblioteca. O Playwright MCP grava
  relativo ao cwd por padrão; por isso o caminho absoluto é obrigatório.
- **Temporários de verificação** (screenshots de conferência, logs): crie em
  `<projeto>/.tmp/` e **apague ao terminar**. Se sobrar, limpe antes de encerrar.
- **Antes de criar QUALQUER arquivo**, confirme: o destino é a pasta do projeto, não o
  `cwd`? Na dúvida, use caminho absoluto do projeto.
- Vale pra **todo projeto**, não só o da Ingrid. O `cwd` ser a biblioteca não autoriza
  escrever output de projeto nela.

## ⭐ Padrão de qualidade criativa — CREATIVE OS

**Lei suprema:** SEMPRE a melhor entrega possível. Tudo que é bom é caro — a régua de
TODA entrega criativa (site, marca, proposta, slides, motion, copy) é **$1M**. Nunca
mire "competente"/"suficiente"; mire o teto. Nível abaixo de $1M só se o Thales pedir
explicitamente.

Toda entrega web/experiência de marca (site, landing, app, peça interativa) segue o
**[CREATIVE-OS.md](CREATIVE-OS.md)** — padrão awwwards / $1M. Resumo da lei:
pensar como agência (Creative Director + WebGL Engineer + Awwwards Judge), não como
dev de landing; nada de SaaS genérico / hero+features+pricing / card grids / template
Tailwind; storytelling + motion com propósito + art direction; autocrítica de Awwwards
Judge (nota 1–10, refatora tudo < 9) antes de finalizar; "parece template/IA?" → refatora.
Operacionalmente: skill `criar-site-premium` (processo) + `site-teardown` (minerar refs)
+ `frontend-design`/`distinctive-frontend` + stack GSAP/ScrollTrigger/Lenis/Three.js.
**Fonte de pesquisa + régua de qualidade = Top 3 global: Awwwards (Design·Usabilidade·
Criatividade·Conteúdo) · FWA (tech de ponta/3D/WebGL/imersivo) · Behance (processo UX→UI).**
Sempre minere os 3 antes de construir e meça o resultado contra eles.

## Regra de ouro

**SEMPRE traga o recurso certo para a melhor entrega.** Antes de produzir qualquer
coisa não-trivial, pergunte-se: *qual squad/chief/skill/MCP eleva essa entrega?* Se
existe um especialista pro problema, use-o — não entregue genérico quando há squad
dedicado. Processo primeiro (superpowers/briefing), depois o especialista de domínio.

## Protocolo (ordem)

0. **Porta de entrada** se o Thales quer COMEÇAR um entregável com pedido raso →
   skill `workflow` (intake interativo: pergunta qual entregável, destrincha via
   briefing, pergunta o nível de qualidade, e roteia pro recurso certo). É a versão
   ativa desta tabela. Dispara com "/workflow", "quero começar", pedido vago.
1. **Briefing** se o pedido é vago → skill `briefing` (transforma contexto
   raso em brief executável; lente `brand` tem trilhos logo/rebranding).
2. **Processo** (plugin superpowers): trabalho criativo novo → `brainstorming`; bug →
   `systematic-debugging`; tarefa multi-passo → `writing-plans` / `executing-plans`;
   código → `test-driven-development`.
3. **Especialista de domínio** → invoque o **chief** do squad (o chief roteia os
   agentes internos). Tabela abaixo. Pra **roteamento fino** (qual especialista
   DENTRO do squad + sequência multi-agent pronta), leia `ROUTING-MAP.md` na raiz —
   índice lazy destilado de `squad-prompts/` (não despeje as personas pesadas no
   contexto; invoque o agent nativo via `Skill` → `<squad-slug>:agents:<id>`).
4. **Skill de execução** (design, site, slides, animação) conforme o entregável.
5. **MCP** pra dados externos: `firecrawl` (web/research/mineração de refs),
   `context7` (docs de libs), Figma/Notion/Supabase/Slack conforme o caso.

## Tabela de roteamento — tarefa → recurso

| Se a tarefa é... | Use |
|---|---|
| Começar um entregável (pedido raso, não sei o tipo/nível ainda) | skill `workflow` (porta de entrada: pergunta tipo → briefing → nível → roteia) |
| Marca, identidade, posicionamento, naming, arquétipo, brand book | squad **brand-squad** (`brand-chief`) + skill `brand` |
| Logo / rebranding (brief) | skill `briefing` (lente brand, trilho logo/rebranding) → `brand-squad` |
| Copy: sales letter, VSL, e-mail, headline, bullets, landing | squad **copy-master** (`copy-master-chief`) ou **copy-squad** (`copy-chief`) |
| Oferta, pricing, leads, geração de demanda, escalar negócio | squad **hormozi-squad** (`hormozi-chief`) |
| Tráfego pago, ads, campanhas, pixel, criativo de ad | squad **traffic-masters** (`traffic-chief`) |
| Narrativa, pitch, apresentação, manifesto, storytelling | squad **storytelling** (`story-chief`) |
| Movimento, comunidade-identidade, manifesto de movimento | squad **movement** (`movement-chief`) |
| Design system, UX flow, component spec, design ops | squad **design-squad** (`design-chief`) |
| Analytics, retenção, growth, comunidade, audiência | squad **data-squad** (`data-chief`) |
| Estratégia executiva, GTM, fundraise, operações, visão | squad **c-level-squad** (`vision-chief`) |
| Conselho de mentores (decisão difícil, sparring estratégico) | squad **advisory-board** (`board-chair`) |
| Pentest, auditoria de segurança, recon, resposta a incidente | squad **cybersecurity** (`cyber-chief`) |
| Config do Claude Code, hooks, MCP, agentes, otimizar setup | squad **claude-code-mastery** (`claude-mastery-chief`) |
| Desenvolvimento de software (analyst→architect→dev→qa→devops) | squad **AIOX** (`aiox-master`) |
| Projeto de software multi-fase / autônomo (ciclo com artefatos `.planning/`) | framework **GSD** (skills `/gsd-*`) — ver desempate GSD↔AIOX abaixo |
| Site/landing premium nível awwwards | skill `criar-site-premium` (+ `firecrawl` p/ minerar refs; usa canvas Stitch 2.0 na direção) |
| Clonar/desconstruir ref de site p/ aprender (pegar HTML+CSS+JS, não screenshot) | skill `site-teardown` (+ `firecrawl` rawHtml) |
| SEO/GEO: rankear no Google + ser citado por IA | **Ver roteamento SEO abaixo** ⬇️ |
| UI component / interface distinta | plugin `frontend-design` + skill `ui-ux-pro-max` |
| Banner social/ads/web/print | skill `banner-design` |
| Apresentação / slides | skill `slides` ou `design-system` |
| Animação web (GSAP, anime.js, CSS, Lottie) | skills `hyperframes` / `hf-*` |
| Motion design, animar logo, vídeo de imagem, ad animado, promo, brand motion | skill `motion-design` (Higgsfield: storyboard grid → Seedance 2.0) |
| Ícone, mockup CIP, social photo | skill `design` (suite) |
| Deploy / Vercel / Next.js | plugin `vercel` |
| Issues, PRs, code review no GitHub | MCP `github` |
| Testar UI real, screenshot, regressão visual, e2e | MCP `playwright` |
| Research web / minerar referências | MCP `firecrawl` (ou WebSearch/`exa` se key off) |
| Raciocínio estruturado / planejamento profundo | MCP `sequential-thinking` + skills GSD |

## Roteamento SEO — qual recurso usar (evita sobreposição)

Stack SEO tem redundância de propósito. Regra de desempate:

- **Audit técnico profundo / produção** → plugin **`claude-seo`** (25 sub-skills + 18 agents, namespaced `claude-seo:*`). É a ferramenta principal. Cobre técnico, schema, GEO, local, i18n, backlinks, drift.
- **Quick / free / 1 tarefa** → skills soltas: `seo-audit` (diagnóstico), `schema` (JSON-LD), `seo-aeo-best-practices` (meta/OG/sitemap), `ai-seo` (GEO/AEO/llms.txt), `internal-linking-optimizer` (linkagem interna — alto impacto), `programmatic-seo` (páginas em escala), `firecrawl-seo-audit` (audit via firecrawl).
- **Achável + citável no `criar-site-premium`** → é a **Barra 4** do gate (rankear no Google + citação por IA antes do ship).
- **Dado real (keyword/SERP/volume/backlink)** → **pago, só quando cliente banca**. Padrão recomendado: **DataForSEO** (extensão nativa do `claude-seo`, mais barato) em vez do plugin `seo-skills` (SE Ranking). `backlink-analyzer`/`seo-geo` scripts = pagos.
- **Dado de busca REAL grátis (maior alavanca p/ rankear rápido)** → **Google Search Console + GA4 + PageSpeed/CrUX**. Scripts já existem (`seo-skills/scripts/`, `claude-seo:seo-google`); falta só fazer OAuth + key. Conectar quando der.

## Roteamento de dev — GSD vs AIOX (evita sobreposição)

Ambos cobrem software. Regra de desempate:

- **Ciclo de projeto multi-fase, autônomo, com artefatos** (`.planning/`, PLAN/RESEARCH/VERIFICATION), commits atômicos e checkpoints → framework **GSD**. Skills `gsd-*`, invocadas via `/gsd-new-project` → `/gsd-plan-phase` → `/gsd-execute-phase` → `/gsd-verify-work` → `/gsd-code-review` → `/gsd-ship`. Track leve: `gsd-ns-*`.
- **Personas de time sob demanda** (analyst/architect/dev/qa/devops) pra consultar/decidir, sem o overhead do ciclo → squad **AIOX** (`aiox-master`), que roteia os agentes internos.
- **Correção:** GSD é instalado como **skills** (`gsd-*`), não command namespace `/gsd:`. Invocação: `/gsd-new-project` (hífen).

## Plugins ativos

- **superpowers** — skills de processo (brainstorming, debugging, TDD, plans). Use ANTES de executar.
- **frontend-design** — UI de alta qualidade, anti-genérico.
- **vercel** — deploy, AI SDK, Next.js, env, marketplace.
- **caveman** — modo de resposta terse (toggle `/caveman`).

## MCP disponíveis

- **github** (remoto, OAuth) — issues, PRs, reviews, Actions. Autenticar via `/mcp`.
- **playwright** (oficial Microsoft) — automação de browser, teste de UI, screenshot,
  regressão visual via accessibility tree.
- **sequential-thinking** — raciocínio estruturado multi-passo. Complementa GSD/plans.
- **firecrawl** (local) — search, scrape, crawl, extract. Research web e mineração de
  referências de design. ⚠️ Depende de FIRECRAWL_API_KEY válida no ~/.claude.json.
- **claude.ai connectors** — Context7 (docs de libs/frameworks), Figma, Notion,
  Supabase, Slack, n8n, Google Drive, Miro, exa, Vercel. Schemas via ToolSearch.

> "Context7 + GitHub + Playwright cobrem ~80% dos workflows de dev" — agora os 3 estão presentes.

## Manutenção da biblioteca

- Editou um recurso GLOBAL (`~/.claude/skills|commands|agents`)? **Sincronize o backup**
  desta biblioteca (`biblioteca/`) — ela é a fonte da verdade versionável.
- `biblioteca/` (backup limpo) ≠ `.claude/` deste projeto (cópia local de uso). Mantenha
  os dois alinhados com o global.
- Atualizou contagem de skills/squads? Atualize `INVENTARIO.md` e `README.md`.
- Semear outro projeto: `./scripts/instalar-em-novo-projeto.sh "/caminho/destino"`.
