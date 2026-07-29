# 3 - Planejamento Backend Supabase

Trilha Supabase | 9 aulas | ~47 min (0,78h) | intermediário

> Como planejar e montar do zero o backend completo de um app EAD no Supabase — conceito, modelagem, tabelas, policies, views e storage — deixando tudo pronto para plugar em qualquer front-end no-code.

## O que você sai sabendo fazer

- Conceitualizar um app antes de codar: definir usuários, funcionalidades por perfil e mapa de telas (feito no Miro).
- Modelar o banco seguindo as 4 etapas (requisitos → conceitual → lógico/DER → físico), incluindo tabela auxiliar para resolver relações muitos-para-muitos.
- Criar tabelas no Supabase com chaves estrangeiras via UI (`foreign relation`), escolhendo o comportamento de update/delete (`no action` vs `cascade`).
- Configurar RLS policies por tabela para liberar acesso e conseguir consumir as APIs REST auto-geradas.
- Escrever views com um ou dois JOINs para juntar dados de 3 tabelas num único endpoint (matrícula + aluno + curso).
- Criar bucket no Storage com políticas e entender o caminho de upload de imagem via API.

## Stack e ferramentas

- **Supabase** — Table Editor, Schema Visualizer, SQL Editor, Authentication/Policies (RLS), API Docs auto-gerada, Storage (buckets), assistente de IA do painel.
- **PostgreSQL / SQL** — `CREATE VIEW`, `DROP VIEW`, `JOIN`, `SELECT`, chaves primárias e estrangeiras.
- **Miro** — desenho da conceitualização, das entidades e do DER.
- **status.supabase.com** — checagem de incidentes/manutenção da plataforma.
- **Postman** (referência do módulo anterior) — testes das chamadas de API.
- Mencionados como destino do backend, sem uso nesta etapa: **FlutterFlow**, **Bubble**, **WeWeb**.

## Pré-requisitos

- Curso de **modelagem de dados SQL** da trilha (declarado como praticamente obrigatório — o instrutor acelera o assunto aqui).
- Módulo anterior de **APIs do Supabase** (o instrutor assume que você já sabe montar as chamadas e vai direto ao ponto).
- Projeto Supabase já iniciado nas aulas anteriores, com as tabelas `cursos` e `usuarios` criadas e a view de join curso/professor existente.

## Aula a aula

### 001 - O que você irá aprender  (00:04:40)
- **Resumo:** Abertura do módulo. O objetivo é fechar 100% do backend do app de cursos EAD para que, nos módulos seguintes, ele seja plugado em qualquer front-end no-code sem retrabalho. O instrutor reforça que nada de FlutterFlow ou Bubble ainda: o foco é só Supabase. Também apresenta a metodologia da NoCode Startup: pensar problema, conceito, usuários, telas e só depois construir.
- **Pontos-chave:**
  - Entregável do módulo: tabelas, views, APIs e policies prontas.
  - Metodologia obrigatória antes de construir — conceitualização geral evita se perder.
  - As telas do app virão prontas (reaproveitadas da trilha "do zero ao web app SaaS"); o foco não é design.
  - Modelagem de dados é a parte mais importante do módulo.
- **Link:** https://flix.nocodestartup.io/m/lessons/2650

### 002 - Conceitualização do App  (00:03:48)
- **Resumo:** Apresentação do conceito do app desenhado no Miro: plataforma EAD com professores e alunos. São listadas as funcionalidades por tipo de usuário, o mapa de telas e os perfis do sistema. A promoção de aluno para professor é uma ação manual do administrador direto no backend.
- **Pontos-chave:**
  - Três tipos de usuário: administrador (o próprio dev), aluno e professor.
  - Professor: lista de cursos criados, total de alunos, CRUD de curso, adicionar/deletar aulas.
  - Aluno: ver cursos disponíveis, detalhes, matricular-se, marcar curso como realizado.
  - Só 3 telas: login/cadastro, dashboard do aluno, dashboard do professor — o resto vira pop-up.
  - Bloqueio de acesso por perfil: aluno não entra no dashboard do professor.
- **Link:** https://flix.nocodestartup.io/m/lessons/2651

### 003 - Modelagem de Dados  (00:08:38)
- **Resumo:** Percorre as quatro etapas da modelagem (análise de requisitos, modelo conceitual, modelo lógico/DER e modelo físico) e aplica ao app. Define as entidades, decide fundir professores e alunos numa única tabela `usuarios` diferenciada por um campo de tipo, e resolve o muitos-para-muitos aluno↔curso com a tabela auxiliar `matriculas`. Fecha com o DER desenhado no Miro.
- **Pontos-chave:**
  - Entidades finais: `usuarios`, `cursos`, `aulas`, `matriculas` (+ `auth.users` nativa do Supabase).
  - `auth.users` não pode ser alterada — cria-se uma tabela `usuarios` própria ligada a ela por relação **um-para-um** compartilhando o mesmo `user_id` como PK.
  - Um professor tem muitos cursos, mas um curso tem um só professor (1:N). Um curso tem muitas aulas (1:N).
  - Aluno↔curso é N:N → exige tabela auxiliar `matriculas`, cada linha = uma matrícula, com FKs `user_id` e `curso_id`.
  - Professor e aluno viram o mesmo registro em `usuarios`, separados por um campo de tipo.
  - Campos de `cursos`: `prof_id`, nome, descritivo, foto de capa, carga horária. Campos de `aulas`: id, `curso_id`, `user_id`, nome e URL da aula.
  - Aviso: errar a modelagem agora obriga a refazer tudo lá na frente.
