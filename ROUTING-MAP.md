# ROUTING-MAP — índice fino de roteamento (squads → especialista → sequência)

> **Pra quê:** camada de roteamento enxuta consumida por `/workflow` e `/briefing`. Diz
> **qual squad**, **qual especialista DENTRO do squad** e **em que ordem** (sequências
> multi-agent prontas). Destilado de `squad-prompts/` (23.5k linhas de personas) — aqui
> só o gatilho, não a persona.
>
> **Disclosure progressivo (NÃO furar):**
> 1. Este arquivo (≈1 tela) é o que o roteador lê pra DECIDIR. Leve.
> 2. A **persona pesada** carrega sob demanda: invoque o agent nativo via `Skill`/`Agent`.
> 3. `squad-prompts/*.md` = backup portátil (GPT/Gemini) + fonte da verdade. **Nunca**
>    despejar no contexto de roteamento — é 350k tokens de context-rot.
>
> **Como invocar um agent nativo:** `Skill` → `<squad-slug>:agents:<id>`
> (ex.: `brand-squad:agents:david-aaker`, `copy-master:agents:gary-halbert`).
> O **chief** roteia internamente; chame o chief quando não souber o especialista exato.

## Tabela rápida — problema → squad (chief)

| Problema | Squad slug | Chief |
|---|---|---|
| Marca, identidade, posicionamento, naming, arquétipo, brand book | `brand-squad` | brand-chief |
| Copy completa: sales letter, VSL, e-mail, headline, landing, pitch | `copy-master` | copy-master-chief |
| Copy sem camada obrigatória de psicologia (subset 23) | `copy-squad` | copy-chief |
| Oferta, leads, pricing, retenção, escala, modelo de negócio | `hormozi-squad` | hormozi-chief |
| Tráfego pago, ads, campanhas, pixel, criativo, scaling | `traffic-masters` | traffic-chief |
| Narrativa, pitch, apresentação, manifesto, storytelling | `storytelling` | story-chief |
| Movimento, identidade tribal, manifesto de movimento | `movement` | movement-chief |
| Design system, UX flow, component spec, design ops | `design-squad` | design-chief |
| Analytics, retenção, growth, comunidade, CLV, audiência | `data-squad` | data-chief |
| Estratégia executiva, GTM, fundraise, operações, AI strategy | `c-level-squad` | vision-chief |
| Conselho de mentores (decisão difícil, sparring) | `advisory-board` | board-chair |
| Pentest, auditoria de segurança, recon, incidente | `cybersecurity` | cyber-chief |
| Config do Claude Code, hooks, MCP, agents, skills, setup | `claude-code-mastery` | claude-mastery-chief |

---

## Brand Squad
- **chief:** brand-chief
- **use when:** construir, auditar, reposicionar ou operacionalizar estratégia de marca
- **specialists:**
  - david-aaker — construir/medir brand equity e identidade estratégica
  - kevin-keller — equity baseada no cliente, pirâmide CBBE, medição
  - jean-noel-kapferer — sistema de identidade, luxo, Identity Prism
  - al-ries — posicionamento, criação de categoria, foco
  - byron-sharp — crescimento por evidência, distinctiveness, mental availability
  - marty-neumeier — diferenciação radical, only-ness, fechar brand gap
  - donald-miller — mensagem, StoryBrand, cliente-herói
  - denise-yohn — fusão marca×cultura, operacionalização, alinhamento interno
  - emily-heyward — branding de startup dia-zero, DTC, escada emocional
  - alina-wheeler — sistema de identidade visual completo, processo 5 fases
  - archetype-consultant — arquétipo, personalidade, tom de voz
  - naming-strategist — geração de nome, fonossemântica, avaliação linguística
  - domain-scout — domínio disponível, handles sociais, viabilidade digital
  - miller-sticky-brand — implementação StoryBrand, BrandScripts, funis
- **sequences:**
  - complete-rebrand: jean-noel-kapferer→al-ries→marty-neumeier→donald-miller→alina-wheeler→naming-strategist
  - new-brand-launch: emily-heyward→naming-strategist→domain-scout→archetype-consultant→donald-miller→alina-wheeler
  - brand-growth: byron-sharp→david-aaker→kevin-keller→al-ries

