# F3.5 - Fundamentos SaaS NoCode

Trilha Nocode IA | 11 aulas | ~52 min (0,87h) | nível iniciante

> Curso de fundamentação que explica o modelo de negócio SaaS/MicroSaaS, compara as principais ferramentas no-code de frontend e backend, e mostra na prática a conexão FlutterFlow + Supabase.

## O que você sai sabendo fazer

- Diferenciar SaaS de MicroSaaS e escolher qual modelo faz sentido pro seu nicho e apetite de risco.
- Descrever a arquitetura de um SaaS (frontend, backend, CRUD) antes de começar a construir.
- Escolher entre Bubble, FlutterFlow e WeWeb com base em critérios objetivos (app nativo, SEO, código-fonte, preço, curva de aprendizado).
- Escolher entre Supabase, Firebase e Xano segundo tipo de banco (relacional x não relacional), integração nativa e custo.
- Navegar o editor do FlutterFlow (elementos, storyboard, painel de propriedades, teste no "raiozinho") e o dashboard do Supabase (tabelas, SQL, auth, policies, storage).
- Conectar FlutterFlow ao Supabase via API URL + Anon Key e alimentar uma ListView com Backend Query e dados dinâmicos.

## Stack e ferramentas

- **FlutterFlow** — frontend escolhido pelo curso (gera código Dart/Flutter).
- **Supabase** — backend escolhido pelo curso (Postgres relacional, open source, banco vetorial).
- Citados na comparação de frontend: Bubble, WeWeb, Adalo, Bravo, Power Apps, Softr.
- Citados na comparação de backend: Firebase, Xano, Baserow, Backendless, Airtable.
- Recomendações fora do FlutterFlow: **Framer** (sites/landing pages), **Make** (automações), Softr/planilhas.
- Exemplos de SaaS com IA citados: Interview Solver, MyGroupMetrics, extensão de IA para Google Meet no Chrome, Synthflow.

## Pré-requisitos

Nenhum formal — o curso é de fundamentos e assume zero conhecimento de SaaS. Ajuda ter noção básica do que é banco de dados/planilha. As aulas de overview pedem conta criada no FlutterFlow e no Supabase (ambas têm plano gratuito) se você quiser acompanhar clicando junto.

## Aula a aula

### 1 - Introdução - O Que Você Irá Aprender (00:01:36)
- **Resumo:** Abertura do módulo, apresentando o roteiro das aulas. O instrutor explica que o bloco cobre fundamentos de SaaS, comparação das melhores ferramentas de frontend, comparação das de backend e um primeiro contato prático com FlutterFlow.
- **Pontos-chave:**
  - Objetivo declarado: sair sabendo escolher ferramenta e ter noção de como unir front e back sem código.
  - A divisão do curso segue a arquitetura frontend (visual/lógica) x backend (dados/inteligência).
  - O FlutterFlow é anunciado desde o início como a ferramenta que será explorada.
- **Link:** https://flix.nocodestartup.io/m/lessons/3078

### 2 - O Que São Saas (00:07:27)
- **Resumo:** Aula conceitual sobre o modelo Software as a Service. Define SaaS como software vendido por assinatura recorrente, lista as vantagens econômicas do modelo e depois contrasta SaaS com MicroSaaS. Fecha com a arquitetura padrão (frontend + backend) e o conceito de CRUD.
- **Pontos-chave:**
  - Exemplos de SaaS do dia a dia: Netflix, Prime Video, Google, Zoom, Slack, Canva, Notion — quase todos com modelo freemium.
  - Vantagens do modelo: baixo custo marginal por cliente novo, receita recorrente e previsível, distribuição 100% digital, mercado global, estrutura enxuta.
  - Empresa tradicional cresce custo junto com faturamento; SaaS descola os dois — é aí que mora a margem.
  - MicroSaaS = nicho específico, menos concorrência, menos risco, menos escala; donos costumam operar sozinhos e mirar MRR na casa de 30–50 mil.
  - Arquitetura: front (telas, fluxo de usuário, lógica) conversando com back (banco, segurança, mídia, servidor) via CRUD — Create, Read, Update, Delete.
