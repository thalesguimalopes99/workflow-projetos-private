# SEO clássico 2026 (Google) — técnico, conteúdo, backlinks, local

Consenso de autoridade + dados do Google API leak / exploit (Content Warehouse, via Mark Williams-Cook). Legenda: **[Google]** · **[leak]**=dados reais do vazamento/exploit · **[estudo]** · **[consenso]** · **[opinião]**.

## As maiores alavancas (por peso de evidência)

1. **Backlinks / PageRank** [leak + estudos] — ainda o maior driver; ~25% da equação. Google usa uma versão do PageRank (confirmado no leak). Priorize aquisição; não gaste 100% do tempo em conteúdo sem promoção. **Qualidade > quantidade**: ~25 links bons > milhares baratos (link velocity suspeita = penalidade).
2. **Demanda de marca / branded search = site quality score** [leak + patente] — o quality score NÃO correlaciona com links; correlaciona com **quantas queries referenciam seu site pelo nome** e quanto você é escolhido no SERP. **Abaixo de 0.4 = inelegível pra featured snippet / People Also Ask.** Existe score sitewide (Google só negou domain-wide). → Invista em brand marketing e tráfego direto. É o sinal mais subestimado.
3. **Digital PR** [caso documentado] — links que não se compram, com efeito cascata (1 história → dezenas de veículos citam). Caso Rehabs UK: PR reativa (<24h, gancho de notícia + Google Trends) → 70+ links (Guardian, .gov) → de centenas a ~60k visitas/mês, superando o NHS, com conteúdo quase inalterado. Faça: monitorar RSS/notícias/Trends + responder jornalistas em <24h (HARO/feature.com).
4. **Topical authority profunda** [consenso] — 1 categoria "um km fundo" por 90–180 dias, não muitas páginas rasas. Backlinko: 300k visitas/mês com só 557 páginas. Clusters/entity hubs + internal links descritivos.
5. **E-E-A-T + originalidade** [Google] — experiência de primeira mão que a IA não tem é o diferencial (oficial). Gary Illyes: foco dos próximos anos = **originalidade / information gain**. Mostre autor/credenciais/data, casos, dados, citações. YMYL exige fontes de alta autoridade.

## Fundamentos técnicos [consenso]

- Crawlability, sitemap acessível, robots.txt correto, HTML5 semântico, mobile-friendly, <2s. Se o site é lento/quebrado, os bots param de voltar.
- **Sitemaps separados/dedicados indexam mais rápido** que um grande [experimento] → sitemap dedicado pra páginas novas.
- **last-mod = confiança binária** [leak]: freshness fake → Google descarta o sinal. Canonicals ruins são ignorados.
- Core Web Vitals = tiebreaker fraco [Google/Illyes]; o dano real é bounce, não o score. Retorno decrescente em perseguir PageSpeed.
- Schema (JSON-LD: Organization, Article, FAQ) alimenta rich results — vale no Google (≠ GEO). Valide no Rich Results Test. **Review schema self-serving no próprio site é proibido** pela política.

## Conteúdo e keywords

- **Keyword = TÓPICO, não densidade** [estudo] — 1.500 SERPs: densidade não correlaciona; **cobertura de tópico** sim. Comece bottom-of-funnel (alta intenção) → suba o funil.
- **Intent / page-type matching** — o tipo da sua página deve casar com o das top-ranking (não ranquear homepage de marca pra intenção comercial). Títulos de alta intenção ("emergency AC repair Dallas same-day" > "personal injury attorney").
- **Money pages em striking distance** [tática de alto ROI] — exporte 3 meses do GSC, ache keywords em **posição 4–15**, otimize pro top-3. Baixo esforço, alto retorno.
- **Internal linking descritivo** — anchors com o tema real ("commercial solar panels"), não "read more". Barato, alto ROI, corrige páginas órfãs.
- **Ownership de SERP** — pra queries de AÇÃO/transacionais (calculator, checker, serviço) a IA não resolve → SEO tradicional vence e os cliques fluem. Filtre essas queries.

## SEO local (Google Business Profile) — núcleo legítimo

Tudo abaixo é pré-IA, documentado, testável (do canal de hype, filtrado do lixo):
- **Categoria primária do GBP = a dominante entre os top-3 do map-pack.** Fator local dos mais fortes. Adicione secundárias relevantes.
- **Reviews:** quantidade + qualidade + recência correlacionam com ranking local. Campanha genuína; nunca falsos.
- **Consistência NAP** (nome/endereço/telefone) entre site e GBP.
- **Páginas serviço+cidade** genuinamente únicas (landmarks/FAQs locais reais) — NÃO template com cidade trocada (vira doorway page penalizável).
- **Proximidade** é fator dominante (mas não falseie endereço).
- Delegue execução a `claude-seo:seo-local` / `:seo-maps`.

## Mitos derrubados (não faça)

- "SEO morreu" (Google +21%/ano, 93% do mercado). · "Precisa de muito conteúdo/publicar todo dia" (97% das páginas: zero tráfego). · "Densidade de keyword" · "Mais longo = melhor" · "Backlinks não importam" (falso — leak confirma). · "Top-10 garante AI Overview" (só ~25%). · Conteúdo 100% IA sem humano ("Mount AI": sobe e desaba em 6–12 meses).
- **Contra diretrizes (nunca):** comprar/"roubar" links, stuffar keyword no nome do GBP, horário 24/7 falso, review schema self-serving, keyword-density stuffing.
- Não surte com micro-mudança de ranking: a patente "rank transition function" rebaixa temporariamente pra pegar manipulação. Jogue o longo prazo.

## Execução → skills instaladas

`claude-seo:seo-audit` (auditoria completa) · `:seo-technical` · `:seo-content` · `:seo-schema` · `:seo-backlinks` · `:seo-local`/`:seo-maps` · `:seo-sitemap` · `web-quality-skills:seo` · `schema`. Sempre **verifique manualmente** o output de auditoria automática (a IA erra contagens, alucina "keywords faltantes", lê elementos JS errado).

Rastreabilidade: `fontes.md` + `ANALYSIS-seo-geo.md` (v14–17: leak/experimentos) e `ANALYSIS-hype-localseo.md` (local, filtrado).
