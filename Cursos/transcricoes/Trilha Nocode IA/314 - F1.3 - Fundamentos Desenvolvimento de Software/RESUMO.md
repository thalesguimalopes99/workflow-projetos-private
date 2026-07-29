# F1.3 - Fundamentos Desenvolvimento de Software

Trilha Nocode IA | 9 aulas | ~29 min (0,48h) | iniciante

> Curso conceitual que estabelece a base para construir apps/SaaS no-code: o que é software (front-end + back-end), como sistemas conversam via API e webhook, e qual o passo a passo metodológico até o desenvolvimento.

## O que você sai sabendo fazer

- Distinguir software de website, e app nativo de web app, para decidir a estrutura do projeto antes de começar.
- Explicar e desenhar a arquitetura de um SaaS separando front-end, banco de dados/back-end e serviços integrados via API.
- Ler e interpretar respostas JSON, e testar uma API GET direto pelo navegador (com extensão JSON Viewer para leitura).
- Montar mentalmente a estrutura de uma chamada de API: endpoint, método, parâmetros de query, headers (Content-Type, Authorization Bearer) e body.
- Escolher entre API (você pergunta) e webhook (o serviço avisa) conforme o caso de uso, especialmente em pagamentos/assinaturas.
- Seguir a metodologia da NoCode Startup — problema → conceitualização → design de telas → modelagem de dados → desenvolvimento → teste/melhoria contínua (PDCA).

## Stack e ferramentas

Citadas ao longo das aulas (a maioria como referência conceitual, não em execução):

- **Front-end / builders:** FlutterFlow (principal na formação), Bubble, Softr, WhatsApp (como interface de bot)
- **Back-end / banco de dados:** Supabase, Xano
- **Automação/integração:** Make, n8n
- **Serviços integrados via API:** OpenAI (ChatGPT / Assistants), Gemini, Stripe, Mercado Pago, Pagar.me, Asaas, Google Maps, Google Translate
- **APIs de teste na prática:** PokéAPI, ViaCEP
- **Ferramentas de apoio:** Postman (testar APIs — indicado via vídeo no YouTube do canal), extensão JSON Viewer para Chrome, Miro (wireframe), Figma (protótipo), Dribbble e Behance (referências de design)
- **Formatos/conceitos:** JSON, HTTP request, métodos GET/POST/PUT/DELETE, webhook, PDCA

## Pré-requisitos

Nenhum. É o módulo de fundamentos da trilha; nada de código ou conta em plataforma é exigido para acompanhar.

## Aula a aula

### 1 - Fundamentos Software (00:01:29) — módulo Intro
- **Resumo:** Abertura do módulo. O instrutor apresenta a tríade da formação (desenvolvimento de produto, SaaS no-code e inteligência artificial/agentes) e enquadra estes fundamentos como a base para tirar uma ideia do papel. Antecipa os três blocos do curso: conceitos de software, APIs e fases de desenvolvimento.
- **Pontos-chave:**
  - Tríade da formação: produto + SaaS no-code + IA/agentes.
  - API é destacada como o conceito mais importante para criar soluções com IA — precisa da teoria e da prática.
  - O curso divide a construção de um app em fases sequenciais.
- **Link:** https://flix.nocodestartup.io/m/lessons/3161

### 2 - O Que São Softwares (00:03:21) — módulo Intro
- **Resumo:** Define software como a união de front-end e back-end em interação constante. O front-end concentra design, UX/UI, lógica de negócio e fluxo do usuário; o back-end concentra banco de dados, segurança/autenticação, armazenamento de mídia, ações de servidor e automações. A aula fecha diferenciando software de site e app nativo de web app.
- **Pontos-chave:**
  - Software = sistema **dinâmico** (ação no front impacta o back); site = projeto **estático**, focado em prover informação.
  - Arquitetura de SaaS: front-end + back-end + tecnologias plugadas (IA, pagamento/assinatura, serviços Google) — todas conectadas via API.
  - App nativo usa recursos do celular (câmera, GPS, geolocalização, velocidade) e é publicado na Google Play / App Store.
  - Web app roda no navegador (Chrome, Firefox), inclusive no celular, sem ser nativo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3162

