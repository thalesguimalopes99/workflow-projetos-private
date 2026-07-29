# Pagamentos Stripe Bubble

Trilha Bubble Geral | 18 aulas | ~47 min (0,79h) | nível intermediário

> Como cobrar dentro de um app Bubble usando o plugin oficial do Stripe: pagamento avulso (carrinho/checkout) e assinatura recorrente completa (assinar, cancelar, trocar plano, trocar cartão).

## O que você sai sabendo fazer

- Instalar e configurar o plugin Stripe (by Bubble) com as chaves de API de teste e de produção, e escolher a versão do checkout.
- Montar o fluxo de pagamento avulso: cobrar o usuário logado como primeiro step do workflow, com valor, nome, descrição e imagem dinâmicos no checkout do Stripe.
- Testar cobranças com os cartões de teste do Stripe (aprovado e recusado) e conferir o resultado no dashboard.
- Criar planos como "produtos" no Stripe, espelhá-los numa tabela do banco do Bubble e listá-los na interface (dropdown/repeating group).
- Inscrever um usuário numa assinatura, salvar o ID da assinatura no User e cancelar essa assinatura.
- Fazer upgrade/downgrade de plano e troca do cartão de cobrança sem sair do app.

## Stack e ferramentas

- **Bubble** (editor, Data/banco de dados, workflows, dropdown, repeating group, preview).
- **Plugin "Stripe" by Bubble** — actions de pagamentos: `Charge the current user`, `Subscribe the user to a plan`, `Cancel the current user's plan`, `Collect the user's CC information`.
- **Dashboard do Stripe** — modo teste, Desenvolvedores > Chaves de API, Produtos (catálogo), Assinaturas, Pagamentos.
- **Cartões de teste do Stripe** (documentação oficial) — `4242...` para aprovado, cartões específicos para recusado.
- Mencionado como alternativa (não usado): **API Connector** do Bubble com a documentação do Stripe.

## Pré-requisitos

- Ter conta no Stripe (a criação é rápida; o modo teste é ativado por um toggle no próprio painel, não exige conta sandbox separada).
- Saber o básico de Bubble: banco de dados, workflows, elementos de UI.
- O app modelo usado já tem carrinho e checkout prontos — o instrutor recomenda ver as aulas anteriores (do Neto) sobre montar carrinho, criar ordem e alterar usuário, porque essas actions aparecem no workflow e não são reexplicadas aqui.
- É obrigatório ter um usuário logado para qualquer cobrança (avulsa ou assinatura).

## Aula a aula

### Módulo: Introdução

### 01 - Introdução (00:01:51)
- **Resumo:** Abertura do curso pelo instrutor Harry. Ele lista o que será coberto: pagamentos avulsos, assinaturas (do plano criado no Stripe até a liberação do sistema e a renovação) e a coleta de credenciais para conectar Bubble e Stripe. Fecha argumentando por que o Stripe é boa escolha para cobrança em app.
- **Pontos-chave:**
  - Vantagens citadas: painel de gestão, API completa, alcance mundial e suporte a múltiplas moedas.
  - Existe plugin oficial do Bubble — basta colar as credenciais do painel do Stripe.
  - Cobrança em outras moedas exige configurar isso no seu fluxo.
- **Link:** https://flix.nocodestartup.io/m/lessons/2473

### 02 - Apresentação do App (00:01:41)
- **Resumo:** Demonstração do resultado final antes de construir. O instrutor adiciona itens ao carrinho do app modelo, confirma a compra e é redirecionado ao checkout hospedado do Stripe em ambiente de teste. Após pagar com cartão de teste, volta ao app, o pedido aparece como pago e o carrinho é limpo.
- **Pontos-chave:**
  - Não é preciso construir as telas de checkout — o Stripe hospeda.
  - O total e a quantidade de itens são livres; só é preciso enviar total, descrição e imagem.
  - Cartão `4242` retorna pagamento aprovado; o cartão fica salvo para próximas compras.
  - Pedido de R$ 200 confirmado como pago na tela "Minhas compras".
- **Link:** https://flix.nocodestartup.io/m/lessons/2474