- **Link:** https://flix.nocodestartup.io/m/lessons/3079

### 3 - Exemplos De Saas Com Ia (00:03:04)
- **Resumo:** Vitrine rápida de produtos reais que combinam SaaS/MicroSaaS com IA, para mostrar que o modelo é monetizável em nichos estreitos. O instrutor comenta o problema que cada um resolve e por que a especificidade do nicho é o que caracteriza o MicroSaaS.
- **Pontos-chave:**
  - Interview Solver: IA para desenvolvedor mandar bem em entrevista técnica de código ao vivo.
  - MyGroupMetrics: resumos, hot topics e métricas de engajamento de grupos de WhatsApp; criado por Bruno e André, tem teste freemium.
  - Extensão de Chrome que transcreve e resume reuniões no Google Meet.
  - Synthflow: SaaS de agentes conversacionais com voz, construído em no-code, captou US$ 1,8 milhão de investimento.
  - A lição: quanto mais nichado o problema, mais fácil o posicionamento e a primeira venda.
- **Link:** https://flix.nocodestartup.io/m/lessons/3080

### 4 - Frontend (00:08:58)
- **Resumo:** Aula-chave de decisão. Filtra o mercado no-code até três finalistas de frontend — Bubble, FlutterFlow e WeWeb — e compara critério a critério, incluindo preço. Termina com um veredito segmentado por perfil (empreendedor x dev/agência) e justifica a escolha do curso.
- **Pontos-chave:**
  - Bubble é o único que traz frontend e backend integrados; FlutterFlow e WeWeb precisam de backend externo.
  - App nativo com funções de celular: só FlutterFlow. SEO: WeWeb melhor, Bubble ok, FlutterFlow fraco. Performance web: Bubble e WeWeb bons, FlutterFlow ainda pesado.
  - Acesso ao código-fonte: FlutterFlow e WeWeb sim, Bubble não.
  - Preços citados: Bubble a partir de US$ 29/mês (com cobrança extra por uso de backend — principal fraqueza) e só 1 app por plano; FlutterFlow entre US$ 25 e 35/mês com apps ilimitados; WeWeb a partir de US$ 39/mês. FlutterFlow e WeWeb têm custo adicional de backend à parte.
  - Veredito: app nativo → FlutterFlow; empreendedor com pouco tempo fazendo web app → Bubble (mais rápido de aprender); dev ou agência → FlutterFlow. O curso segue com **FlutterFlow**.
- **Link:** https://flix.nocodestartup.io/m/lessons/3081

### 5 - O Poder Do Flutterflow (00:03:09)
- **Resumo:** Apresenta o FlutterFlow para quem nunca usou, mostrando cases de mercado e delimitando quando a ferramenta é ou não a escolha certa. Aula pulável para quem já conhece a plataforma.
- **Pontos-chave:**
  - Gera código Dart (framework Flutter) e o código é seu — autonomia sobre a tecnologia.
  - Cases citados: AB Money (600 mil+ usuários, US$ 100 mil+ de faturamento) e Atlas (100 mil+ downloads, na Apple Store); mais exemplos no Showcase oficial.
  - Usar para: SaaS robusto, app com recursos nativos, projeto que exige código-fonte próprio.
  - **Não** usar para: sites e landing pages, projetos que dependem de SEO forte, automações avulsas, projetos baseados em planilha.
  - Alternativas recomendadas para esses casos: Framer (site/landing da sua SaaS), Make (automações), Softr (planilhas).
- **Link:** https://flix.nocodestartup.io/m/lessons/3082

