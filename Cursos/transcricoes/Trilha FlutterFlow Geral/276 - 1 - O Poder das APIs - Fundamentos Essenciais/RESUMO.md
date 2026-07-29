# 1 - O Poder das APIs - Fundamentos Essenciais

Trilha FlutterFlow Geral | 10 aulas | ~48 min (0,81 h) | nível iniciante

> Ensina o que é uma API, como ler a estrutura de uma chamada (endpoint, método, headers, body, JSON) e como configurar e rodar chamadas de API dentro do FlutterFlow com segurança.

## O que você sai sabendo fazer

- Explicar o papel de uma API na ponte entre front-end (FlutterFlow) e back-end/serviços externos, e escolher o método HTTP certo (GET/POST/PUT/DELETE).
- Ler a documentação de uma API e montar a chamada: URL base, endpoint, parâmetros de consulta, headers, chave de autorização e body em JSON.
- Testar uma chamada direto pela URL no navegador (com extensão JSON Viewer) e, em casos mais complexos, pelo Postman.
- Criar uma API Call no FlutterFlow com variáveis dinâmicas, testar a resposta na aba Response & Test e salvar JSON Paths pré-definidos.
- Disparar a chamada por uma action de botão (On Tap), tratar os caminhos de sucesso e erro, e exibir os campos retornados em widgets de texto.
- Proteger chaves de API tirando a chamada do client side — via chamada privada no Firebase Cloud Functions ou via ferramenta de automação intermediária.

## Stack e ferramentas

- **FlutterFlow** (API Calls, variáveis, JSON Path, actions, Widget State, Action Outputs, Test Mode)
- **APIs de exemplo:** PokéAPI (aberta, sem chave), ViaCEP (viacep.com.br), OpenAI API (com chave/Bearer)
- **Postman** — teste de chamadas mais complexas (com headers e parâmetros)
- **Extensão JSON Viewer** no navegador — formatar o JSON de resposta
- **Firebase** (Firestore, regras de segurança, Cloud Functions, plano Blaze) e **Supabase** (auth, policies, Edge Functions)
- **Ferramentas de automação como back-end intermediário:** Make, n8n, BuildShip
- Citados como destino de integração: Stripe (pagamentos), Xano (referido na transcrição como "Xeno"/"Zeno")

## Pré-requisitos

Aulas anteriores da formação sobre diferença entre front-end e back-end, noção de CRUD e o básico do FlutterFlow (criar projeto, montar tela, adicionar actions). Ter conta no FlutterFlow para acompanhar a prática. O instrutor pede explicitamente para não pular este módulo antes dos projetos práticos.

## Aula a aula

### 1 - O poder das APIs - Introdução  (00:01:54)
*(Módulo: Conceitos importantes)*
- **Resumo:** Abertura da trilha de APIs, com o mapa do que vem pela frente. O instrutor divide o conteúdo em três blocos: fundamentos teóricos + prática leve, depois dois projetos completos feitos do zero no FlutterFlow. A promessa final é conseguir conectar qualquer aplicativo a qualquer API aberta.
- **Pontos-chave:**
  - Sequência da trilha: o que são APIs → exemplos no navegador → APIs dentro do FlutterFlow → segurança.
  - Projetos práticos que vêm depois: app de super-heróis e app conectado ao ChatGPT (OpenAI).
  - Aviso: não pular o módulo de fundamentos, senão a pessoa se perde nos projetos.
- **Link:** https://flix.nocodestartup.io/m/lessons/2950

### 2 - Conceitos Fundamentais  (00:07:44)
*(Módulo: Conceitos importantes)*
- **Resumo:** Define API (Application Programming Interface) como a camada de comunicação entre sistemas, usando a analogia do garçom levando o pedido do cliente até a cozinha e trazendo o prato de volta. Posiciona o FlutterFlow como ferramenta de front-end que fala com back-ends (Supabase, Xano) e com serviços externos por meio de APIs. Fecha apresentando os métodos HTTP como equivalentes do CRUD e o JSON como formato padrão de troca de dados.
- **Pontos-chave:**
  - FlutterFlow = front-end; back-end e banco ficam em Firebase/Supabase/Xano — a conexão nativa com Supabase também é API por trás dos panos.
  - Mapeamento CRUD → HTTP: POST cria, GET lê, PUT atualiza, DELETE apaga.
  - Fluxo de uma chamada: request → o servidor processa → response com os dados.
  - JSON é o formato dominante (XML é a alternativa citada); chaves para objetos, colchetes para listas.
  - JSON Path serve para consultar/filtrar um valor específico dentro do JSON (ex.: pegar o primeiro item de uma lista).
