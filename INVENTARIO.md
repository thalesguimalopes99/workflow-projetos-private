# Inventario da Biblioteca

> Gerado a partir do conteudo realmente copiado para `biblioteca/`.
> Data: 2026-05-30 · atualizado 2026-06-17 (107 skills; +9 SEO skills.sh: seo-audit, ai-seo, programmatic-seo, firecrawl-seo-audit, backlink-analyzer, seo-geo, seo-aeo-best-practices, schema, internal-linking-optimizer)

## Resumo

| Bloco   | Quantidade            | Tamanho aprox. |
|---------|-----------------------|----------------|
| skills  | 107 subpastas         | ~45 MB         |
| squads  | 14 squads             | ~5,3 MB        |
| agents  | 33 agents globais (.md) | ~0,3 MB      |
| config  | 1 arquivo de referencia | ~0,01 MB     |
| **Total** | 107 skills · 14 squads · 33 agents | **~51 MB**   |

> Sincronizado com `~/.claude/skills` global em 2026-05-31 (85 = 85). frontend-design
> instalada via `npx skills add` em ~/.agents/skills (symlink p/ Claude Code) em 2026-06-02.

Lixo excluido na copia: `node_modules` (797 MB), `.venv` (339 MB), `dist` (129 MB),
`build`, `cache`, `.git`, alem de binarios pesados (`.mp4`, `.dll`, `.exe`, `.node`).
As fontes originais somavam ~1,6 GB; a biblioteca limpa tem ~41,5 MB.

---

## Skills (96)

### Skills GSD (Get Shit Done) — 67
gsd-add-tests, gsd-ai-integration-phase, gsd-audit-fix, gsd-audit-milestone,
gsd-audit-uat, gsd-autonomous, gsd-capture, gsd-cleanup, gsd-code-review,
gsd-complete-milestone, gsd-config, gsd-debug, gsd-discuss-phase, gsd-docs-update,
gsd-eval-review, gsd-execute-phase, gsd-explore, gsd-extract-learnings, gsd-fast,
gsd-forensics, gsd-graphify, gsd-health, gsd-help, gsd-import, gsd-inbox,
gsd-ingest-docs, gsd-manager, gsd-map-codebase, gsd-milestone-summary,
gsd-mvp-phase, gsd-new-milestone, gsd-new-project, gsd-ns-context, gsd-ns-ideate,
gsd-ns-manage, gsd-ns-project, gsd-ns-review, gsd-ns-workflow, gsd-pause-work,
gsd-phase, gsd-plan-phase, gsd-plan-review-convergence, gsd-pr-branch,
gsd-profile-user, gsd-progress, gsd-quick, gsd-resume-work, gsd-review,
gsd-review-backlog, gsd-secure-phase, gsd-settings, gsd-ship, gsd-sketch,
gsd-spec-phase, gsd-spike, gsd-stats, gsd-surface, gsd-thread, gsd-ui-phase,
gsd-ui-review, gsd-ultraplan-phase, gsd-undo, gsd-update, gsd-validate-phase,
gsd-verify-work, gsd-workspace, gsd-workstreams

### Skills HyperFrames / Video — 7
hf-animejs, hf-css-animations, hf-gsap, hf-hyperframes, hf-hyperframes-cli,
hyperframes (skill completa, sem node_modules/.venv/mp4), video-use (sem .venv)

### Skills Design / Marketing — 7
banner-design (22 estilos; social/ads/web/print), brand (voz, identidade visual,
asset management), design (suite: logo 55 estilos, CIP, slides, banner, icon,
social photos), design-system (tokens 3 camadas, component specs, slides),
slides (apresentacoes Chart.js), ui-styling, ui-ux-pro-max (50+ estilos, 161
paletas, 57 font pairings, shadcn/ui MCP). Copiadas do global em 2026-05-30.

### Skills Marketing (skills.sh) — 10
Instaladas via `npx skills add` em 2026-06-16, GLOBAL (~/.claude/skills) + LOCAL
(.claude/skills), --copy. Todas Socket 0 alerts. Fonte coreyhaines31/marketingskills
(top do leaderboard skills.sh) salvo onde indicado:
- copywriting, marketing-psychology, social, content-strategy, cro, ad-creative,
  competitor-profiling (coreyhaines31/marketingskills)
- humanizer (blader/humanizer) — remove sinais de escrita de IA
- content-research-writer (skillcreatorai/ai-agent-skills)
- brand-landingpage (wshobson/agents) — substituto de "Landing Page Premium"

