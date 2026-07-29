# Criando Plataformas com Integração API | Lovable

Trilha Lovable | 7 aulas | ~24 min | iniciante

> Ensina o que é uma API (e um webhook), e leva você a construir no Lovable um app real que envia a foto de um prato para a API da OpenAI e devolve a análise nutricional.

## O que você sai sabendo fazer

- Explicar o papel de uma API e de um webhook e decidir qual usar para conectar um app a um serviço externo (pagamento, mapas, calendário, WhatsApp, LLM).
- Criar conta na plataforma de API da OpenAI, gerar uma API key em Settings e adicionar créditos em Billing.
- Usar o ChatGPT como gerador de prompt: descrever a ideia em linguagem simples e receber um prompt técnico e estruturado para colar no Lovable.
- Construir no Lovable um web app de duas telas (upload de imagem → tela de resultados) que consome a API da OpenAI para visão.
- Depurar erro de execução no Lovable pedindo diagnóstico pelo chat antes de mandar implementar a correção (economiza créditos).
- Identificar quando a chave de API pode ficar no front-end (só em aprendizado) e quando ela precisa ir para o back-end/Supabase.

## Stack e ferramentas

- **Lovable** — construção do web app (interface + lógica no front-end).
- **API da OpenAI** — modelo com análise de imagem; chave gerada em Settings, créditos em Billing.
- **ChatGPT** (ou Claude/Gemini) — para redigir o prompt que vai para o Lovable e para ler documentação de API.
- Citados como alternativas/possibilidades, não usados no projeto: Gemini, Claude, Asaas, Stripe, Google Calendar, Cal.com, Z-API, Evolution API, Google Maps, Mapbox, Apify, RapidAPI, Google Sheets, Supabase, LinkedIn API.

## Pré-requisitos

- Conta no Lovable (com créditos — o projeto consome ~2,7 créditos).
- Conta na plataforma de API da OpenAI com cerca de US$ 5 em créditos.
- Familiaridade básica com a interface do Lovable (o curso não ensina o básico da ferramenta).

## Aula a aula

### 1.1 - Introdução ao Módulo (00:00:45)
- **Resumo:** Abertura do módulo de APIs. O instrutor posiciona a promessa: aprender API na prática para conectar o app a qualquer outro sistema da internet — pagamentos, mapas, OpenAI. Anuncia que haverá um resumo conceitual e depois um case real construído do zero.
- **Pontos-chave:**
  - Entender API é pré-requisito para criar software, aplicativos e automações.
  - Estrutura do módulo: teoria condensada primeiro, case prático em seguida.
- **Link:** https://flix.nocodestartup.io/m/lessons/4862

### 1.2 - Resumo sobre APIs (00:05:15)
- **Resumo:** Revisão conceitual de API (Application Programming Interface) como interface de comunicação entre sistemas, usando a analogia cliente/garçom/cozinha — o front-end pede, a API leva e traz. Mostra que dá para ler, criar e editar dados do outro lado, sempre conforme a documentação de cada ferramenta, e passa um catálogo de casos de uso reais. Fecha diferenciando API de webhook.
- **Pontos-chave:**
  - Analogia: cliente = sua aplicação/front-end, garçom = API, cozinha = serviço externo.
  - Exemplos citados: LinkedIn (GET de posts, agendar post), Asaas (assinatura recorrente), OpenAI (clone de chat), Mapbox (mapas).
  - Categorias cobertas por API: IA, pagamentos, calendário, WhatsApp, mapas, marketplaces de API (Apify, RapidAPI), CRM/ERP.
  - Toda API costuma exigir uma chave — ela é secreta, porque quem tiver acesso gasta os seus créditos. Há APIs gratuitas e pagas.
  - Webhook é o inverso: em vez de você pedir, o serviço avisa sozinho quando um evento acontece (pagamento confirmado, resposta no WhatsApp).
- **Link:** https://flix.nocodestartup.io/m/lessons/4863

### 2.1 - Planejamento do Projeto: Aplicativo de Análise de Refeições (00:03:09)
- **Resumo:** Define o case: clonar de forma simplificada o Cal AI — app em que o usuário fotografa o prato e recebe calorias, proteínas, carboidratos, gorduras e um score de saúde. O instrutor desenha o fluxo em duas telas e explica a decisão de arquitetura: sem back-end, sem banco, chamando a OpenAI direto do front. Também separa ChatGPT (interface de chat) de API da OpenAI (acesso programático ao LLM, cobrado por crédito).
- **Pontos-chave:**
  - Referência do case: Cal AI, citado como app criado por um garoto de 17 anos e faturando cerca de US$ 1 milhão/mês.
  - Escopo deliberadamente simples: só front-end no Lovable, sem automações e sem banco de dados.
  - ChatGPT ≠ API da OpenAI: para construir sistemas você precisa da API (OpenAI, Gemini ou Claude) e de créditos.
  - Aviso explícito: deixar a chave de API no front-end NÃO é boa prática — é só didático; o lugar correto é o back-end/Supabase, tratado em módulo posterior.
- **Link:** https://flix.nocodestartup.io/m/lessons/4864

### 2.2 - Configurando a API da OpenAI (00:03:41)
- **Resumo:** Passo a passo do setup da OpenAI: acessar a plataforma de API (não o site do ChatGPT), navegar rapidamente pela documentação e API reference, e gerar a chave em Settings → API keys, nomeando-a para o projeto. Em seguida mostra o Billing e o valor mínimo recomendado de créditos. Fecha com a orientação de como lidar com documentação de qualquer outra API.
- **Pontos-chave:**
  - Caminho: plataforma da OpenAI → engrenagem (Settings) → API keys → criar nova chave; copiar e guardar em local seguro na hora, pois será usada depois.
  - Billing: adicionar US$ 5 já é suficiente para bastante uso em apps, automações e agentes.
  - Para qualquer outra API: ler a documentação para saber se é gratuita, como cobra e como gerar a chave.
  - Atalho prático: mandar o link da documentação para o ChatGPT e deixar ele traduzir para o prompt técnico — mas entenda o básico, não fique alienado do que está acontecendo.