### 3 - Definições (00:05:20) — módulo Apis
- **Resumo:** Aula central de conceito de API (Application Programming Interface) como interface de comunicação entre sistemas diferentes. Usa a analogia do garçom — leva o pedido do cliente à cozinha e volta com o prato — para explicar o ciclo requisição/resposta. Mapeia onde cada ferramenta entra na arquitetura e apresenta os quatro métodos HTTP básicos e o JSON como linguagem oficial das APIs.
- **Pontos-chave:**
  - API conecta seu software a qualquer tecnologia externa: OpenAI, Stripe, Mercado Pago, Gemini, Google Maps, Google Translate.
  - Mapa da arquitetura: front-end (FlutterFlow, Softr, Bubble, WhatsApp) → banco/back-end (Supabase, Xano) → automação (Make, n8n) → serviços via API.
  - Métodos: **POST** cria dados, **GET** só puxa, **PUT** atualiza, **DELETE** apaga.
  - FlutterFlow tem integração nativa com Supabase (mais rápida que montar a chamada de API na mão).
  - JSON é leve, legível por humano e máquina, e permite relações complexas (colchete = lista).
- **Link:** https://flix.nocodestartup.io/m/lessons/3163

### 4 - Pokeapi E Viacep (00:03:47) — módulo Apis
- **Resumo:** Demonstração prática de chamadas GET sem escrever código. O instrutor usa a PokéAPI (base de dados de Pokémon) buscando "pikachu" pelo próprio site e depois colando a URL no navegador, mostrando o JSON bruto retornado. Instala a extensão JSON Viewer para formatar a resposta e navegar por habilidades, movimentos, espécies e imagens. Repete o exercício com o ViaCEP, que devolve o endereço a partir de um CEP.
- **Pontos-chave:**
  - Toda chamada GET é uma URL: cola no navegador e o JSON aparece.
  - Extensão **JSON Viewer** (Chrome) organiza o JSON e tem tema dark — sem ela a leitura é inviável.
  - PokéAPI retorna até URLs de imagem (sprites frente/costas) dentro do JSON.
  - ViaCEP: passa o CEP na URL, recebe o endereço completo em JSON.
  - Aviso final: POST (criar/atualizar dados) **não** dá para testar pela URL do navegador — precisa de plataforma dedicada, pois há outros parâmetros.
- **Link:** https://flix.nocodestartup.io/m/lessons/3164

### 5 - Estrutura De Uma Chamada (00:03:28) — módulo Apis
- **Resumo:** Destrincha as partes de uma requisição de API. Explica a URL como endpoint (URL base + recurso + `?` para parâmetros de consulta + `&` para encadear filtros, incluindo a chave da API). Depois mostra o que muda num POST: método, cabeçalho e corpo. Usa a documentação da OpenAI (criação de assistente) como exemplo real de POST e encerra recomendando o Postman.
- **Pontos-chave:**
  - Endpoint: URL base → recurso → `?` parâmetros de consulta → `&` para múltiplos filtros/chave.
  - Header de um POST: formato do conteúdo (JSON) + autorização com a palavra **Bearer** seguida da chave.
  - Body: JSON com os dados a inserir (no exemplo genérico, nome e emprego).
  - Exemplo OpenAI: POST para criar um assistente, passando header de autorização, cabeçalho de beta, modelo e instruções em JSON.
  - Regra do instrutor: sempre ler a documentação do serviço com calma antes de conectar.
  - **Postman** é a ferramenta recomendada para testar GET, POST e PUT de forma organizada (há vídeo dedicado no YouTube do canal).
- **Link:** https://flix.nocodestartup.io/m/lessons/3165

### 6 - Webhooks (00:02:45) — módulo Apis
- **Resumo:** Contrasta webhook com API pela mesma analogia do restaurante: na API você pergunta e recebe resposta; no webhook a cozinha avisa sozinha quando o prato fica pronto. O webhook dispensa a requisição — fica aguardando um gatilho e envia o dado automaticamente. O exemplo central é controle de assinatura em SaaS.
- **Pontos-chave:**
  - API = requisição + resposta (você puxa). Webhook = envio automático a partir de um gatilho (você espera).
  - Caso de uso: em vez de perguntar ao gateway se o usuário pagou, o gateway avisa no vencimento.
  - Gateways citados para assinatura: Stripe, Mercado Pago, Pagar.me, Asaas.
  - Ficar perguntando (polling) seria trabalhoso — daí a existência do webhook.
  - Pagamentos é o cenário onde webhook é mais usado.
- **Link:** https://flix.nocodestartup.io/m/lessons/3166

