---
name: criar-site-premium
description: Use SEMPRE que for criar, construir ou desenhar um site/landing/web app com padrão de qualidade alto ("nível awwwards", "site que vale 1M", "premium", "topo de linha", "não pode ter cara de template/IA genérica"). Dispara quando a pessoa diz "quero fazer um site", "vamos construir um site bonito", "/site", ou traz referências de design (dribbble, awwwards, pinterest, 21st.dev) querendo chegar num resultado profissional, não-genérico. Também ative antes de começar a codar qualquer interface web de marca, OU quando pedirem pra auditar/avaliar/elevar um site que já existe ao padrão premium ("esse site tá bom?", "como deixar nível awwwards", "audita meu site").
---

# Criar Site Premium — workflow de site nível awwwards ($1M)

Transforma "quero um site bonito" num site que **vale $1M**: inovador, premium e com valor que o cliente ENXERGA. O valor está em ter **uma ideia-assinatura**, **minerar referência antes de codar**, **passar por um gate de 3 barras** e **entregar o valor de forma percebida** — não em jogar seções limpas na tela.

## O que separa $1M de $200k

Competência limpa (a11y, perf, responsivo, sem-lorem) é só o **piso** — vale ~$200-300k. Os $1M vêm de 3 eixos que a maioria pula:
1. **Distinção** — UMA ideia memorável. O cliente lembra de UMA coisa. (Sem conceito = bonito-e-esquecível.)
2. **Negócio** — o site vende/posiciona. Oferta clara, conversão, confiança. (Sem isso = portfólio caro.)
3. **Valor percebido** — o cliente SENTE os $1M na entrega: rationale, antes/depois, reveal. (Sem isso = "achei caro".)

## O princípio

Site premium não nasce do código — nasce do **conceito + direção decididos antes**. Siga as fases em ordem; cada uma trava uma decisão que a próxima usa.

**A regra de ouro:** não escreva a primeira linha de UI sem ter (1) brief fechado, (2) **conceito-assinatura aprovado**, (3) direção visual escolhida, (4) tokens definidos. Pular qualquer uma = retrabalho e cara de template.

## Pilha de skills — quem faz o quê (você é o maestro)

Esta skill ORQUESTRA outras. Não reinvente o que elas já fazem; invoque na fase certa:

| Skill | Entrega | Use na fase | Ressalva |
|---|---|---|---|
| `briefing` | Brief estruturado (lente site-app) | Brief | — |
| `frontend-design` | **Taste/distinção**: direção bold, tipografia distinta, atmosfera, motion de impacto, anti-IA-genérica | Conceito, Direção, Build | Prosa/guideline. É a alavanca dos $1M. Sem ela = seguro demais |
| `ui-ux-pro-max` | **Higiene/competência** + 161 paletas, 57 pares de fonte, gerador de design-system (CLI Python `search.py`) | Direção, Sistema, Gate | **App-leaning** (iOS/RN). Pra site web: use só a11y/tipo/cor/perf/paleta. RODE o CLI, senão só vira checklist |
| `design-system` | Estrutura formal de tokens (primitive→semantic→component) | Sistema | — |
| `copy-master` / `traffic-masters` | **Negócio**: oferta, headline, conversão, prova, posicionamento | Brief, Build | Squads que você já tem. O eixo negócio mora aqui |
| `site-teardown` | **Mineração profunda**: pega HTML+CSS+JS *inteiros* de uma ref (via firecrawl) pra aprender a técnica e templar | Mineração, Build | Use quando a ref merece desconstrução real — não só "destilar de cabeça". Resolve o "vibe gap" |
| `seo-audit` · `seo-aeo-best-practices` · `ai-seo` · `web-quality-audit` · `firecrawl-seo-audit` | **Achável + citável**: técnico (meta/schema/sitemap/CWV), GEO/AEO (citação por IA), structured data | Build, Gate (Barra 4), Ship | Plantar no build, não polir no fim. Free/offline. Dados reais de SERP/keyword (`seo-geo` pago, `backlink-analyzer`, plugin `seo-skills`) só no tier pago |