- **Link:** https://flix.nocodestartup.io/m/lessons/2951

### 3 - Exemplo de uma API na prática!  (00:03:57)
*(Módulo: Conceitos importantes)*
- **Resumo:** Demonstração ao vivo com a PokéAPI: o instrutor usa o formulário de teste do site para buscar um Pokémon, copia a URL gerada e abre direto no navegador para ver o JSON cru. Instala/usa a extensão JSON Viewer para deixar a resposta legível e navega pelos campos, inclusive imagens. Em seguida abre a documentação da OpenAI para contrastar com uma API que exige chave de acesso.
- **Pontos-chave:**
  - Endpoint = a URL que você chama; sempre ler a documentação da API antes de usar.
  - PokéAPI é aberta (sem chave); OpenAI exige gerar uma chave de acesso e entender autenticação.
  - Extensão **JSON Viewer** no navegador formata o JSON de resposta.
  - Trocar o parâmetro final da URL (o nome do Pokémon) muda o resultado — primeira noção de parâmetro dinâmico.
  - Na doc da OpenAI, o endpoint de chat usa POST com corpo em JSON.
- **Link:** https://flix.nocodestartup.io/m/lessons/2952

### 4 - Estrutura Completa de uma API  (00:04:49)
*(Módulo: Conceitos importantes)*
- **Resumo:** Disseca a anatomia de uma requisição: URL base + caminho do recurso + parâmetros de consulta depois da interrogação, mais método, headers e body. Explica que headers carregam as regras da API (tipo de conteúdo aceito) e a chave de autorização no padrão Bearer. Usa a API da OpenAI como exemplo completo, mostrando request e response, e recomenda o Postman para testar chamadas que não cabem numa URL simples.
- **Pontos-chave:**
  - Estrutura: URL base → endpoint/recurso → `?` + parâmetros de consulta (filtros por nome, data, valor etc.).
  - Componentes da chamada: URL, método, headers, body.
  - Header típico: `Content-Type: application/json` + `Authorization: Bearer <sua chave>`.
  - Body em JSON só é necessário em POST; GET dispensa body.
  - Parâmetros podem ser obrigatórios (required) ou opcionais, conforme a documentação.
  - **Postman** é a ferramenta recomendada quando a chamada tem headers/parâmetros e não dá para testar só pela URL.
- **Link:** https://flix.nocodestartup.io/m/lessons/2953

### 5 - Configurações API no FF  (00:05:20)
*(Módulo: API dentro do Flutterflow - Bora pra prática!)*
- **Resumo:** Tour pela área de API Calls do FlutterFlow em um projeto novo. Percorre cada campo do formulário de criação de uma chamada — nome, método, URL base, headers, parâmetros de consulta e variáveis — e mostra como criar uma variável tipada para alimentar um filtro. Termina revisando as configurações avançadas: chamada no front-end vs. privada, proxy, cache e decodificação UTF-8.
- **Pontos-chave:**
  - Menu **API Calls**: chamadas individuais ou em grupo (grupo é recurso do plano Pro).
  - Plano Free permite poucas chamadas (o instrutor cita duas ou três); plano Pro libera chamadas ilimitadas.
  - Variáveis são tipadas (ex.: string, marcador "is list") e entram nos parâmetros de consulta.
  - Por padrão a chamada roda no front-end; existe a opção de chamada privada (tratada na última aula do módulo).
  - Deixar o **proxy padrão ligado** — é a defesa do FlutterFlow contra erros de CORS.
  - Cache guarda a resposta para evitar repetir a chamada a cada troca de página (otimização vista em aulas futuras).
  - Ativar **decodificar resposta em UTF-8** quando o retorno em português vier com acento/ç/til quebrados.
- **Link:** https://flix.nocodestartup.io/m/lessons/2954

