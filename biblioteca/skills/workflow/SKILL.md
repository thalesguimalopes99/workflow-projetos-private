---
name: workflow
description: PORTA DE ENTRADA da biblioteca — use SEMPRE que o Thales quiser COMEÇAR um entregável e trouxe um pedido raso/minimalista, sem dizer ainda o tipo exato ou o nível de qualidade. Dispara com "/workflow", "quero começar um projeto", "vamos criar/construir algo", "preciso de um [site/logo/marca/landing/copy/ad/apresentação]" sem escopo fechado, ou qualquer pedido criativo vago. O que faz: (1) pergunta QUAL entregável (site, landing, brand book, logo, rebranding, manual de marca, copy, oferta, tráfego, apresentação, naming...), (2) destrincha via briefing, (3) pergunta o NÍVEL de qualidade/escopo do entregável, (4) roteia pro squad/skill/processo certo e dá o handoff. Não entrega genérico — traz sempre o especialista.
---

# Workflow — porta de entrada e roteamento de entregáveis

Esta skill é o **intake interativo** da biblioteca Workflow Projetos. O Thales chega com algo raso ("quero um site", "preciso de uma marca") e esta skill **destrincha junto com ele**: descobre o entregável, o nível de qualidade desejado, e roteia pro recurso certo — em vez de sair entregando genérico.

**Princípio (regra de ouro da biblioteca):** sempre trazer o recurso certo pra melhor entrega. Se existe um squad/chief/skill pro problema, use-o. Processo primeiro (briefing/superpowers), depois o especialista de domínio.

## Abertura (PRIMEIRA mensagem — sempre)

Ao ser invocada (`/workflow` ou pedido raso), **abra com uma saudação curta + a pergunta do que construir**, e dispare o menu de entregáveis com `AskUserQuestion` na MESMA resposta. Não espere o Thales falar de novo — já chegue perguntando.

Modelo da abertura (adapte o tom, mantenha curto):

> **Bora começar.** Sou a porta de entrada da sua biblioteca — me diz o que vamos construir e eu trago o time certo, destrincho o brief e ajusto o nível da entrega.
>
> O que você quer criar agora?

Logo em seguida, `AskUserQuestion` com as opções de entregável (site, landing, clonar site existente, brand book, logo, rebranding, manual de marca, copy, oferta, tráfego, apresentação, naming, software, outro). Aceite "Outro" pra texto livre.

Se o Thales já disse o que quer ao invocar (ex: "/workflow quero uma landing"), pule a pergunta do tipo e vá direto pro briefing (etapa 2) — mas ainda assim abra com uma linha curta confirmando o entregável.

## Fluxo (siga em ordem)

### 1. Descobrir O QUE é o entregável
Já feito na **Abertura** acima (saudação + `AskUserQuestion`). Se o Thales já disse claramente (ex: "quero uma landing de captura"), pule pra etapa 2. Aceite "Outro" pra texto livre.

Pode ser **mais de um** entregável (ex: marca + site). Se for, trate em ordem de dependência: marca/identidade ANTES de site/landing (o site usa os tokens da marca).

### 2. Destrinchar FUNDO (interrogatório de excelência)
Invoque a skill `briefing` com a **lente certa** pro entregável (ver coluna "Briefing"). Mas **briefing é o piso, não o teto.** O Thales QUER ser destrinchado — perguntar pouco é falha, não economia. Cave em **rodadas** até o brief estar afiado o bastante pra entregar excelência, não genérico.

**8 dimensões que você DEVE extrair antes de rotear** (não avance com buracos — se faltar, pergunte mais):

1. **Objetivo nº1** — o que muda na vida/negócio do Thales se isso der MUITO certo? (não "um site", mas "fechar 3 clientes/mês")
2. **Público exato** — quem vê, em que estado mental, o que pensa/sente antes e depois.
3. **Sucesso medível** — como o Thales vai saber que ficou EXCELENTE? Qual a métrica/sensação-alvo?
4. **Referências (ama / odeia)** — 2-3 que admira e por quê + o que NÃO quer parecer. Mina o gosto real.
5. **Ângulo / diferencial** — por que isso não pode ser igual a todo mundo do nicho? Qual a assinatura?
6. **Restrições** — prazo, budget, marca existente (cores/voz/tokens), limites técnicos, canal/onde roda.
7. **O que já existe** — assets, conteúdo, rascunho, marca pronta, ou zero.
8. **Não-objetivos** — o que está FORA do escopo (evita inchar e perder foco).

