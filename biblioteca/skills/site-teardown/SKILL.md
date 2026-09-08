---
name: site-teardown
description: >-
  Use SEMPRE que for minerar uma referência de site/landing/componente para APRENDER e TEMPLAR — não só descrever ou tirar print. Dispara quando a pessoa manda um link de referência (awwwards, dribbble, 21st.dev, pinterest, concorrente do nicho) e quer entender COMO o site é feito, replicar um efeito/animação/layout, ou "clonar pra aprender". Também ative dentro do fluxo de criar-site-premium na fase de mineração, sempre que uma referência merecer desconstrução profunda. A regra de ouro: screenshot trava no "vibe gap" (~50%) — pegue o CÓDIGO real (HTML + CSS + JS) pra ver o como, não só o quê.
---

# Site Teardown — desconstruir referência pra aprender e templar

Transforma "achei esse site lindo" em **"sei como ele faz e consigo recriar do meu jeito"**. O valor não está em copiar pixel — está em **pegar o código real** (HTML + CSS + JS inteiros), entender as técnicas por trás dos efeitos, e absorver isso como repertório pro nosso build. Cada teardown te educa: vira ferramenta nova na caixa.

## O problema que isso resolve (o "vibe gap")

Mostrar screenshot pro Claude e pedir "faça parecido" trava em ~50%. Print é um meio visual; o Claude faz tudo em código. Existe uma tradução lossy: ele *adivinha* como o efeito foi feito. Resultado: "mais ou menos perto", e você fica preso prompt-print-prompt-print sem nunca cravar.

**A saída é ir abaixo da superfície:** pegar o HTML + os arquivos CSS e JS *inteiros* da referência. Aí o Claude lê o "livro de receitas" real — o mesmo que o site usa — e consegue (a) replicar com precisão e (b) te explicar como funciona. Você sai sabendo.

## Princípio: aprender roubando dos pros (não plagiar)

Isto **não** é "copia o site e chama de seu". É: achar referências que você curte → desconstruir → usar como **template/baseline** que você reinventa com seu spin. Como em qualquer ofício: vê o que o pro faz, tenta emular, aprende muito, e com o tempo dá sua cara. O ganho duplo é templating **+** educação: você passa a reconhecer técnicas e a ter vocabulário pra pedir o que quer.

## As 3 partes de um site (modelo mental)

- **HTML = ossos** — a estrutura, como o conteúdo é organizado.
- **CSS = roupa** — o estilo: cor, layout, tipografia, efeitos visuais, animações.
- **JS = músculos** — o comportamento: o que acontece em scroll, click, hover, parallax.

Teardown bom olha as 3. A maioria do "como fizeram isso?" mora no CSS (animações, gradientes, glass, grid) e no JS (scroll-triggers, GSAP, observers).

## Fluxo de teardown

### 1. Pegue o CÓDIGO — não o screenshot
Use `firecrawl` (primário). Screenshot só complementa, **nunca** substitui o código.

- **HTML inteiro:** `firecrawl_scrape` com `formats: ["rawHtml"]` na URL da ref. (Equivale ao `Ctrl+U` do navegador, mas trazido pro contexto.)
- **Achar os assets:** no fim do `rawHtml`, identifique os `<link rel="stylesheet" href="...">` (CSS) e `<script src="...">` (JS). Geralmente no `<head>` e no fim do `<body>`.
- **CSS e JS inteiros:** `firecrawl_scrape` em cada URL de `.css` e `.js` com `formats: ["rawHtml"]` (ou `markdown`) pra puxar o **conteúdo completo** do arquivo.
- **Opcional — visual de apoio:** `formats: ["screenshot"]` (fullPage) só pra ancorar a leitura.

⚠️ **Por que NÃO usar WebFetch puro pra isso:** WebFetch chama um modelo menor que **resume** a página e devolve o resumo — você perde o CSS/JS específico que é justamente o que ensina. Para teardown, precisa do arquivo **inteiro**. Use firecrawl com `rawHtml`.

⚠️ Se o site é SPA/render-no-cliente (Next/React) e o `rawHtml` vier vazio de conteúdo, use `firecrawl_scrape` com `waitFor` (ms) e/ou `actions` de scroll pra renderizar antes de capturar.

### 2. Dê o código ao Claude e mande desconstruir
Junte HTML + CSS + JS no contexto e peça análise dirigida. Não aceite "tá bonito" — pergunte o COMO:

- "Como funciona este background/efeito? Que técnica?"
- "Como fizeram a animação de scroll? É GSAP, Intersection Observer, CSS scroll-driven?"
- "Que estrutura de grid/layout sustenta isto?"
- "Quais variáveis CSS / design tokens eles usam?"

### 3. Identifique técnica → efeito
Mapeie cada efeito que você quer à técnica que o produz (ex: "header que some no scroll = IntersectionObserver + transform/opacity"; "fundo com profundidade = gradiente em camadas + blur + noise"). Esse mapa é o aprendizado que fica.

### 4. Adapte com seu spin (não cole cru)
Porte a técnica pro nosso site e ajuste à nossa direção (paleta, conceito, marca). Reimplemente no nosso código — é template/baseline, não cópia. Peça ao Claude pra aplicar a técnica no **nosso** contexto, não pra colar o trecho deles.

## Fontes canônicas pra teardown

| Fonte | O que desconstruir |
|---|---|
| **awwwards.com** | O teto. Sites premiados do nicho → técnicas de ponta (motion, WebGL leve, composição) |
| **dribbble.com** | Micro-interações e detalhes de UI |
| **21st.dev/community/components** | Componentes React/Tailwind prontos — pegue o código do componente direto |
| **pinterest** | Mood/atmosfera (mais visual; teardown raso, complementa com print) |
| **godly.website** | Scroll infinito de designs fortes |
| **Concorrentes diretos do nicho do projeto** | Entender o padrão do mercado-alvo antes de subir a barra |

Antes de minerar: **entenda escopo + nicho** do projeto (pra quê é o site, o que ele faz) — isso decide quais referências valem teardown.

## Integração com criar-site-premium

Esta skill é o braço de **mineração profunda** do `criar-site-premium`. Na fase 3 (Mineração + direção), quando uma referência merece mais que "destilar princípio de cabeça", chame `site-teardown` pra pegar o código real. O fluxo maior (conceito → direção → tokens → build → gate) continua em `criar-site-premium`; aqui você só extrai e aprende a técnica.

## Limites (nível 7 — fora de alcance hoje)

Sites de WebGL/shaders/3D custom (muitos "site of the day" do awwwards) **não** dão teardown útil — `rawHtml` traz um canvas e bundles minificados/ofuscados. São arte de time de design, não templáveis via scrape. Reconheça quando a ref está nessa fronteira e não gaste tempo: capture como inspiração visual e siga.

## Erros comuns

- ❌ Mandar só screenshot pro Claude e esperar precisão → vibe gap, trava em ~50%. **Pegue o código.**
- ❌ Usar WebFetch (resume) achando que pegou o CSS/JS → pegou um resumo. Use firecrawl `rawHtml` no arquivo inteiro.
- ❌ Esquecer de puxar os arquivos `.css`/`.js` linkados → só o HTML não mostra os efeitos. Os efeitos moram no CSS/JS.
- ❌ Colar o trecho deles cru no nosso site → é template pra aprender e adaptar, não plágio. Dê seu spin.
- ❌ Tentar teardown de site WebGL/3D ofuscado → não rende; trate como inspiração visual.
- ❌ Minerar sem entender nicho/escopo → referência errada. Escopo primeiro.
