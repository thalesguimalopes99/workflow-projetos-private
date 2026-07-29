# F5.4 - Conectando Assistente de IA aos Dados do App

Trilha Nocode IA | 18 aulas | ~1h15min | avançado (dentro da trilha)

> Como fazer um chat com IA (clone do ChatGPT em FlutterFlow) consultar de verdade o banco de dados do seu app: a OpenAI decide chamar uma função, os parâmetros extraídos viram filtros numa chamada API do Supabase, e o JSON retornado volta pra IA responder em linguagem natural.

## O que você sai sabendo fazer

- Montar o ciclo completo de Function Calling com dados reais: pergunta → função ativada → parâmetros estruturados → chamada API no banco → segunda chamada à OpenAI com os dados → resposta em linguagem natural.
- Configurar chamadas API REST no Supabase dentro do FlutterFlow (endpoint da tabela, headers `apikey` e `Authorization`, `select=*`) e aplicar filtros por query string (`eq`, `gt`, `lt`, `gte`, `lte`).
- Escrever o JSON de uma function calling com parâmetros tipados, `enum` de categorias permitidas, campos `required` e `tool_choice: auto`.
- Escrever o system prompt que governa quando a IA deve (e não deve) chamar a função, com persona, restrições anti-alucinação e lista fechada de categorias.
- Criar custom functions no FlutterFlow para extrair cada parâmetro do JSON de resposta e gravá-los em component state.
- Montar a action chain no FlutterFlow que encadeia as duas chamadas de API, injeta o resultado do banco na conversa e esconde do usuário a mensagem técnica (usando role `system`).
- Adicionar filtro de período (data início / data fim) para perguntas do tipo "quanto gastei em março de 2024".

## Stack e ferramentas

- **FlutterFlow** — web app, chat app (pop-up de assistente), API Calls, Custom Functions, Actions, component state.
- **Supabase** — banco de dados (tabela `registros`), Enumerated Types para categorias, API docs por tabela, Project Settings → API (URL + anon/public key), import de CSV, autenticação (pegar o user ID).
- **OpenAI API** — endpoint `chat/completions`, function calling, roles `system` / `user` / `assistant`.
- **ChatGPT** — usado como ferramenta auxiliar para corrigir formatação de JSON quebrado.
- **Google Sheets / Google Docs / Drive** — planilha de dados para enriquecer o Supabase via CSV e documento de apoio para copiar/colar prompts e URLs.
- Materiais do curso: prompts prontos, JSON da função e planilha, linkados abaixo da aula e na comunidade.

## Pré-requisitos

As aulas assumem que você já fez os módulos anteriores da trilha:

- O chat app clone do ChatGPT construído do zero (fase 4, aula 3).
- As aulas de Function Calling com a função de cotação de moeda (fase 4, aula 4) — o código é reaproveitado e adaptado o tempo todo.
- O web app financeiro (micro SaaS de finanças pessoais) já conectado ao Supabase.
- Noção de chamadas API. O instrutor avisa explicitamente que não vai reexplicar esses conceitos.

## Aula a aula

### 1 - O Que Você Vai Aprender  (00:01:30)
- **Resumo:** Abertura do módulo. Apresenta a proposta: unir o SaaS financeiro já construído com IA, de forma que o chat converse diretamente com o banco de dados. O instrutor deixa claro que é conteúdo mais avançado de Function Calling e que as aulas anteriores são pré-requisito real.
- **Pontos-chave:**
  - O exemplo usa Supabase, mas a lógica serve para qualquer banco de dados.
  - Aplicável a qualquer SaaS ou micro SaaS que precise de consulta conversacional.
  - Recomenda revisar a fase 4 (Function Calling) antes de continuar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3458

### 2 - Planejamento Projeto  (00:04:23)
- **Resumo:** Desenha o fluxo completo antes de codar. O usuário pergunta algo no FlutterFlow, a OpenAI decide se responde direto ou aciona a função `get_despesas`; se acionar, ela devolve parâmetros estruturados (categoria e tipo) que viram filtros numa chamada API ao Supabase; o JSON retornado é reinjetado na OpenAI para gerar a resposta final em linguagem natural.
- **Pontos-chave:**
  - Fluxo: prompt → decisão da IA → função com parâmetros → API Supabase filtrada → JSON de volta pra IA → resposta natural.
  - Roteiro do módulo: setup → API do Supabase → configurar function calling → atualizar as actions.
  - Primeiro se resolve o filtro por categoria; só depois entra o filtro de datas.
  - O foco é o chat app; a integração com o web app fica pro final.