Faça em **2-4 rodadas curtas** de `AskUserQuestion` (agrupe 1-3 perguntas relacionadas por rodada), reagindo a cada resposta com a próxima camada — como um diretor criativo fazendo sparring, não um formulário. Cada resposta abre a próxima pergunta. **Pare quando** as 8 dimensões estiverem respondidas E você conseguiria explicar o entregável pra um especialista sem deixar buraco. Antes de avançar, **espelhe** o brief de volta em 4-6 linhas e confirme: "É isso? Falta algo?"

### 3. Perguntar o NÍVEL / qualidade do entregável
Antes de produzir, pergunte (`AskUserQuestion`) o nível desejado. Todo entregável tem tiers — o nível decide quanto processo e quais especialistas entram. Use os tiers da coluna "Níveis". Pergunte também: **prazo**, **uso** (quem vê, onde roda) e **o que já existe** (conteúdo/assets prontos, rascunho, ou zero).

### 4. Rotear + handoff
Com tipo + brief + nível, invoque o **chief do squad** ou a **skill de execução** (coluna "Roteia pra"). O chief roteia os agentes internos. Confirme o plano em 3-5 linhas e só então execute.

**Roteamento fino (especialista interno + sequência):** a tabela abaixo é grossa (entregável → squad). Pra saber **qual especialista DENTRO do squad** e **em que ordem encadear**, leia `ROUTING-MAP.md` na raiz da biblioteca — índice fino com gatilho por agente + sequências multi-agent prontas (ex: rebrand = kapferer→ries→neumeier→miller→wheeler→naming). **Leia só quando for rotear** (lazy); não carregue as personas pesadas de `biblioteca/squads/<slug>/agents/`. Invoque o agent nativo via `Skill` → `<squad-slug>:agents:<id>`.

**Entregável composto / ponta-a-ponta (cruza squads + skills + MCP + AIOX):** quando o entregável NÃO cabe num squad só (ex: lançamento completo = marca + oferta + copy + site + ads + tracking), leia `references/synergy-pipelines.md` (nesta skill) — cadeias prontas que amarram squad↔squad↔skill↔MCP↔AIOX por entregável, com gate CREATIVE-OS. Também lazy: só ao montar o pipeline. ROUTING-MAP = roteamento DENTRO do squad; synergy-pipelines = cadeia ENTRE recursos.

## Tabela de roteamento — entregável → recurso

