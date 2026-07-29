# 1.2 - Extra: Use IA como seu Super Funcionário

Trilha Supabase | 7 aulas | ~22 min (00:22:48) | iniciante

> Ensina a usar IA (a assistente nativa do Supabase e o bot de Supabase da NoCode StartUp) para escrever SQL, modelar banco de dados, gerar dados de teste e depurar erros sem precisar dominar SQL.

## O que você sai sabendo fazer

- Gerar SQL de `CREATE TABLE` e `INSERT` a partir de pedidos em português dentro do SQL Editor do Supabase.
- Corrigir erros de query com o botão "Debug with Supabase AI", que aponta a linha real do erro e a correção.
- Pedir uma modelagem de dados completa (tabelas, campos e relações) para um app do zero e receber o SQL pronto para colar.
- Montar consultas com JOIN e chave estrangeira descrevendo a relação em linguagem natural.
- Popular tabelas com dezenas de registros aleatórios para testes.
- Tirar dúvidas técnicas de Supabase (API REST, permissões de endpoint) com um bot alimentado pela documentação oficial.

## Stack e ferramentas

- **Supabase** — SQL Editor, assistente de IA integrada ("Ask Supabase AI to modify your query"), "Debug with Supabase AI", seção de Funções SQL, painel de configuração de API / API REST.
- **IA da NoCode StartUp** ("NoCode IAs") — bots especialistas por ferramenta (Supabase, WeWeb, Bubble, Firebase), construídos juntando a documentação da ferramenta com o ChatGPT. Gratuito para alunos.
- **ChatGPT / Bard** — citados como alternativas genéricas.
- **PostgreSQL** — base do Supabase, mencionada como diferencial de performance.

## Pré-requisitos

Ter noção básica de SQL e do funcionamento do Supabase (o instrutor trata este módulo como extra sobre as aulas anteriores de SQL, JOIN e API da mesma trilha). Para usar o bot da NoCode StartUp é preciso ter acesso à plataforma.

## Aula a aula

### 1 - Introdução IA  (00:01:15)
- **Resumo:** Abertura do módulo extra. O instrutor posiciona a IA como um "super funcionário" especialista em Supabase e SQL, útil justamente quando você trava na parte técnica: escrever uma query ou modelar o banco. Adianta que serão usadas tanto IAs genéricas quanto as duas específicas do módulo.
- **Pontos-chave:**
  - Foco do módulo: os prompts certos, não a ferramenta em si.
  - Opções citadas: ChatGPT, Bard, IA do Supabase e IA da NoCode StartUp.
  - Objetivo prático: acelerar a construção do projeto e a modelagem de dados.
- **Link:** https://flix.nocodestartup.io/m/lessons/2628

### 2 - Criar tabelas e Dados  (00:04:30)
- **Resumo:** Demonstra a IA nativa do Supabase dentro do SQL Editor, acionada pelo botão que oferece modificar a query atual. Pedindo em português, ela gera o `CREATE TABLE` de uma tabela de cursos, aceita refinamento com lista explícita de campos e, na sequência, gera os `INSERT` com dados aleatórios. Fecha pedindo a modelagem inteira de um clone de rede social e recebendo várias tabelas conectadas.
- **Pontos-chave:**
  - Botão da IA no SQL Editor: "Ask Supabase AI to modify your query"; a sugestão vem como diff para aceitar ou descartar antes do Run.
  - Prompt eficaz = enumerar os campos desejados (ID, nome do curso, duração, nota, professor, data de criação, quantidade de alunos).
  - Ela erra tipo de dado às vezes (duração veio como texto) — revisar antes de aceitar.
  - Pedido de "preencher com dados aleatórios" gera os INSERT aproveitando o contexto da tabela criada antes.
  - Pedido amplo ("tabelas de um app tipo Facebook") retornou usuários, friends, posts, comentários e likes já relacionados.
- **Link:** https://flix.nocodestartup.io/m/lessons/2629

### 3 - Correção de Erros  (00:02:24)
- **Resumo:** Mostra o uso da IA para depuração. O instrutor introduz de propósito uma vírgula errada numa função SQL, roda e recebe uma mensagem de erro que aponta a linha errada (o `FROM`, quando o problema estava na linha anterior). O botão "Debug with Supabase AI" localiza o erro real e explica como corrigir.
- **Pontos-chave:**
  - A mensagem de erro nativa do Postgres frequentemente aponta a linha seguinte à do erro real.
  - "Debug with Supabase AI" aparece junto ao erro e devolve causa + correção.
  - Recomendação de escopo: use a IA do Supabase para a parte técnica de SQL (funções, JOINs); para dúvidas conceituais, o bot da NoCode StartUp.
  - Um JOIN entre cursos e usuários poderia ter sido gerado só descrevendo os campos e os IDs a conectar.
- **Link:** https://flix.nocodestartup.io/m/lessons/2630

### 4 - Modelagem de Dados  (00:05:30)
- **Resumo:** Apresenta os bots da NoCode StartUp, treinados com a documentação completa da ferramenta somada ao ChatGPT. Usando o bot de Supabase, o instrutor define o papel dele ("você é meu consultor de modelagem de dados") e pede a modelagem de um app de cursos online: recebe tabelas, campos e relações, e depois pede o SQL correspondente. Repete o exercício com um clone de Airbnb e tenta popular uma das tabelas.
- **Pontos-chave:**
  - Estrutura de prompt: atribuir papel ao bot + descrever o projeto + pedir tabelas e relações; depois pedir "as funções SQL para copiar e colar no Supabase".
  - Modelagem sugerida para o app de cursos: cursos, usuários, inscrições, aulas, progresso.
  - Clone de Airbnb devolveu listings, users, bookings e reviews (nomes em inglês, precisam ser traduzidos).
  - O bot mantém contexto da conversa e melhora as respostas com base nas anteriores.
  - Quando ele "se perde" (responde em inglês ou ignora o pedido), a saída é recarregar e refazer as perguntas.