- **Link:** https://flix.nocodestartup.io/m/lessons/3457

### 3 - Setup Flutterflow E Supabase  (00:06:05)
- **Resumo:** Prepara o ambiente. Duplica o projeto do chat app da fase anterior para não perder o backup, atualiza o system prompt do assistente financeiro seguindo boas práticas (persona, instruções, restrições), enriquece o Supabase com mais categorias e mais registros, e conecta o projeto FlutterFlow ao Supabase.
- **Pontos-chave:**
  - Duplicar o projeto no FlutterFlow em vez de editar o original.
  - Categorias adicionadas em Enumerated Types: aluguel, supermercado, delivery, farmácia, estudos, academia, salário, rendimento extra, gasolina, lazer, capacitação, bar.
  - Para importar o CSV de registros, edite antes a coluna `user_id` com um ID real (pego em Authentication no Supabase) — senão os dados não ficam associados ao seu usuário.
  - Conexão FlutterFlow ↔ Supabase: Project Settings → API, copiar a URL e a anon/public key, depois "Get Schema".
  - O prompt pede respostas diretas e sem enrolação também por economia de tokens.
- **Link:** https://flix.nocodestartup.io/m/lessons/3460

### 4 - Configurar Chamada Api  (00:06:26)
- **Resumo:** Ensina a montar do zero uma chamada GET à tabela do Supabase dentro do FlutterFlow. Mostra onde ficam os API Docs de cada tabela no Supabase (com exemplos em bash), monta a URL com `select=*`, cria os headers com a chave API como variável e testa até receber status 200 com a lista de registros em JSON.
- **Pontos-chave:**
  - Cada tabela e cada view tem seu próprio API Docs no Supabase; troque a linguagem para **bash** para ver o formato de URL/curl.
  - Dois headers obrigatórios: `apikey` e `Authorization`, ambos apontando para a mesma variável com a anon/public key.
  - Não colar as aspas da documentação dentro do campo de URL do FlutterFlow.
  - Operadores de filtro do Supabase: `eq` (igual), `gt` (maior que), `lt` (menor que).
  - Status 200 e o JSON em colchetes confirmam que veio uma lista de registros.
  - Limite do plano gratuito do FlutterFlow forçou apagar a API antiga de cotação de moeda para caber a nova.
- **Link:** https://flix.nocodestartup.io/m/lessons/3459

### 5 - Colocar Filtros Na Chamada Api  (00:02:38)
- **Resumo:** Transforma a chamada genérica numa chamada filtrada. Acrescenta os parâmetros `categoria` e `tipo` na query string como variáveis do FlutterFlow e testa combinações (supermercado/saída, salário/entrada) até validar o retorno.
- **Pontos-chave:**
  - Sintaxe: `?select=*&categoria=eq.[categoria]&tipo=eq.[tipo]` — a interrogação inicia os parâmetros, o `&` encadeia os seguintes.
  - Ambas as variáveis são string.
  - Passar valor vazio no filtro gera erro na chamada — a solução adotada é atribuir um valor padrão na action.
  - Registros do tipo "entrada" no projeto: salário e rendimento extra.
- **Link:** https://flix.nocodestartup.io/m/lessons/3462

### 6 - Entendendo A Função  (00:03:33)
- **Resumo:** Explica o JSON da function calling `get_despesas` e o prompt que a acompanha, ambos disponíveis nos materiais para copiar. O prompt define quando a IA pode acionar a função, quais categorias existem e proíbe inventar dados; a função define os parâmetros que a IA precisa extrair da pergunta.
- **Pontos-chave:**
  - Parâmetros nesta etapa: `categoria` (com `enum` das categorias válidas) e `tipo` (entrada ou saída) — os dois marcados como `required`.
  - Usar `enum` evita que o modelo invente categorias inexistentes.
  - O prompt manda ser 100% fiel aos dados, admitir quando não tem a informação e nunca omitir nem criar informação.
  - Se o usuário pedir categoria inexistente, a IA deve avisar e listar as disponíveis.
  - `tool_choice` fica em `auto` — a própria OpenAI decide se ativa a função.
  - Exemplo dentro da descrição da função ("quanto gastou em supermercado" → categoria supermercado, tipo saída) ajuda o modelo a acertar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3461

