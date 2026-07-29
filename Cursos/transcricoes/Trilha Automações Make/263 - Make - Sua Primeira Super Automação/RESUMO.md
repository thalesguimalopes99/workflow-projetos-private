# Make | Sua Primeira Super Automação
Trilha Automações Make | 5 aulas | ~19min20s | iniciante
> Constrói do zero, no Make, uma automação de 3 módulos que lê respostas de um formulário no Google Sheets, manda pro ChatGPT classificar/resumir o feedback e devolve o resultado na própria planilha.

## O que você sai sabendo fazer
- Vincular um Google Forms a uma planilha do Google Sheets e usá-la como fonte de dados de uma automação.
- Configurar o módulo Google Sheets "Watch New Rows" como gatilho (arquivo, aba e quantidade de linhas por execução).
- Conectar o módulo OpenAI no Make usando API Key + Organization ID e criar um completion com role de usuário.
- Montar um prompt que injeta o campo de resposta do formulário como variável vinda do módulo anterior.
- Gravar a saída da IA de volta na linha certa da planilha com "Update a Row" (spreadsheet ID, sheet name, row number, coluna).
- Ajustar o prompt para controlar o formato da resposta (uma palavra, resumo em 2–3 frases) e evitar respostas longas demais.

## Stack e ferramentas
- **Make** (cenários, módulos, execução "run once"/rodar em todos)
- **Google Forms** (pesquisa de satisfação/feedback)
- **Google Sheets** (módulos "Watch New Rows" e "Update a Row")
- **OpenAI / ChatGPT** via API (módulo Create a Completion, modelo GPT-3.5)
- Painel da OpenAI: página de **API Keys** e **Organization ID** (settings)

## Pré-requisitos
- Conta no Make e noção básica de como montar um cenário (o instrutor cita que o módulo anterior cobriu a parte mais técnica).
- Conta Google (Forms + Sheets) e conta na OpenAI com acesso à API para gerar a chave.

## Aula a aula

### 001 - Descrição do Caso de Uso  (00:02:06)
- **Resumo:** Abertura do módulo apresentando o case prático: um cenário simples, menos técnico que o do módulo anterior, já usando IA. O problema real é receber muitos feedbacks de usuários de uma ferramenta, cada um escrito de um jeito diferente, e não conseguir tratar isso manualmente. A proposta é usar automação + IA para qualificar e resumir esses feedbacks, perdendo o mínimo de tempo.
- **Pontos-chave:**
  - Ferramentas do case: Google Forms + ChatGPT.
  - Contexto: coletar feedback dos primeiros usuários de um micro-SaaS via formulário.
  - Dois objetivos possíveis da automação: classificar em positivo/negativo ou resumir cada feedback.
  - A automação será construída do zero na sequência.
- **Link:** https://flix.nocodestartup.io/m/lessons/2841

### 002 - Overview do Cenário do Caso  (00:03:28)
- **Resumo:** Demonstração do resultado final antes de construir. O cenário tem apenas 3 módulos: receber o dado, tratar o dado, anotar em outro lugar. O instrutor responde o próprio formulário com um feedback fictício negativo, roda a automação e mostra a linha da planilha sendo atualizada com a qualificação gerada pelo ChatGPT.
- **Pontos-chave:**
  - Arquitetura em 3 passos: Google Sheets (trigger) → ChatGPT (tratativa) → update na planilha.
  - Escolheu Google Forms por ter integração nativa com Sheets; daria para coletar por Webhook, ensinado em aulas futuras.
  - O prompt inicial pede para classificar o sentimento do feedback.
  - Ganho prático: com 200–300 respostas, basta filtrar positivo/negativo no Sheets para priorizar a análise.
- **Link:** https://flix.nocodestartup.io/m/lessons/2842

### 001 - Integrando Google Sheets  (00:02:40)
- **Resumo:** Início da construção. Antes de configurar o Make, o instrutor volta ao Google Forms e cria a pesquisa "V2 - Pesquisa de Opinião", vinculando as respostas a uma planilha nova pela aba de respostas. Com a planilha existindo, configura no Make o módulo Google Sheets com a função "Watch New Rows", apontando arquivo, aba e o número de linhas coletadas por execução.
- **Pontos-chave:**
  - Ordem correta: criar o formulário e vincular a planilha PRIMEIRO, porque o arquivo só existe depois disso.
  - No Forms, na aba de respostas, dá para criar uma planilha nova ou selecionar uma existente.
  - Renomeie o formulário antes de as respostas começarem a chegar (senão vira "Formulário sem título").
  - Módulo Make: Google Sheets → **Watch New Rows** → arquivo + aba + limite de linhas (1, 5, 10 — depende do uso e do intervalo de verificação).
  - Precisa dar refresh no Make para a planilha recém-criada aparecer na lista.
