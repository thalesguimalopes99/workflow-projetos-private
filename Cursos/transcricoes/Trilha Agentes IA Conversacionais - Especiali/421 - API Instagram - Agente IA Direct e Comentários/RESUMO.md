# API Instagram - Agente IA Direct e Comentários

Trilha Agentes IA Conversacionais | Especialistas · 10 aulas · ~46 min (0,76h) · nível intermediário

> Como plugar um agente de IA feito no n8n na API oficial do Instagram, para receber e responder Directs (e comentários) automaticamente.

## O que você sai sabendo fazer

- Criar um app no Facebook Developers, colocá-lo em modo "Ao vivo" e gerar o token de acesso do Instagram sem cair nos erros de permissão.
- Configurar o webhook do Instagram apontando para o n8n, respondendo o desafio de verificação (`hub.challenge`) para validar a integração.
- Receber eventos de mensagem do Direct no n8n, tratar o payload (account ID, sender ID, recipient ID, message ID, texto) e filtrar as mensagens do próprio bot.
- Responder no Direct via HTTP Request para `graph.instagram.com`, autenticando por header `Authorization: Bearer <token>`.
- Migrar o fluxo de teste para produção (URL de produção do webhook + workflow ativo) e replicar o mesmo padrão para responder comentários trocando a URL do endpoint.
- Plugar tudo no template mestre do Instagram, que já trata texto, áudio e imagem, faz buffer de mensagens, humaniza a resposta e salva o lead.

## Stack e ferramentas

- **n8n** (nós: Webhook, Respond to Webhook, Set/Edit Fields, Filter, AI Agent, HTTP Request; credencial Header Auth via Generic Credential Type)
- **Facebook Developers / Meta for Developers** — criação do app, configuração da API do Instagram com login do Instagram, webhooks
- **API Graph do Instagram** — `graph.instagram.com`, versão v22.0 na gravação, endpoint `/{account-id}/messages`
- **OpenAI** — chat model do AI Agent, transcrição de áudio e leitura de imagem
- **Redis** — gestão de estado do fluxo (agente ativado/desativado, inatividade) no template mestre
- **Supabase** — tabela de leads (quem mandou Direct/comentário) no template mestre
- Duas contas de Instagram (uma com o agente, outra para testar)

## Pré-requisitos

As aulas assumem conteúdo anterior da trilha e vão direto ao ponto:

- Módulo de fundamentos essenciais da trilha.
- Fundamentos de n8n e "sua primeira automação com n8n + agente de IA".
- O **template mestre** (primeiro módulo da trilha) já entendido — o instrutor não reexplica os blocos base.
- Conta no Facebook Developers e conta OpenAI conectada.
- Duas contas do Instagram para conseguir testar o envio/recebimento.

## Aula a aula

### 1.1 - Introdução API e Agentes de Instagram  (00:01:36)
- **Resumo:** Abertura do módulo, apresentando o objetivo: conectar qualquer agente de IA a um gatilho e a uma resposta no Instagram. O instrutor mostra os dois entregáveis do curso — responder Directs e responder comentários — e reforça a lista de pré-requisitos.
- **Pontos-chave:**
  - Escopo: agente respondendo Direct + agente respondendo comentários em posts.
  - Pré-requisitos explícitos: fundamentos essenciais, fundamentos de n8n, primeira automação e o template mestre.
  - Aviso de ritmo: as aulas seguem rápidas porque partem do que já foi ensinado antes.
- **Link:** https://flix.nocodestartup.io/m/lessons/4344