### 7 - Configurando Api  (00:05:59)
- **Resumo:** Cola o novo body (prompt + função) na chamada `chat/completions` do FlutterFlow e testa direto no painel de API. Valida os dois caminhos: pergunta genérica não ativa a função (tipo de resposta nulo) e pergunta sobre gastos ativa (tipo `function`, com os argumentos categoria e tipo preenchidos corretamente).
- **Pontos-chave:**
  - Truque útil: quando o FlutterFlow trava por JSON malformado, copiar o JSON inteiro e pedir ao ChatGPT para corrigir a formatação — vírgula ou colchete perdido é difícil de achar no editor.
  - Para testar rápido, substitui temporariamente o histórico da conversa por uma variável simples `pergunta`; depois devolve o histórico completo.
  - Renomeia o retorno para "parâmetros da função resposta" no path pré-definido.
  - "Quanto ganhei com meu salário" retorna categoria salário / tipo entrada — prova que a IA estrutura texto livre em parâmetros.
  - O instrutor esbarrou no limite de créditos da OpenAI no meio do teste e precisou recarregar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3464

### 8 - Atualizando Custom Functions  (00:02:34)
- **Resumo:** Adapta as custom functions do FlutterFlow que extraem valores do JSON de resposta. A função antiga (código da moeda) é renomeada e ajustada para extrair `categoria`, e depois duplicada para extrair `tipo`, testando cada uma com valores de exemplo.
- **Pontos-chave:**
  - As funções seguem o mesmo padrão da aula de cotação de moeda; só muda o campo extraído.
  - Duplicar a função existente é mais rápido que criar do zero.
  - Sempre rodar o botão de check/validação e testar com um valor de amostra antes de salvar.
  - Renomear funções quebra referências nas actions — os erros aparecem e precisam ser corrigidos depois.
- **Link:** https://flix.nocodestartup.io/m/lessons/3463

### 9 - Setup Inicial  (00:06:30)
- **Resumo:** Corrige os erros deixados pelas renomeações e reconstrói a action chain do pop-up de chat. Cria as variáveis de component state `tipo` e `categoria`, liga cada uma à custom function correspondente lendo o output da chamada da OpenAI, desativa temporariamente as actions que ainda não servem e coloca um dialog para inspecionar os valores extraídos.
- **Pontos-chave:**
  - Variáveis de componente `tipo` e `categoria`: string, nullable.
  - Caminho do valor: output da API Call → JSON body → predefined path → "parâmetros função resposta".
  - Ordem importa: primeiro seleciona a custom function, depois passa o output como argumento.
  - Usar "Disable Action" em vez de deletar enquanto testa, e um dialog com Combine Text para exibir tipo + categoria.
  - Conselho central: avançar em partes pequenas — fazer tudo de uma vez impede achar o erro.
  - O system prompt atualizado (com a seção de funções e categorias) é colado na action de carregamento do pop-up.
- **Link:** https://flix.nocodestartup.io/m/lessons/3466

### 10 - Testes Iniciais  (00:02:41)
- **Resumo:** Testa o app rodando. Perguntas genéricas ("olá, tudo bem", "o que você faz") são respondidas pela persona sem acionar a função; perguntas sobre gastos disparam a função e o dialog mostra categoria e tipo corretos. Também valida o comportamento de categoria inexistente.
- **Pontos-chave:**
  - "Quanto gastei com supermercado" → dialog mostra saída / supermercado.
  - Perguntar por gasolina/combustível faz a IA recusar e listar as categorias disponíveis, sem acionar a função — comportamento programado no prompt.
  - Um erro apareceu na chamada durante o teste; recomendação do instrutor é colocar um `if` para exibir a mensagem de erro e conseguir diagnosticar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3465

### 11 - Chamada Supabase  (00:03:10)
- **Resumo:** Encaixa a chamada ao Supabase logo depois da extração dos parâmetros. Passa `categoria` e `tipo` do component state para a API call e troca o conteúdo do dialog pelo corpo bruto da resposta, confirmando que o JSON completo dos registros filtrados chega ao app.
- **Pontos-chave:**
  - A API call precisa de um nome de output definido (ex.: `apiResultGetSupabase`) para ficar disponível nas actions seguintes.
  - Usar **Raw Body Text** para pegar a resposta inteira como texto — é esse texto que vai alimentar a próxima chamada à OpenAI.
  - Com o JSON completo em mãos, a IA passa a enxergar valores, datas e tipos de cada registro.
- **Link:** https://flix.nocodestartup.io/m/lessons/3467