- **Link:** https://flix.nocodestartup.io/m/lessons/2631

### 5 - Criar Consultas Complexas  (00:04:09)
- **Resumo:** Sobe o nível: em vez de tabelas isoladas, constrói passo a passo uma relação. Cria a tabela de cursos, depois a de professores, adiciona um campo `prof_id` como chave estrangeira e por fim pede uma consulta que junte as duas via JOIN. O resultado reproduz praticamente a query que o curso tinha ensinado a escrever à mão nas aulas anteriores.
- **Pontos-chave:**
  - Trabalhe em etapas: criar tabela → criar segunda tabela → adicionar FK → pedir o JOIN.
  - No prompt da FK, diga explicitamente qual campo, em qual tabela e por meio de qual ID da tabela alvo.
  - Peça os campos do resultado por nome (nome do curso, duração, nome do professor, e-mail do professor).
  - A query gerada usa aliases (`c` para cursos, `p` para professores) e faz o JOIN em `c.prof_id = p.id`.
  - Prompt vago confunde o bot; refine o texto e repita até sair certo.
- **Link:** https://flix.nocodestartup.io/m/lessons/2632

### 6 - Criar registros para tabelas  (00:01:20)
- **Resumo:** Aula curta sobre gerar massa de dados para teste. Basta pedir uma quantidade específica de registros para uma tabela e o bot devolve os `INSERT` prontos, respeitando os campos já definidos, inclusive o ID do professor nas linhas de curso.
- **Pontos-chave:**
  - Prompt direto: "crie N registros para a tabela X" (usados 15, 20, 30 e 50 na demonstração).
  - Ele preenche as chaves estrangeiras existentes.
  - Sem instrução extra os nomes saem sequenciais ("Professor 32"); peça explicitamente nomes aleatórios se quiser variedade.
  - Fluxo: copiar o SQL gerado e colar no Supabase.
- **Link:** https://flix.nocodestartup.io/m/lessons/2633

### 7 - Perguntas Específicas  (00:03:40)
- **Resumo:** Fecha o módulo mostrando o bot como fonte de consulta técnica e estratégica. Primeiro uma pergunta genérica sobre criar API retorna resposta vaga; ao especificar "dentro do Supabase, a partir das tabelas criadas", a resposta fica útil e aponta o caminho no painel. Depois o instrutor faz perguntas comparativas e até pede que o bot o convença a usar Supabase.
- **Pontos-chave:**
  - Especificidade muda a qualidade: contextualize a pergunta na ferramenta e no seu cenário.
  - Caminho de API indicado: painel do Supabase → configurações de API → API REST, com URL por endpoint e permissões de acesso configuráveis por endpoint.
  - Comparativo Supabase x Firebase citado pelo bot: leituras básicas ~300% mais rápidas (benchmarks da própria Supabase), por ser construído sobre PostgreSQL.
  - Outros argumentos que ele levantou: código aberto, escalabilidade para milhares de requisições simultâneas e carga serverless, preço acessível, comunidade ativa, acesso direto a recursos do Postgres (views, funções).
  - Dá para conversar iterativamente ("ainda não me convenceu") e receber novos argumentos.
- **Link:** https://flix.nocodestartup.io/m/lessons/2634

## Pegadinhas e insights

- **Sempre revise o SQL gerado.** A IA do Supabase escolheu tipo texto para um campo de duração que deveria ser numérico. Aceitar sem olhar leva erro para dentro do schema.
- **Erro de sintaxe do Postgres mente sobre a linha.** No exemplo da vírgula extra, a mensagem apontou o `FROM` da linha seguinte. É exatamente o caso em que "Debug with Supabase AI" economiza tempo.
- **O bot da NoCode StartUp troca de idioma e perde o fio.** Aconteceu na aula de modelagem: ele passou a responder em inglês e deixou de entender o pedido. Solução do instrutor: recarregar e refazer as perguntas.
- **Nomes em inglês nas modelagens.** Modelos gerados (listings, bookings, reviews) vêm em inglês; padronize antes de aplicar no projeto.
- **Divisão de trabalho entre as duas IAs, segundo o instrutor:** a nativa do Supabase é melhor para a parte técnica dentro do editor (criar/alterar tabela, função SQL, debug); o bot da NoCode StartUp é melhor para consultoria — modelagem do zero, explicação conceitual e dúvidas de documentação.
- **Por que o bot da NoCode StartUp é preferido a ChatGPT genérico:** é gratuito para alunos e está atualizado com a documentação completa do Supabase (citada como ~4 milhões de caracteres); a IA genérica pode estar desatualizada.
- **Padrão de prompt que funciona:** atribuir um papel ("você é meu consultor de modelagem"), descrever o projeto, enumerar os campos, e só então pedir o SQL. Ir por etapas em vez de pedir tudo de uma vez.
- **Tese central do módulo:** saber SQL vira base para avaliar e corrigir o que a IA produz, não pré-requisito para produzir. O que passa a importar é formular a pergunta certa.
