# CLAUDE.md — Roteamento de recursos (Workflow Projetos)

Este projeto é a **biblioteca central** de skills, squads e agents do Thales.

- **Skills e agents** carregam do **global** (`~/.claude/`): 165 skills instaladas (67 GSD) · 44 agents.
- **Squads** carregam do **local** (`.claude/commands/`): 14.
- **Fonte da verdade versionada** = `biblioteca/`: 145 skills · 34 agents · 14 squads.
  A diferença global↔biblioteca é majoritariamente `aios-core` (repo próprio) + wrappers de squad.

Índice exaustivo: INVENTARIO.md (**gerado** por `scripts/gerar-inventario.sh` — não editar à mão).

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

Toda entrega de **marca/identidade** (logo, rebranding, sistema visual, paleta,
tipografia, identidade verbal, brand book/MIV) segue o
**[CLAUDE-BRANDING-OS.md](CLAUDE-BRANDING-OS.md)** — mesma régua $1M, lente de agência
de branding (Brand Strategist + Creative Director + Art Director + Identity Designer +
Typography Specialist + Verbal Identity Strategist). Traz princípios de logo, identidade
visual, cor, tipografia e verbal; estrutura de MIV/brand book; territórios criativos;
e três portões antes de fechar: **SELF-CRITIQUE**, **AI DETECTION CHECK** e
**PREMIUM BRAND CHECK**. É o par do CREATIVE-OS: web → CREATIVE-OS, marca → BRANDING-OS.

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
   índice lazy destilado das personas dos squads (`biblioteca/squads/<slug>/agents/`;
   não despeje as personas pesadas no contexto — invoque o agent nativo via `Skill` →
   `<squad-slug>:agents:<id>`).
4. **Skill de execução** (design, site, slides, animação) conforme o entregável.
5. **MCP** pra dados externos: `firecrawl` (web/research/mineração de refs),
   `context7` (docs de libs), Figma/Notion/Supabase/Slack conforme o caso.

## Tabela de roteamento — tarefa → recurso

| Se a tarefa é... | Use |
|---|---|
| Começar um entregável (pedido raso, não sei o tipo/nível ainda) | skill `workflow` (porta de entrada: pergunta tipo → briefing → nível → roteia) |
| Marca, identidade, posicionamento, naming, arquétipo, brand book | squad **brand-squad** (`brand-chief`) + skill `brand` — sob a lei do **CLAUDE-BRANDING-OS.md** |
| Logo / rebranding (brief) | skill `briefing` (lente brand, trilho logo/rebranding) → `brand-squad` — gate final = SELF-CRITIQUE + AI DETECTION + PREMIUM BRAND CHECK do **CLAUDE-BRANDING-OS.md** |
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
| Construir feature/produto com LLM (RAG, agente, tools/MCP, avaliação) | **Ver roteamento IA aplicada abaixo** ⬇️ |
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

## Roteamento IA aplicada — construir sistema com LLM (evita sobreposição)

Esta biblioteca **é** uma operação de LLM, mas os recursos de *construir* sistema de IA
estavam órfãos do roteamento. Regra de desempate, do mais barato pro mais caro —
**não pule pro caro sem esgotar o anterior**:

1. **Prompt / contexto** — o comportamento cabe na instrução? Resolve em skill/agent
   versionado. É o default desta casa (145 skills versionadas). Custo ~zero. Skill `skill-creator`.
2. **Tools / function calling / MCP** — o modelo precisa *agir* ou ler dado vivo (API,
   banco, arquivo)? Não é RAG, é ferramenta. Skill `mcp-builder` (servidor próprio,
   Python FastMCP ou TS SDK). Custo baixo.
3. **RAG / retrieval** — conhecimento grande demais pro contexto e que muda? Recupera,
   não treina. Local sobre código/docs → `graphify`. Produção → `supabase` + pgvector
   (+ `supabase-postgres-best-practices` pra índice e RLS). Custo médio.
4. **Fine-tuning** — só quando falta *forma/estilo/formato consistente*, não conhecimento,
   e prompt+RAG já falharam **com dataset de avaliação provando a falha**. Custo alto,
   trava versão de modelo. Sem recurso local: é decisão de arquitetura, passa por
   `gsd-ai-integration-phase`.

**Regra curta:** conhecimento que muda → RAG. Ação no mundo → tools/MCP. Comportamento e
formato → prompt. Estilo que prompt não segura, com eval provando → fine-tuning.

| Se a tarefa é... | Use |
|---|---|
| Projetar fase de produto que usa IA (contrato `AI-SPEC.md`) | skill `gsd-ai-integration-phase` → agents `gsd-framework-selector` (matriz de framework), `gsd-domain-researcher` (critério do domínio), `gsd-ai-researcher` (docs do framework), `gsd-eval-planner` (rubrica + guardrails) |
| Auditar se o sistema de IA já construído tem avaliação de verdade | skill `gsd-eval-review` (agent `gsd-eval-auditor` → `EVAL-REVIEW.md`, COVERED/PARTIAL/MISSING) |
| Servidor MCP próprio (expor API/serviço como tool) | skill `mcp-builder` |
| App direto na API da Anthropic (SDK, prompt caching, tool use, Managed Agents) | skill `claude-api` |
| Store vetorial / pgvector / RLS pra RAG em produção | skills `supabase` + `supabase-postgres-best-practices` |
| RAG local sobre a própria codebase/docs | skill `graphify` (`query` / `path` / `explain`) |
| App de IA no ecossistema Vercel (AI SDK, gateway, agentes, workflow durável) | plugin `vercel` (`vercel:ai-sdk`, `vercel:ai-gateway`, `vercel:build-agents`, `vercel:workflow`) + agent `vercel:ai-architect` |
| Estratégia de IA / pipeline ML / IA responsável (nível executivo) | squad **c-level-squad** → agent `caio-architect` |

**Avaliação não é opcional.** Sistema de IA sem eval é chute versionado: `gsd-eval-planner`
entra no design (antes), `gsd-eval-review` audita (depois). Mesma lei do CREATIVE-OS —
mire o teto, não o "funciona no happy path".

**Fundamentos já transcritos** (não reescreva teoria): `Cursos/CONHECIMENTO.md` §2
"Fundamentos de IA, LLM, RAG e agentes" e §4 "Conectar a IA aos seus dados (RAG e
function calling)".

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