## Copy Master
- **chief:** copy-master-chief
- **use when:** qualquer copy: VSL, sales letter, e-mail, ad, landing, launch, pitch, oferta
- **specialists:**
  - gary-halbert — starving crowd, long-form emocional, mala direta
  - eugene-schwartz — diagnóstico de awareness, estratégia de headline
  - claude-hopkins — teste, advertising científico, data-driven
  - gary-bencivenga — proof stacking, audiência cética, bater controles
  - robert-collier — abertura empática, mental movie, nurture
  - john-carlton — selling power cru, ângulo escondido, Sales Detective
  - jim-rutz — consertar copy chata, formato (magalogs), revisão ética
  - john-caples — teste de headline, split test, fórmulas DR
  - rosser-reeves — USP, consistência, ownership de um benefício
  - dan-kennedy — oferta, Ultimate Sales Letter, high-ticket, info-marketing
  - frank-kern — intent-based branding, launch, webinar, goodwill-first
  - russell-brunson — arquitetura de funil, Value Ladder, Hook-Story-Offer
  - todd-brown — Big Marketing Idea, mecanismo de oferta, conceito de campanha
  - stefan-georgi — RMBC, VSL, research-first, descoberta de mecanismo
  - jon-benson — VSL, sales page long-form, script de vídeo
  - ry-schwartz — sequência de e-mail de launch, coach/course, Moment of Tension
  - sabri-suby — sistema de venda completo, lead magnet, 8-Phase Selling
  - evaldo-albuquerque — copy financeira long-form, core belief, 10 perguntas
  - ben-settle — daily email, copy de personalidade, infotainment, polarização
  - andre-chaperon — storytelling em e-mail, Soap Opera, open loops
  - dan-koe — short-form, marca pessoal, newsletter, filosofia
  - joe-sugarman — Slippery Slide, DR impresso, gatilhos psicológicos
  - david-ogilvy — brand advertising, big idea elegante, prestígio
  - clayton-makepeace — Four-Legged Stool, emoções dominantes
  - parris-lampropoulos — fascination bullets, research-obsessed, magalog
  - david-deutsch — CopyTHINKING, múltiplos controles vencedores, Boardroom
  - alex-hormozi — $100M Offers, Value Equation, copy de funil moderno
  - joanna-wiebe — conversion copy, message mining, SaaS, Voice of Customer
  - robert-cialdini — camada de psicologia obrigatória, 7 princípios de influência
  - blair-warren — gatilhos emocionais, 5 drivers, persuasão inconsciente
  - chris-voss — high-ticket, objeção, tactical empathy, frame control
  - oren-klaff — pitch deck, frame control, croc brain, high-stakes
- **sequences:**
  - sales-letter-legacy: gary-halbert→robert-collier→john-carlton→gary-bencivenga→robert-cialdini
  - vsl-blueprint: stefan-georgi→jon-benson→todd-brown→blair-warren
  - launch-sequence: frank-kern→russell-brunson→ry-schwartz→sabri-suby
  - financial-letter: evaldo-albuquerque→clayton-makepeace→gary-bencivenga→robert-cialdini
  - email-nurture: andre-chaperon→ben-settle→dan-koe
  - funnel-architecture: russell-brunson→frank-kern→ry-schwartz→sabri-suby→chris-voss
  - offer-engineering: alex-hormozi→dan-kennedy→gary-bencivenga→robert-cialdini
  - headline-testing: john-caples→rosser-reeves→eugene-schwartz
  - pitch-mastery: oren-klaff→chris-voss→alex-hormozi

