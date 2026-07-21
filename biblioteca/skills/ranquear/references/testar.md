# Filtro cético + como testar uma tática

Use isto ANTES de aplicar/recomendar qualquer tática de SEO/GEO — principalmente se veio de vídeo, influencer, "hack" ou promessa. O campo é cheio de correlação vendida como causa e gente vendendo curso.

## Framework de evidência (classifique a fonte)

Da mais forte pra mais fraca:
1. **Fonte primária** — Google (Search Central, Illyes, patentes), Mosseri, o **leak/exploit** do Content Warehouse. Peso máximo.
2. **Estudo com dados** — análise de N SERPs, experimento controlado (ex: Profound, Ahrefs 1st-party, os experimentos do Mark Williams-Cook).
3. **Consenso de praticantes** — várias fontes independentes de topo dizem o mesmo (Aleyda + King + Ahrefs...).
4. **Opinião isolada** — 1 praticante, sem dado. Trate como hipótese.
5. **Anedota / "funcionou pra mim" / 1 comentário de YouTube** — quase zero. Red flag se vendido como regra.

Nunca apresente 2–5 como se fosse 1. Se uma "regra" só tem anedota, diga isso.

## Os 4 testes rápidos (rode em qualquer tática)

1. **Evidência:** de qual nível acima? Se ≤4, é hipótese, não fato.
2. **Diretrizes:** viola política do Google/plataforma? (comprar link, stuffar nome do GBP, horário falso, review self-serving, cloaking) → **NÃO recomendar**, risco de penalidade/suspensão.
3. **Causa vs correlação:** a fonte inferiu de N pequeno (ex: "fatores de ranking" de 5 perfis)? Duração igual, número exato ("precisa de 5 links DR70"), "opportunity score" → falsa precisão.
4. **Testável:** dá pra montar experimento com controle? Se a fonte "garante ranking/posição/prazo" e não dá teste → red flag clássico. Rankeamento é probabilístico; ninguém garante #1.

## Como montar o teste (quando a tática passa nos 4)

- **Grupo de controle vs teste**: metade das páginas/perfis recebe a mudança, metade não. Só assim você isola o efeito de updates do Google e ruído.
- **Uma variável por vez.** Mudou 5 coisas, não sabe qual moveu.
- **Baseline + janela**: registre a posição/métrica antes; espere 2–8 semanas (local) / 4–12 (orgânico); local grid via Local Falcon; orgânico via GSC (impressões/posição por query).
- **Meça o certo**: muita "tática de GBP" (posts, atributos, resposta rápida) move **cliques/conversão**, não ranking — meça no Insights, não espere subir posição.
- **GEO é probabilístico**: múltiplas checagens/dia + média; share of voice por tópico, não 1 prompt.
- **Verifique output de IA manualmente**: auditoria automática alucina "keyword faltante", conta H1 errado, lê elementos JS errado. Confira contra o código-fonte.

## Detector de hype (sinais de que é venda, não método)

Aprendido dissecando 34 vídeos de um canal de "SEO com IA" (ver `ANALYSIS-hype-localseo.md`):
- 🚩 **Garantia de posição/prazo**: "#1 garantido", "em 24h/10min/5h". SEO ético não garante ranking.
- 🚩 **Métrica-herói absurda/inconsistente**: o mesmo case citado como "$1.7M", "$1.7 bilhão", "$2.8M" em vídeos diferentes = copy-paste, não resultado.
- 🚩 **Correlação como causa**: "fatores de ranking" de n=5; números exatos inventados.
- 🚩 **Conflito de interesse**: todo conteúdo é funil pra lead-magnet ("comente 'prompt'") → call com a agência. Os "alertas de risco" viram razão pra te contratar.
- 🚩 **"Grátis" enganoso**: "faça de graça com IA" mas exige Ahrefs (~$100/mês) + plano caro.
- 🚩 **Demo contradiz o pitch**: o vídeo mostra a ferramenta lenta/bugada enquanto narra "4 SEOs 24/7 por $20".
- 🚩 **Puffery de autoridade**: "#1 SEO global segundo [site self-serve]", "TED talk" (TEDx local), "X anos" — substitutos de evidência.
- 🚩 **Tática contra diretriz apresentada casualmente** como se fosse normal.
- 🚩 **Re-upload/duplicata**: mesma "biblioteca" rebatizada pra parecer volume.

Quando o Thales trouxer "vi um vídeo dizendo pra fazer X" → rode os 4 testes + detector, classifique a evidência, e responda: **vale / vale mas teste assim / não (viola diretriz ou é folclore)**. Seja direto.

## Contraste "SEO com IA/automação"

A automação (Claude com browser/ferramentas) **acelera trabalho braçal** (auditoria, keyword-gap, competitor spying) mas **não muda o que ranqueia**. Dois pontos reais: (1) **grounding** — logar nas ferramentas evita alucinar métricas; (2) **contexto** ("brain" do negócio) melhora o output. Mas: output sempre precisa de verificação manual; deixar a IA **executar ao vivo** em GBP/site é arriscado (sem QA/rollback, GBP suspende) — use draft/staging. "Vira um SEO de 14 anos" é marketing: contexto ≠ correção.
