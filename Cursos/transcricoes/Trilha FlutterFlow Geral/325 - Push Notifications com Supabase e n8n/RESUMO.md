# Push Notifications com Supabase e n8n

Trilha FlutterFlow Geral | 11 aulas | ~34 min (00:34:12) | nível intermediário

> Como enviar notificações push para dispositivos Android num app FlutterFlow, usando FCM (Firebase Cloud Messaging) como entregador, Supabase como base de tokens/usuários e n8n como orquestrador do envio (simples, agendado, segmentado e via webhook).

## O que você sai sabendo fazer

- Criar o projeto Firebase pelo FlutterFlow e gerar a chave privada de **conta de serviço** (JSON) para autenticar máquina-a-máquina no Google Cloud.
- Escrever uma custom action em Dart (pacote `firebase_messaging`) que pede permissão, obtém o token FCM do dispositivo e grava esse token num App State.
- Gravar o token FCM na tabela de usuários do Supabase no momento do cadastro, com relação de cascata para `auth.users`.
- Montar no n8n a credencial **Google Service Account API** com escopo do Firebase Messaging e disparar `POST` para `fcm.googleapis.com` (`messages:send`).
- Enviar notificação de 4 formas: manual (clique), agendada (Schedule Trigger), segmentada por filtro no Supabase (por token, não por tópico) e reativa via Webhook do Supabase.

## Stack e ferramentas

- **FlutterFlow** — app Android, custom action, App State, ação de criar conta.
- **Firebase / FCM (Firebase Cloud Messaging)** — serviço gratuito de entrega de push; API `fcm.googleapis.com` método `messages:send`.
- **Google Cloud** — projeto espelho do Firebase; credencial de conta de serviço (client_email + private_key); Google Auth para emissão do token de acesso.
- **Supabase** — tabela `users` (token, tipo de usuário, id FK de `auth.users`), Database > Webhooks, chaves de API (URL do projeto + service_role secret).
- **n8n** — workflows, credenciais, nós: Manual Trigger, Schedule Trigger, Webhook, HTTP Request, Supabase (Get Many rows).
- **Dart / pacote `firebase_messaging`** (PubDev) — código da custom action.
- **ChatGPT** — usado para consolidar trechos dispersos da documentação do Firebase num único código.
- **VS Code / bloco de notas** — só para abrir o JSON da chave.

## Pré-requisitos

- Conta e projeto no FlutterFlow (o projeto do módulo está disponível para clonar).
- Projeto Supabase com autenticação já em uso (o curso usa auth do Supabase, não do Firebase).
- Conta no n8n (plano pago ou self-hosted).
- Noção básica de FlutterFlow (App State, ações de página) ajuda; programação Dart não é obrigatória — o código é fornecido pronto.

## Aula a aula

### Intro / 001 - Introdução  (00:00:57)
- **Resumo:** Abertura do módulo. O instrutor apresenta o objetivo: enviar push para Android combinando Supabase e n8n. Adianta os temas — conceito de push, o processo por trás, webhooks no Supabase, chaves do FCM e automação no n8n.
- **Pontos-chave:**
  - Ao final você consegue disparar notificações de promoção, feature ou comunicado no seu app.
  - O projeto do módulo está disponível no FlutterFlow para clonar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3475

### Intro / 002 - O que são notificações push  (00:01:03)
- **Resumo:** Conceitua push como mensagem que chega ao dispositivo mesmo com o app fechado. Define o escopo do módulo: só Android nativo, via FCM, que é gratuito. Lista as quatro formas de envio que serão construídas.
- **Pontos-chave:**
  - FCM é serviço gratuito.
  - Módulo é 100% Android; iOS fica para um módulo específico futuro.
  - Quatro formas: simples, agendada, segmentada e via webhook.
  - Segmentada e webhook usam o Supabase como apoio.
- **Link:** https://flix.nocodestartup.io/m/lessons/3476