## Copy Squad
- **chief:** copy-chief
- **use when:** copy elite SEM camada obrigatória de psicologia (subset 23-agentes do copy-master)
- **note:** cross-ref ao copy-master; prefira copy-master quando quiser a camada Cialdini obrigatória
- **specialists:** subconjunto do copy-master (halbert, schwartz, hopkins, bencivenga, collier, carlton, rutz, kennedy, kern, brunson, todd-brown, stefan-georgi, jon-benson, ry-schwartz, ben-settle, andre-chaperon, dan-koe, sugarman, ogilvy, makepeace, parris-lampropoulos, david-deutsch)
- **sequences:**
  - complete-sales-letter: robert-collier→gary-halbert→stefan-georgi→gary-bencivenga
  - vsl: todd-brown→stefan-georgi→jon-benson→gary-bencivenga
  - launch-sequence: frank-kern→russell-brunson→andre-chaperon→ry-schwartz

## Hormozi Squad
- **chief:** hormozi-chief
- **use when:** negócio: oferta, leads, pricing, venda, retenção, escala, modelo, conteúdo, ads, launch
- **specialists:**
  - hormozi-advisor — diagnóstico estratégico, teoria da restrição
  - hormozi-offers — oferta converte mal, "tá caro", sem diferenciação
  - hormozi-leads — poucos clientes, pipeline inconsistente, não escala aquisição
  - hormozi-pricing — competindo em preço, margem fina, não cobra o suficiente
  - hormozi-closer — lead não converte, ciclo longo, fechamento fraco
  - hormozi-retention — churn alto, LTV baixo, cliente sai em 1-3 meses
  - hormozi-scale — receita estagnada, gargalo no dono, operação quebrando
  - hormozi-models — modelo errado, margem fina, teto de escala
  - hormozi-content — orgânico fraco, sem sistema de conteúdo, construir audiência
  - hormozi-ads — ads pagos não lucram, CPA alto, fadiga de criativo
  - hormozi-hooks — conteúdo sem engajamento, open rate baixo, ad sem clique
  - hormozi-launch — lançar produto, entrar em mercado, do zero, pré-venda
  - hormozi-workshop — workshop, treino em grupo, evento premium, intensivo
  - hormozi-copy — sales/landing page, ad copy no estilo Hormozi direto
  - hormozi-audit — saúde do negócio, o que está quebrado, benchmark
- **sequences:**
  - complete-turnaround: hormozi-audit→hormozi-advisor→(especialista por restrição)→hormozi-scale
  - new-product-launch: hormozi-models→hormozi-offers→hormozi-launch→hormozi-leads
  - existing-growth: hormozi-audit→hormozi-advisor→(especialista por restrição)→hormozi-retention

## Traffic Masters
- **chief:** traffic-chief
- **use when:** ads pagos: setup, scaling, troubleshooting ou otimização
- **specialists:**
  - molly-pittman — Facebook/Meta, construção sistemática do zero
  - ralph-burns — performance full-funnel, nCAC, creative lab
  - depesh-mandalia — scaling Facebook, BPM Method, AC-4, graduation testing
  - nicholas-kusmich — Facebook high-ROI, Contextual Congruence, Give-Give-Give-Ask
  - tom-breeze — YouTube ads, ADUCATE, estrutura de vídeo 3 atos
  - kasim-aslam — Google Ads, Performance Max, "You vs Google"
  - pedro-sobral — mercado Brasil/LATAM, gestor de tráfego, Meta Ads
  - ad-midas — estratégia de criativo, scripts, hooks, briefs, matriz de teste
  - media-buyer — setup, otimização diária, execução cross-platform, bid
  - performance-analyst — métricas, dashboards, relatório de funil, KPI
  - creative-analyst — decompor criativos, fadiga, análise competitiva
  - scale-optimizer — fases de scaling, CPA marginal, realocação de budget
  - pixel-specialist — tracking, CAPI, privacidade iOS, UTM, qualidade de dado
  - ads-analyst — auditoria forense, spend desperdiçado, estrutura
  - fiscal — alocação de budget, fluxo de caixa, ROAS líquido, payback
- **sequences:**
  - new-facebook-campaign: depesh-mandalia→molly-pittman→ad-midas→pixel-specialist→media-buyer→fiscal
  - account-audit: ads-analyst→pixel-specialist→performance-analyst→fiscal
  - scale-winning-campaign: scale-optimizer→creative-analyst→depesh-mandalia→fiscal
  - youtube-funnel: tom-breeze→ad-midas→pixel-specialist→media-buyer