### 03 - Conhecendo Dashboard do Stripe (00:01:45)
- **Resumo:** Tour rápido pelo painel do Stripe apontando só o que importa para a integração. Mostra como ativar o modo teste no cabeçalho e onde ficam as chaves de API dentro da seção Desenvolvedores.
- **Pontos-chave:**
  - Não precisa de conta sandbox separada: basta ativar "modo teste" no painel.
  - Desenvolvedores > Chaves de API é o único lugar necessário nesse momento.
  - Dá para criar conjuntos de chaves adicionais para separar aplicativos que usam a mesma conta.
  - Webhooks, eventos e logs existem, mas não são usados no curso.
- **Link:** https://flix.nocodestartup.io/m/lessons/2475

### 04 - Formas De Integrar Bubble Com Stripe (00:01:14)
- **Resumo:** Compara os dois caminhos de integração: montar as chamadas manualmente no API Connector a partir da documentação do Stripe, ou usar plugin. Explica a decisão de arquitetura do curso: usar o plugin oficial do Bubble.
- **Pontos-chave:**
  - API Connector = controle total, trabalho manual; plugin = prático e rápido.
  - Existem plugins de terceiros e o plugin do próprio Bubble.
  - O plugin oficial cobre cobrança avulsa, assinatura e atualização de dados do usuário — segundo o instrutor, ~99% das necessidades de pagamento.
  - Só parta para o API Connector se precisar de algo além disso.
- **Link:** https://flix.nocodestartup.io/m/lessons/2529

### 05 - Configurando o Plugin Stripe (00:02:32)
- **Resumo:** Instalação do plugin e preenchimento das credenciais. Mostra os campos separados para ambiente live e ambiente de teste, cola a public key e a secret key do modo teste, e configura a aparência e a versão do checkout.
- **Pontos-chave:**
  - Plugins > Add plugin > buscar "Stripe" — confirmar que é o *by Bubble*.
  - Campos: Live/Test Client ID, Secret Key e Publishable Key. Preencher live e test de uma vez evita trocar chave na hora do deploy.
  - Client ID só é necessário para split de pagamento — não usado aqui.
  - Configurar imagem e nome que aparecem no checkout.
  - **Stripe Checkout Version:** o padrão é `Legacy` (pop-up); trocar para a **versão 3**, mais completa e recomendada.
  - Opção para coletar endereço do usuário direto no checkout do Stripe, se necessário.
- **Link:** https://flix.nocodestartup.io/m/lessons/2476

### Módulo: Pagamento Avulso

### 06 - Introdução Pagamentos Avulsos (00:02:32)
- **Resumo:** Abre o módulo mostrando o workflow já existente do botão "Confirmar compra" no checkout do app. Explica a lógica de encadeamento: a cobrança entra como step 1 e todos os steps seguintes (criar ordem, alterar usuário, notificação, redirecionar) só rodam se a cobrança for aprovada.
- **Pontos-chave:**
  - Só o step de cobrança é adicionado neste módulo; o resto do workflow vem das aulas anteriores da trilha.
  - Pagamento aprovado = retorno automático ao app e continuação do workflow.
  - Pagamento negado = usuário fica preso no checkout do Stripe e precisa voltar manualmente (botão voltar/navegador).
- **Link:** https://flix.nocodestartup.io/m/lessons/2530

### 07 - Configurando Ações do Stripe (00:05:13)
- **Resumo:** Aula central do módulo. Adiciona a action de cobrança no workflow do botão de confirmar pedido, configura todos os campos do checkout e faz um teste de compra completo com dois itens somando R$ 200.
- **Pontos-chave:**
  - Action: **Payment > Charge the current user** — já puxa o e-mail do usuário logado.
  - **Amount:** valor total puxado dinamicamente (no exemplo, `Current User's carrinho: subtotal: sum`).
  - **Currency:** BRL para formatar como real no checkout.
  - **Name / Description / Image:** podem ser fixos ou dinâmicos (nome do produto, foto do banco).
  - Marcar a opção para não exibir a mensagem de sucesso padrão do navegador, que interrompe o fluxo.
  - Arrastar o step de cobrança para a posição 1 do workflow.
  - Adicionar um `Go to page` no final para levar ao index — não precisa de condicional, porque o step só roda se o pagamento passar.
  - No primeiro pagamento o Stripe cria o cliente; nos seguintes ele reconhece pelo e-mail.