Regra: **frontend-design = teto de taste · ui-ux-pro-max = piso de competência · copy/traffic = eixo negócio · site-teardown = como o pro fez · SEO/GEO = achável e citável.** Nenhuma sozinha dá $1M — a soma orquestrada dá.

## Ferramentas de canvas visual (direção fora do terminal)

Mexer em design visual dentro do terminal trava — texto pra um meio visual. Na fase de **Direção** (e quando o build estiver "flat" e precisar de salto visual), use um canvas AI/visual pra iterar a direção, depois traga o resultado de volta pro Claude:

| Ferramenta | Pra quê | Ponte pro Claude |
|---|---|---|
| **Stitch 2.0** (Google, grátis, ~350 ger./mês) | Gerar/remixar direção visual: variações, edição por screenshot, design system (cor/type/botão/espaço) | Exporta **código React/HTML + `Design.md`** → importa no Claude como handoff. O `Design.md` carrega as regras do sistema |
| **Figma** | Design manual preciso, handoff | Plugin Stitch→Figma; ou screenshots → Claude |
| **paper.design / pencil.dev** | Canvas ao vivo dentro do editor (cursor/VS Code) | Edita visual em tempo real, sincroniza com código |

⚠️ Essas tools são **web/manuais** (sem API): a skill as usa como **guia de processo**, não execução automática. O fluxo é: gera direção no canvas → exporta código/Design.md ou tira prints → Claude transforma em produto preservando o sistema.

## Dois modos

- **Modo criação (greenfield)** — site novo, do zero. Roda o fluxo completo de 6 fases abaixo.
- **Modo auditoria (site existente)** — site já construído/no ar. Pula brief→direção→sistema→build (já feitos) e vai direto pro Quality Gate sobre o que existe. Ver seção "Modo auditoria".

Na dúvida, detecte: existe `package.json`/build/deploy ou seções já codadas? → modo auditoria.

## Quando NÃO usar

- Protótipo descartável / teste rápido de ideia → vá direto, sem cerimônia.
- App interno / 1 componente avulso sem exigência de negócio → `frontend-design` basta, sem orquestrar tudo.
- Ajuste de 1 linha/cor num site existente → edite direto, sem rodar o gate inteiro.

## Top 3 do mercado global — a régua de pesquisa e qualidade

Antes de qualquer build, calibre a barra contra os **3 benchmarks canônicos do planeta**. São a fonte de pesquisa primária E a régua de "isso é nível $1M?". Sempre minere aqui primeiro (via `firecrawl`/`site-teardown`):

| Benchmark | Por que é régua | O que minerar / como usar |
|---|---|---|
| **Awwwards** (awwwards.com) | Ecossistema mais completo da comunidade. Avalia rigoroso em **Design · Usabilidade · Criatividade · Conteúdo**. "Site of the Day" = prestígio internacional imediato | O teto de qualidade. Estude 3-5 "SOTD"/honorable do nicho → o que os torna premium. Use os 4 critérios como rubrica do gate |
| **FWA** (thefwa.com) | Premiação mais tradicional e inovadora da web (desde 2000). **Topo absoluto pra tech de ponta**: experiências imersivas, 3D, WebGL, interatividade radical | Quando o conceito pede experiência imersiva/3D/WebGL. Minere a técnica de ponta — é onde mora o "uau" interativo |
| **Behance** (behance.net) | Maior rede de portfólios criativos do mundo (Adobe). Mostra o **processo completo**: do rascunho de UX às telas finais de UI | Estude case studies inteiros — raciocínio de UX→UI, não só a tela final. Calibra a lógica de design por trás do resultado |

## Fontes complementares (mineração) — o que tirar de cada uma

| Fonte | O que minerar | Como usar |
|---|---|---|
| **21st.dev/community/components** | Componentes React/Tailwind premium prontos | Building blocks do build — copie e adapte, não reinvente botão/navbar |
| **dribbble.com** | Micro-interações, detalhes de UI, combinações ousadas | Inspiração de detalhe e motion. NÃO copie shot inteiro — destile o princípio |
| **pinterest** | Mood board: paleta, tipografia, layout, atmosfera | Monte mood board → extraia direção visual (cor + type + clima) |
| **YouTube (walkthrough)** | Técnica/tutorial específico de build ou design | Aplique a técnica concreta que o vídeo ensina |