- **Link:** https://flix.nocodestartup.io/m/lessons/2843

### 002 - Integrando Open AI  (00:05:42)
- **Resumo:** Configuração do segundo e terceiro módulos. No módulo OpenAI escolhe "Create a Completion", cria a conexão com API Key e Organization ID pegos no painel da OpenAI, seleciona o modelo 3.5 e escreve a mensagem com role de usuário contendo o prompt de classificação de sentimento mais a variável do campo de resposta do formulário. Depois adiciona o Google Sheets de escrita e testa a automação de ponta a ponta respondendo o formulário como se fosse um cliente.
- **Pontos-chave:**
  - Conexão OpenAI exige **API Key** e **Organization ID**; ambos ficam nas páginas de API Keys e de settings/organization da conta.
  - Modelo usado: **3.5**. Role da mensagem: **user**.
  - O prompt concatena o texto fixo ("classifique o sentimento do seguinte feedback") com a variável da coluna de resposta do Forms.
  - Antes do update, crie na planilha a coluna que vai receber o resultado (qualificação/resumo do feedback).
  - **Correção do instrutor:** o módulo certo NÃO é "Update a Cell", é **Update a Row** — assim ele escreve na linha correta.
  - No Update a Row dá para reaproveitar as variáveis do módulo anterior: Spreadsheet ID, Sheet Name e **Row Number**; a coluna C recebe o `content` de dentro do `message`/output do ChatGPT.
- **Link:** https://flix.nocodestartup.io/m/lessons/2844

### 003 - Ajustes Prompts OpenAI  (00:05:24)
- **Resumo:** Refino do prompt. A primeira resposta da IA veio como frase longa, ruim para filtrar na planilha, então o instrutor reescreve o prompt para forçar saída apenas "positivo" ou "negativo" e separa a instrução em duas ordens (o que analisar e qual formato de saída). Depois troca o prompt por um pedido de resumo em duas ou três frases e roda a automação com três feedbacks para comparar o comportamento.
- **Pontos-chave:**
  - Resposta longa demais atrapalha filtro no Sheets — peça saída curta e específica.
  - Separar o prompt em instruções explícitas (tarefa + formato do output) melhora a aderência.
  - Prompts em inglês costumam funcionar melhor; evite gírias e palavras ambíguas.
  - Dá para rodar o cenário sobre todas as linhas ("rodar a partir de todos") para reprocessar respostas já existentes.
  - Segunda versão do fluxo: em vez de classificar, pedir "resumo do feedback em duas ou três frases" — o prompt pode ser em português.
  - No teste com 3 feedbacks, o resumo do feedback negativo inventou detalhe (funcionalidade X) — invenção do próprio GPT.
- **Link:** https://flix.nocodestartup.io/m/lessons/2845

## Pegadinhas e insights
- **Ordem de criação importa:** o arquivo do Sheets só aparece no Make depois que o Forms é vinculado a uma planilha. Renomeie tudo antes das primeiras respostas para não ficar com "Formulário sem título".
- **Update a Cell ≠ Update a Row:** o instrutor erra ao vivo e corrige — para atualizar a resposta na linha certa, use **Update a Row** com o Row Number vindo do módulo de trigger.
- **Mapeie a saída certa da OpenAI:** o texto útil é o `content` que vem dentro do `message` do output, não o output inteiro.
- **O output da IA varia conforme o prompt.** Sem instrução de formato, ele devolve frase completa e quebra o filtro da planilha. Quanto mais específico o prompt, mais próximo do que você quer.
- **Prompt em inglês tende a performar melhor**, e gírias devem ser evitadas.
- **Alucinação acontece:** o resumo gerado citou uma funcionalidade que não existia no feedback original — sinal de que a saída da IA precisa de conferência.
- Crie a coluna de destino na planilha antes de configurar o update, senão não há onde gravar o resultado.
- O número de linhas por execução no Watch New Rows é decisão de arquitetura: depende do volume e do intervalo de verificação do cenário.