### 6 - Exemplo Prático VIA CEP (parte 1)  (00:06:54)
*(Módulo: API dentro do Flutterflow - Bora pra prática!)*
- **Resumo:** Primeira metade do projeto de consulta de CEP. Apresenta a documentação do ViaCEP (API aberta, sem chave nem headers), clona um projeto FlutterFlow com o design já pronto e cria a API Call do tipo GET com a URL da documentação. Testa a chamada com um CEP fixo, depois torna a URL dinâmica com uma variável entre colchetes e salva os JSON Paths que serão usados na tela.
- **Pontos-chave:**
  - ViaCEP: envia um CEP na URL, devolve JSON com logradouro, complemento, bairro, localidade, UF, IBGE, DDD.
  - Nenhum header, chave ou parâmetro de segurança é necessário nessa API.
  - Sintaxe de variável na URL do FlutterFlow: colocar o nome **entre colchetes**; depois criar a variável (tipo string, sem valor padrão).
  - Aba **Response & Test** executa a chamada; é preciso preencher o valor da variável antes de testar.
  - Status **200** = chamada bem-sucedida.
  - O FlutterFlow sugere **JSON Paths recomendados** a partir da resposta — adicionar logradouro, bairro, localidade e UF como paths nomeados evita escrever o caminho na action depois.
  - CEP usado no exemplo: 04094-00 (região do Parque Ibirapuera, São Paulo).
- **Link:** https://flix.nocodestartup.io/m/lessons/2955

### 7 - Exemplo Prático VIA CEP (parte 2)  (00:06:01)
*(Módulo: API dentro do Flutterflow - Bora pra prática!)*
- **Resumo:** Liga a chamada à interface. Adiciona uma action On Tap no botão com o tipo API Call, passa o conteúdo do campo de CEP (via Widget State) para a variável da API e nomeia o resultado. Configura os dois ramos do fluxo — sucesso e falha — e depois preenche cada texto da tela com Action Output + JSON Body + JSON Path pré-definido. Fecha rodando o app em Test Mode e conferindo o preenchimento.
- **Pontos-chave:**
  - A action de API Call abre automaticamente dois caminhos: sucesso e erro.
  - Valor da variável vem de **Widget State → input do CEP**; o resultado recebe um nome (ex.: result CEP).
  - No ramo de erro, mostrar um Alert Dialog usando **Action Outputs → Raw Body Text** para exibir a mensagem real da API.
  - Nos textos: Action Output → API result → **JSON Body** → JSON Path pré-definido (logradouro, bairro, localidade, UF).
  - Sempre preencher o **valor padrão** (ex.: "...") — sem ele o app pode estourar a tela vermelha de erro por valor nulo.
  - Os próximos projetos da trilha vão além do GET e cobrem POST.
- **Link:** https://flix.nocodestartup.io/m/lessons/2956

### 8 - Está gostando do curso?  (00:00:27)
*(Módulo: API dentro do Flutterflow - Bora pra prática!)*
- **Resumo:** Interrupção curta, sem conteúdo técnico. O instrutor pede que o aluno deixe um feedback sobre a formação no link indicado abaixo do vídeo, de preferência com foto de perfil.
- **Pontos-chave:**
  - Aula institucional de pedido de depoimento — pode ser pulada sem perda de conteúdo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3030