### 6 - Overview Flutterflow (00:07:43)
- **Resumo:** Tour guiado pela interface do FlutterFlow. O instrutor cria um projeto em branco ("app de tarefas"), passeia pelo painel de elementos e propriedades, monta um container com coluna e título, e depois puxa um template de lista para explicar como a hierarquia de widgets se organiza. É reconhecimento de terreno, não passo a passo.
- **Pontos-chave:**
  - Criar via **Create Blank** — o instrutor desaconselha começar por templates prontos até você já saber mexer.
  - No setup inicial dá para definir nome, cores, habilitar web e configurar Firebase (ele pula o Firebase nesta aula).
  - Cada elemento selecionado abre suas propriedades no painel da direita (padding, alinhamento, largura/altura em % etc.); há área de segurança reservada na tela.
  - Menu lateral: storyboard (fluxo de telas), banco de dados, data types, App State, chamadas de API, mídias, código customizado, Cloud Functions, testes automatizados, tema de cores, settings.
  - Barra superior: páginas, componentes, geração por IA, troca de viewport (iPad/desktop), dark mode, comentários, performance, bugs, branches, download do código e o "raiozinho" para rodar/testar o app.
  - Estrutura típica de um template de lista: coluna → linha → texto → **ListView** (é a ListView que depois se conecta às listas do banco).
- **Link:** https://flix.nocodestartup.io/m/lessons/3083

### 7 - Comparativo (00:06:32)
- **Resumo:** Espelho da aula de frontend, agora para backend. Compara Supabase, Firebase e Xano em tipo de banco, recursos, integração com FlutterFlow e preço, explicando a diferença entre banco relacional e não relacional. Termina definindo o backend oficial do curso.
- **Pontos-chave:**
  - Relacional (tabelas ligadas entre si): Supabase e Xano. Não relacional (documentos e coleções, mais flexível): Firebase.
  - Todos têm banco integrado, autenticação, functions/webhooks, storage e realtime. Interface no-code: só Xano. Open source: só Supabase (dá para self-hospedar sem custo). Firebase é da Google e tem o maior leque de funcionalidades (ex.: machine learning).
  - Integração com FlutterFlow: Firebase é a mais profunda (nasceram juntos), Supabase também é nativa, Xano só via API.
  - Preços: Firebase é pay-as-you-go (até 20 mil documentos gravados por dia no gratuito — modelagem errada pode gerar susto na fatura); Supabase tem freemium e plano pago a US$ 25/mês; Xano começa em US$ 85/mês e o gratuito não dá para testar de verdade — vale pedir desconto regional para brasileiro.
  - O curso segue 100% com **Supabase**, também por ele ser forte para aplicações de IA.
- **Link:** https://flix.nocodestartup.io/m/lessons/3085

### 8 - O Poder Do Supabase (00:01:40)
- **Resumo:** Introdução curta ao Supabase como alternativa relacional ao Firebase. Lista os serviços que compõem a plataforma e destaca o banco vetorial como diferencial para projetos de IA.
- **Pontos-chave:**
  - Modelo de linhas e colunas é mais fácil para quem não é programador do que documentos/coleções do Firebase.
  - Traz banco de dados, autenticação, storage de mídia, Edge Functions, realtime e construtor de API.
  - Vector Database para aplicações de inteligência artificial mais robustas.
  - Argumentos de venda: performance, escalabilidade, segurança e aderência a leis de proteção de dados.
- **Link:** https://flix.nocodestartup.io/m/lessons/3086

### 9 - Overview Supabase (00:04:37)
- **Resumo:** Tour prático pelo dashboard do Supabase. O instrutor cria um projeto novo, monta a tabela `tarefas`, insere registros de exemplo e passa pelas seções de SQL, autenticação, políticas de segurança, storage e Edge Functions.
- **Pontos-chave:**
  - Na criação do projeto dá para escolher a **região** do banco — importa para performance e para exigências legais (há região no Brasil).
  - Tabela `tarefas` criada com ID e data automáticos + colunas título, descrição e imagem (link), todas do tipo texto.
  - Editor SQL disponível para consultas; relações entre tabelas são configuradas na criação das colunas.
  - **Políticas de segurança (RLS)** são obrigatórias para definir quem acessa a tabela: no exemplo ele cria uma policy permissiva em `public.tarefas`, liberando todas as operações com a condição `true`.
  - Demais seções: storage para PDFs/imagens, Edge Functions, banco realtime, relatórios e documentação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3087