- **Link:** https://flix.nocodestartup.io/m/lessons/2477

### 08 - Teste com Cartão de Erro (00:01:42)
- **Resumo:** Teste do caminho de falha usando um cartão de recusa da lista oficial de cartões de teste do Stripe. Mostra que o pedido não é confirmado e que o item permanece no carrinho, e em seguida repete a compra com o cartão aprovado que já ficou salvo.
- **Pontos-chave:**
  - A documentação do Stripe traz cartões para vários cenários (recusado, roubado, suspenso, países/bancos diferentes) — o link fica na descrição da aula.
  - Só o número do cartão importa para o teste.
  - Cartão recusado: nada acontece no app, o pedido não é confirmado.
  - O plugin salva o cartão do usuário automaticamente — via API seria preciso tratar isso manualmente.
- **Link:** https://flix.nocodestartup.io/m/lessons/2478

### 09 - Vendo Resultados no Dash do Stripe (00:01:04)
- **Resumo:** Fecha o módulo conferindo os pagamentos na aba Pagamentos do dashboard. Mostra que aparecem tanto os bem-sucedidos quanto os falhos e incompletos, e antecipa que o próximo módulo (assinatura) exige mais atenção.
- **Pontos-chave:**
  - Coluna de status separa concluído, falhou e incompleto.
  - "Incompleto" = usuário abriu o checkout e desistiu antes de finalizar.
  - A descrição configurada na action aparece na listagem.
- **Link:** https://flix.nocodestartup.io/m/lessons/2479

### Módulo: Assinatura

### 10 - Introdução Assinaturas (00:00:41)
- **Resumo:** Abertura curta do módulo listando o escopo do que será construído em assinaturas recorrentes no Bubble com Stripe.
- **Pontos-chave:**
  - Escopo: inscrever usuário num plano, cancelar, alterar o plano atual, trocar o cartão de cobrança e liberar os benefícios do plano.
- **Link:** https://flix.nocodestartup.io/m/lessons/2531

### 11 - Dashboard De Assinaturas Stripe (00:02:15)
- **Resumo:** Mostra onde ficam planos e assinaturas no painel do Stripe. Explica que os "produtos" do catálogo são os planos oferecidos no app e passa pela tela de assinaturas, que lista clientes ativos, plano e e-mail.
- **Pontos-chave:**
  - Produtos não aparece no menu lateral por padrão — use a busca do topo ("produtos" > Todos os produtos).
  - No catálogo também existem cupons, tarifas de envio, alíquotas e tabela de preços.
  - Na tela de assinaturas dá para criar assinatura manualmente para um cliente (via link), atualizar e cancelar.
  - As chaves de API já foram configuradas — não precisa mexer de novo.
- **Link:** https://flix.nocodestartup.io/m/lessons/2532

### 12 - Apresentação Do App (00:00:59)
- **Resumo:** Apresenta a página dedicada criada no mesmo projeto do módulo anterior para demonstrar assinaturas. A tela expõe os dados que serão manipulados e os botões de cada função.
- **Pontos-chave:**
  - Mesmo projeto do pagamento avulso, com uma página nova só para assinatura.
  - Elementos de texto exibindo: ID da assinatura, usuário logado, plano vinculado e status.
  - Botões: selecionar plano, assinar, cancelar plano e trocar cartão.
- **Link:** https://flix.nocodestartup.io/m/lessons/2533