- **Link:** https://flix.nocodestartup.io/m/lessons/2652

### 004 - Criar Tabelas  (00:07:09)
- **Resumo:** Mão na massa no Table Editor criando as duas tabelas que faltavam: `matriculas` e `aulas`. Mostra como declarar chave estrangeira pela UI (`foreign relation` → schema `public` → tabela → coluna) e escolher a ação de referência. Depois popula tudo com dados de exemplo, criando usuários novos e associando cada um ao registro correspondente em `auth.users`.
- **Pontos-chave:**
  - `matriculas`: `id`, `created_at`, `user_id` (FK → `public.usuarios.user_id`), `curso_id` (FK → `public.cursos.id`).
  - Escolheu **`no action`** em vez de `cascade` para que deletar uma matrícula não afete os usuários.
  - `aulas`: `id`, `created_at`, `curso_id` (FK → `cursos`), `prof_id` (FK → `usuarios`), `aula_nome` (text), `aula_url` (text).
  - Inserir usuário em `usuarios` dá erro se não for vinculado a um registro existente em `auth.users` — é preciso puxar o ID de lá.
  - `Database → Schema Visualizer` mostra as relações já montadas graficamente.
  - Se o Supabase apresentar banner de incidente ou comportamento estranho, consulte `status.supabase.com`.
  - Observação do instrutor: o `prof_id` em `aulas` talvez fosse dispensável, já que a aula já se liga ao curso, que se liga ao professor.
- **Link:** https://flix.nocodestartup.io/m/lessons/2653

### 005 - Policies Tabelas  (00:01:57)
- **Resumo:** Aula curta configurando RLS em Authentication → Policies para as tabelas novas. Cria policies do tipo "liberar tudo" (`ALL`, com `true`/`true`) em `matriculas`, `cursos` e `aulas`, inclusive relaxando a policy de `cursos` que antes exigia usuário autenticado. Encerra lembrando que com as tabelas liberadas todas as APIs REST de CRUD já estão disponíveis e documentadas.
- **Pontos-chave:**
  - Sem policy, a tabela não é acessível pela API — é o passo que destrava o front-end.
  - Padrão usado no curso: policy `all` com condição `true` e `true`.
  - O instrutor libera geral só para simplificar o aprendizado e recomenda restringir a usuários autenticados no projeto real.
  - Toda tabela ganha automaticamente CRUD via API + documentação no painel.
- **Link:** https://flix.nocodestartup.io/m/lessons/2654

### 006 - Dados Completos Curso e Professores  (00:06:02)
- **Resumo:** Parte do mockup do dashboard para justificar as views: o pop-up de detalhe do curso precisa mostrar dados que vivem em tabelas diferentes (curso + professor). Reaproveita e enriquece a view de join criada nas aulas iniciais, adicionando campos, e mostra que view não se edita — derruba com `DROP VIEW` e recria. No fim popula fotos de perfil e comprova que a view reflete a atualização na hora.
- **Pontos-chave:**
  - Regra prática: quando o layout pede dados de tabelas diferentes num só lugar, isso é uma view.
  - View `dados_curso_prof`: junta `cursos` (alias `c`) com `usuarios` (alias `u`) dando match `c.prof_id = u.user_id`.
  - Campos adicionados: capa do curso (URL), descrição longa, nota, e nome/e-mail/foto de perfil do professor.
  - Fluxo para alterar uma view: `DROP VIEW <nome>` e rodar o `CREATE VIEW` novo no SQL Editor.
  - A view é sempre um espelho: mudou a URL da foto na tabela, a view já mostra atualizado.
  - Desenhar a tela antes revela quais views o backend precisa ter.
- **Link:** https://flix.nocodestartup.io/m/lessons/2655