### 10 - Unindo Frontend + Backend Do App (00:05:38)
- **Resumo:** A aula que fecha o ciclo: liga o app FlutterFlow ao projeto Supabase e faz a lista de tarefas exibir dados reais do banco. Configura a integração, cria a query no ListView, mapeia os campos dinâmicos e testa adicionando um registro novo pelo Supabase.
- **Pontos-chave:**
  - Integração em **Settings → Integrations → Supabase**, informando **API URL** e **Anon Key** (ambas em Settings → API no Supabase) e clicando em **Get Schema** para importar as tabelas.
  - No template de lista, deletar os itens duplicados e deixar só um — ele é o modelo que a ListView vai repetir.
  - Na ListView, usar **Backend Query** → Query Type: Supabase → tabela `tarefas` → lista de linhas (sem filtro e sem ordenação no exemplo).
  - Trocar os textos fixos por dados dinâmicos clicando no ícone laranja e apontando para `tarefa row → título / descrição / imagem`, com fallback null quando vazio.
  - Antes de testar, ajustar a página inicial em **Settings → App Details**; testar pelo "raiozinho" (a primeira sessão de teste demora a carregar).
  - Autenticação foi deliberadamente deixada de fora para manter o exemplo simples.
- **Link:** https://flix.nocodestartup.io/m/lessons/3089

### 11 - Aprendizados - Como Aprender Mais FF (00:01:49)
- **Resumo:** Encerramento com recapitulação do que foi visto e indicação dos próximos cursos da plataforma para se aprofundar em cada ferramenta.
- **Pontos-chave:**
  - Recap: fundamentos e arquitetura de SaaS, melhores ferramentas de front, melhores de back, e FlutterFlow + Supabase em conjunto.
  - Formação completa de FlutterFlow (do zero ao avançado, 60–70 horas) inclusa no mesmo pacote.
  - Também inclusos no pacote: formação de Bubble e curso de WeWeb.
  - Próximo módulo junta tudo para construir projetos de SaaS com IA.
- **Link:** https://flix.nocodestartup.io/m/lessons/3090

## Pegadinhas e insights

- **Bubble cobra pelo uso do backend.** Como front e back são integrados, consumo alto vira taxa extra — o instrutor alerta que fica caro para brasileiro pagando em dólar. Plano inicial de US$ 29 cobre apenas 1 app.
- **FlutterFlow tem custo escondido:** o plano (US$ 25–35) é só de frontend; o banco de dados é conta à parte. Em compensação, apps ilimitados no mesmo plano.
- **Firebase pode gerar fatura-surpresa.** O gratuito é generoso (até 20 mil gravações de documento por dia), mas modelagem errada dos dados dispara o consumo.
- **Xano é o mais caro** (US$ 85/mês para começar) e o gratuito não permite testar um app de verdade — mas vale pedir desconto regional para o Brasil.
- **Não use FlutterFlow para site/landing page.** SEO é ponto fraco do Flutter; a orientação é fazer a landing em Framer e mandar o usuário para o SaaS.
- **Não comece por templates prontos no FlutterFlow** se você ainda não domina a ferramenta — você fica perdido na estrutura que outra pessoa montou.
- **Policies de segurança no Supabase não são opcionais.** Sem policy, a tabela não é acessível; a policy `true` usada na aula libera tudo e serve só para demonstração — não é configuração de produção.
- **Escolha da região do banco no Supabase é decisão de compliance,** não só de performance: há legislações (ex.: Europa) que exigem os dados dentro do território.
- **Decisão de arquitetura do curso:** FlutterFlow (front, código-fonte próprio, multiplataforma, boas integrações com IA) + Supabase (relacional, open source, US$ 25/mês, banco vetorial para IA). Firebase seria a alternativa se a prioridade fosse integração mais profunda com FlutterFlow.
- A ListView do FlutterFlow é o ponto onde o app encosta no banco — entender que ela repete um único item-modelo evita a confusão de tentar editar todos os itens duplicados do template.
