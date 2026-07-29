# Introdução aos Pagamentos - bubble

Trilha Bubble Geral | 5 aulas | ~18 min (00:18:12) | nível iniciante

> Curso de abertura da trilha "Mestres dos Pagamentos": a fundação teórica de como funcionam gateways de pagamento, assinaturas, APIs e webhooks antes de integrar qualquer meio de pagamento num app Bubble.

## O que você sai sabendo fazer

- Explicar o caminho de um pagamento: cliente → loja → gateway → adquirente/subadquirente → banco emissor, e por que o app nunca conversa direto com a conta bancária.
- Escolher um gateway de pagamento pelos critérios que importam (cartão/Pix/boleto, parcelamento, antifraude, antecipação, split, suporte a assinatura recorrente).
- Entender o papel de uma API na integração (requisição → resposta com sucesso/insucesso) e agir sobre esse retorno dentro do app.
- Diferenciar chamada de API de webhook e saber quando cada um é usado — webhook é obrigatório para manter assinatura e acesso do usuário em sincronia.
- Desenhar a lógica de liberar/bloquear acesso a um SaaS conforme o gateway avisa que a mensalidade foi paga ou não.
- Localizar os materiais, links e editores das aplicações da formação NoCode Startup.

## Stack e ferramentas

- **Bubble** — plataforma onde a aplicação de estudo é construída.
- **NoCodeStore** — projeto/estudo de caso da trilha: loja virtual com catálogo (telefones, tablets, TVs, acessórios), carrinho, cadastro de usuário, checkout e tela "Minhas Compras" com status Pago.
- **Gateways citados**: Stripe (primeira integração da trilha), Asaas, Mercado Pago, Pagar.me, PayPal, Yuno.
- **Gateways de infoproduto citados** (com área de membros pronta): Hotmart, Kiwify.
- **Conceitos operacionais**: APIs, webhooks, assinatura recorrente.
- **NoCodeFlix / comunidade** — trilha "Começa por Aqui", pasta no Google Drive e Google Docs com os links dos editores; post fixado na área de Bubble da comunidade.

## Pré-requisitos

Nenhum pré-requisito formal para este curso (é 100% conceitual). O instrutor recomenda, porém, que a construção visual da loja venha de outras trilhas: **Fundamentos** (criar elementos do zero) e **Design e Responsividade**. Este curso não ensina design.

## Aula a aula

### 001 - Introdução  (00:06:31)
- **Resumo:** Abertura da trilha Mestres dos Pagamentos. O instrutor apresenta os objetivos (entender pagamentos, assinaturas, APIs e webhooks e depois integrar os principais gateways), o desenho dos cursos da trilha e faz uma demonstração ao vivo da aplicação que acompanhará todo o conteúdo, a NoCodeStore. Na demo ele adiciona e remove itens do carrinho, cria conta, finaliza o pedido, paga num checkout Stripe com cartão de teste e mostra o pedido com status Pago.
- **Pontos-chave:**
  - Sequência da trilha: (1) introdução conceitual → (2) carrinho de compra e ordem de compra → (3) integração Stripe → (4) integração Asaas → (5) Mercado Pago no futuro.
  - Stripe é o primeiro gateway por ser grande no mundo e ter integração facilitada com Bubble.
  - Mesma loja é reaproveitada em todas as integrações — troca-se só o gateway.
  - Detalhe de arquitetura demonstrado: o carrinho criado por usuário anônimo é associado à conta depois do cadastro, sem perder os itens.
  - Conhecimento de carrinho/ordem serve para loja virtual, delivery e marketplaces.
- **Link:** https://flix.nocodestartup.io/m/lessons/2458

### 002 - Gateways de Pagamentos  (00:04:19)
- **Resumo:** Aula conceitual sobre o que é um gateway e por que ele é indispensável. Usando o exemplo do "João", que quer receber na conta do Nubank, o instrutor mostra que a loja se integra ao gateway via API e só depois o dinheiro é transferido para a conta bancária. Também descreve a cadeia completa do pagamento e fecha com uma analogia didática de API.
- **Pontos-chave:**
  - Cadeia do pagamento: cliente → loja → gateway → subadquirente/adquirente/operadora → banco emissor.
  - O que os gateways resolvem: cartão de crédito, Pix, boleto, parcelamento, análise de fraude, antecipação e, em alguns casos, split de pagamentos.
  - Nem todo gateway oferece as mesmas funções (split, por exemplo, varia) — mas todos operam de forma análoga.
  - Gateways para loja/marketplace: Asaas, Stripe, Pagar.me, Mercado Pago, PayPal, Yuno. Para infoproduto: Hotmart e Kiwify (já entregam área de membros).
  - Analogia da API: cliente → garçom → cozinha; o garçom é a API que leva o pedido e traz a resposta (pagamento aprovado ou recusado).