### 007 - Dados Completos Matricula Alunos e Cursos  (00:09:02)
- **Resumo:** Constrói a view mais avançada do módulo, com dois JOINs a partir da tabela auxiliar. O problema: `matriculas` só guarda IDs, inútil para exibir uma lista na tela. A solução é partir de `matriculas` e juntar primeiro `usuarios`, depois `cursos`. O instrutor testa em etapas — comenta a linha do `CREATE VIEW` e roda só o `SELECT` — corrige erros de vírgula e de nome de tabela no plural, e só cria a view quando o resultado sai certo.
- **Pontos-chave:**
  - View `dados_matricula_alunos_cursos`: `matriculas m` + join `usuarios u` em `u.user_id = m.user_id` + join `cursos c` em `c.id = m.curso_id`.
  - Retorna id da matrícula, nome/e-mail/foto do aluno e nome, descrição curta, descrição longa e nota do curso.
  - Técnica de depuração: comentar o `CREATE VIEW` e rodar só o `SELECT` até o retorno estar correto, evitando criar view quebrada.
  - Aliases claros (`m`, `u`, `c`) e renomear as colunas de saída (`aluno_nome` no lugar de `prof_nome`) para o front não se confundir.
  - Erros reais que apareceram: vírgula faltando na lista de campos e nome de tabela no singular (é `matriculas`, plural).
  - View não aceita insert — inserir dados é sempre na tabela de origem; a view atualiza sozinha.
  - O instrutor sugere escrever o SQL na mão em vez de pedir para a IA do Supabase, para de fato aprender.
- **Link:** https://flix.nocodestartup.io/m/lessons/2656

### 008 - Upload de Imagens  (00:04:45)
- **Resumo:** Fecha as duas pontas que faltavam para o front. Primeiro a busca: usar o filtro `ilike` da API REST para o campo de pesquisa por nome (a API Docs também traz paginação). Depois o upload de imagem, que não está documentado na API Docs da tabela — o instrutor recorre à documentação geral e ao assistente de IA para descobrir o endpoint. Termina criando o bucket no Storage com políticas liberadas.
- **Pontos-chave:**
  - Busca por nome no app = filtro `ilike` da API do Supabase (mesmo modelo testado no Postman).
  - Upload por API exige POST no endpoint de storage passando nome do bucket, caminho do arquivo, header de autorização e o arquivo — é o ponto mais chato de montar via API.
  - No FlutterFlow a integração com Supabase é nativa: upload e boa parte das URLs de API são desnecessárias. WeWeb também é citado como nativo; no Bubble talvez seja preciso plugin.
  - Storage → `New bucket` chamado `imagens`, com políticas de select, insert, update e delete liberadas para todos (configuração padrão confirmada).
- **Link:** https://flix.nocodestartup.io/m/lessons/2657

### 009 - Aprendizados do Módulo  (00:00:53)
- **Resumo:** Fechamento rápido. Recapitula que o backend está completo — tabelas, APIs, views e policies — e pronto para receber qualquer front-end. Anuncia que o próximo módulo constrói o app de fato, com FlutterFlow para quem está nessa formação.
- **Pontos-chave:**
  - Backend concluído e independente da ferramenta de front.
  - Próximo passo da trilha: construir o app EAD no FlutterFlow.
- **Link:** https://flix.nocodestartup.io/m/lessons/2658

## Pegadinhas e insights

- **A tabela `auth.users` do Supabase é intocável.** Crie uma tabela `usuarios` própria e ligue por relação um-para-um usando o mesmo `user_id` como chave primária. Inserir em `usuarios` sem vincular a um registro de `auth.users` retorna erro.
- **Muitos-para-muitos sempre pede tabela auxiliar.** Aluno↔curso vira `matriculas`, uma linha por matrícula com as duas FKs — sem isso você duplica dado e quebra as formas normais.
- **Fundir professor e aluno numa tabela `usuarios` com campo de tipo** simplifica muito o modelo em vez de manter duas tabelas separadas.
- **`no action` vs `cascade`:** o instrutor escolheu `no action` nas FKs de `matriculas` justamente para que apagar uma matrícula não propague deleção para usuários.
- **Policies liberadas (`all` / `true` / `true`) são didáticas, não de produção.** O próprio instrutor avisa: no projeto real, restrinja a usuários autenticados. Ele inclusive afrouxou a policy de `cursos`, que já estava mais segura, só para não travar as aulas.
- **View não se edita nem recebe insert.** Para mudar, `DROP VIEW` + `CREATE VIEW`. Para inserir dados, use a tabela de origem — a view atualiza sozinha.
- **Teste o `SELECT` antes de criar a view:** comente o `CREATE VIEW`, rode só a consulta e valide o resultado. Poupa criar e derrubar view repetidamente.
- **Nome de tabela no plural** foi a causa de um dos erros ao vivo (`matricula` vs `matriculas`) — junto com vírgula faltando na lista de campos.
- **Upload de imagem não aparece na API Docs da tabela.** É preciso ir na documentação de Storage; a montagem manual do POST com bucket, path, autorização e arquivo é a parte mais trabalhosa. FlutterFlow e WeWeb resolvem nativamente; Bubble pode exigir plugin.
- **Desenhe a tela antes de decidir as views.** Foi olhando o mockup do pop-up (nome do curso + nome e foto do professor) que ficou claro qual join era necessário.
- **Não terceirize o SQL para a IA do painel logo de cara** — escrever na mão é o que fixa o aprendizado, segundo o instrutor.
- **`status.supabase.com`** é o lugar para checar se um comportamento estranho da plataforma é incidente/manutenção e não erro seu.
- **Campo possivelmente redundante:** o `prof_id` em `aulas` pode ser dispensável, já que a aula aponta para o curso, que já aponta para o professor.