### 13 - Criar Planos No Bd E No Stripe (00:06:32)
- **Resumo:** Aula mais longa do curso. Cria a estrutura de planos em dois lugares: um type no banco do Bubble e produtos recorrentes no catálogo do Stripe, ligando os dois pelo ID da API. Depois monta um dropdown que lista os planos com nome e valor formatado.
- **Pontos-chave:**
  - **Decisão de arquitetura:** o Stripe não expõe uma chamada para listar planos no Bubble, então os planos precisam existir também no banco do Bubble (ou fixos em cards).
  - Type `Plano de assinatura` com campos: `ID Stripe` (text), `nome` (text), `valor` (number).
  - Dropdown: Type of choices = Plano de assinatura, Choices source = Do a search for; option caption com nome + valor formatado como moeda.
  - No Stripe: Produtos > Adicionar novo produto, nome, descrição, moeda (BRL) e preço; marcar como **recorrente/mensal**, sem uso por consumo.
  - Após salvar, o Stripe abre os detalhes do produto — copiar o **ID da API** e colar no campo `ID Stripe` do registro correspondente no Bubble.
  - Exemplo criado: Plano 1 (R$ 59,90) e Plano 2 (R$ 49,90).
- **Link:** https://flix.nocodestartup.io/m/lessons/2534

### 14 - Ações De Criar Assinatura (00:05:42)
- **Resumo:** Configura a action que inscreve o usuário no plano escolhido no dropdown, percorrendo cada checkbox e campo da ação e explicando para que serve. Cobre plano dinâmico versus fixo, trial e opções que ficam desmarcadas.
- **Pontos-chave:**
  - Action: **Payment > Subscribe the user to a plan**.
  - Primeiro checkbox marcado = aplica ao Current User; desmarcado permite assinar em nome de outro usuário (útil para colaboradores).
  - `Update existing subscription` fica **desmarcado** aqui (é o que se usa depois para trocar de plano).
  - Plano dinâmico: apontar para `Dropdown Select Plano's value's ID Stripe`. Se desmarcar "dynamic", o Bubble lista os IDs dos produtos do Stripe para escolha fixa — é o único ponto onde ele lista os planos.
  - Quantidade só importa se o produto for por volume.
  - Promotions/cupom, coleta de Tax ID e taxas: deixados desmarcados.
  - **Trial:** informar dias grátis, ou usar `end of trial` com data (`Current date/time + days`). O cartão é coletado na hora; a cobrança e o ciclo de 30 dias começam ao fim do trial.
  - Marcar a opção de não exibir a mensagem de sucesso do navegador.
- **Link:** https://flix.nocodestartup.io/m/lessons/2535

### 15 - Testes Criar Assinatura (00:03:26)
- **Resumo:** Executa a assinatura de ponta a ponta com cartão de teste e descobre um problema: ao voltar do checkout a página não atualiza sozinha. Resolve adicionando dois steps depois da cobrança — salvar o ID da assinatura no usuário e recarregar a página.
- **Pontos-chave:**
  - Após o pagamento, a página mostra ID da assinatura, ID e nome do plano e status `active`.
  - O retorno do Stripe funciona como um "go back" e não reflete os dados novos na tela.
  - Solução: step **Refresh page** após a cobrança.
  - Step **Make changes to Current User** salvando `ID assinatura` (campo text) com o subscription ID vindo do Result of step 1.
  - Se a assinatura foi criada para outro usuário, é esse outro usuário que precisa receber o ID.
  - Data do cartão de teste precisa ser futura; o CVV pode ser qualquer número.
- **Link:** https://flix.nocodestartup.io/m/lessons/2536

### 16 - Cancelar Assinatura (00:02:11)
- **Resumo:** Monta o workflow do botão de cancelar, explicando a diferença entre cancelar todas as assinaturas do usuário ou apenas uma específica. Limpa o ID salvo no usuário e testa o cancelamento no preview.
- **Pontos-chave:**
  - Action: **Payment > Cancel the current user's plan**.
  - Checkbox marcado = cancela **todas** as assinaturas daquele usuário no Stripe. Desmarque e informe o ID quando o usuário puder ter planos extras/adicionais.
  - O ID pode vir do campo `ID Assinatura` do usuário ou do `Stripe subscription ID` que o plugin expõe.
  - Steps seguintes: `Make changes to Current User` limpando o ID da assinatura + `Refresh page`.
- **Link:** https://flix.nocodestartup.io/m/lessons/2537