### 2.1 - Gerando Token de Acesso  (00:04:05)
- **Resumo:** Passo a passo de criação do aplicativo no Facebook Developers e geração do token de acesso do Instagram. Antes de gerar o token é preciso preencher a URL de política de privacidade nas configurações básicas e virar o app para o modo "Ao vivo". Depois adiciona-se a conta do Instagram, autorizam-se as permissões e copia-se o token.
- **Pontos-chave:**
  - Criar app: nome, e-mail, caso de uso "Outro", tipo empresa; não é necessário vincular portfólio empresarial.
  - Configurações do app → Básico → URL da política de privacidade (e termos de uso) — sem isso o app não vai para "Ao vivo".
  - Painel → configurar Instagram → adicionar conta → "Gerar token de acesso" → marcar "estou ciente" → copiar.
  - Guarde o token em algum lugar seguro na hora: refazer o processo é o único caminho se perder.
- **Link:** https://flix.nocodestartup.io/m/lessons/4345

### 2.1 [Extra] Como Gerar Token Sem Erros  (00:06:20)
- **Resumo:** Aula de reforço gravada por outro instrutor, refazendo a criação do app com foco nos erros que a turma reportou. Mostra o erro de permissão que aparece quando se tenta gerar o token com o app ainda em modo desenvolvimento e o caminho para contas do Instagram que exigem autorização extra via usuário de teste.
- **Pontos-chave:**
  - Gerar token com o app em "Desenvolvimento" retorna erro de função de desenvolvedor insuficiente — mude para "Ao vivo" primeiro.
  - O bloqueio para ir "Ao vivo" é a URL de política de privacidade ausente em Configurações básicas.
  - Contas que não conseguem gerar token: Funções do app → Usuários de teste → adicionar usuário, e aceitar o convite na página de gerenciamento de acesso do Instagram.
  - O token aparece uma única vez na tela — copiar e salvar em bloco de notas antes de fechar.
- **Link:** https://flix.nocodestartup.io/m/lessons/4451

### 2.2 - Configuração Webhook  (00:03:51)
- **Resumo:** Montagem no n8n do par Webhook + Respond to Webhook que valida a integração com o Instagram. O Instagram envia um código de verificação (`hub.challenge`) para a URL de callback e espera receber esse mesmo código de volta; o fluxo devolve o valor como texto e a integração é confirmada.
- **Pontos-chave:**
  - Webhook de verificação usa método **GET**, respondendo pelo nó Respond to Webhook.
  - No painel da Meta: URL de callback (a URL de teste do webhook n8n) + token de verificação — sem autenticação no fluxo, pode ser um valor qualquer, ex.: `000`.
  - Rode "Test workflow" no n8n antes de clicar em "Verificar e salvar" para o webhook estar escutando.
  - É comum falhar duas ou três vezes; basta repetir o processo até carregar "Webhook configurado".
- **Link:** https://flix.nocodestartup.io/m/lessons/4346

### 2.3 - Recebendo Mensagens  (00:05:06)
- **Resumo:** Construção do webhook que recebe de fato as mensagens do Direct. Duplica-se o webhook de verificação, troca-se o método para POST e assina-se o campo de eventos correto no painel da Meta. Depois o payload é inspecionado e normalizado num nó Set, e um filtro impede que o agente reaja às próprias mensagens.
- **Pontos-chave:**
  - Webhook de mensagens: método **POST**, Respond to Webhook em modo imediato; o webhook de verificação fica desativado.
  - No painel, assinar o evento **messages** (a lista traz também comentários, comentários em live e reações) — sem isso nada chega.
  - Payload relevante no body: objeto `instagram`, timestamp, `sender` (quem enviou), `recipient` (quem recebe), ID e texto da mensagem.
  - Nó Set "tratar dados" salva: account ID, sender ID, recipient ID, message ID e o texto.
  - Fixar (pin) o retorno do webhook facilita montar o resto do fluxo sem ficar reenviando mensagens.
  - Filtro obrigatório para o agente não responder a si mesmo quando a própria resposta dispara o webhook.
- **Link:** https://flix.nocodestartup.io/m/lessons/4347