| Entregável | Briefing (lente) | Roteia pra | Níveis (tiers a perguntar) |
|---|---|---|---|
| **Site / web app** | site-app | `criar-site-premium` (maestro; usa `firecrawl`+`site-teardown` p/ refs, canvas Stitch 2.0, `frontend-design`, `ui-ux-pro-max`, deploy `vercel`) | Competente ($200-300k: a11y/perf/responsivo) · Premium ($1M: conceito-assinatura + distinção + negócio) |
| **Landing page** | site-app | `criar-site-premium` + `copy-master`/`copy-squad` (copy que converte) | Validação rápida (MVP de teste) · Conversão (copy + prova + CTA forte) · Premium (awwwards + conversão) |
| **Clonar site existente → codebase Next.js** | site-app | template `ai-website-cloner` (em `Projetos\ai-website-cloner\`) — abrir Claude Code **DENTRO da pasta**: `claude --chrome` → `/clone-website <url>`. Pipeline recon→foundation→specs→build→assembly (Next 16 / React 19 / shadcn / Tailwind v4). ⚠️ project-scoped: a skill `/clone-website` só existe no cwd daquele projeto. **Ao rotear aqui, OFEREÇA rodar**: confirme url + escopo, e se já estiver no cwd do projeto dispare `/clone-website <url>`; senão, instrua o handoff (`cd` + `claude --chrome` + comando). **Difere de `site-teardown`** (minera código de ref p/ APRENDER, não reconstrói o site) | 1 página · Multi-página · Site completo (todas rotas + assets) |
| **Brand book / Identidade visual** | brand (identidade completa) | squad `brand-squad` (`brand-chief`) + skill `brand` | Mini-guia (logo+cor+fonte) · Brand book (voz, sistema, aplicações) · Sistema completo (arquétipo, posicionamento, governança) |
| **Logo** | brand (trilho logo) | skill `briefing` → `brand-squad` (`brand-chief`) + `design` (suite logo, 55 estilos — **SVG/vetorial, sem imagem IA**) | 1 conceito · 3 rotas + variações · Sistema de logo (responsivo, clear space, usos) |
| **Rebranding** | brand (trilho rebranding) | `brand-squad` (`brand-chief`) — auditoria → estratégia → identidade nova | Refresh (ajuste visual) · Reposicionamento (estratégia+visual) · Rebrand total (naming+identidade+migração) |
| **Manual de marca / Brand guidelines** | brand | `brand-squad` (`brand-chief`) + `design-system` (tokens formais) | Quick reference · Manual completo · Design system operacional (tokens→componentes) |
| **Naming** | brand | `brand-squad` (`naming-strategist`, `domain-scout`) | Lista de candidatos · Naming + validação (domínio/legal) · Naming + arquétipo + narrativa |
| **Copy (sales letter, VSL, email, headline, bullets)** | criativo/conteúdo | squad `copy-master` (`copy-master-chief`) ou `copy-squad` (`copy-chief`) | Peça única · Sequência · Funil completo |
| **Oferta / pricing / leads / escalar** | projeto | squad `hormozi-squad` (`hormozi-chief`) | Diagnóstico · Oferta+pricing · Sistema de aquisição |
| **Tráfego pago / ads / criativo** | criativo | squad `traffic-masters` (`traffic-chief`) | Setup+tracking · Campanha · Escala+otimização |
| **Apresentação / pitch / slides** | conteúdo | squad `storytelling` (`story-chief`) + skill `slides`/`design-system` | Deck rápido · Pitch narrativo · Apresentação premium (narrativa+design) |
| **Manifesto / movimento / comunidade** | conteúdo | squad `movement` (`movement-chief`) | Manifesto · Narrativa de movimento · Estratégia de comunidade |
| **Banner / social / ads / print** | criativo | skill `banner-design` (22 estilos — **layout/código, sem imagem gerada por IA**; usar asset real/fornecido) | 1 peça · Kit (formatos) · Campanha visual |
| **Componente UI / interface distinta** | site-app | plugin `frontend-design` + skill `ui-ux-pro-max` | 1 componente · Conjunto · Mini design-system |
| **Animação web (GSAP/anime/CSS/Lottie)** | criativo | skills `hyperframes` / `hf-*` | Micro-interação · Sequência · Hero animado |
| **Motion design / vídeo / animar logo / ad animado / promo** | criativo | skill `motion-design` (Higgsfield: brief → storyboard grid GPT Image 2 → vídeo Seedance 2.0) | classicMD (ads/brand/logo reveal, cinematic) · highMD (kinetic/esportes/tech, cortes agressivos, sem humanos realistas) — perguntar duração (5/10/15s) e formato (16:9/9:16/1:1) |
| **Estratégia executiva / GTM / fundraise** | projeto | squad `c-level-squad` (`vision-chief`) | Diagnóstico · Plano · Operação |
| **Decisão difícil / sparring estratégico** | projeto | squad `advisory-board` (`board-chair`) | — (conselho de mentores) |
| **Software (analyst→dev→qa→devops)** | projeto | squad `AIOX` (`aiox-master`) + processo `superpowers` | Spike · MVP · Produção |
| **Projeto de software multi-fase / autônomo (ciclo com artefatos)** | projeto | framework **GSD** (`/gsd-new-project` → `/gsd-plan-phase` → `/gsd-execute-phase` → `/gsd-verify-work` → `/gsd-code-review` → `/gsd-ship`). Ver desempate GSD↔AIOX abaixo. | Sketch/Spike · MVP (`/gsd-mvp-phase`) · Produção (ciclo completo + secure/ui/eval-review) |
| **Outro / não sei ainda** | genérico | `briefing` (lente genérica) pra clarear, depois re-rotear | — |

### Desempate GSD ↔ AIOX (ambos fazem software)

| Use **GSD** quando | Use **AIOX** quando |
|---|---|
| Projeto real multi-fase; quer ciclo disciplinado com artefatos (`.planning/`, PLAN/RESEARCH/VERIFICATION); execução autônoma/checkpointada; commits atômicos | Quer personas de time sob demanda (analyst/architect/dev/qa/devops) pra consultar/decidir, sem o overhead do ciclo de fases |
| Invoca skills `gsd-*` via `/gsd-new-project`, `/gsd-plan-phase`... | Invoca o chief `AIOX:agents:aiox-master` (roteia os agentes internos) |

> GSD é instalado como **skills** (`gsd-*`), não command namespace. `/gsd-new-project` (hífen).

### Clusters de skills utilitárias (fora da tabela principal, mas disponíveis)

Não são entregáveis de marca, mas o intake deve lembrar delas:

- **Docs/Office:** `docx`, `pdf`, `pptx`, `xlsx`, `doc-coauthoring`, `internal-comms`
- **Mídia:** `video-extract`, `yt-dlp`, `slack-gif-creator`, `curso-ripper`
- **Dev-infra:** `claude-api`, `mcp-builder`, `supabase`, `supabase-postgres-best-practices`, `webapp-testing`, `web-artifacts-builder`, `remotion-best-practices`, `distinctive-frontend`
- **Criativo extra:** `algorithmic-art`, `canvas-design`, `theme-factory`, `criativo-cliente`, `instagram-creative-director`, `brand-guidelines`
- **Growth:** `ranquear` (rankear no Google + citação por IA + crescer no Instagram — filtro cético de táticas SEO/GEO)
- **Meta/infra:** `skill-creator`, `template-skill`, `find-skills`

> Índice exaustivo de TODAS as skills: `INVENTARIO.md` (gerado). GSD: ver `ROUTING-MAP.md`.

## Regras de processo (sempre)

- **Processo antes do especialista.** Trabalho criativo novo → `superpowers:brainstorming`. Bug → `superpowers:systematic-debugging`. Multi-passo → `writing-plans`/`executing-plans`. Código → `test-driven-development`.
- **Mineração de refs é padrão em qualquer visual.** Site/landing/marca/banner → `firecrawl` nas fontes do nicho + concorrentes; pegar **código** das refs (não só print) via `site-teardown`. Entender escopo+nicho primeiro.
- **MCP pra dados externos:** `firecrawl` (web/refs), `context7` (docs de libs), Figma/Notion/Supabase/Slack conforme o caso.
- **Arquivos vão na pasta do PROJETO ativo**, nunca nesta biblioteca.
- **SEM imagem gerada por IA.** `nano-banana`/Gemini image estão desinstalados e proibidos neste projeto. Não rote pra geração de imagem por IA. Visual = referência real, asset entregue pelo Thales, ou design vetorial/código (SVG, CSS, layout). Se um entregável pedir imagem, use stock/asset fornecido ou produção manual.

## Como conduzir o intake (tom)

- **Destrinchar fundo é o trabalho, não fricção a evitar.** O Thales pediu explicitamente pra ser interrogado mais. Perguntar de menos = entrega genérica = falha. Várias rodadas curtas > uma rasa.
- **Rodadas, não questionário único.** Agrupe 1-3 perguntas relacionadas por `AskUserQuestion` e reaja a cada resposta com a próxima camada. Sparring de diretor criativo, não formulário despejado de uma vez.
- **Não roteie com buraco.** Só avance pro nível/handoff quando as 8 dimensões (etapa 2) estiverem respondidas e você conseguir explicar o entregável a um especialista sem lacuna.
- Use `AskUserQuestion` pros menus (tipo, nível, opções fechadas). Aceite sempre resposta livre.
- Se o Thales já deu uma resposta ("quero nível awwwards", "público é X"), não re-pergunte — registre e siga pra próxima camada.
- **Espelhe e confirme** ao fim de cada etapa: devolva o que entendeu em poucas linhas e pergunte o que falta, antes de avançar.
- Objetivo: do raso/minimalista → brief AFIADO (8 dimensões) + nível definido + recurso certo engatado. A fricção que vira clareza é bem-vinda.

## Exemplo

> Thales: "quero fazer um site"
> 1. `AskUserQuestion`: é site institucional, landing de captura, web app, ou e-commerce? + pra qual nicho?
> 2. **Destrinchar fundo (2-4 rodadas)** + `briefing` (lente site-app):
>    - Rodada A: objetivo nº1 (o que muda se der certo?) + público exato + sucesso medível.
>    - Rodada B: 2-3 referências que ama/odeia e por quê + ângulo/diferencial (por que não genérico?).
>    - Rodada C: restrições (prazo, budget, marca/tokens existentes) + o que já existe + não-objetivos.
>    - Espelha o brief em 5 linhas: "É isso? Falta algo?"
> 3. `AskUserQuestion`: nível — competente ($200-300k) ou premium awwwards ($1M)?
> 4. Premium → engata `criar-site-premium` (minera refs via firecrawl/site-teardown, conceito, direção, tokens, build, gate, ship). Confirma plano. Executa.