## Storytelling
- **chief:** story-chief
- **use when:** framework narrativo pra qualquer desafio de storytelling
- **specialists:**
  - joseph-campbell — arquétipos míticos, padrões universais de história
  - dan-harmon — estrutura de episódio, narrativa episódica
  - blake-snyder — roteiro, logline, estrutura de 15 beats
  - shawn-coyne — editar história, diagnosticar por que não funciona
  - matthew-dicks — história pessoal, memoir, momento de transformação
  - kindra-hall — histórias de negócio, lacunas de story no marketing
  - nancy-duarte — apresentação, keynote, dado em narrativa
  - park-howell — framework ABT, storytelling de marca
  - keith-johnstone — bloqueio criativo, espontaneidade, improv
  - oren-klaff — pitch a investidor, persuasão high-stakes
  - marshall-ganz — organizar movimento, ação coletiva, valores-em-ação
- **sequences:**
  - brand-narrative: park-howell→kindra-hall→nancy-duarte→joseph-campbell
  - personal-brand-story: matthew-dicks→kindra-hall→park-howell→marshall-ganz
  - investor-pitch: oren-klaff→nancy-duarte→kindra-hall
  - movement-campaign: marshall-ganz→joseph-campbell→park-howell

## Movement
- **chief:** movement-chief
- **use when:** construir movimento da tensão ao impacto; diagnosticar movimento travado/fragmentado
- **specialists:**
  - fenomenologo — mapear tensão não-nomeada, experiência vivida, sentimento-core
  - identitario — stack de identidade tribal, fronteiras, arquitetura quando fragmenta
  - manifestador — cristalizar identidade em palavras espalháveis, documento fundador
  - estrategista-de-ciclo — mecânica de crescimento, sequência de ativação, multiplicação
  - analista-de-impacto — medir mudança real além de vanity, saúde da comunidade
  - movement-architect — topologia da comunidade, escada de engajamento, rituais, governança
- **sequences:**
  - full-build: fenomenologo→identitario→manifestador→movement-architect→estrategista-de-ciclo→analista-de-impacto
  - diagnosis: analista-de-impacto→fenomenologo→estrategista-de-ciclo
  - identity-crisis: identitario→fenomenologo→manifestador
  - narrative-launch: manifestador→identitario→estrategista-de-ciclo

## Design Squad
- **chief:** design-chief
- **use when:** design system, novo produto/feature, auditoria de acessibilidade, design ops, asset visual
- **specialists:**
  - brad-frost — atomic design, pattern library, governança de componentes
  - dan-mall — adoção/escala de design system, direção criativa, Hot Potato
  - dave-malouf — maturidade de design ops, workflow, estrutura de time
  - ux-designer — research, IA, wireframe, usabilidade, auditoria WCAG
  - design-system-architect — design tokens, API de componente, Storybook
  - visual-generator — prompt de imagem IA, sistema de ícone, identidade visual
  - ui-engineer — React/Tailwind, responsivo, pixel-perfect, acessibilidade
- **sequences:**
  - design-system-creation: brad-frost→dan-mall→design-system-architect→ui-engineer
  - new-product-design: ux-designer→visual-generator→brad-frost→ui-engineer
  - feature-design: ux-designer→brad-frost→ui-engineer
  - design-ops-setup: dave-malouf→dan-mall→design-chief
  - accessibility-audit: ux-designer→brad-frost→ui-engineer

## Data Squad
- **chief:** data-chief
- **use when:** analytics, growth, retenção, comunidade, educação, valor do cliente
- **specialists:**
  - avinash-kaushik — web analytics, dashboard, modelo de medição, KPI, vanity
  - peter-fader — CLV, segmentação, modelagem de lifetime value, whale curve
  - sean-ellis — growth hacking, PMF, experimentos, AARRR, North Star
  - wes-kao — cohort course, audiência, produto educacional, POV afiado
  - nick-mehta — customer success, health score, NRR, churn, retenção
  - david-spinks — estratégia de comunidade, SPACES, community-led growth