### 12 - Testando De Forma Completa  (00:08:43)
- **Resumo:** Fecha o ciclo. Cria a variável da segunda pergunta, monta com Combine Text um texto que junta a instrução de análise com o JSON do Supabase, adiciona essa mensagem ao histórico, dispara a segunda chamada à OpenAI e adiciona a resposta como `assistant` na lista exibida no chat. O app responde com resumo de categoria, período e total gasto.
- **Pontos-chave:**
  - Nova variável de componente para a "pergunta pós Supabase API" (string, nullable).
  - A instrução usada: pedir um resumo dos registros dizendo categoria, período analisado e total gasto, seguido dos dados (Raw Body Text).
  - Nunca enviar só a pergunta — é preciso adicionar cada mensagem à lista do histórico de conversa antes de chamar a API.
  - A segunda chamada é uma API call separada (nomeada com sufixo 2) para não confundir os outputs.
  - Ganho de contexto: perguntas de follow-up ("qual foi meu maior gasto de supermercado") são respondidas sem nova chamada, porque o JSON já está no histórico.
- **Link:** https://flix.nocodestartup.io/m/lessons/3468

### 13 - Últimos Ajustes  (00:02:40)
- **Resumo:** Resolve o problema visual de o JSON gigante aparecer como mensagem no chat. A solução é enviar essa mensagem com a role `system` em vez de `user`, já que as condições de visibilidade do chat só renderizam `user` e `assistant`. Também refina a instrução para respostas mais diretas e melhor formatadas.
- **Pontos-chave:**
  - Truque de arquitetura: mensagem técnica vai como `system` — fica no contexto do modelo mas invisível para o usuário.
  - As condições de visibilidade do chat filtram por role.
  - Ajuste no prompt: "faça um resumo direto ao ponto" e pedir espaçamento entre as respostas para padronizar o formato.
  - Teste final com a categoria capacitação retorna período e total gasto corretamente, sem exibir o JSON.
- **Link:** https://flix.nocodestartup.io/m/lessons/3470

### 14 - Setup Geral  (00:03:48)
- **Resumo:** Inicia a segunda funcionalidade: filtro por período. Sem ele, perguntas com mês ou ano quebram. Atualiza o JSON da função com dois novos parâmetros (data início e data fim), atualiza o prompt informando ao assistente qual é o ano corrente, e cria as custom functions para extrair as duas datas.
- **Pontos-chave:**
  - Novos parâmetros: data início (filtro "maior que") e data fim (filtro "menor ou igual").
  - Formato das datas precisa ser ano-mês-dia, o mesmo usado pelo Supabase.
  - O prompt passa a informar explicitamente que o ano é 2024, para a IA interpretar "esse ano".
  - As custom functions de extração são duplicadas a partir das anteriores; cuidado para renomear tudo (o instrutor errou o nome e teve que voltar).
- **Link:** https://flix.nocodestartup.io/m/lessons/3469

### 15 - Supabase Api  (00:03:28)
- **Resumo:** Adiciona os filtros de data na URL da chamada ao Supabase, usando a coluna `created_at` com os operadores de comparação. Define valores padrão amplos para quando as variáveis vierem vazias e testa a chamada com um intervalo específico para confirmar que só voltam registros dentro do período.
- **Pontos-chave:**
  - Sintaxe: `&created_at=gte.[data_inicio]&created_at=lte.[data_fim]`.
  - `gte` = maior ou igual (greater than), `lte` = menor ou igual — nomenclatura usada pelo instrutor na aula.
  - As datas são variáveis do tipo **string**, não do tipo data.
  - Valores padrão definidos no campo "valor se vazio": 2000-01-01 e 2050-12-31, para abranger tudo.
  - Teste com 2023-01-01 a 2023-06-01 retorna apenas registros de 2023.
- **Link:** https://flix.nocodestartup.io/m/lessons/3471

### 16 - Action E Testes  (00:07:45)
- **Resumo:** Finaliza a action com os quatro parâmetros e faz a bateria de testes reais. Cria as variáveis de component state das datas, liga as custom functions de extração e passa tudo para a chamada do Supabase. Nos testes, algumas perguntas funcionam perfeitamente e outras falham, e o instrutor mostra as limitações honestamente.
- **Pontos-chave:**
  - Quatro parâmetros no total: categoria, tipo, data início, data fim — todos vindos do primeiro output (`get_despesas`) via predefined path.
  - Nomes de variáveis no FlutterFlow não aceitam certos caracteres/acentos.
  - Definir valor padrão (2000 a 2050) diretamente na chamada para evitar erro quando a IA não devolve data.
  - Comportamentos observados: "quanto gastei com academia esse ano" funciona; "março desse ano" às vezes falha por ambiguidade de contexto; sem período informado, a IA pede o período em vez de chamar a função — o que o instrutor considera bom e ruim ao mesmo tempo.
  - Alerta importante: o modelo pode errar cálculos; vale criar views no Supabase para somar e conferir os totais.
