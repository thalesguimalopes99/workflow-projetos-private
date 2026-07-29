# Pagamentos Supabase + Flutterflow - Intro

Trilha FlutterFlow Geral | 6 aulas | ~24 min (00:23:52) | nivel iniciante

> Modulo conceitual que prepara o terreno para colocar pagamentos (avulsos e assinaturas) num app FlutterFlow com Supabase: como funciona um gateway, por que webhook e melhor que ficar consultando API, e quais ferramentas complementares serao usadas nos modulos praticos.

## O que voce sai sabendo fazer

- Explicar o fluxo completo de uma cobranca online: cliente → loja → gateway → operadora/adquirente → banco → sua conta.
- Escolher gateway com criterio, sabendo o trade-off entre Stripe (mais caro, mais facil, doc/API melhor) e Asaas (nacional, forte em Pix).
- Diferenciar API (voce pergunta, o sistema responde) de webhook (o sistema avisa sozinho) e decidir qual usar para controlar assinatura ativa.
- Desenhar a arquitetura de uma assinatura recorrente: gateway cobra → webhook avisa o Make → Make libera ou revoga o acesso no app.
- Comparar Make, Zapier e n8n e justificar a escolha da ferramenta de automacao do projeto.
- Comparar Framer e Webflow para montar a landing page que antecede o checkout.

## Stack e ferramentas

- **FlutterFlow** — front-end do app (projeto base: app financeiro do curso gratuito de FlutterFlow do YouTube da NoCode StartUp, clonavel).
- **Supabase** — backend e modelagem de dados de todo o projeto.
- **Stripe** — gateway principal das aulas (assinaturas + pagamentos avulsos).
- **Asaas** — gateway nacional, usado nas aulas de pagamento avulso via Pix (aparece na transcricao como "Asas"/"Asus").
- **Make (Integromat)** — automacao e recepcao dos webhooks de pagamento.
- **Framer** — landing page (opcional/bonus).
- Citados como alternativas, nao usados: Pagar.me, PagSeguro, Juno, Mercado Pago, PayPal, Zapier, n8n, Webflow, Wix, Carrd, WordPress.

## Pre-requisitos

- Aulas de fundamentos de **API e webhooks** que existem no inicio da formacao — o instrutor faz so uma revisao rapida aqui e avisa que sem elas voce se perde.
- Nocao basica de FlutterFlow e Supabase (o projeto base ja pressupoe o app financeiro montado).
- Assistir os modulos e as aulas **na ordem**; a estrutura didatica e sequencial.

## Aula a aula

### Introdução / 001 - O Que Você Irá Aprender  (00:01:35)
- **Resumo:** Abertura do modulo. O instrutor lista o percurso: fundamentos de pagamento do zero, revisao de APIs e webhooks, ferramentas de automacao e integracao com os gateways escolhidos. Deixa claro que o backend de referencia e o Supabase e que toda a modelagem de dados sera orientada a ele. Fecha pedindo que as aulas e modulos sejam vistos na ordem, porque tudo dito aqui reaparece adiante.
- **Pontos-chave:**
  - Gateways cobertos na formacao: Stripe e Asaas.
  - Objetivo final: implementar pagamento avulso e assinatura com cobranca recorrente mensal.
  - Aviso explicito de nao pular aulas — a base conceitual e reaproveitada nos modulos praticos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3630

### Pagamentos / 001 - Fundamentos  (00:03:11)
- **Resumo:** Usa a personagem "Ana", dona de uma loja online, para explicar por que nao da para receber dinheiro direto na conta bancaria. Define o papel do gateway como responsavel por todo o processamento da venda e mostra a cadeia ate o banco. Termina com um panorama dos gateways do mercado e a justificativa da dupla escolhida no curso.
- **Pontos-chave:**
  - Gateway cuida de cartao, Pix, boleto, parcelamento, seguranca, analise de fraude e split de pagamento.
  - Cobranca do gateway e por taxa de transacao (percentual da venda, tipicamente 2%–3%), nao mensalidade fixa.
  - Fluxo: cliente → loja → gateway → operadora/adquirente → banco do pagador → liberacao.
  - Stripe: mais caro, porem estrutura e documentacao de API muito boas. Asaas: gateway nacional.
  - A essencia e a mesma em qualquer gateway — quem entende os fundamentos consegue migrar para Mercado Pago, Pagar.me etc.
- **Link:** https://flix.nocodestartup.io/m/lessons/3629

### Pagamentos / 002 - Assinaturas  (00:04:37)
- **Resumo:** Passa do pagamento unico para o recorrente, usando um micro SaaS da mesma personagem como exemplo. Revisa API com a analogia do garcom no restaurante e webhook com a analogia da cozinha avisando sozinha (estilo notificacao do iFood). Mostra por que polling em API para saber se o cliente pagou e ruim e como o webhook resolve, e antecipa que o Make sera o receptor desse webhook.
- **Pontos-chave:**
  - API = voce pede e recebe de volta; webhook = o dado chega sem voce pedir.
  - Ficar chamando a API do gateway para perguntar "pagou?" encarece e degrada a performance do sistema.
  - Fluxo da assinatura: gateway controla a data da fatura → dispara webhook em pagamento feito ou nao feito → app libera ou revoga o acesso.
  - Da para receber webhook no proprio Supabase, mas envolve codigo e e mais tecnico; o curso opta pelo Make por ser mais fluido e barato.
- **Link:** https://flix.nocodestartup.io/m/lessons/3631