- **sequences:**
  - new-saas-setup: sean-ellis→avinash-kaushik→nick-mehta→peter-fader
  - community-first: david-spinks→sean-ellis→avinash-kaushik→wes-kao
  - mature-optimization: peter-fader→nick-mehta→avinash-kaushik
  - full-product-launch: sean-ellis→avinash-kaushik→peter-fader→wes-kao→nick-mehta→david-spinks

## C-Level Squad
- **chief:** vision-chief
- **use when:** decisão estratégica cruzando funções, counsel executivo, fundraise, brownfield, M&A
- **specialists:**
  - coo-orchestrator — gargalo de escala, processo, OKR, estrutura de time, KPI
  - cmo-architect — posicionamento, GTM, demand gen, CAC, ROI de marketing
  - cto-architect — stack, arquitetura, build vs buy, dívida técnica, cultura de eng
  - cio-engineer — segurança, compliance, fornecedor, governança de TI
  - caio-architect — estratégia de IA, pipeline ML, IA responsável, LLM, agents
- **sequences:**
  - new-product-launch: vision-chief→cmo-architect→cto-architect→coo-orchestrator→cio-engineer
  - fundraising-prep: vision-chief→coo-orchestrator→cmo-architect→cto-architect
  - post-incident-review: cio-engineer→cto-architect→coo-orchestrator→vision-chief
  - ai-adoption: caio-architect→cto-architect→coo-orchestrator→cio-engineer

## Advisory Board
- **chief:** board-chair
- **use when:** decisão estratégica multi-domínio; founder em encruzilhada; cultura/investimento/escala
- **specialists:**
  - ray-dalio — investimento, risco, princípios, ciclos econômicos, transparência radical
  - charlie-munger — modelos mentais, viés cognitivo, inversão, multidisciplinar
  - naval-ravikant — criação de riqueza, leverage, specific knowledge, founder-vida
  - peter-thiel — contrarian, teoria de monopólio, zero-to-one, power law
  - reid-hoffman — escala, blitzscaling, network effects, alianças
  - simon-sinek — liderança com propósito, golden circle, infinite game
  - brene-brown — confiança via vulnerabilidade, coragem, Dare to Lead
  - patrick-lencioni — saúde de time, disfunção organizacional, accountability
  - derek-sivers — minimalismo, autonomia contrarian, hell yeah or no
  - yvon-chouinard — negócio com missão, sustentabilidade, propósito sobre lucro
- **sequences:**
  - invest: ray-dalio→charlie-munger→naval-ravikant
  - scale: reid-hoffman→peter-thiel→derek-sivers
  - culture: patrick-lencioni→brene-brown→simon-sinek
  - founder: naval-ravikant→derek-sivers→yvon-chouinard
  - contrarian: peter-thiel→charlie-munger→derek-sivers

## Cybersecurity
- **chief:** cyber-chief
- **use when:** pentest, security assessment, resposta a incidente, red team, app security
- **specialists:**
  - peter-kim — segurança ofensiva e red team, metodologia de playbook
  - georgia-weidman — segurança mobile, dev de exploit, pentest hands-on
  - jim-manico — app security, OWASP, secure coding, API security
  - chris-sanders — network monitoring, análise de pacote, investigação
  - omar-santos — gestão de vulnerabilidade, incidente, programa de cyber
  - marcus-carey — liderança em segurança, threat intel, simulação de breach
  - command-generator — traduzir objetivo em comando/sintaxe exata de ferramenta
  - cartographer — recon, mapeamento de superfície, topologia de rede
  - busterer — descoberta de conteúdo web, enumeração de endpoint, brute-force de dir
  - dirber — enumeração de serviço (SMB, LDAP, SNMP, NFS, RPC, DNS)
  - fuzzer — fuzzing de input/parâmetro, SQLi, XSS, command injection
  - ripper — quebra de credencial, hash, wordlist, análise de senha
  - rogue — exploração, pós-exploração, privesc, movimento lateral
  - shannon-runner — OSINT, exposição de credencial, perfil de pessoa/org/tech