### Intro / 003 - Entendendo o processo  (00:04:09)
- **Resumo:** Aula conceitual que desenha a arquitetura toda. Explica que criar projeto no Firebase cria também um projeto no Google Cloud, onde o FCM é uma das APIs disponíveis. Justifica por que a credencial correta é a conta de serviço (e não OAuth nem API key), já que quem conversa com o Google é o n8n, não um humano. Fecha mostrando o fluxo completo: token do dispositivo → tabela no Supabase → n8n autentica → POST para o FCM → notificação entregue.
- **Pontos-chave:**
  - Acesso ao FCM: via SDK ou via requisição HTTP à API — o curso usa a API.
  - Conta de serviço = conta que não representa usuário humano; é o tipo certo para aplicação↔Google Cloud.
  - É preciso criar projeto Firebase pelo FlutterFlow, mas **não** é obrigatório usar Firebase Auth (a auth é do Supabase).
  - A notificação vai para o **dispositivo** (token), não para o usuário; a tabela no Supabase é o que amarra token ↔ usuário e permite segmentar.
  - O n8n já resolve sozinho a obtenção do token no Google Auth a partir da credencial de conta de serviço.
- **Link:** https://flix.nocodestartup.io/m/lessons/3478

### Desenvolvimento / 001 - Criando o projeto no Firebase e obtendo a credencial de conta de serviço  (00:02:00)
- **Resumo:** Passo a passo prático da criação do projeto Firebase a partir do FlutterFlow (Settings > Firebase > criar projeto > gerar arquivos de configuração) e da geração da chave privada no console do Firebase. Mostra o JSON baixado e indica quais campos serão usados depois no n8n.
- **Pontos-chave:**
  - Caminho no console: Configurações do projeto > Contas de serviço > gerar nova chave privada (baixa um JSON).
  - Do JSON inteiro só interessam `client_email` e `private_key`.
  - A geração dos arquivos de configuração no FlutterFlow leva menos de um minuto.
  - A chave é secreta — o instrutor só mostra na tela porque vai apagá-la depois.
- **Link:** https://flix.nocodestartup.io/m/lessons/3477

### Desenvolvimento / 002 - Criando uma custom action para obter um token do FCM  (00:08:47)
- **Resumo:** Aula mais densa do módulo. Mostra que a documentação do Firebase espalha o código em várias páginas (instanciar, configurar notificação, pegar token, inscrever em tópico) e como ele usou o ChatGPT para unir os trechos numa única função assíncrona em Dart. Cria a custom action `push notifications` com a dependência `firebase_messaging`, sem argumentos e sem retorno, envolta em try/catch. O token retornado por `getToken()` é atribuído a uma variável de App State (`FCM token`, tipo string) e a action é registrada em Final Actions para rodar no start do app. Demonstra no celular: cria conta, o app exibe o token na home e a linha aparece no Supabase.
- **Pontos-chave:**
  - Pacote do PubDev: `firebase_messaging`; código em Dart com `try/catch`.
  - Enxugue as opções de configuração da notificação sugeridas pela IA — várias não servem (ex.: CarPlay é da Apple).
  - `getToken()` → variável local → App State `FCM token` (string).
  - Registrar a action em **Custom Files > Final Actions** para executá-la depois dos loads iniciais.
  - Ele inscreve o dispositivo num tópico chamado "geral", mas o tópico é só demonstrativo — a segmentação real será feita pelo Supabase.
  - Na ação de criar conta: primeiro `Auth Create Account` (provider e-mail), depois insert no Supabase com `fcm_token`, nome, tipo ("gratuito", fixo) e `id` = User ID autenticado.
  - Na tabela `users` do Supabase, `id` é PK e FK de `auth.users` com cascata — apagar o usuário apaga a linha.
- **Link:** https://flix.nocodestartup.io/m/lessons/3480