Princípio da mineração: **destile princípios, não copie pixels.** Referência boa responde "por que isso é premium?", não "como clonar isso?".

**Minere de verdade — não invente.** No Claude Code você não navega esses sites logado. Então:
- **Sempre use `mcp__firecrawl`** pra acessar as referências do nicho. É o passo padrão de TODO build: entenda escopo+nicho → busque refs nas fontes canônicas + concorrentes diretos.
- `firecrawl_search` pra achar refs por nicho; `firecrawl_scrape` pra capturar.
- 21st.dev: copie o código do componente. ui-ux-pro-max: rode o CLI pra paleta/fonte.
- Prints do usuário **complementam**, mas não substituem o código.
- ❌ Nunca finja ter "minerado" descrevendo de cabeça. Sem fonte real → puxe via firecrawl ou peça print, ou marque `[suposição]`.

**Pegue o CÓDIGO, não só o screenshot — o "vibe gap".** Print sozinho trava em ~50%: é meio visual, o Claude faz tudo em código, e a tradução é lossy (ele *adivinha* como o efeito foi feito). Pra cravar uma referência (animação, fundo, layout), pegue o **HTML + CSS + JS inteiros** com `firecrawl_scrape` (`formats: rawHtml`), incluindo os arquivos `.css`/`.js` linkados — não o resumo do WebFetch. Quando a ref merecer desconstrução profunda, **invoque a skill `site-teardown`** (ela faz exatamente isso e te ensina a técnica). Destile princípios e adapte com seu spin — template pra aprender, não plágio.

## Fluxo (siga em ordem)

1. **Brief.** Invoque `briefing` (lente site-app). Trave: objetivo nº1, público, conteúdo (pronto/rascunho/zero), stack. **+ eixo negócio:** qual ação converte? qual a oferta? (puxe `copy-master` se a oferta estiver crua). Sem brief → não avance.
2. **Conceito-assinatura.** ANTES de qualquer pixel: defina UMA ideia memorável — a resposta de `frontend-design` pra *"qual a única coisa que vão lembrar?"*. Pode ser uma interação, um sistema de layout, uma linguagem de motion, uma metáfora visual. Escreva em 1 frase + confirme. **Sem conceito aprovado → não avança.** (É este passo que vira $1M.)
3. **Mineração + direção visual.** Minere de verdade (acima). Monte mood board. **Escolha UMA direção** alinhada ao conceito (estilo, paleta, par tipográfico, princípio de motion). Use `frontend-design` pra ousar e `ui-ux-pro-max` pra paleta/fonte. Devolva em ~5 linhas + confirme.
4. **Sistema de design.** Tokens: cores (primitive→semantic), escala tipográfica/espaçamento, raios, sombras, motion tokens. Componentes base de 21st.dev + shadcn. Use `design-system` pra estrutura formal.
5. **Build.** Stack premium (default: Next.js + Tailwind + shadcn/ui). Seção a seção do brief, conteúdo real (zero lorem). Mobile-first. **Materialize o conceito** (a ideia da fase 2 tem que aparecer no produto). Motion de impacto com `frontend-design`. Copy que converte com `copy-master`. **Tipografia:** heading forte e intencional muda tudo (Google Fonts; trocar fonte genérica é o maior ganho barato). **Os "little things" que somam craft:** hesitação no load, counters animando (0→Nm), scroll progress bar, ticker/borda natural entre seções, hover/reveal sutis. Hero pode ser arte própria (Midjourney/Nano Banana/Seedream) ou vídeo de fundo (loop sutil ~15s; mobile cai pra still por performance) — sempre com **visual storytelling** amarrado à marca. **SEO desde o markup:** HTML semântico, 1 H1 por página, meta/title/OG por rota, alt em imagem, JSON-LD do tipo certo, sitemap+robots — não é polimento de fim, planta no build (`seo-aeo-best-practices`).
6. **Gate de 4 barras.** NÃO chame de pronto sem passar nas 4 (abaixo) — inclui SEO/GEO.
7. **Ship.** Deploy (Vercel), domínio, verificação em prod. `vercel:deploy` / `verify`. **Pós-deploy:** rode `seo-audit`/`web-quality-audit` no site VIVO (CWV/Lighthouse real), submeta sitemap no Search Console, confira indexação.
8. **Apresentação de valor.** Entregue de forma que o cliente SINTA os $1M: rationale do conceito, antes/depois, tour das decisões de design, métricas (Lighthouse/CWV). Site entregue sem narrativa de valor = cliente acha caro.

