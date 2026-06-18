# Synergy Pipelines — cadeias cross-recurso ponta-a-ponta

> **Pra quê:** o `ROUTING-MAP.md` roteia DENTRO de um squad. Este arquivo conecta
> **squads + skills + MCP + AIOX + processo** numa cadeia única por entregável composto.
> Leia quando o entregável for ponta-a-ponta (não cabe num squad só). Lazy-load: só
> quando for montar o pipeline. Invoque agent nativo via `Skill` → `<squad>:agents:<id>`.

## Regras universais (valem em TODA cadeia)
- **`briefing` sempre primeiro** — pedido raso → brief executável.
- **Pesquisa = padrão:** `competitor-profiling` (skill) + MCP `firecrawl` na fase de
  research de quase tudo (marca, launch, ads, GTM). Site/visual → `site-teardown` (pega código das refs).
- **`humanizer` (skill) roda DEPOIS de toda copy gerada por squad** — tira cara de IA. Universal.
- **`marketing-psychology` (skill) = camada** sobre copy/cro/oferta (Cialdini, vieses, framing).
- **Gate CREATIVE-OS** em todo visual: Awwwards Judge nota 1–10, < 9 → refatora.
- **Imagem/vídeo:** asset real/fornecido, Canva (brand/composição), Higgsfield (geração via MCP).
  ⚠️ a SKILL.md ainda diz "sem imagem IA / nano-banana proibido" — isso é nano-banana/Gemini;
  Higgsfield+Canva são o stack atual aprovado. Reconciliar a linha quando rever a skill.
- **Processo antes do especialista:** `superpowers:brainstorming` (criativo novo),
  `writing-plans`/`executing-plans` (multi-passo), `test-driven-development` (código).

---

## A. MARKETING / WEB CORE

### Site premium
`briefing(site-app)` → `competitor-profiling`+firecrawl+`site-teardown` (minerar refs+código)
→ tokens de marca (`brand-squad` se nova; senão usa existente) → `copywriting`(skill) das páginas
→ `marketing-psychology` (camada) → `humanizer` → `criar-site-premium` (maestro: conceito→direção→build;
puxa `frontend-design`, `ui-ux-pro-max`, motion `hf-gsap`) → `cro`(skill) revisa conversão
→ MCP `playwright` (QA visual) → `vercel` deploy → **gate CREATIVE-OS**.

### Landing page
`briefing(site-app)` → firecrawl refs → `copy-master`(headline-testing/offer) **ou** `copywriting`(skill)
→ `marketing-psychology` → `humanizer` → `brand-landingpage`(skill) **ou** `criar-site-premium`
→ `cro`(skill) → `playwright` → `vercel` → **gate**.

### Lançamento completo
`briefing` → `competitor-profiling`+firecrawl → `brand-squad`(new-brand-launch) *se marca nova*
→ `hormozi-squad`(new-product-launch: models→offers→launch→leads) → `copy-master`(launch-sequence)
→ `humanizer` → `storytelling`(investor-pitch p/ narrativa do lançamento)
→ `criar-site-premium`+`brand-landingpage` (página) → `traffic-masters`(new-facebook-campaign)+`ad-creative`(skill)
→ `data-squad`(full-product-launch: tracking + North Star) → **gate**.

### VSL / Sales letter
`briefing(criativo)` → `copy-master`(vsl-blueprint: stefan-georgi→jon-benson→todd-brown→blair-warren)
[camada Cialdini já embutida] → `humanizer` → *se vídeo:* Higgsfield (b-roll) + Canva → **gate**.

### Campanha de ads
`briefing(criativo)` → `competitor-profiling`+firecrawl (ad library) → `traffic-masters`(new-facebook-campaign
**ou** youtube-funnel) → `ad-creative`(skill: variações em escala) + `copy-master`(write-ad-copy: ângulos)
→ `humanizer` → Higgsfield/Canva (criativo visual) → `traffic-masters`:pixel-specialist (tracking)
→ :fiscal (budget) → :performance-analyst (leitura).

### Proposta comercial premium
`briefing(projeto)` → `hormozi-squad`(offers/pricing: engenharia da oferta) → `copy-master` (copy persuasiva)
→ `storytelling`(create-pitch) → `criar-proposta-comercial-premium`(skill) → `slides`/`design-system`
→ `humanizer` → **gate**.

### Conteúdo / social
`briefing(conteúdo)` → `content-strategy`(skill: pilares, calendário, clusters)
→ `content-research-writer`(skill: long-form com pesquisa+citações) **ou** `copy-master`(dan-koe/ben-settle p/ short)
→ `social`(skill: adapta LinkedIn/X/IG/TikTok + social listening) → `marketing-psychology` (hooks) → `humanizer`
→ `data-squad`(measure-growth) → Canva/Higgsfield (visual).

---