### Desenvolvimento / 003 - Conhecendo a interface do n8n  (00:04:01)
- **Resumo:** Tour pela ferramenta antes de construir os fluxos: workflows, templates prontos, credenciais, variáveis compartilhadas entre workflows e histórico de execuções com debug. Abre um workflow em branco para explicar gatilho + ações, arrastar/conectar/remover blocos e testar nó a nó ou o fluxo inteiro. Termina falando de preço e da opção self-hosted.
- **Pontos-chave:**
  - Credenciais ficam guardadas como variáveis de ambiente e não são expostas nas chamadas.
  - Gatilhos disponíveis incluem app event, On Schedule, Webhook, formulário, manual e chamada por outro workflow — o módulo usa manual, webhook e agendado.
  - Dá para testar um bloco isolado ou o workflow completo.
  - n8n é pago; a alternativa gratuita é self-hosting, mas a própria documentação alerta que é para usuários experientes (risco de perda de dados, problemas de segurança e queda do servidor).
- **Link:** https://flix.nocodestartup.io/m/lessons/3479

### Desenvolvimento / 004 - Criando uma notificação simples via n8n  (00:04:09)
- **Resumo:** Cria a credencial Google Service Account API no n8n com os dados do JSON e envia o primeiro push. O workflow tem só dois blocos: gatilho manual e HTTP Request fazendo POST para a API do FCM com body em JSON. Testa ao vivo com o celular espelhado e a notificação chega com título, corpo e imagem.
- **Pontos-chave:**
  - Credentials > Add Credential > **Google Service Account API**; preencher Service Account Email (`client_email`) e Private Key (a chave inteira, do começo ao fim).
  - Habilitar o escopo (scope) do Firebase Messaging; o n8n testa a conexão na hora.
  - HTTP Request: método POST, endpoint do FCM (`googleapis`) com `messages:send`, autenticando pela credencial criada.
  - Habilitar "Send Body" / JSON Body e escrever o corpo à mão.
  - Estrutura do JSON usada: `topic` (o "geral" da custom action) + `notification` com título, corpo e imagem (URL).
  - Dois blocos e uma credencial já bastam para o envio simples.
- **Link:** https://flix.nocodestartup.io/m/lessons/3481

### Desenvolvimento / 005 - Criando notificações agendadas  (00:01:15)
- **Resumo:** Variação mínima do fluxo anterior: troca o gatilho manual pelo Schedule Trigger e mantém o mesmo HTTP Request. Configura a recorrência e ativa o workflow, esperando ao vivo a notificação chegar no minuto seguinte.
- **Pontos-chave:**
  - O bloco HTTP Request é idêntico ao da notificação simples — só o trigger muda.
  - Schedule Trigger aceita intervalo em segundos, minutos, horas, dias, semanas e seleção de dias da semana.
  - No exemplo, envio a cada 1 minuto; é preciso ativar (habilitar) o fluxo para o agendamento rodar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3482

### Desenvolvimento / 006 - Criando notificações segmentadas por tipo de usuário  (00:04:21)
- **Resumo:** Insere um nó Supabase antes do HTTP Request para buscar apenas os usuários que interessam. Cria a credencial Supabase no n8n, configura Get Many na tabela `users` com filtro por tipo de usuário e usa o `fcm_token` retornado de forma dinâmica no body. Aqui o JSON deixa de usar `topic` e passa a usar `token`. Explica que o n8n já itera item a item sem precisar de bloco de loop.
- **Pontos-chave:**
  - Credencial Supabase no n8n: Host (URL do projeto) + **Service Role Secret**, ambos em Configurações do projeto > API.
  - Nó Supabase: operação Get Many na tabela `users` com filtro (ex.: tipo = "gratuito").
  - Testar o bloco anterior primeiro para que o n8n reconheça o formato do JSON de saída e você consiga arrastar a variável.
  - No body do HTTP Request, trocar `topic` por `token` e injetar o `fcm_token` dinâmico (variável aparece destacada em verde).
  - **Não precisa de nó de loop:** o n8n executa o bloco seguinte uma vez por linha retornada automaticamente.
  - Filtro sem correspondência retorna vazio e nada é enviado — jeito rápido de validar a segmentação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3483