- **Link:** https://flix.nocodestartup.io/m/lessons/2459

### 003 - Assinaturas  (00:03:54)
- **Resumo:** Explica como funciona cobrança recorrente e introduz webhooks. O exemplo do João muda de loja virtual para um SaaS que cobra mensalidade. O instrutor argumenta que o gateway é quem guarda e recobra o cartão, e por isso o app precisa de um canal para saber se a renovação foi paga — esse canal é o webhook, que mantém app e gateway sincronizados.
- **Pontos-chave:**
  - Nunca armazene dados de cartão dentro do seu aplicativo; deixe a segurança e a guarda com o gateway (é possível, mas não recomendado).
  - Nem todo gateway suporta assinatura — validar essa função antes de escolher (hoje a maioria suporta).
  - Com o cartão salvo no gateway, o usuário não reinforma dados nas renovações.
  - Diferença central: API = você faz a requisição e recebe a resposta; webhook = o outro sistema dispara a informação sozinho quando algo acontece.
  - Fluxo de assinatura: chamada de API na 1ª cobrança → assinatura criada no gateway → renovação mensal/anual → webhook avisa pago/não pago → o app mantém ou remove o acesso.
- **Link:** https://flix.nocodestartup.io/m/lessons/2460

### 004 - Avisos  (00:02:01)
- **Resumo:** Dois recados antes da parte prática. O primeiro delimita o escopo: a trilha ensina estruturar carrinho, ordem de compra, banco de dados e a integração com os meios de pagamento — não ensina o design da loja, que fica com as trilhas de Fundamentos e de Design e Responsividade. O segundo apresenta o instrutor que conduzirá as integrações.
- **Pontos-chave:**
  - Escopo da trilha: carrinho, ordem de compra, modelagem de banco e lógica; pagamento avulso e assinatura.
  - Fora do escopo: construção visual/responsividade — buscar as trilhas Fundamentos e Design e Responsividade.
  - Cada trilha tem foco próprio; assistir o conteúdo certo na hora certa evita perder tempo.
  - As integrações com gateways serão conduzidas pelo Harry, do Imperio NoCode (agência de desenvolvimento em Bubble, com canal próprio de conteúdo).
- **Link:** https://flix.nocodestartup.io/m/lessons/2461

### 005 - Links  (00:01:27)
- **Resumo:** Aula operacional mostrando onde encontrar os materiais e os editores das aplicações da formação. O instrutor navega pela NoCodeFlix até a trilha "Começa por Aqui", abre a seção de materiais e links, chega na pasta do Google Drive e no Google Docs que reúne os links dos editores — incluindo o da trilha Mestres dos Pagamentos. Mostra também o caminho alternativo pela comunidade.
- **Pontos-chave:**
  - Caminho 1: NoCodeFlix → trilha "Começa por Aqui" → aula/seção "material e links importantes".
  - De lá se chega a uma pasta do Google Drive e a um Google Docs com os links de todos os editores por trilha.
  - Caminho 2: comunidade → área Bubble → post fixado de materiais, informações e links importantes.
  - O editor da trilha Mestres dos Pagamentos está listado nesses materiais.
- **Link:** https://flix.nocodestartup.io/m/lessons/2462

## Pegadinhas e insights

- **Não armazene dados de cartão no seu app.** Tecnicamente dá, mas o instrutor desaconselha: toda a estrutura de segurança e guarda de cartão/senha fica com o gateway.
- **Suporte a assinatura não é universal.** Antes de fechar o gateway, confirme se ele tem recorrência nativa — sem isso, não dá para implementar mensalidade.
- **Sem webhook a assinatura desincroniza.** Só a chamada de API cobre a primeira cobrança; as renovações acontecem no gateway, e sem webhook o app não fica sabendo de inadimplência e continua liberando acesso indevidamente.
- **Escolha do gateway depende do modelo de negócio.** Hotmart e Kiwify são orientados a infoproduto e já entregam área de membros; Stripe, Asaas, Mercado Pago, Pagar.me, PayPal e Yuno são os indicados para loja virtual, marketplace e loja física.
- **Split de pagamentos é diferencial, não padrão** — alguns gateways oferecem, outros não.
- **Decisão de arquitetura mostrada na demo:** o carrinho de usuário anônimo é vinculado à conta no momento do cadastro, preservando os itens.
- **Stripe foi escolhido como primeira integração** pela facilidade de integração com o Bubble, não por ser o mais usado no Brasil (está em crescimento por aqui).
- **Este curso é só teoria.** A mão na massa começa no curso seguinte (carrinho e ordem de compra) — e o design da loja não será ensinado em nenhum momento da trilha.