## Gate de 4 barras — a régua dos $1M

Tem que cruzar AS QUATRO. Passar só na Competência = site profissional de $200-300k, não $1M. Site lindo que o Google não rankeia e a IA não cita = $1M invisível.

### Barra 1 — Competência (o piso · ferramenta: `ui-ux-pro-max` + Lighthouse)
- [ ] **Responsivo** — impecável mobile/tablet/desktop. Testado, não suposto
- [ ] **Performance** — Lighthouse 90+, imagens otimizadas, sem layout shift
- [ ] **Acessibilidade** — contraste AA, foco visível, teclado, alt
- [ ] **Conteúdo real** — copy e imagens de verdade. Zero lorem
- [ ] **Acabamento** — estados (hover/active/loading/erro/vazio), 404, favicon, meta/OG

### Barra 2 — Distinção (o teto · ferramenta: `frontend-design`)
- [ ] **Conceito presente** — a ideia-assinatura da fase 2 se materializou? Dá pra apontar a "UMA coisa"?
- [ ] **Memorável** — passaria no teste "5 segundos": fecha o site, lembra de algo? (Se não → genérico)
- [ ] **Tipografia com caráter** — fonte distinta e intencional (NÃO Inter/Roboto/system por preguiça)
- [ ] **Composição** — layout com tensão (assimetria, sobreposição, respiro como composição), não grid previsível
- [ ] **Motion de impacto** — pelo menos UM momento orquestrado (entrada/scroll-reveal), não só hover
- [ ] **Atmosfera** — textura/profundidade/cor com história, não fundo chapado

### Barra 3 — Negócio (o que justifica o preço · ferramenta: `copy-master`/`traffic-masters`)
- [ ] **Oferta clara** — em 5s dá pra saber o que é, pra quem, e o próximo passo
- [ ] **Conversão** — CTA óbvio e repetido na hora certa; caminho até a ação sem fricção
- [ ] **Confiança** — prova social, autoridade, garantias onde pesa a decisão
- [ ] **Posicionamento** — o site comunica POR QUE essa marca e não outra

### Barra 4 — SEO/GEO (achável e citável · ferramentas: `seo-audit` · `seo-aeo-best-practices` · `ai-seo` · `web-quality-audit`)
Site $1M tem que **rankear rápido no Google E ser citado pela IA** (ChatGPT/Perplexity/Gemini). Rode antes do ship:
- [ ] **Técnico** — `seo-audit` / `web-quality-audit`: title/meta/canonical, headings H1→Hn, robots.txt, sitemap.xml, HTML semântico, sem links âncora quebrados, render mobile-first (SSR/SSG se SPA)
- [ ] **Structured data** — `seo-aeo-best-practices`: JSON-LD correto pro tipo (Organization, Product, Article, FAQ…), Open Graph/Twitter cards
- [ ] **GEO/AEO** — `ai-seo`: conteúdo answer-first, estatísticas citáveis, `llms.txt`, EEAT — pra a IA citar como fonte
- [ ] **Core Web Vitals** — LCP/INP/CLS no verde (cruza com Barra 1); imagens em next-gen, lazy
- [ ] **i18n** (se multi-idioma) — `seo-geo`: hreflang válido, parity de conteúdo

> Free e offline: `seo-audit`, `seo-aeo-best-practices`, `ai-seo`, `web-quality-audit`, `firecrawl-seo-audit` (usa firecrawl). Dados reais de SERP/keyword/backlink (`seo-geo` scripts pagos, `backlink-analyzer`, plugin `seo-skills`) só quando o cliente paga o tier de dados.

## Modo auditoria (site existente)

Quando o site já existe, brief/direção/sistema/build já foram decididos — repetí-los é desperdício. Faça assim:

1. **Capture o estado.** Leia README/docs, `lib/data`, CSS/tokens, componentes. Veja a screenshot ou rode `npm run dev`. Entenda o que já está no ar.
2. **Minere referência só pra calibrar a barra.** Compare o site contra 3-5 sites premium do nicho no Top 3 global (Awwwards/FWA/Behance). Pergunta: onde fica abaixo do teto?
3. **Rode o Gate de 4 barras sobre o que existe.** A maioria dos sites "ok" passa a Barra 1 e reprova a 2 (Distinção), a 3 (Negócio) e a 4 (SEO/GEO) — é aí que mora o gap pros $1M. Não pare na competência.
4. **Verifique o que é estático vs vivo:**
   - Estático (lê código): distinção (conceito/tipo/composição), negócio (oferta/CTA/prova), conteúdo-real, acabamento, a11y de markup.
   - Vivo (precisa rodar): Performance (Lighthouse no deploy), Responsivo (mobile/tablet real), Motion (reveal/entrada em ação).
   - **Não declare PASS num item "vivo" só lendo código.** Rode ou marque `❓ precisa rodar`.
5. **Liste correções priorizadas** por barra (o que reprovou) e ofereça aplicar. Diga francamente em qual barra o site está parado.

Sinais objetivos baratos antes de tudo: `npm run typecheck`, `npm run lint`, `npm test`, `npm run build`.

⚠️ **Deploy ≠ código atual.** Lighthouse/auditoria no site ao vivo mede o que foi **deployado**, que pode estar defasado vs o código local. Antes de culpar o código por um achado do site vivo, confira se o deploy está em sincronia (ex.: o elemento reprovado existe no código?). Se defasado: a correção pode já estar feita — falta só redeploy.

⚠️ **O projeto pode mudar sob você.** Em site existente, outra sessão/pessoa pode estar refatorando ao mesmo tempo (ex.: migração de design system). Antes de editar, cheque o estado atual (qual sistema de classe/CSS está vivo? que arquivos mudaram?). Se um arquivo seu foi sobrescrito ou achar 2 sistemas convivendo → **pare e realinhe** em vez de empilhar edição. Não brigue com um writer concorrente.

⚠️ **Nunca deixe 2 design systems colidindo.** Se o site está migrando (ex.: `ik-` → `k-`), trate o sistema NOVO como fonte da verdade e **convirja**: porte a mudança pro sistema novo, remova duplicatas (componentes/CSS órfãos), apague o que ficou no sistema velho. 2 sistemas vivos = bug visual + manutenção dobrada.

## Erros comuns

- ❌ Codar antes de escolher a direção visual → vira template. **Direção primeiro.**
- ❌ Copiar um shot do dribbble inteiro → destile o princípio, não clone.
- ❌ Pular o sistema de tokens e ir "no olho" → inconsistência. **Tokens primeiro.**
- ❌ Lorem ipsum + imagem placeholder até o fim → conteúdo real desde cedo muda o design.
- ❌ "Tá bom o suficiente" sem passar no quality gate → o gate É o que separa de site comum.
- ❌ Estética genérica de IA (gradiente roxo, glass em tudo, layout central previsível) → use `frontend-design`.
- ❌ **Pular a fase Conceito e ir pro layout** → vira bonito-e-esquecível. Conceito primeiro, sempre.
- ❌ **Confundir competência com $1M** → passar a Barra 1 não basta. Sem Distinção + Negócio é site de $200k.
- ❌ **"Minerar" de cabeça sem fonte real** → puxe via firecrawl/WebFetch ou peça prints. Senão é invenção.
- ❌ **Entregar e sumir** → sem apresentação de valor (rationale/antes-depois) o cliente não enxerga os $1M.
- ❌ Tratar `ui-ux-pro-max` como fonte de inovação → ela é piso de competência (e app-leaning). Distinção vem de `frontend-design`.
- ❌ (auditoria) Declarar PASS em Performance/Responsivo/Motion só lendo código → rode no vivo ou marque `❓ precisa rodar`.
- ❌ (auditoria) Refazer brief/direção/sistema de um site que já existe → pule direto pro gate.

## Próximo passo

Termine cada fase confirmando antes de avançar. Ao final do build, rode o quality gate item a item e só então ofereça o ship.
