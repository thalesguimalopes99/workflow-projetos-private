# Introdução aos Pagamentos - FlutterFlow

(sem trilha) | 4 aulas | ~19 min (00:18:57) | iniciante

> Aula inaugural da trilha "Mestre dos Pagamentos": explica o que é gateway de pagamento, a diferença entre API e webhook, onde entram as ferramentas de automação e como o projeto-exemplo em FlutterFlow vai amarrar tudo isso.

## O que você sai sabendo fazer

- Explicar o caminho do dinheiro numa venda: cliente → gateway → operadora/banco → conta bancária (PJ) do dono do negócio.
- Escolher um gateway de pagamento comparando taxas, parcelamento, meios de pagamento suportados, prazo de repasse e features extras (antecipação, split, antifraude).
- Diferenciar API (você pergunta e recebe resposta) de webhook (o outro sistema avisa você quando um evento acontece) e decidir qual usar para checar assinatura.
- Desenhar o fluxo de uma assinatura recorrente: webhook do gateway dispara automação que libera ou corta o acesso ao app.
- Identificar por que FlutterFlow sozinho não resolve pagamento recorrente e onde entram Firebase/Supabase ou automação no-code.

## Stack e ferramentas

- **FlutterFlow** — front-end/lógica do app (não tem back-end próprio).
- **Gateways ensinados na trilha:** Stripe (primeiro módulo, o mais detalhado), Asaas, Mercado Pago — com outros previstos.
- **Gateways citados como opções de mercado:** Pagar.me, PagSeguro, Juno (adquirida pela Yuno), PayPal.
- **Back-end/banco:** Firebase ou Supabase (exigem código para webhooks, automações e ações agendadas).
- **Automação no-code:** Make (principal usado no curso) e Zapier.

## Pré-requisitos

Nenhum pré-requisito formal, mas o instrutor pressupõe que você já viu (ou vai ver) a aula específica de APIs da formação, onde os métodos GET/POST/PUT são detalhados. Ter noção de FlutterFlow ajuda, já que o projeto final é construído nele.

## Aula a aula

### 001 - Como Funcionam os Pagamentos  (00:07:29)

- **Resumo:** Abertura da trilha, com o mapa do que será coberto (pagamentos, APIs, webhooks, ferramentas de automação e integração com vários gateways). Usa a história fictícia da Ana, que abriu uma loja virtual no-code, para explicar por que não dá para receber direto no banco tradicional e qual o papel do gateway de pagamento. Fecha listando as opções nacionais e internacionais de gateway e os critérios para escolher.
- **Pontos-chave:**
  - O gateway faz o processamento bancário, comunica com a operadora/banco do cliente, autoriza a compra e depois permite a transferência para a conta bancária (recomendado: PJ).
  - O gateway define quais meios existem: cartão, parcelamento, PIX, boleto (inclusive boleto recorrente).
  - Também cobre segurança, análise de fraude, antecipação e split de pagamentos (útil em marketplace).
  - Cada gateway cobra taxa própria por transação e por parcelamento — comparar antes de escolher.
  - Estrutura da trilha: um módulo por gateway; Stripe é o primeiro e o mais didático — os módulos seguintes (Mercado Pago, Asaas) não repetem a base.
- **Link:** https://flix.nocodestartup.io/m/lessons/2327

### 002 - Pagamentos de Assinatura  (00:05:38)

- **Resumo:** Ataca o caso mais complexo: cobrança recorrente. Retoma a analogia do garçom para explicar API (o app pergunta, o sistema responde) e introduz webhook como o oposto: o gateway avisa o app quando o evento ocorre, sem ninguém perguntar. Aplica os dois modelos ao problema real de saber se a assinatura do cliente está paga e ativa.
- **Pontos-chave:**
  - Analogia: cliente = seu app/front-end, garçom = API, cozinha = banco de dados ou outro sistema.
  - Métodos citados: GET (consultar), POST (escrever), PUT (atualizar).
  - API é sempre requisição + resposta; webhook é disparado por evento, automaticamente.
  - Webhook evita ficar fazendo requisições repetidas de polling, que deixam o software pesado — por isso é o caminho preferido para assinatura.
  - Depois do aviso de pagamento, ainda é preciso rodar uma automação que mantém o acesso liberado (ou corta, se não pagou).