- **sequences:**
  - full-pentest: cyber-chief→cartographer→dirber→busterer→fuzzer→ripper→rogue
  - web-app-test: cyber-chief→jim-manico→busterer→dirber→fuzzer→command-generator
  - network-assessment: cyber-chief→chris-sanders→cartographer→command-generator→omar-santos
  - mobile-security: cyber-chief→georgia-weidman→command-generator→fuzzer
  - incident-response: cyber-chief→omar-santos→chris-sanders→marcus-carey
  - osint-investigation: cyber-chief→shannon-runner→cartographer→marcus-carey

## Claude Code Mastery
- **chief:** claude-mastery-chief
- **use when:** hooks, MCP, agents, config, skills, integração de projeto, roadmap do ecossistema
- **specialists:**
  - hooks-architect — controlar evento de lifecycle, bloquear tool, automação determinística
  - mcp-integrator — compor stack de tools, budget de contexto, adicionar server
  - swarm-orchestrator — topologia multi-agent, spawnar times, trabalho paralelo
  - config-engineer — hierarquia de settings, permissão, CLAUDE.md, sandbox
  - skill-craftsman — criar skill, command, plugin, workflow spec-driven
  - project-integrator — integrar projeto, scaffold, brownfield, CI/CD
  - roadmap-sentinel — rastrear mudança do ecossistema, adoção, plan-first
- **sequences:**
  - hook-pipeline: hooks-architect→config-engineer→project-integrator
  - mcp-setup: mcp-integrator→config-engineer→project-integrator
  - team-orchestration: swarm-orchestrator→skill-craftsman→project-integrator
  - full-integration: project-integrator→config-engineer→hooks-architect→skill-craftsman
  - adoption-strategy: roadmap-sentinel→skill-craftsman→project-integrator

---

_Gerado de `squad-prompts/` (v2, ~56% cobertura). Ids reconciliados com os agents instalados
(`~/.claude/agents` + `.claude/`). Quando um squad ganhar/perder agente, atualize aqui — este
índice é a fonte de roteamento; as personas pesadas continuam em `squad-prompts/`._

---

## GSD — framework de projeto multi-fase (67 skills `gsd-*`)

Não é squad; é ciclo. Regra de desempate com AIOX: GSD = ciclo disciplinado com artefatos (`.planning/`), autônomo; AIOX = personas de time sob demanda. Invocação: `/gsd-<skill>` (hífen — é skill, não command).

**Ciclo canônico:** `new-project` → `plan-phase` → `execute-phase` → `verify-work` → `code-review` → `ship`.

**8 clusters:**

1. **Início/Projeto** — `new-project`, `new-milestone`, `complete-milestone`, `milestone-summary`
2. **Planejar** — `plan-phase`, `discuss-phase`, `spec-phase`, `ultraplan-phase`, `plan-review-convergence`, `sketch`, `spike`
3. **Executar** — `execute-phase`, `mvp-phase`, `phase`, `fast`, `quick`, `autonomous`
4. **Verificar/QA** — `verify-work`, `validate-phase`, `code-review`, `secure-phase`, `ui-review`, `eval-review`, `audit-fix`, `audit-milestone`, `audit-uat`, `add-tests`
5. **Debug/Forense** — `debug`, `forensics`, `health`
6. **Docs/Contexto** — `docs-update`, `map-codebase`, `ingest-docs`, `capture`, `explore`, `graphify`, `surface`, `thread`
7. **Manutenção/Estado** — `cleanup`, `resume-work`, `pause-work`, `undo`, `update`, `config`, `settings`, `workspace`, `progress`, `stats`, `ship`, `pr-branch`, `import`, `inbox`, `review-backlog`, `manager`, `workstreams`, `extract-learnings`, `profile-user`, `help`, `review`
8. **Track leve `gsd-ns-*`** — `ns-context`, `ns-ideate`, `ns-project`, `ns-review`, `ns-manage`, `ns-workflow`

> Lista sempre atual: `INVENTARIO.md` (gerado). Prefixo `gsd-` = 67; `gsd-ns-` = track leve.