### Skills standalone — 6
- motion-design (criacao de motion design via conector Higgsfield; fluxo: brief
  intake -> storyboard como UMA folha-grade GPT Image 2 -> video Seedance 2.0.
  Dois modos: classicMD (ads/brand/logo reveal, cinematic) e highMD (kinetic/
  esportes/tech, cortes agressivos, sem humanos realistas — so silhuetas/chrome/3D).
  Dispara com "motion design", "animate this", "video do meu logo", "promo/ad video".
  Instalada 2026-06-16. GLOBAL em ~/.claude/skills/motion-design.)
- frontend-design (interfaces frontend distintas, production-grade, anti-"AI slop";
  oficial anthropics/skills. Instalada via `npx skills add github.com/anthropics/skills
  --skill frontend-design` em 2026-06-02. Vive em ~/.agents/skills/frontend-design,
  symlink p/ Claude Code. Socket 0 alerts / Snyk Low Risk. So SKILL.md + LICENSE.txt.)
- workflow (PORTA DE ENTRADA da biblioteca; intake interativo: pergunta QUAL
  entregavel via AskUserQuestion -> destrincha via briefing -> pergunta NIVEL de
  qualidade/escopo -> roteia pro squad/skill/processo certo e da o handoff.
  Operacionaliza a tabela de roteamento do CLAUDE.md de forma ativa. Dispara com
  "/workflow", "quero comecar um projeto", ou pedido criativo raso. Criada
  2026-05-31. GLOBAL em ~/.claude/skills/workflow.)
- briefing (de contexto raso a brief executavel; 6 lentes: site-app, criativo,
  brand, projeto, conteudo, generico). A lente `brand` tem 3 trilhos: identidade
  completa, logo, rebranding (atualizado 2026-05-30). GLOBAL em ~/.claude/skills/briefing.
- criar-site-premium (workflow de site nivel awwwards/$10k: brief -> minerar 5
  fontes -> direcao visual -> sistema de tokens -> build premium -> quality gate
  -> ship). Fontes: 21st.dev, dribbble, awwwards, pinterest, YouTube. Criada
  2026-05-30; atualizada 2026-05-31 (ferramentas de canvas visual Stitch 2.0/
  Figma/paper.design; regra firecrawl "pegar codigo nao screenshot"; conceito
  vibe gap; link p/ site-teardown; detalhes de craft na fase Build). Tambem
  GLOBAL em ~/.claude/skills/criar-site-premium.
- site-teardown (desconstruir referencia de site/componente p/ APRENDER e
  templar: pega HTML+CSS+JS inteiros via firecrawl `rawHtml` em vez de screenshot,
  resolve o "vibe gap", ensina a tecnica por tras dos efeitos). Braco de minera-
  cao profunda do criar-site-premium. Fontes: awwwards, dribbble, 21st.dev,
  pinterest, godly.website, concorrentes. Criada 2026-05-31 a partir dos videos
  "7 Levels of Building ELITE Websites" + "Stop Making Ugly Websites + Stitch".
  GLOBAL em ~/.claude/skills/site-teardown.

---

## Squads (14)

Cada squad contem `agents/`, `tasks/` (quando aplicavel), `checklists/`,
`workflows/`/`data/` e um `squad.yaml` ou `config.yaml`.

### AIOX — 11 agents, 0 tasks
aiox-master, analyst, architect, data-engineer, dev, devops, pm, po, qa,
squad-creator, ux-design-expert

### advisory-board — 11 agents, 7 tasks
board-chair, brene-brown, charlie-munger, derek-sivers, naval-ravikant,
patrick-lencioni, peter-thiel, ray-dalio, reid-hoffman, simon-sinek,
yvon-chouinard

### brand-squad — 15 agents, 9 tasks
al-ries, alina-wheeler, archetype-consultant, brand-chief, byron-sharp,
david-aaker, denise-yohn, domain-scout, donald-miller, emily-heyward,
jean-noel-kapferer, kevin-keller, marty-neumeier, miller-sticky-brand,
naming-strategist

### c-level-squad — 6 agents, 7 tasks
caio-architect, cio-engineer, cmo-architect, coo-orchestrator, cto-architect,
vision-chief

### claude-code-mastery — 8 agents, 26 tasks
claude-mastery-chief, config-engineer, hooks-architect, mcp-integrator,
project-integrator, roadmap-sentinel, skill-craftsman, swarm-orchestrator