### 17 - Troca Do Plano Do Usuário Stripe (00:04:12)
- **Resumo:** Cria o botão de atualizar plano reaproveitando a mesma action de assinatura, agora com o modo de atualização ligado. Explica a consequência de cobrança dessa escolha e testa a migração do Plano 1 para o Plano 2.
- **Pontos-chave:**
  - Mesma action **Subscribe the user to a plan**, agora com **`Update existing subscription` marcado**.
  - Informar o subscription ID existente (`Current User's ID assinatura` ou `Stripe subscription ID`) e o novo plano dinâmico pelo dropdown.
  - Nesse modo o usuário **mantém o período já pago** e só é cobrado o novo valor na próxima fatura.
  - Para cobrar imediatamente na troca: cancelar o plano e iniciar uma nova assinatura no mesmo fluxo.
  - Não abre o checkout do Stripe — os dados de faturamento e o cartão já estão salvos lá.
  - Steps finais: atualizar o `ID assinatura` no usuário, `Refresh page` e mensagem de sucesso.
- **Link:** https://flix.nocodestartup.io/m/lessons/2538

### 18 - Troca Do Cartão Do Usuário (00:01:43)
- **Resumo:** Última aula: workflow para o usuário substituir o cartão de cobrança da assinatura. Usa a action de coleta de dados do cartão com a opção de atualização ativada e testa o formulário no preview.
- **Pontos-chave:**
  - Action: **Payment > Collect the user's CC information**, com a opção de atualizar o cartão do usuário marcada.
  - Preencher a descrição que aparece no formulário (ex.: "atualizar cartão de cobrança").
  - Marcar a opção de não mostrar a mensagem do navegador; adicionar mensagem própria de sucesso.
  - Aqui **não** é preciso `Refresh page` — nada visível na tela depende disso.
  - A troca sempre substitui o **cartão padrão** do cliente no Stripe.
- **Link:** https://flix.nocodestartup.io/m/lessons/2539

## Pegadinhas e insights

- **Ordem do workflow é a regra de negócio.** A cobrança tem que ser o step 1: no Bubble, os steps seguintes só executam se o anterior retornar sucesso. É isso que garante que a ordem só é criada com pagamento aprovado — sem precisar de condicional.
- **Pagamento recusado deixa o usuário preso no checkout do Stripe.** Não há retorno automático; ele precisa voltar pelo navegador. Vale considerar isso na UX.
- **Checkout Legacy é o padrão do plugin e não é o que você quer.** Troque para a versão 3.
- **O Stripe não lista planos para o Bubble.** É por isso que existe a tabela `Plano de assinatura` no banco — é espelho manual do catálogo do Stripe, ligada pelo ID da API. Criar plano vira processo de dois lados: se esquecer de colar o ID, a assinatura não funciona.
- **O retorno do checkout não atualiza a tela.** Comportamento de "go back": sempre adicione `Refresh page` depois da action de assinatura/cancelamento se a página exibe status.
- **Salve o subscription ID no User.** Sem isso, cancelar e trocar plano ficam mais trabalhosos (dá para usar o `Stripe subscription ID` do plugin, mas o campo próprio é mais prático).
- **Cancelar assinatura vem marcado para cancelar TUDO.** Se o seu modelo permite planos adicionais, desmarque e passe o ID específico — caso contrário você derruba todas as assinaturas do cliente.
- **Trocar plano não cobra na hora.** O usuário aproveita o período já pago e o novo valor só entra na próxima fatura. Para cobrança imediata, o padrão indicado é cancelar + assinar de novo.
- **Ativar Client ID só serve para split de pagamento** — ignore se você não faz marketplace.
- **A mensagem de sucesso padrão do navegador interrompe o fluxo.** Marque a opção de ocultar em todas as actions do plugin.
- **Preencha as chaves live e test de uma vez** no plugin, para não ter que trocar credencial na hora do deploy.
- Cobrança avulsa e assinatura exigem **usuário logado**; o plugin salva o cartão do cliente automaticamente (via API Connector isso seria trabalho manual).