### 7 - Metodologia (00:02:12) — módulo Fases de Desenvolvimento
- **Resumo:** Apresenta a metodologia da NoCode Startup em etapas encadeadas, partindo sempre do problema a resolver. Depois vêm conceitualização da solução, design de telas (wireframe e alta fidelidade), modelagem do banco de dados e só então o desenvolvimento, unindo front-end e back-end. O instrutor reforça que o ciclo é contínuo: medir, testar com usuários, aprender e voltar ao problema.
- **Pontos-chave:**
  - Ordem: problema → conceitualização → design de telas → banco de dados → desenvolvimento.
  - Conceitualização = resumo geral de telas, usuários e funcionalidades.
  - Wireframe é esboço; alta fidelidade é a tela pronta.
  - Modelagem de dados e relações é a etapa mais pulada — e a que mais gera retrabalho.
  - O processo é cíclico: teste com usuário pode mudar layout, banco ou o próprio conceito da solução.
- **Link:** https://flix.nocodestartup.io/m/lessons/3167

### 8 - Exemplo Prático (00:06:08) — módulo Fases de Desenvolvimento
- **Resumo:** Aplica a metodologia inteira num caso concreto: uma rede de escolas que precisa de um sistema para alunos acessarem cursos EAD online. O instrutor percorre cada fase — conceito do app, lista de funcionalidades por tipo de usuário, mapa de telas e pop-ups, wireframe no Miro, tela de alta fidelidade, modelo conceitual do banco com as relações entre tabelas — até o desenvolvimento em FlutterFlow com Supabase. Fecha com o ciclo PDCA de melhoria contínua.
- **Pontos-chave:**
  - Três tipos de usuário no exemplo: administrador, professor e aluno — funcionalidades mapeadas separadamente para cada um.
  - Telas listadas: login, cadastro, dashboard, além dos pop-ups.
  - Referência de design: Dribbble e Behance. Conselho do instrutor: não crie design do zero, junte modelos prontos como referência.
  - Protótipo/wireframe feito no Miro; Figma também serve. A alta fidelidade foi montada direto no FlutterFlow.
  - Relações do modelo de dados: professor→cursos é **um para muitos**; alunos↔cursos é **muitos para muitos**.
  - Stack final do exemplo: FlutterFlow (front-end) + Supabase (back-end), rodando em celular e desktop.
  - **PDCA** = planejar, fazer, checar, agir — o loop de melhoria com base no teste real com usuários.
  - Existe um curso completo de modelagem de dados e SQL na formação; aqui o tema é só tangenciado.
- **Link:** https://flix.nocodestartup.io/m/lessons/3168

### 9 - Aprendizados (00:00:25) — módulo Conclusão
- **Resumo:** Encerramento curto. Recapitula os três eixos vistos — o que é software, comunicação via API e webhook, e as fases de desenvolvimento — e posiciona o módulo como base para os próximos da formação.
- **Pontos-chave:**
  - Recapitulação: software, API/webhook, fases de desenvolvimento.
  - Serve de pré-requisito conceitual para os módulos seguintes.
- **Link:** https://flix.nocodestartup.io/m/lessons/3169

## Pegadinhas e insights

- **O erro mais comum apontado pelo instrutor:** pular direto para o desenvolvimento. O resultado é descobrir tarde que as telas e o banco de dados estão errados e ter que voltar tudo.
- **Modelagem de dados é a etapa mais negligenciada** e a que mais custa caro depois. Definir tabelas, campos e cardinalidade (1:N, N:N) antes de construir.
- **GET você testa no navegador; POST/PUT não.** POST exige método, headers e body, então precisa de uma plataforma como o Postman.
- **Sem extensão JSON Viewer, ler o retorno de uma API no navegador é impraticável** — a resposta vem como um bloco corrido.
- **Autorização em API se escreve com `Bearer` + chave** no header, junto do Content-Type JSON.
- **Webhook existe para você não ficar perguntando.** Em assinaturas, perguntar ao gateway a cada ciclo é insustentável — deixe o gateway avisar no gatilho.
- **Integração nativa > chamada de API manual** quando disponível: FlutterFlow↔Supabase é o caso citado como bem mais rápido.
- **Não desenhe do zero.** O conselho explícito é minerar Dribbble/Behance e combinar referências, porque a maioria não é boa em design.
- **Leia a documentação de cada serviço antes de integrar** — cada API tem sua própria forma de teste e seus próprios parâmetros.
- Site estático e software dinâmico são projetos diferentes: confundir os dois leva a escolher a arquitetura errada logo no início.
