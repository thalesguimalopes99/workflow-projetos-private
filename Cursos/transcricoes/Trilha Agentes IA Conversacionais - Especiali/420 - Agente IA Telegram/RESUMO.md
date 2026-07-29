# Agente IA Telegram

Trilha Agentes IA Conversacionais | Especialistas · 3 aulas · ~17min (00:17:31) · intermediário

> Como plugar um agente de IA feito no n8n dentro do Telegram: criar o bot, receber e responder mensagens, e depois trocar o canal do "template mestre" para o Telegram.

## O que você sai sabendo fazer
- Criar um bot no Telegram via BotFather, pegar o token de API e cadastrar a credencial no n8n.
- Montar o fluxo mínimo: trigger do Telegram (mensagem recebida) → AI Agent → node de resposta.
- Endereçar a resposta corretamente usando o `chat ID` (e não o ID da mensagem).
- Ligar memória por conversa usando o ID do chat como chave de sessão.
- Adaptar o template mestre (usado antes com outro canal) para operar no Telegram, incluindo os ramos de texto, áudio, imagem e PDF.
- Remover a assinatura automática do n8n nas respostas enviadas.

## Stack e ferramentas
- n8n (nodes: Telegram Trigger, Telegram "Send a text message", AI Agent, memória, Set/variáveis de fluxo)
- Telegram + BotFather (comando `/newbot`, token de API)
- OpenAI (modelo do agente, visão para imagem, transcrição de áudio)
- Supabase (registro das conversas/usuários no template mestre)
- Banco de dados vetorial / RAG sobre PDF (opcional, já visto em aulas anteriores)
- Template mestre da trilha (fluxo pronto com buffer, roteamento por tipo de mídia e resposta fatiada)

## Pré-requisitos
As aulas são explicitamente uma continuação e assumem: fundamentos da formação, curso de n8n, a aula de primeira automação e — o mais importante — o módulo do **template mestre** da própria trilha. O instrutor avisa que quem pular direto para cá vai ficar perdido. Também é preciso ter conta e app do Telegram instalado (celular ou desktop).

## Aula a aula

### 1.1 - Setup Telegram  (00:03:20)
- **Resumo:** Abertura do módulo com o escopo das aulas: criar o agente, receber o gatilho de mensagem no Telegram e responder, para depois integrar isso ao template mestre. Em seguida mostra a configuração inicial no n8n — adicionar o nó Telegram como trigger "quando receber a mensagem" e criar a credencial. O caminho da credencial é o próprio passo a passo que o n8n exibe: conversar com o BotFather, criar o bot e colar a chave de API.
- **Pontos-chave:**
  - Fluxo do BotFather: `Start` → comando `/newbot` → informar nome → informar username → recebe a chave de API.
  - No n8n: `Create New Credential` no nó Telegram e colar o token.
  - Pré-requisito prático: Telegram instalado e conta criada.
  - O instrutor deixa claro que vai acelerar por assumir os módulos anteriores vistos.
- **Link:** https://flix.nocodestartup.io/m/lessons/4340

### 2.1 - Receber e Responder Mensagens Telegram  (00:06:05)
- **Resumo:** Aula prática construindo o fluxo mínimo ponta a ponta. Primeiro testa o trigger mandando um "oi" pelo bot e inspeciona o payload que chega (ID da mensagem, se é bot, nome do remetente, chat, texto). Depois adiciona um AI Agent com prompt vindo do campo de texto da mensagem e um modelo da OpenAI, e fecha com o nó Telegram de envio para devolver a resposta. Termina ligando memória e colocando o fluxo em produção.
- **Pontos-chave:**
  - No AI Agent, trocar a origem do prompt para `Define below` e apontar para o campo de texto da mensagem.
  - Node de resposta: ação `Send a text message` (o node Telegram tem várias outras operações).
  - **Erro corrigido ao vivo:** usar o *message ID* no campo de destino dá erro de "chat não encontrado" — o certo é o **chat ID**.
  - Texto enviado = `output` do AI Agent.
  - Desmarcar `Append n8n Attribution` nas opções para tirar a assinatura "enviado pelo n8n" da resposta.
  - Memória: também precisa de `Define below`, usando o ID do chat como chave de sessão.
  - Truque de teste: pinar (pin) a mensagem recebida para reexecutar o fluxo sem precisar mandar mensagem nova — e despinar antes de ativar.
- **Link:** https://flix.nocodestartup.io/m/lessons/4341

### 3.2 - Aplicando ao Template MESTRE  (00:08:06)
- **Resumo:** Tour pelo template mestre já adaptado ao Telegram, apontando exatamente o que muda em relação à versão original. A estrutura geral se mantém (gatilho, variáveis de fluxo, dados do lead, buffer de mensagens, registro no Supabase, agente, resposta fatiada); o que precisa de adaptação são os ramos de mídia, porque no Telegram é preciso pegar o file ID, baixar o arquivo e converter para binário antes de entregar à OpenAI. Depois roda testes reais enviando texto, áudio, imagem e PDF pelo bot e acompanha o caminho de cada um no fluxo.
- **Pontos-chave:**
  - Os dados do lead capturados do Telegram: ID da conversa, mensagem, quem enviou (ID e nome) e flag de bot; há um filtro específico para Telegram e nada além disso é necessário.
  - Ramo de **áudio**: baixar o arquivo pelo Telegram → transcrever → adicionar à lista de mensagens.
  - Ramo de **imagem**: pegar o arquivo → baixar → converter para binário → converter de novo para o formato que a OpenAI entende.
  - Ramo de **PDF**: baixar o documento, converter e extrair o texto para a lista de mensagens.
  - A parte de gestão de agentes fica desativada nesse exemplo; o RAG (banco vetorial com PDF de serviços) é opcional.
  - A resposta sai fatiada em partes, com pausa/buffer, simulando atendimento humano.
  - O template traz webhooks de exemplo para copiar e colar durante os testes.
- **Link:** https://flix.nocodestartup.io/m/lessons/4342

## Pegadinhas e insights
- **Chat ID ≠ message ID.** É o erro que trava a resposta ("não achou o chat"). O campo de destino do envio quer o ID do chat.
- **Campos que exigem `Define below`:** tanto o prompt do AI Agent quanto a chave de sessão da memória precisam ser trocados do modo automático para o manual, apontando para o campo certo do Telegram.
- **Assinatura do n8n:** por padrão o bot manda "esta mensagem foi enviada pelo n8n"; desligue em `Append n8n Attribution`.
- **Sem memória o bot não mantém contexto.** No teste inicial, o agente responde solto; a memória por chat ID é o que dá continuidade à conversa.
- **Pin de mensagem atrapalha em produção.** Ótimo para testar, mas precisa ser removido antes de ativar o fluxo, senão o dado fica congelado.
- **Diferença arquitetural do Telegram para outros canais:** o Telegram entrega um identificador de arquivo, não o arquivo; por isso todo ramo de mídia ganha etapas extras de download e conversão binária.
- **Comportamento esperado do agente:** ao receber uma imagem fora do contexto (foto de cachorro), o agente registra o que viu mas não responde — o instrutor explica que isso é intencional, porque o prompt define um atendente que não deve responder assuntos alheios ao serviço.
- **Sobre a pasta:** o módulo 3 começa direto na aula 3.2 nesta transcrição; não há arquivo de uma aula 3.1.
- Os valores citados nos testes (12.500 à vista, 6x totalizando 13.500) são conteúdo do PDF de exemplo do agente, não preço do curso.