### 2.4 - Respondendo Mensagens  (00:05:45)
- **Resumo:** Fecha o ciclo ligando um AI Agent simples ao fluxo e devolvendo a resposta pelo HTTP Request da API do Instagram. Mostra como montar a URL do endpoint, cadastrar a credencial de header com o token e montar o corpo da requisição. O instrutor erra o nome do header ao vivo e corrige na hora.
- **Pontos-chave:**
  - AI Agent de teste: System Message simples ("atendente feliz e simpático"), chat model OpenAI, sem memória nesse estágio.
  - HTTP Request **POST** para `graph.instagram.com/<versão>/<account_id>/messages` (v22.0 na gravação).
  - Autenticação: Generic Credential Type → Header Auth, nome do header **Authorization**, valor `Bearer <token>`.
  - Body: `recipient.id` = **sender ID** de quem escreveu (não o recipient), `message.text` = output do agente.
  - Erro demonstrado: usar outro nome de header faz a chamada falhar com token "inválido".
- **Link:** https://flix.nocodestartup.io/m/lessons/4348

### 2.4 [Extra] Dicas para Integrar Instagram e Correção erros  (00:06:11)
- **Resumo:** Aula de correção baseada nos erros mais frequentes dos alunos ao copiar as expressões do HTTP Request. Percorre referência a nó, caminho do JSON, plural do endpoint e a escolha do ID correto no `recipient.id`, e depois esclarece qual URL vai em cada campo do painel da Meta.
- **Pontos-chave:**
  - Expressões quebram porque o nome do nó Set do aluno é diferente do nome usado pelo instrutor — ajuste a referência ao seu próprio nó.
  - Caminho correto vai até o item/JSON e depois o objeto salvo no Set (ex.: `account` → `id`); maiúsculas/minúsculas importam.
  - O endpoint é `/messages` no plural; escrito errado, a chamada falha.
  - Em `recipient.id` vai o **sender ID** (quem te mandou a mensagem), não o campo chamado recipient — erro muito comum.
  - URL de callback do webhook = URL do webhook do n8n. A URL de política de privacidade é outro campo (Configurações básicas); para teste vale até a URL do editor n8n, em produção use uma URL válida (site do cliente ou uma página só com a política, ex. no WordPress).
- **Link:** https://flix.nocodestartup.io/m/lessons/4453

### 2.5 - Colocando Agente em Produção  (00:02:36)
- **Resumo:** Transição do fluxo de teste para produção. Troca-se a URL de callback no painel da Meta pela URL de produção do webhook e ativa-se o workflow no n8n. Durante o teste o instrutor descobre que o filtro estava com os campos errados e corrige ao vivo.
- **Pontos-chave:**
  - Desative o webhook de verificação e ative os nós do fluxo de mensagens antes de publicar.
  - A URL de produção só funciona com o workflow **ativo** no n8n; então volte ao painel, verifique e salve.
  - Correção do filtro: a comparação certa é **account ID diferente de sender ID** (não sender vs. recipient), senão o agente responde a si mesmo.
  - Aviso: com o fluxo ativo, todo Direct recebido é respondido — desative quando não quiser isso.
  - Para comentários, repete-se o mesmo processo mudando o endpoint conforme a documentação do Instagram.
- **Link:** https://flix.nocodestartup.io/m/lessons/4349

### 3.2 - Template Mestre Instagram  (00:05:33)
- **Resumo:** Importação do template mestre já pronto para Instagram e bateria de testes reais pelo celular. O instrutor conecta as dependências (Redis, Supabase, OpenAI), roda o fluxo em modo teste e valida os três tipos de entrada: texto, imagem e áudio.
- **Pontos-chave:**
  - O template vem com o webhook e exemplos de payload prontos (texto, áudio, imagem) para colar no nó e testar sem enviar mensagem real.
  - É preciso conectar Redis e Supabase; a tabela do Supabase guarda quem está conversando (captura de lead).
  - O fluxo humaniza a resposta quebrando-a em várias mensagens enviadas em sequência.
  - Imagem: a OpenAI descreve a foto enviada no Direct. Áudio: é baixado, convertido e transcrito antes de chegar ao agente.
  - Tempo do buffer (espera por mensagens seguintes do usuário) é configurável no fluxo.