### copy-master — 33 agents, 14 tasks
alex-hormozi, andre-chaperon, ben-settle, blair-warren, chris-voss,
claude-hopkins, clayton-makepeace, copy-master-chief, dan-kennedy, dan-koe,
david-deutsch, david-ogilvy, eugene-schwartz, evaldo-albuquerque, frank-kern,
gary-bencivenga, gary-halbert, jim-rutz, joanna-wiebe, joe-sugarman, john-caples,
john-carlton, jon-benson, oren-klaff, parris-lampropoulos, robert-cialdini,
robert-collier, rosser-reeves, russell-brunson, ry-schwartz, sabri-suby,
stefan-georgi, todd-brown

### copy-squad — 23 agents, 13 tasks
andre-chaperon, ben-settle, claude-hopkins, clayton-makepeace, copy-chief,
dan-kennedy, dan-koe, david-deutsch, david-ogilvy, eugene-schwartz, frank-kern,
gary-bencivenga, gary-halbert, jim-rutz, joe-sugarman, john-carlton, jon-benson,
parris-lampropoulos, robert-collier, russell-brunson, ry-schwartz, stefan-georgi,
todd-brown

### cybersecurity — 15 agents, 8 tasks
busterer, cartographer, chris-sanders, command-generator, cyber-chief, dirber,
fuzzer, georgia-weidman, jim-manico, marcus-carey, omar-santos, peter-kim,
ripper, rogue, shannon-runner

### data-squad — 7 agents, 6 tasks
avinash-kaushik, data-chief, david-spinks, nick-mehta, peter-fader, sean-ellis,
wes-kao

### design-squad — 8 agents, 7 tasks
brad-frost, dan-mall, dave-malouf, design-chief, design-system-architect,
ui-engineer, ux-designer, visual-generator

### hormozi-squad — 16 agents, 9 tasks
hormozi-ads, hormozi-advisor, hormozi-audit, hormozi-chief, hormozi-closer,
hormozi-content, hormozi-copy, hormozi-hooks, hormozi-launch, hormozi-leads,
hormozi-models, hormozi-offers, hormozi-pricing, hormozi-retention, hormozi-scale,
hormozi-workshop

### movement — 7 agents, 6 tasks
analista-de-impacto, estrategista-de-ciclo, fenomenologo, identitario,
manifestador, movement-architect, movement-chief

### storytelling — 12 agents, 7 tasks
blake-snyder, dan-harmon, joseph-campbell, keith-johnstone, kindra-hall,
marshall-ganz, matthew-dicks, nancy-duarte, oren-klaff, park-howell, shawn-coyne,
story-chief

### traffic-masters — 16 agents, 16 tasks
ad-midas, ads-analyst, creative-analyst, depesh-mandalia, fiscal, kasim-aslam,
media-buyer, molly-pittman, nicholas-kusmich, pedro-sobral, performance-analyst,
pixel-specialist, ralph-burns, scale-optimizer, tom-breeze, traffic-chief

---

## Agents globais (33)

Subagents GSD que vivem em `.claude/agents/` (nivel global, fora dos squads):

gsd-advisor-researcher, gsd-ai-researcher, gsd-assumptions-analyzer,
gsd-code-fixer, gsd-code-reviewer, gsd-codebase-mapper, gsd-debug-session-manager,
gsd-debugger, gsd-doc-classifier, gsd-doc-synthesizer, gsd-doc-verifier,
gsd-doc-writer, gsd-domain-researcher, gsd-eval-auditor, gsd-eval-planner,
gsd-executor, gsd-framework-selector, gsd-integration-checker, gsd-intel-updater,
gsd-nyquist-auditor, gsd-pattern-mapper, gsd-phase-researcher, gsd-plan-checker,
gsd-planner, gsd-project-researcher, gsd-research-synthesizer, gsd-roadmapper,
gsd-security-auditor, gsd-ui-auditor, gsd-ui-checker, gsd-ui-researcher,
gsd-user-profiler, gsd-verifier

> Observacao: a pasta `agents/` tambem trazia duas subpastas de skill embutidas
> (`hyperframes/` e `video-use/`) com `SKILL.md`. Os `node_modules` aninhados
> dentro delas foram removidos na limpeza; apenas o texto foi mantido.

---

## Config

- `biblioteca/config/settings.global.referencia.json` — copia do
  `~/.claude/settings.json` global (hooks GSD, plugins habilitados, statusLine,
  permissoes). Mantido como REFERENCIA. Nao sobrescreva o settings de um projeto
  novo com este sem revisar os caminhos absolutos de hooks.
