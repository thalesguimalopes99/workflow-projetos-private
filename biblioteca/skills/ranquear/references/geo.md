# GEO / AEO — ser citado por IA (ChatGPT, Perplexity, Google AI Overviews, Claude, AI Mode)

Consenso de fontes de autoridade (Ahrefs, iPullRank/Mike King, Aleyda Solís, Google, Ethan Smith/Graphite, SparkToro). Legenda: **[Google]**=fonte primária · **[estudo]**=dados citados · **[consenso]**=várias fontes independentes · **[opinião]**=praticante.

## O jogo do GEO em 1 frase

A resposta da IA é uma **síntese de muitas citações**, não 1 link azul. Você não quer "ranquear #1" — quer ser **mencionado o máximo de vezes** (share of voice) nas fontes que a IA lê. Startup pode ser citada amanhã via 1 boa menção; não precisa de domain authority madura.

## Como funciona (mecanismo) — query fan-out [Google, confirmado]

O motor expande a pergunta em dezenas de sub-queries (implícitas, explícitas, especulativas), busca páginas que ranqueiam pra cada uma, e costura a resposta. AI Overviews ~5–10 sub-queries; ChatGPT ~3–7; AI Mode 20–100. **Cada sub-query onde você aparece = 1 bilhete de rifa.** → Cobrir muitos ângulos/perguntas de um tópico multiplica chances. Ferramenta: Qforia (Mike King) ou interseção de keywords das URLs já citadas.

## Práticas validadas (ordenadas por consenso)

1. **Consenso off-site no ecossistema** [consenso forte] — espalhe a mesma mensagem alinhada em Reddit + YouTube + Digital PR + review sites + diretórios. A IA busca consenso entre fontes.
   - **Reddit = fonte nº1 citada** [estudo] em todas as plataformas. Conta real, diga quem é/onde trabalha, resposta útil em threads que já são citadas. 5 bons comentários > 10.000 spam.
   - **YouTube = nº2 citada** [estudo]. Google transcreve tudo. Poucos fazem vídeo de nicho B2B de alto valor → oportunidade. Sem risco de moderação de comunidade.
2. **Menções de marca com contexto** [estudo Ahrefs] — "Marca X é [categoria] e faz [Y]" em muitos lugares. Superam backlinks/DR na correlação com AI Overviews. Shift de links → menções.
3. **Conteúdo extraível** [consenso + prova mensurável] — a IA seleciona um *chunk* que caiba na resposta (passage indexing). Demo cosine-similarity: dividir 1 parágrafo em 2 (1 assunto cada) +15% relevância. Faça: quebrar paredões de texto, 1 tópico por seção, headings como fronteiras, tabelas/listas que a IA cita verbatim.
4. **Answer-first + 1ªs frases entity-rich** [consenso praticantes] — AI Overviews tendem a citar as 1–2 primeiras frases. Modelo: resposta curta → por que importa → dado/exemplo. FAQ com resposta imediata.
5. **Cobrir a jornada inteira / cauda longa** [Graphite] — a cauda é MAIOR em chat que em search (~25 palavras/prompt vs ~6 no Google); perguntas nunca feitas antes. 60% das respostas de IA vêm de FAQ. Otimize help center (subdiretório, não subdomínio; cross-link; preencha use cases obscuros). Se você é a única fonte que responde, vence.
6. **Semantic triples + densidade de evidência** [opinião, fundado em IR] — frases sujeito-predicado-objeto com números/datas/fatos verificáveis. Facilita extração.
7. **Original research / dados próprios** [estudo] — pesquisa original = 3× mais citações (BuzzSumo). Information gain: diga algo que ninguém disse. Publique benchmarks/surveys como ativos estruturados.
8. **Tabelas / comparações / "X alternatives" / "X vs Y"** [consenso] — a IA extrai células e cita páginas de comparação/roundup/review pra queries "best/top/vs/alternative". Consiga review em roundups de terceiros.
9. **Presença em bases estruturadas** [consenso] — Wikipedia/Wikidata, Crunchbase, G2, Capterra, GBP, perfis sociais consistentes. Alimentam o knowledge graph.
10. **Freshness real** [consenso] — data visível + conteúdo de fato atualizado (motores sem índice confiam na data exibida). Não só trocar a data.
11. **Citation-worthy e ON-BRAND** [Aleyda] — só compõe autoridade se a marca é reconhecida por aquilo. Alavanque experts internos; NÃO persiga tráfego genérico off-brand (punido em core updates).

## Portões técnicos (diferentes do Google — CRÍTICO)

- **AI crawlers NÃO rodam JavaScript** [Aleyda, forte] → conteúdo/nav client-side é invisível. Sirva HTML puro (server-side render).
- **Page speed = portão** [King, caso real] → ChatGPT/Perplexity buscam em tempo real; se lento, desistem e logam **erro 499**. Nenhuma ferramenta SEO sinaliza isso — cheque logs.
- **Não bloquear bots de IA** [Aleyda, caso real] → hosting/CDN bloqueia GPTBot etc. por padrão. Cheque robots.txt e regras de CDN; faça opt-out do bloqueio.
- **Meta description + slug semântico** [estudo Profound] — pra LLM, o slug muito relacionado à query = +11,4% citações (o oposto do Google, onde slug é irrelevante). Vale pra páginas NOVAS; não mude URLs antigas.

## Como ranquear em cada engine (elas divergem — só 14% de overlap)

- **Google AI Overviews:** cita YouTube/Reddit/Quora; roda sobre o ranking clássico (esteja no top-10, mas isso dá só ~25% de chance). Fan-out ~5–10.
- **ChatGPT:** cita publishers/news (DR mediana ~90); busca em tempo real (Bing index) → page speed + server-side importam muito. Cauda longa.
- **Perplexity:** cita sites que já ranqueiam no Google (~28% overlap com Google) → bom SEO clássico ajuda direto aqui.
- **AI Mode (Google):** fan-out massivo (20–100), infra própria + memória paramétrica.
→ **Não existe 1 estratégia AEO única.** Priorize por onde seu público pergunta.

## Medição

Probabilístico. Rastreie **share of voice + sentimento por TÓPICO** (não prompt isolado), múltiplas checagens/dia + média, grupo de controle vs teste. Extraia as citações de uma resposta de IA → sua marca aparece? Se não, liste os domínios citados e consiga menção neles. Ferramentas: Ahrefs Brand Radar, AI visibility reports (Ubersuggest), Profound.

## Não perca tempo (sem evidência)

`llms.txt` e markdown files (estudo: sem diferença); schema pra LLM (experimento: tratado como texto puro; Common Crawl remove HTML); cloaking/servir markdown pra bots; assumir que top-10 garante AI Overview.

## Divergências entre fontes (honesto)

- **Schema:** King usa por convicção; MWC (experimento) mostra ChatGPT ignorando. Veredito: schema ajuda rich results no Google (vale), mas sem evidência de que LLM lê. Não priorize schema como tática de GEO.
- **É só SEO?** Ethan Smith/OpenAI: "só faça conteúdo bom". King: estratégia diferente ("relevance engineering"). Veredito prático: fundamentos são iguais, a *estratégia de distribuição* muda (menções > backlinks).
- **AEO vs GEO (nome):** dá no mesmo; o mercado usa GEO.

Rastreabilidade completa (qual vídeo disse o quê): `fontes.md` + `Desktop\wtf\Youtube\base-conhecimento\ANALYSIS-seo-geo.md`.