### 9 - Segurança Backends e APIs  (00:08:48)
*(Módulo: Segurança das APIs)*
- **Resumo:** Aula mais densa do curso, dividida em duas frentes. Primeiro, como proteger a conexão com o back-end: regras do Firestore + autenticação no Firebase, e policies em todas as tabelas + autenticação no Supabase. Depois, o problema real das chamadas de API feitas no client side — o instrutor mostra um print do inspecionar do navegador em que o token de autorização da OpenAI aparece exposto no app. Encerra com as alternativas para tirar a chamada do front-end.
- **Pontos-chave:**
  - Firebase: sair do modo teste, escrever regras de segurança e exigir autenticação; as regras são configuráveis visualmente pelo FlutterFlow e sincronizam com o Firestore, sem código.
  - Supabase: autenticação + policies em todas as tabelas; chave pública no front-end, chaves privadas nunca expostas.
  - Tudo que roda no front-end é inspecionável pelo usuário — a chave da OpenAI vira crédito gasto por terceiros.
  - **Solução 1:** ativar a chamada privada nas configurações avançadas da API Call, que executa a requisição no **Firebase Cloud Functions**. Exige projeto no Firebase e plano **Blaze** (cartão), mas o volume gratuito cobre muitas chamadas. Fica um pouco mais lento e não exige escrever código.
  - **Solução 2:** colocar uma ferramenta de automação entre o app e a API — **Make, n8n ou BuildShip** — que guarda a chave e devolve o dado; BuildShip é destacado pelas integrações com Supabase e OpenAI.
  - As Edge Functions do Supabase resolveriam o mesmo problema, mas exigem código e ainda não têm integração nativa com o FlutterFlow.
  - Dá para combinar: Supabase como back-end e Firebase Cloud Functions apenas para rodar as chamadas de API.
- **Link:** https://flix.nocodestartup.io/m/lessons/2957

### 10 - Aprendizados e Próximos Passos  (00:02:28)
*(Módulo: Segurança das APIs)*
- **Resumo:** Fechamento do módulo, recapitulando fundamentos, JSON e configuração de chamadas no FlutterFlow. Indica a sequência de estudo: os dois projetos práticos da própria trilha e, depois, conteúdos mais avançados em outras trilhas da formação.
- **Pontos-chave:**
  - Próximos projetos: app de super-heróis (didático, recomendado) e app com ChatGPT — este último ainda em gravação quando a aula foi gravada.
  - Aviso: o projeto de super-heróis foi gravado meses antes e algumas funções/telas do FlutterFlow mudaram, mas a lógica continua válida.
  - Aprofundamento em API e tokens: trilha de Xano (FlutterFlow conversa com Xano 100% via API).
  - Trilha de Supabase tem um módulo dedicado a Supabase + API.
- **Link:** https://flix.nocodestartup.io/m/lessons/2958

## Pegadinhas e insights

- **Chave de API no front-end é o erro central do curso.** Chamada configurada direto no FlutterFlow roda no dispositivo do usuário; basta inspecionar o app no navegador para achar o `Authorization: Bearer`. O instrutor demonstra isso com um print de um app próprio de ChatGPT e diz que quase ninguém fala desse assunto.
- **Correção prática:** ligar a opção de chamada privada (Firebase Cloud Functions) nas configurações avançadas da API Call — depois disso o token some do front-end. Custo: precisa do plano Blaze do Firebase (com cartão, mas com franquia gratuita ampla) e a resposta fica um pouco mais lenta.
- **Limite de plano:** chamadas em grupo (API group) são recurso do plano Pro do FlutterFlow; o Free permite só duas ou três chamadas.
- **Valor padrão obrigatório:** ao vincular um texto a um JSON Path, sem valor padrão o app pode quebrar com erro de null (tela vermelha) enquanto a chamada não retornou. Usar algo como "..." como placeholder.
- **Acentuação quebrada:** ativar "decodificar resposta em UTF-8" quando a API devolve português com acento, til ou cedilha corrompidos.
- **Proxy:** manter o padrão ligado no FlutterFlow evita erros de CORS; desativar já gerou problemas relatados na comunidade.
- **Teste primeiro fora do FlutterFlow:** URL no navegador + JSON Viewer resolve APIs simples; para qualquer coisa com headers e parâmetros, usar Postman.
- **Documentação antes de tudo:** cada API define sua própria forma de montar URL, filtros e autenticação — o curso repete que ler a doc é o passo zero.
- **JSON Paths pré-definidos** economizam trabalho: nomeados na própria API Call, aparecem prontos na action e evitam digitar o caminho do JSON em cada widget.
- **Limitação do Supabase no fluxo:** as Edge Functions poderiam hospedar as chamadas, mas exigem código e não têm integração nativa com o FlutterFlow — por isso a rota recomendada é Firebase Functions ou uma automação intermediária.
- Observação de transcrição: o áudio grafa "Xeno"/"Zeno" (Xano), "Viasap" (ViaCEP), "build chip" (BuildShip), "erro de cores" (erro de CORS) e "logadouro" (logradouro).