### Desenvolvimento / 007 - Criando notificações via webhooks do Supabase  (00:02:51)
- **Resumo:** Último exemplo: notificação reativa a mudanças no banco. Usa o trigger Webhook do n8n, que expõe uma URL, e cria no Supabase um Database Webhook apontando para ela no evento de update da tabela `public.users`. Ao alterar o tipo do usuário de gratuito para pagante, o fluxo dispara e a notificação chega. Fecha alertando sobre a mudança de caminho das variáveis no payload.
- **Pontos-chave:**
  - Trigger Webhook do n8n com método POST; copiar a URL gerada e ligar direto no HTTP Request.
  - No Supabase: Database > Webhooks > Create Webhook; escolher tabela (`public.users`), evento (insert/update/delete — aqui update), tipo HTTP Request, método POST e colar a URL.
  - Usar "Test workflow" no n8n para ele ficar aguardando o evento.
  - **Atenção:** o payload do webhook traz `record` (dado novo) e `old_record` (dado anterior) — o caminho das variáveis no JSON muda em relação aos fluxos anteriores.
- **Link:** https://flix.nocodestartup.io/m/lessons/3484

### Finalização / 001 - Conclusão  (00:00:39)
- **Resumo:** Encerramento curto recapitulando o percurso: chaves do Google Cloud e uso do FCM, configuração de tabelas e webhooks no Supabase, e a montagem das quatro formas de envio no n8n. Convida a levar dúvidas para a comunidade.
- **Pontos-chave:**
  - Recapitula as quatro formas de envio construídas no módulo.
  - Escopo entregue: push em dispositivos Android.
- **Link:** https://flix.nocodestartup.io/m/lessons/3485

## Pegadinhas e insights

- **Credencial certa é conta de serviço.** OAuth e API key não servem aqui, porque quem fala com o Google Cloud é uma aplicação (n8n), não uma pessoa. O n8n já embute o fluxo de pedir o token ao Google Auth — você só cola `client_email` e `private_key`.
- **A chave privada é secreta.** O instrutor só a exibe porque vai excluí-la depois da gravação; nunca compartilhe o JSON.
- **Firebase sim, Firebase Auth não.** É obrigatório criar o projeto Firebase (gratuito) pelo FlutterFlow, mas a autenticação do app continua sendo a do Supabase.
- **Push vai para o dispositivo, não para o usuário.** O FCM não sabe quem são seus usuários. A ponte token↔usuário é a tabela no Supabase — é ela que viabiliza segmentar (pagante, gratuito, recém-criado etc.).
- **Tópicos do FCM foram deliberadamente descartados.** A custom action inscreve todos num tópico "geral" só para o exemplo simples; a arquitetura escolhida segmenta pelo banco, o que é bem mais assertivo.
- **Documentação do Firebase é fragmentada.** O código da custom action não existe pronto em uma página só; o instrutor juntou trechos com ajuda do ChatGPT — e alerta para revisar/remover opções irrelevantes que a IA sugere (ex.: CarPlay, que é da Apple).
- **A custom action precisa rodar no início do app.** Ela é registrada em Custom Files > Final Actions; sem isso o token nunca é solicitado.
- **Erro fantasma no editor.** Depois de salvar o código da custom action pode aparecer erro na tela — basta atualizar a página que o debug roda de novo e mostra tudo ok.
- **Sem bloco de loop.** O n8n itera automaticamente sobre cada linha retornada do Supabase; adicionar loop é desnecessário.
- **Payload do webhook muda os caminhos.** Com webhook o JSON traz `record` e `old_record`; se você reaproveitar o body dos fluxos anteriores sem ajustar o caminho da variável, quebra.
- **n8n é pago.** O instrutor defende o custo comparando com contratar dev ou manter servidor próprio; o self-hosting é gratuito, mas a documentação oficial o classifica como coisa de usuário experiente pelo risco de perda de dados, falha de segurança e queda do servidor.
- **Escopo limitado a Android.** iOS ficaria para um módulo dedicado.