- **Link:** https://flix.nocodestartup.io/m/lessons/4350

### 3.3 - Template Mestre - Explicando o Template  (00:04:45)
- **Resumo:** Passeio bloco a bloco pelo template mestre, explicando onde mexer quando algo quebra ou muda. Cobre os parâmetros de fluxo, o filtro anti-loop, a checagem de estado no Redis, o roteamento por tipo de mídia, o buffer, a gravação do lead, o prompt do agente e o HTTP Request final.
- **Pontos-chave:**
  - Parâmetros de fluxo (marcados em vermelho) a atualizar: ID do agente, tempo de buffer, tempo de inatividade e temperatura do modelo.
  - Gestão de fluxo via Redis: checa se o agente está ativado/desativado (ex.: usuário pediu atendimento humano) e interrompe.
  - Roteamento por tipo: texto vai direto ao buffer; áudio passa por download + conversão + transcrição OpenAI; imagem é lida pela OpenAI a partir da URL; o ramo de PDF vem desativado porque o Instagram não envia PDF.
  - Buffer de mensagens agrega o que chegou antes de acionar o agente; depois o Supabase registra o lead.
  - Prompt: altere apenas a parte indicada, mantendo a estrutura do prompt mestre.
  - No HTTP Request final, Direct já vem configurado; para responder comentário é preciso trocar a URL do endpoint.
- **Link:** https://flix.nocodestartup.io/m/lessons/4351

## Pegadinhas e insights

- **Token só é gerado com o app "Ao vivo".** Em modo desenvolvimento a Meta retorna erro de função de desenvolvedor insuficiente. O que destrava o modo ao vivo é a URL de política de privacidade em Configurações básicas.
- **O token aparece uma única vez.** Copie e salve imediatamente; do contrário é preciso refazer o processo inteiro.
- **Contas que travam na autorização** precisam ser adicionadas como usuário de teste (Funções do app → Usuários de teste) e aceitar o convite na página de gerenciamento de acesso do Instagram.
- **Dois webhooks, dois métodos.** Verificação usa GET e devolve o `hub.challenge`; recebimento de mensagem usa POST. Manter os dois ativos ao mesmo tempo atrapalha.
- **Verificar o webhook costuma falhar duas ou três vezes** — o instrutor trata isso como normal e apenas repete o processo com o workflow escutando.
- **Assinar o evento errado (ou nenhum)** é a causa de "nada chega". Para Direct, o campo é `messages`; a lista também traz comentários, comentários em live e reações.
- **Filtro anti-loop é obrigatório** e a versão correta é account ID ≠ sender ID. A versão inicial (sender ≠ recipient) foi corrigida na aula de produção.
- **Header de autenticação é `Authorization`** com valor `Bearer <token>`. Nome errado = falha silenciosa que parece problema de token.
- **No body, `recipient.id` recebe o sender ID** de quem escreveu — o erro mais comum da turma é usar o campo homônimo do payload.
- **Endpoint no plural (`/messages`)** e versão da API explícita na URL (v22.0 à época) — confira a versão vigente no painel.
- **Expressões do template quebram se você renomear os nós.** Ajuste as referências ao nome do seu próprio nó Set e respeite maiúsculas/minúsculas no caminho do JSON.
- **Em produção a URL de callback precisa ser a de produção e o workflow ativo no n8n** — a Meta só valida se o fluxo estiver ligado.
- **Cuidado ao ativar:** com o fluxo em produção, todo Direct recebido passa a ser respondido pelo agente.
- **Política de privacidade improvisada só serve para estudo.** Para produção, use a URL real do cliente ou publique uma página com a política.
- **Decisão de arquitetura do template:** Redis para estado/handoff humano, Supabase como base de leads, buffer para agrupar mensagens picadas e quebra da resposta em partes para parecer humano.
- **Comentários reaproveitam 100% do fluxo de Direct**, mudando apenas o evento assinado e a URL do endpoint de resposta.
