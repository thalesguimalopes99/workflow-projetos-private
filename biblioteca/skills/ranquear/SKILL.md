---
name: ranquear
description: >-
  Use quando o Thales quer ranquear/ser encontrado — site no Google (SEO), ser citado por IA (GEO/AEO — ChatGPT, Perplexity, Google AI Overviews, Claude), ou crescer/ser descoberto no Instagram. Triggers: "como ranqueio meu site", "aparecer no ChatGPT/Perplexity/AI Overviews", "otimizar pra SEO/GEO", "ser citado pela IA", "quero crescer no Instagram", "meu site não aparece no Google", "vale a pena essa tática de SEO?", "isso que o [fulano] falou funciona?". Também é o filtro cético: avaliar se uma tática/promessa de SEO/GEO faz sentido antes de aplicar.
---

# ranquear

Playbook **validado** pra ranquear em SEO (Google), GEO/AEO (busca por IA) e Instagram. Destilado de 56 vídeos curados (fontes de autoridade + 1 canal de hype como contraste) e cruzado: **o que várias fontes confiáveis repetem = regra de ouro; promessa isolada de canal de venda = flag**.

Esta skill é o **cérebro de estratégia + detector de BS**. Ela decide O QUE fazer e por quê; a EXECUÇÃO delega pras skills de SEO já instaladas (ver "Roteamento"). Base bruta e análises em `Desktop\wtf\Youtube\base-conhecimento\` (ver `references/fontes.md`).

## Regra nº1 — passar tática pelo filtro cético ANTES de aplicar

Todo o campo de SEO/GEO é cheio de folclore, correlação vendida como causa, e gente vendendo curso. Antes de recomendar ou aplicar QUALQUER tática — principalmente se veio de um vídeo/influencer/"hack" — rode ela por `references/testar.md`:
1. **Força da evidência?** Fonte primária (Google/Mosseri/leak) > estudo com dados > consenso de praticantes > opinião isolada > anedota/1 comentário.
2. **Contra as diretrizes?** Se viola política do Google/plataforma (comprar link, stuffar nome, horário falso, review self-serving) → NÃO recomendar. Risco de penalidade/suspensão.
3. **Como testar?** Toda tática séria tem um teste com grupo de controle. Se não dá pra testar e a fonte "garante ranking", é red flag.

Nunca apresente correlação como causa. Nunca prometa posição ("#1 garantido", "em 24h"). Rankeamento é probabilístico.

## Princípios validados (sobreviveram ao cruzamento de fontes)

1. **SEO não morreu — é +1 canal.** Google tem 93% do mercado, +21% buscas/ano, ~373× o volume do ChatGPT. Não é soma-zero. Não abandone SEO por GEO.
2. **Ranquear #1 no Google ≠ ser citado pela IA.** Jogos diferentes, **mesmos fundamentos**. Estar no top-10 dá só ~25% de chance de aparecer no AI Overview. Bom SEO é a base dos dois; a diferença é de estratégia, não de tática.
3. **Marca é o sinal mais forte agora.** Branded search alimenta o *site quality score* do Google (abaixo de 0.4 nem pega featured snippet — do leak); menções de marca superam backlinks/DR na correlação com AI Overviews. Investir em demanda de marca move os dois.
4. **GEO = ser mencionado no ecossistema, não ranquear #1.** A resposta da IA é síntese de muitas citações. Reddit é a fonte nº1 mais citada; YouTube nº2; Digital PR. Espalhe a mesma mensagem alinhada em muitos lugares confiáveis.
5. **Backlinks + Digital PR seguem a maior alavanca clássica** (Google ainda usa PageRank). Qualidade > quantidade (~25 links bons > milhares). PR reativa gera links que não se compra.
6. **Profundidade tópica > volume.** 1 categoria a fundo (90–180 dias), não muitas páginas rasas. 97% das páginas têm zero tráfego. Originalidade / information gain (foco declarado do Google) > tamanho.
7. **Pra IA: conteúdo extraível.** Resposta direta no início (answer-first), parágrafos curtos 1-assunto-por-bloco, headings, listas, tabelas, fatos/números específicos (semantic triples). A IA cita o *trecho*, não a página.
8. **Portões técnicos da IA** (diferentes do Google): AI crawlers **não rodam JavaScript** → server-side render obrigatório; buscam em tempo real → page speed vira portão (erro 499 no log); hosting/CDN **bloqueia bots de IA por padrão** → liberar GPTBot etc.
9. **Instagram virou motor de busca.** Otimize nome/@/bio/legenda/alt-text/topics com as palavras que o público digita. Viralidade = **rates, não reach**: watch time (mais forte) > like rate (seguidores) > send rate (não-seguidores). "Sem bala de prata" (Mosseri).
10. **Meça com ceticismo.** Resultados de IA são probabilísticos (variam por run) → rastrear share of voice/sentimento por tópico, múltiplas checagens, grupo de controle. Não confie em "best practice" sem teste.

## Decisão — qual objetivo?

| Objetivo do Thales | Carregue | Executa via (skills instaladas) |
|---|---|---|
| Ranquear no **Google** (SEO clássico, técnico, conteúdo, backlinks, local) | `references/seo.md` | `claude-seo:seo-audit`, `:seo-technical`, `:seo-content`, `:seo-schema`, `:seo-backlinks`, `:seo-local`, `web-quality-skills:seo` |
| Ser citado por **IA** (ChatGPT, Perplexity, AI Overviews, Claude) — GEO/AEO | `references/geo.md` | `claude-seo:seo-geo`, `seo-aeo-best-practices`, `claude-seo:seo-sxo` |
| Crescer / ser encontrado no **Instagram** | `references/instagram.md` | `social`, `instagram-creative-director` |
| **Avaliar uma tática/promessa** ("isso funciona?") | `references/testar.md` | — (é análise, não execução) |
| Ver **de onde veio cada afirmação** (rastreabilidade/credibilidade) | `references/fontes.md` | — |

Sempre carregue a reference do tema ANTES de agir — ela tem as práticas concretas, por-engine, com força de evidência e como testar. Este SKILL.md é só a orientação.

## O que o Google/plataformas dizem que NÃO funciona (não perca tempo)

- **GEO:** `llms.txt` e markdown files (estudo Profound: sem diferença); schema pra recuperação em LLM (experimento: ChatGPT trata como texto; Common Crawl remove); "uma estratégia AEO única pra todos os motores" (só 14% de overlap entre engines).
- **SEO:** densidade de keyword (1.500 SERPs, sem correlação — o que conta é cobertura); "conteúdo mais longo sempre ranqueia"; publicar todo dia; conteúdo 100% gerado por IA sem humano (sobe e desaba em 6–12 meses); meta description pra maioria das páginas (Google reescreve 60–70%).
- **Instagram:** "10x seguidores em 30 dias"/hacks; "algoritmo suprime pra forçar ads" (desmentido pelo Mosseri); keyword stuffing na legenda.
- **Contra diretrizes (nunca recomendar):** comprar/"roubar" backlinks, stuffar keyword no nome do GBP, marcar horário 24/7 falso, review schema self-serving, coaching de review roteirizado.

## Nota sobre "SEO com Claude / automação de IA"

A automação (Claude usando browser/ferramentas) **acelera o trabalho braçal** (auditoria, keyword-gap, competitor spying) mas **não muda o que ranqueia** — é uma camada sobre Ahrefs/SEMrush/GSC. Dois pontos reais e úteis dessa abordagem: (1) **grounding** — dar dado real (logar nas ferramentas) evita o LLM alucinar métricas; (2) **contexto** — um doc de contexto do negócio ("brain") melhora muito o output. Tudo que a IA gerar (auditoria, "fatores de ranking", contagens) **precisa de verificação manual** — ela erra, alucina e conta errado. Ver o contraste completo em `references/testar.md`.