### Ferramentas Complementares / 001 - Make Integromat Para Automações  (00:06:04)
- **Resumo:** Apresentacao rapida do Make para ambientacao. Compara as tres principais plataformas de automacao em integracoes prontas, facilidade, flexibilidade e preco, e explica a logica de triggers, acoes e buscas. Termina navegando pelo site do Make e mostrando onde fica o modulo de webhook que sera usado para escutar o pagamento do Stripe.
- **Pontos-chave:**
  - Comparativo: Zapier tem mais integracoes prontas e e o mais facil, porem menos flexivel e o mais caro; Make e o meio-termo visual e acessivel; n8n e o mais flexivel, mais tecnico e pode ser self-hosted por ser open source (o que barateia).
  - Perfil de cada uma: Zapier para equipes internas, Make para empreendedores/marketeiros/freelancers, n8n para desenvolvedores.
  - Estrutura do Make: trigger (gatilho) → acao → busca (ex.: consultar planilha ou banco).
  - Integracoes nativas citadas: Google Sheets, Gmail, Facebook Ads, Trello, WordPress, Stripe.
  - Modulo **Custom Webhook** e o que vai ficar aguardando o aviso de pagamento do gateway.
  - Tarefa: criar conta no Make — ha um link especial na comunidade, conferir antes de se cadastrar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3632

### Ferramentas Complementares / 002 - Framer Para Landing Page  (00:03:41)
- **Resumo:** Bonus opcional sobre onde construir a pagina que leva ao checkout. Argumenta que FlutterFlow nao e a ferramenta certa para landing page, ja que site institucional/portfolio/LP e conteudo focado em front-end sem interacao com backend. Compara Webflow e Framer e defende o Framer pela praticidade, mostrando o site da ferramenta e o que sera construido depois.
- **Pontos-chave:**
  - Ferramentas no-code de site citadas: Framer, Webflow, Wix, Carrd, WordPress.
  - Webflow: maior comunidade, CMS forte, exporta codigo, mais caro e menos facil. Framer: facil de aprender, comunidade em ascensao, CMS basico, mais barato, boa integracao com Figma, **nao exporta codigo**.
  - A LP sera construida do zero em uma ou duas aulas, so para fechar o ecossistema compra → assinatura → uso do app.
  - Etapa opcional: quem quiser pode mandar o usuario direto para o link de pagamento do Stripe.
- **Link:** https://flix.nocodestartup.io/m/lessons/3634

### Conclusão / 001 - Como As Aulas Estão Organizadas  (00:04:44)
- **Resumo:** Fecha o modulo explicando a sequencia dos proximos e apresentando o projeto base. Define a ordem: Stripe assinaturas → Stripe pagamentos avulsos → Asaas pagamento avulso com Pix. Mostra o app financeiro que sera clonado e descreve o cenario de negocio que sera implementado: assinatura para liberar o app e uma compra avulsa de produto dentro dele.
- **Pontos-chave:**
  - Ordem obrigatoria dos modulos: este primeiro, depois Stripe, depois Asaas.
  - Assinatura vem antes de pagamento avulso por ser o tema mais pedido.
  - Pix no Stripe existe, mas exige conta validada por alguns meses e solicitacao de liberacao — por isso Pix e ensinado no Asaas.
  - Projeto base: app financeiro do curso gratuito de FlutterFlow da NoCode StartUp (YouTube), com botao de clonar; o link e disponibilizado.
  - So a parte de usuarios do projeto sera alterada; pode ser necessario pausar/remover alguns numeros do app clonado para nao dar erro, e a conexao com o Supabase e feita no proximo modulo.
  - Cenario alvo: pagou → libera o app; nao pagou → revoga. Mais uma compra avulsa (ex.: consultoria financeira) dentro do app.
- **Link:** https://flix.nocodestartup.io/m/lessons/3633

## Pegadinhas e insights

- **Nao pule aulas nem modulos.** O instrutor repete isso em tres aulas diferentes; a sequencia didatica e proposital e os fundamentos daqui sao pressupostos adiante.
- **Polling em API para checar pagamento e antipadrao.** Chamar o gateway repetidamente perguntando se o cliente pagou fica caro e prejudica a performance. Webhook e a decisao de arquitetura do curso.
- **Webhook no Supabase e possivel, mas foi descartado de proposito.** Da para fazer, so que exige codigo e e mais tecnico; a escolha pelo Make e por fluidez e custo, nao por limitacao tecnica.
- **Pix no Stripe tem barreira de entrada.** Precisa de conta validada por alguns meses e pedido de liberacao — por isso o curso ensina Pix pelo Asaas.
- **Stripe custa mais caro que os concorrentes**, e o instrutor assume isso: paga-se pela facilidade, estrutura, documentacao de API e suporte/comunidade.
- **Gateway cobra percentual por transacao (~2%–3%), nao taxa fixa** — a conta muda conforme o volume, nao conforme o tempo.
- **Make tem plano gratuito generoso**; a expectativa e so migrar para plano pago quando houver volume real de clientes.
- **Framer nao exporta codigo.** Se lock-in for problema, Webflow e a alternativa (exporta, tem CMS mais forte, mas e mais caro e menos facil).
- **FlutterFlow nao serve para landing page.** Erro comum apontado pelo instrutor: tentar fazer LP dentro do app.
- **O aprendizado e transferivel entre gateways.** Depois de dominar Stripe e Asaas, adaptar para Mercado Pago ou Pagar.me e so questao de ler a documentacao.
- Ha um **link de cadastro especial do Make na comunidade** — vale conferir antes de criar conta direto no site.