- **Link:** https://flix.nocodestartup.io/m/lessons/2328

### 003 - Ferramentas para Automação de Pagamentos  (00:02:17)

- **Resumo:** Explica a lacuna arquitetural: FlutterFlow cuida do front-end e da lógica, mas não tem back-end. Firebase e Supabase resolvem webhooks e ações agendadas, só que exigem código e ficam técnicos. A alternativa apresentada é usar automação no-code, com Make como ferramenta principal do curso.
- **Pontos-chave:**
  - FlutterFlow = front-end + lógica + conexão com banco; sem back-end próprio.
  - Firebase pode ficar bem complicado para essa parte; Supabase também exige código.
  - No Make você cria o webhook, ele fica aguardando o evento e dispara a cadeia de ações (gatilho → módulos seguintes).
  - Fluxo-resumo da trilha: gateway → webhook do evento de pagamento → automação no Make → libera/mantém a assinatura no app FlutterFlow.
  - Make e Zapier são apresentados como úteis para qualquer projeto, não só pagamentos.
- **Link:** https://flix.nocodestartup.io/m/lessons/2329

### 004 - O projeto que iremos construir  (00:03:33)

- **Resumo:** Tour rápido pelo app que será construído ao longo da trilha. Ele cobre os dois modelos de cobrança — produto avulso e assinatura — com lista de produtos, lista de compras, lista de assinaturas e um checkout que permite escolher o gateway. O instrutor demonstra o pagamento por Stripe redirecionando para a página de checkout externa e mostra o dashboard de criação de produtos.
- **Pontos-chave:**
  - Telas previstas: lista de produtos (avulsos e assinatura), minhas compras, minhas assinaturas, checkout e dashboard para criar produtos.
  - No checkout dá para escolher o gateway (Stripe, Asaas, Mercado Pago) e o método; no exemplo, assinatura aceita apenas cartão.
  - Exemplo usado na demonstração: assinatura de 420 por ano, com plano de recorrência criado no Stripe.
  - O curso ensina a criar os produtos dentro de cada gateway (avulso e recorrente).
  - Design/layout do projeto não é ensinado aqui — fica no canal do Daniel Neto (Neto NoCode), novo membro do time NoCode Startup.
- **Link:** https://flix.nocodestartup.io/m/lessons/2330

## Pegadinhas e insights

- **Não pule o módulo de Stripe, mesmo que você só vá usar Asaas ou Mercado Pago.** A base conceitual (API, webhook, criação de produto, checkout) é explicada só uma vez, no primeiro módulo; os seguintes são diretos ao ponto e assumem esse conhecimento.
- **O projeto é didático, não é template pronto.** Ele junta vários gateways na mesma tela (com botões tipo "realizar pagamento por API") para fins de ensino. Para produção, você precisa enxugar: escolher um gateway, remover os botões extras e ajustar o fluxo.
- **A decisão de arquitetura central da trilha:** como FlutterFlow não tem back-end, a lógica de recorrência não fica no app. Ela fica no webhook + automação externa. O app só consulta/reflete o estado da assinatura.
- **Por que webhook e não API para assinatura:** ficar consultando o gateway em loop para saber se pagou deixa o app pesado. O webhook empurra a informação só quando o evento acontece.
- **Make foi escolhido no lugar de código** justamente para fugir da complexidade técnica de implementar isso em Firebase Functions ou Supabase.
- **Escolher gateway é decisão sua e depende do modelo de negócio:** taxa por transação, custo do parcelamento, meios suportados e prazo de repasse variam. A preferência declarada do time para apps no-code é Stripe (boas integrações e documentação bem estruturada), seguido de Asaas e Mercado Pago.
- **Conta bancária PJ** é a recomendação para o destino do repasse — deixa a estrutura mais profissional.
- Nenhum valor de taxa específico é citado nestas aulas; só o exemplo de assinatura de 420/ano usado na demo do checkout.