- **Link:** https://flix.nocodestartup.io/m/lessons/4865

### 2.3 - Criando o Aplicativo no Lovable (00:04:37)
- **Resumo:** Mostra o fluxo de gerar o prompt no ChatGPT antes de tocar no Lovable. O instrutor escreve um pedido curto descrevendo objetivo, telas, design e a exigência de guardar a chave no front-end sem Supabase; o ChatGPT devolve um prompt estruturado (objetivo, páginas, validações, ações, estilo de UI, tipografia, estados, dados). Ele cola esse prompt no Lovable, remove trechos desnecessários e gera o app.
- **Pontos-chave:**
  - No prompt para o ChatGPT: descrever dor/funcionalidade, tela 1 (upload) e tela 2 (resultados em cards), design clean e apenas light mode.
  - Instrução obrigatória no prompt: "não utilize Supabase" e "chave de API armazenada direto no front-end" — senão o Lovable insiste em puxar Supabase por segurança.
  - Para projetos maiores, o instrutor recomenda o framework da NoCode Startup (dores, funcionalidades, custos, ferramentas, banco de dados, regras de negócio, concorrentes) em vez do atalho.
  - Geração de app não é determinística: o mesmo prompt produz resultados diferentes a cada vez.
  - Custo observado: 2 créditos do Lovable para gerar a primeira versão; em caso de erro na geração existe o botão "Try to fix".
  - O app já nasce com um campo para colar a chave da OpenAI e salvá-la.
- **Link:** https://flix.nocodestartup.io/m/lessons/4866

### 2.4 - Testando o Aplicativo no Lovable (00:05:14)
- **Resumo:** Teste real ponta a ponta: colar a chave da OpenAI no app, salvar e subir uma foto de hambúrguer. A primeira análise falha com erro; o instrutor demonstra o método de depuração — descrever o erro no chat do Lovable para que ele investigue os logs e proponha um plano antes de autorizar a correção. Depois de corrigido, o app analisa duas fotos com sucesso e mostra o resultado completo.
- **Pontos-chave:**
  - Fluxo técnico confirmado: foto → requisição para a API da OpenAI → modelo analisa a imagem → JSON volta e é renderizado no front-end.
  - Erro encontrado: falha de parsing da resposta (o retorno vinha dentro de bloco de código), diagnosticado pelo próprio Lovable via logs.
  - Técnica de economia: primeiro perguntar/investigar no chat (sem gastar crédito) e só então mandar "implementar a correção".
  - Saída do app: calorias aproximadas (~850 no hambúrguer), proteínas, gorduras, carboidratos, fibras, açúcares, sódio, itens detectados, porção, observações adicionais e índice de confiabilidade (80% no segundo teste).
  - Extras gerados: baixar o JSON, copiar um resumo e reanalisar com observações adicionais.
  - Custo total: 2,7 créditos do Lovable (2 na criação + 0,7 na correção).
- **Link:** https://flix.nocodestartup.io/m/lessons/4867

### 2.5 - Finalização (00:01:21)
- **Resumo:** Fechamento do módulo consolidando o método reproduzível para qualquer API, não só a da OpenAI. O instrutor reforça a sequência: desenhar o projeto, buscar a documentação da API escolhida, transformar isso em prompt com ajuda do ChatGPT, construir no Lovable e ajustar. Menciona que projetos maiores devem seguir o framework da casa.
- **Pontos-chave:**
  - Passo a passo padrão: desenhar → documentação da API → prompt elaborado no ChatGPT → Lovable → testar e ajustar.
  - Enviar o link da documentação da API ao ChatGPT melhora a qualidade do prompt gerado, porque ele consegue acessá-la.
  - O mesmo método serve para APIs de pagamento, calendário, mapas etc.
- **Link:** https://flix.nocodestartup.io/m/lessons/4868

## Pegadinhas e insights

- **Chave de API no front-end é dívida consciente.** O instrutor avisa duas vezes que essa é uma escolha didática para simplificar o primeiro projeto; em produção a chave vai para o back-end/Supabase. Se você reaproveitar esse app, mova a chave antes de publicar.
- **O Lovable "briga" com você para colocar Supabase.** Se o prompt não proibir explicitamente, ele tenta adicionar Supabase por conta própria por questão de segurança.
- **Confundir ChatGPT com API da OpenAI é o erro clássico.** São produtos e modelos de cobrança diferentes; para construir sistemas você precisa da plataforma de API, com créditos separados da assinatura do chat.
- **Erro de parsing na resposta do LLM é esperado.** A resposta pode vir embrulhada em bloco de código e quebrar o front. Tratar isso faz parte do trabalho — não é sinal de que a integração está errada.
- **Debug barato:** perguntar antes de mandar corrigir. Investigar pelo chat não consome crédito; só a implementação da correção consome.
- **Geração não é determinística.** Rodar o mesmo prompt não devolve o mesmo app — não espere reproduzir a tela do vídeo pixel a pixel.
- **Números citados:** US$ 5 de crédito na OpenAI cobrem bastante uso; o app inteiro custou 2,7 créditos no Lovable.
- **A chave é um segredo com custo direto.** Quem obtiver sua API key gasta os seus créditos.