## B. MARCA / NARRATIVA

### Rebrand completo
`briefing(brand:rebranding)` → `competitor-profiling`+firecrawl
→ `brand-squad`(complete-rebrand: kapferer→ries→neumeier→miller→wheeler→naming)
→ :naming-strategist+:domain-scout *se renomear* → `storytelling`(brand-narrative)
→ `design`(logo SVG)+`design-system`(tokens) → `criar-site-premium` (site novo) → **gate**.

### Marca nova (dia zero)
`briefing(brand)` → firecrawl nicho → `brand-squad`(new-brand-launch: emily-heyward→naming→domain-scout→archetype→miller→wheeler)
→ `storytelling`(brand-narrative) → `design`(logo suite SVG)+`design-system`(tokens)
→ `criar-site-premium` → **gate**.

### Manifesto / movimento
`briefing(conteúdo)` → `movement`(full-build: fenomenologo→identitario→manifestador→movement-architect→estrategista-de-ciclo→analista-de-impacto)
→ `storytelling`(movement-campaign) → `copy-master`(email-nurture: andre-chaperon→ben-settle p/ espalhar)
→ `humanizer` → `data-squad`(community-first) → **gate**.

### Pitch a investidor
`briefing(projeto)` → `c-level-squad`(fundraising-prep: vision→coo→cmo→cto)
→ `storytelling`(investor-pitch: oren-klaff→nancy-duarte→kindra-hall) → `copy-master`(write-pitch-deck)
→ `slides`/`design-system` → `humanizer` → `advisory-board`(invest: dalio→munger→naval) *sparring* → **gate**.

### Storytelling de marca
`briefing(conteúdo)` → `storytelling`(brand-narrative: park-howell→kindra-hall→nancy-duarte→joseph-campbell)
→ `brand-squad`:donald-miller (StoryBrand) → `copywriting`(skill: aplicar nas páginas) → `humanizer`.

---

## C. SOFTWARE (AIOX)

### App / produto digital
`briefing(projeto)` → `superpowers:brainstorming`
→ `AIOX`(analyst → pm/po → architect → ux-design-expert)
→ `design-squad`(new-product-design: ux-designer→visual-generator→brad-frost→ui-engineer) + `ui-ux-pro-max`/`frontend-design`
→ `superpowers:writing-plans` → `AIOX`:dev + `superpowers:test-driven-development`
→ `AIOX`:data-engineer *se dados* (+ `supabase` MCP) → `AIOX`:qa + `webapp-testing`/`playwright`
→ `AIOX`:devops + `vercel` deploy. Docs de lib via MCP `context7`. **Gate:** `/code-review`.

---

## D. ESTRATÉGIA / NEGÓCIO

### Diagnóstico de negócio
`briefing(projeto)` → `hormozi-squad`(audit→advisor→*especialista por restrição*)
→ `data-squad`(analyze-data/measure-growth) → `c-level-squad`:vision-chief (síntese)
→ `advisory-board` *se decisão difícil*.

### Fundraise
`briefing(projeto)` → `c-level-squad`(fundraising-prep: vision→coo→cmo→cto)
→ `storytelling`(investor-pitch) → `copy-master`(write-pitch-deck) → `advisory-board`(invest) → `slides` premium.

### GTM (go-to-market)
`briefing(projeto)` → `competitor-profiling`+firecrawl → `c-level-squad`(plan-go-to-market via cmo-architect)
→ `hormozi-squad`(offers+leads) → `traffic-masters`(create-ad-strategy) → `content-strategy`(skill)
→ `data-squad`(North Star).

### Decisão difícil / sparring
`advisory-board`(board-chair → sequence por tema: invest / scale / culture / founder / contrarian)
→ `c-level-squad` *se for execução* → síntese.

### Pricing / escala
`briefing(projeto)` → `hormozi-squad`(pricing **ou** scale **ou** models)
→ `data-squad`:peter-fader (CLV) → `c-level-squad`:coo-orchestrator (ops)
→ `advisory-board`(scale: reid-hoffman→peter-thiel→derek-sivers).

---

## Onde as 10 skills novas (skills.sh) plugam
| Skill | Entra em |
|---|---|
| `copywriting` | copy de páginas (site, landing, storytelling de marca) |
| `marketing-psychology` | camada sobre copy/cro/oferta em qualquer cadeia |
| `social` | conteúdo/social, distribuição de launch |
| `content-strategy` | conteúdo/social, GTM |
| `content-research-writer` | long-form/blog dentro de conteúdo |
| `cro` | site premium, landing (revisão de conversão) |
| `ad-creative` | campanha de ads, lançamento |
| `competitor-profiling` | fase research: marca, launch, ads, GTM |
| `humanizer` | DEPOIS de toda copy de squad (universal) |
| `brand-landingpage` | landing (alternativa/builder ao criar-site-premium) |