- **Link:** https://flix.nocodestartup.io/m/lessons/3472

### 17 - Finalização  (00:02:19)
- **Resumo:** Diretrizes para levar o chat app pronto para dentro do web app financeiro. O processo é manual, mas simples: copiar o design do pop-up, as custom functions, as action chains e as duas chamadas de API para o projeto do micro SaaS, e expor um botão para o usuário abrir o assistente.
- **Pontos-chave:**
  - Copiar pop-up: selecionar o container maior, Ctrl+C, criar um componente novo no projeto destino e colar.
  - Copiar actions: usar **Copy Action Chain** no botão/elemento.
  - Não esquecer de copiar as duas API calls (OpenAI chat completions e Supabase registros) e as custom functions.
  - A mesma arquitetura funciona com qualquer outro modelo além da OpenAI.
  - O próximo módulo da trilha integra com WhatsApp.
- **Link:** https://flix.nocodestartup.io/m/lessons/3473

### 18 - Desafio  (00:00:46)
- **Resumo:** Propõe o exercício que fecha a lacuna de segurança/multiusuário do projeto: incluir o `user_id` do usuário logado como mais um parâmetro na chamada ao Supabase, para que o assistente retorne apenas os gastos daquela pessoa.
- **Pontos-chave:**
  - Sem o filtro de `user_id`, a chamada traz registros de todos os usuários.
  - Fazer depois que o web app estiver integrado ao chat app.
  - Dúvidas devem ser levadas à comunidade.
- **Link:** https://flix.nocodestartup.io/m/lessons/3474

## Pegadinhas e insights

- **Filtro vazio quebra a chamada.** Passar valor vazio em qualquer parâmetro da URL do Supabase gera erro. A solução do curso é usar o campo de valor padrão do FlutterFlow ("valor se a variável for nula ou vazia") — datas de 2000-01-01 a 2050-12-31 para abranger tudo.
- **A mensagem técnica vai como `system`.** Decisão de arquitetura mais elegante da aula: para reinjetar o JSON do banco no chat sem poluir a interface, envie essa mensagem com role `system`. Ela entra no contexto do modelo, mas as condições de visibilidade (que só mostram `user` e `assistant`) a escondem do usuário.
- **`enum` nos parâmetros vale ouro.** Listar as categorias válidas dentro do JSON da função (e repeti-las no prompt) faz a IA recusar categorias inexistentes e sugerir as disponíveis, em vez de alucinar filtros que não retornam nada.
- **Duas chamadas à OpenAI, não uma.** O ciclo exige a primeira chamada (decidir + extrair parâmetros) e a segunda (interpretar o JSON do banco e responder). São duas API calls distintas no FlutterFlow, com nomes de output diferentes.
- **JSON quebrado no FlutterFlow é armadilha.** O editor não indica onde está o erro e simplesmente bloqueia. Copie o JSON inteiro e peça ao ChatGPT para corrigir a formatação.
- **Limite do plano gratuito do FlutterFlow.** O instrutor precisou apagar uma API call antiga para caber a nova — o plano free limita a quantidade de chamadas API configuradas.
- **Créditos da OpenAI acabam no meio do teste.** Aconteceu durante a gravação; tenha saldo antes de começar a bateria de testes.
- **Import de CSV no Supabase exige o `user_id` correto.** Edite a planilha antes do upload colando um ID real pego em Authentication, senão os registros não ficam associados ao seu usuário.
- **O modelo pode errar contas.** Recomendação explícita: criar views no Supabase para somar e conferir os totais em vez de confiar cegamente na soma feita pela IA.
- **Contexto ajuda e atrapalha.** Como o JSON completo fica no histórico, perguntas de follow-up são respondidas sem nova chamada API (ótimo). Por outro lado, expressões como "esse ano" e "março" são interpretadas de forma inconsistente dependendo do que veio antes na conversa — o próprio instrutor mostra a falha e a deixa como ponto de melhoria.
- **Avance em partes pequenas.** Conselho repetido: teste cada etapa isolada (extrair parâmetros → mostrar em dialog → chamar Supabase → reinjetar na IA). Fazer tudo de uma vez impede localizar o erro.
- **Falta de `user_id` no filtro é um furo real.** No estado em que o projeto termina, a chamada traz os registros sem filtrar por usuário logado — corrigir isso é o desafio final.
