# M1 - Fundamentos Dify

Trilha Dify | 12 aulas | ~1h14min | nível iniciante (com pré-requisitos)

> Ensina os fundamentos do Dify e leva você a colocar no ar um agente de atendimento real, conectado ao WhatsApp via n8n + Z-API, com os dados dos usuários e das conversas guardados no Supabase.

## O que você sai sabendo fazer

- Criar uma conta no Dify, conectar um provedor de LLM próprio (chave da OpenAI) e entender a diferença entre chatbot, chatflow, agente, gerador de texto e fluxo de trabalho.
- Montar um chatbot no Dify com prompt estruturado (hierarquia por `#`/`##`), variáveis dinâmicas, escolha de modelo e ajuste de parâmetros (temperatura, top P, penalidades, limite de tokens, saída em JSON).
- Ligar/desligar os recursos do chat (visão, citações e atribuições, abertura de conversa, perguntas de acompanhamento, texto-para-voz, fala-para-texto) e saber para que serve cada um.
- Pegar a chave e a URL da API do app no Dify e consumir o endpoint `chat-messages` a partir de um sistema externo.
- Modelar uma tabela no Supabase para guardar nome, celular, `conversation_id` e `user_id` do Dify, e liberar acesso via política RLS.
- Montar o fluxo n8n ponta a ponta: webhook da Z-API → filtro de grupo/mensagem própria → busca do usuário no Supabase → cria conversa no Dify + cria usuário → responde no WhatsApp por HTTP.

## Stack e ferramentas

- **Dify** (plano gratuito) — chatbot, prompt, variáveis, recursos do chat, logs, dashboard, chave de API.
- **OpenAI** — provedor de LLM conectado ao Dify (GPT-4o mini como padrão de custo-benefício; GPT-4o citado como o mais forte na gravação). Exige créditos na conta (o instrutor sugere US$ 5).
- **n8n** — orquestração das integrações (instância hospedada na Railway no vídeo). Nós usados: Webhook, IF/condição, Set (informações manuais), Supabase (get row / create row), HTTP Request.
- **Z-API** — API não oficial de WhatsApp: instância, token, token de segurança da conta, webhook "ao receber mensagem", endpoint de envio de texto simples.
- **Supabase** — banco Postgres, editor de tabelas, políticas RLS, URL + chave de API para conectar no n8n.
- Materiais de apoio do curso com prompts prontos e o fluxo n8n em JSON para importar.

## Pré-requisitos

O instrutor assume conteúdo anterior da formação e não revisa:
- Fundamentos de automações e de agentes de IA.
- Fundamentos de desenvolvimento de apps: o que é API e o que é JSON.
- Fundamentos de n8n (os fluxos são importados prontos, não construídos do zero).
- Conta com créditos na OpenAI e conta na Z-API (teste grátis de 2 dias) + um número de WhatsApp para testar.

## Aula a aula

### 1 - Boas Vindas Formação Dify (00:03:43)
- **Resumo:** Abertura com Matheus Castelo, um dos fundadores da NoCode Startup. Ele apresenta o escopo da formação (do zero ao avançado em agentes com Dify, sempre amarrado em cases práticos) e lista os pré-requisitos que não serão revisados. Fecha com o método de estudo recomendado e onde ficam os materiais de apoio.
- **Pontos-chave:**
  - Pré-requisitos explícitos: automações, agentes de IA, API/JSON e n8n.
  - n8n aqui é ferramenta auxiliar — os fluxos vêm prontos, o foco é o Dify.
  - Método sugerido: fundamentos → praticar junto → pegar um projeto real do seu círculo → voltar às aulas só nas dúvidas pontuais.
  - Materiais linkados abaixo da aula trazem prompts e fluxos para copiar/colar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3783

### 2 - O Poder do Dify (00:07:35)
- **Resumo:** Revisão teórica rápida dos conceitos que serão usados o tempo todo: RAG, function calling e a anatomia de um agente. Depois compara o Dify com os assistants da OpenAI e mostra por que a flexibilidade de multi-LLM e o open source pesam a favor. Termina detalhando o que cabe no plano gratuito.
- **Pontos-chave:**
  - Anatomia de um agente: modelo + prompt base + memória + RAG + tools.
  - RAG = treinar com conhecimento externo (PDF, site, planilha); tools = acionar serviços externos (Google, e-mail, WhatsApp, banco de dados).
  - Vantagem sobre o assistants da OpenAI: no Dify você pluga OpenAI, Claude ou Gemini; é open source e dá para self-hostar.
  - Ferramentas nativas citadas: busca no Google, geração de imagem com DALL·E, gráficos, web scraper, YouTube, Wikipedia.
  - Plano gratuito no momento da gravação: 1 membro, 10 apps, 5 MB de base vetorial, upload de 50 documentos — suficiente para todo o módulo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3784

### 3 - Conhecendo o Dify por Dentro (00:07:14)
- **Resumo:** Primeiro tour pela plataforma: criação de conta, painel do Estúdio e os tipos de app disponíveis. Explica a diferença conceitual entre chatbot básico, chatflow, agente e fluxo de trabalho, passa por Conhecimento, Ferramentas e Explorar (templates). Fecha conectando a chave da OpenAI como fornecedor de modelo.
- **Pontos-chave:**
  - Tipos de app: chatbot (básico ou chatflow), gerador de texto, agente e fluxo de trabalho. Agente é o que ativa funções; o módulo foca no chatbot básico.
  - Em "Conhecimento" você sobe planilha, PDF, texto ou site para treinar o bot.
  - Em "Ferramentas" há integrações nativas (algumas exigem autorizar a conta, como o DALL·E) e a opção de criar ferramenta personalizada.
  - Configurações → Fornecedor de modelo: cole a chave da OpenAI (organização opcional, API base dispensável).
  - Os créditos nativos do Dify acabam rápido — conectar seu próprio provedor é o caminho. Exige créditos na OpenAI (~US$ 5 para começar).
- **Link:** https://flix.nocodestartup.io/m/lessons/3786

### 4 - Funcionalidades Chat - Prompt, Variáveis e LLM (00:07:21)
- **Resumo:** Cria um chatbot do zero e percorre a coluna de configuração: prompt (com gerador automático), seleção de modelo, parâmetros e variáveis. Testa tudo no painel de preview lateral e mostra que o app publicado já vem com interface pronta e link compartilhável.
- **Pontos-chave:**
  - GPT-4o mini como padrão de custo-benefício; parâmetros vêm em presets criativo / equilibrado / preciso (o instrutor prefere "preciso").
  - Parâmetros explicados: temperatura, top P, penalidade de presença e de frequência, limite de tokens e formato de resposta em JSON.
  - Variáveis são referenciadas no prompt entre chaves e viram campos que o usuário preenche antes de iniciar a conversa (exemplo: cidade → plano de viagem).
  - Publicar dá: executar em outra aba, incorporar no site (inclusive como bolinha no canto) e ver a referência da API.
  - Aviso: a ferramenta é nova e a interface muda com frequência — a essência permanece.
- **Link:** https://flix.nocodestartup.io/m/lessons/3785

### 5 - Funcionalidades Chat - Recursos, API e Dashboard (00:06:52)
- **Resumo:** Percorre um a um os recursos opcionais do chat, testando ao vivo (o texto-para-voz trava um pouco antes de funcionar em português). Depois abre a área de API, os registros de conversa e o dashboard de uso.
- **Pontos-chave:**
  - Recursos: visão (ler imagens), citações e atribuições (mostra qual conhecimento/tool foi usado), abertura de conversa, perguntas de acompanhamento, texto-para-voz e fala-para-texto.
  - Moderação de conteúdo e cache de respostas existem, mas o instrutor não os considera úteis no dia a dia.
  - A tela de API documenta o POST de mensagem: URL, headers e body (query, tipo, ID) — é o que será copiado para o n8n.
  - Registros guardam o histórico completo das conversas; o dashboard mostra tokens consumidos e custo (US$ 0,04 nos testes da aula).
  - A chave de API do app é criada nessa mesma área e será usada na integração.
- **Link:** https://flix.nocodestartup.io/m/lessons/3787

### 6 - Planjeamento do Projeto + Setup N8N e Supabase (00:05:08)
- **Resumo:** Define a arquitetura do case: um bot de atendimento da NoCode Startup usando o próprio WhatsApp como front-end. Justifica cada peça da stack e cria o projeto no Supabase, além de conferir as credenciais já configuradas no n8n.
- **Pontos-chave:**
  - Arquitetura: WhatsApp (interface) → Z-API (conexão) → n8n (automação) → Dify (agente, com GPT) → Supabase (backend).
  - Usar o WhatsApp evita construir front-end; alternativas citadas: Instagram, FlutterFlow, Bubble.
  - Planilha funcionaria como banco, mas não é a opção profissional/segura — daí o Supabase.
  - Ao criar o projeto Supabase: definir senha e escolher a região Brasil (menor latência).
  - Credenciais necessárias no n8n: OpenAI e Supabase (URL + chave copiadas em Configurações → APIs). n8n do vídeo roda hospedado na Railway.
- **Link:** https://flix.nocodestartup.io/m/lessons/3788

### 7 - Criar Bot dify + Tabela Supabase (00:06:05)
- **Resumo:** Cola no Dify um prompt de atendimento pronto e explica por que ele é escrito em markdown hierárquico. Em seguida modela no Supabase a tabela que vai amarrar cada contato do WhatsApp à sua conversa no Dify.
- **Pontos-chave:**
  - Estrutura do prompt: quem é você, o que é a empresa, ecossistema (formações, comunidade), estilo de escrita, o que pode responder, não revelar que é IA.
  - Usar `#` para título maior e `##` para subtítulo faz o modelo entender a hierarquia da informação — técnica recomendada pelo instrutor.
  - Ao colar o prompt no Dify, use "colar com o mesmo estilo" para preservar a formatação.
  - Tabela `usuarios` no Supabase com colunas de tipo texto: nome, celular, conversa_dify_id e user_dify_id. Deixar RLS ligado.
  - Divisão de responsabilidade: o Dify guarda a conversa em si; o Supabase guarda apenas os IDs para reencontrá-la.
- **Link:** https://flix.nocodestartup.io/m/lessons/3789

### 8 - Overview Fluxo N8N (00:04:50)
- **Resumo:** Baixa o fluxo pronto dos materiais do curso, importa no n8n e explica a lógica completa antes de preencher os nós. Apresenta também a Z-API como a API de WhatsApp escolhida.
- **Pontos-chave:**
  - Importar fluxo: baixar o JSON nos materiais (três pontinhos → download) → n8n → adicionar workflow → três pontinhos → importar arquivo.
  - Lógica do fluxo: webhook recebe a mensagem → filtra grupo e mensagem do próprio bot → extrai nome/celular/mensagem → busca usuário no Supabase → se não existe, cria conversa no Dify e usuário no Supabase → se existe, chama o agente → responde via Z-API.
  - A condição de "não é grupo" e "não é mensagem de mim para mim" evita o bot responder a si mesmo em loop.
  - Z-API é API não oficial de WhatsApp, com 2 dias de teste grátis; existem alternativas no mercado.
  - Recomendação: já criar a conta na Z-API e ter um número disponível para os testes.
- **Link:** https://flix.nocodestartup.io/m/lessons/3790

### 9 - Conexão N8N, Z-API, Dify e Supabase 1 (00:06:26)
- **Resumo:** Primeira metade da montagem prática. Conecta o webhook do n8n à instância da Z-API, dispara uma mensagem real do celular e inspeciona o payload recebido. Com os dados em mãos, preenche o nó de condição, o nó de extração de campos e a busca no Supabase.
- **Pontos-chave:**
  - Na Z-API: instância → três pontinhos → editar → Webhooks → colar a URL de teste do n8n na ação "ao receber mensagem".
  - O payload traz chatName, phone, isGroup, fromMe, instanceId, texto da mensagem e até a foto do contato.
  - "Pinar" o dado no n8n permite continuar montando os nós seguintes sem reenviar mensagem a cada teste.
  - Condição: seguir apenas quando isGroup = false E fromMe = false.
  - Nó Supabase com operação GET na tabela `usuarios`, filtrando por celular igual ao do remetente; retorno vazio significa usuário novo e manda o fluxo para o ramo de criação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3792

### 10 - Conexão N8N, Z-API, Dify e Supabase 2 (00:06:50)
- **Resumo:** Constrói a chamada HTTP para o Dify no ramo de usuário novo e grava o registro no Supabase. No caminho aparece um erro de permissão que é resolvido criando uma política de RLS.
- **Pontos-chave:**
  - Atalho valioso: copiar o cURL da documentação da API do Dify e usar "importar URL" no nó HTTP do n8n — a estrutura vem montada.
  - Endpoint `chat-messages` (POST), header de autorização com a chave de API do app + content-type JSON.
  - Body: inputs vazio, `query` = mensagem do usuário, `response_mode` = blocking, `user` = celular do contato; `conversation_id` fica vazio na primeira interação.
  - A resposta do Dify devolve `conversation_id` e `user_id`, que são gravados no Supabase junto com nome e celular.
  - Erro de inserção no Supabase = falta de política RLS. Solução da aula: criar política liberando select/insert/update com condição `true`.
  - Salvar o workflow com frequência — o instrutor reforça isso.
- **Link:** https://flix.nocodestartup.io/m/lessons/3791

### 11 - Conexão N8N, Z-API, Dify e Supabase 3 (00:07:05)
- **Resumo:** Fecha o circuito montando a resposta de volta no WhatsApp pela Z-API e replicando a configuração no ramo do usuário já existente. Ao final troca a URL de teste do webhook pela de produção e ativa o fluxo.
- **Pontos-chave:**
  - Envio de texto na Z-API exige três coisas: ID da instância e token na URL, e o token de segurança da conta no header.
  - O token de segurança fica em uma área separada do painel e some depois de gerado — copie na hora.
  - Body do envio: `phone` (celular do contato) e `message` (o campo `answer` retornado pelo Dify). Opcionais úteis: delay da mensagem e delay de digitação, que deixam a resposta mais natural.
  - No ramo do usuário existente, a chamada ao Dify é a mesma, mudando a autorização e passando o `conversation_id` já salvo.
  - Antes de ir para produção: substituir a URL de teste pela de produção no webhook da Z-API e ativar o workflow no n8n.
- **Link:** https://flix.nocodestartup.io/m/lessons/3794

### 12 - Testes Finais e Aprendizados do Módulo (00:05:08)
- **Resumo:** Testa nó a nó o ramo do usuário já cadastrado, depois conversa com o bot direto do WhatsApp e confere as execuções no n8n. Encerra recapitulando o que foi aprendido e adiantando o próximo módulo.
- **Pontos-chave:**
  - Teste isolado com "test step" + pin de dados valida cada nó antes do teste ponta a ponta.
  - Conversa real no WhatsApp confirma que o agente responde segundo o prompt (identidade e descrição da empresa).
  - A aba "Execuções" do n8n mostra o caminho que cada mensagem percorreu — é o lugar para depurar erros.
  - Lembrete: despinar os dados antes de salvar o fluxo final.
  - Esse padrão de conexão com WhatsApp será reutilizado sem ser reexplicado; os próximos módulos focam na interface do Dify e em treinar o bot com PDFs, planilhas e sites.
- **Link:** https://flix.nocodestartup.io/m/lessons/3793

## Pegadinhas e insights

- **Créditos nativos do Dify acabam rápido.** Conectar seu próprio provedor (OpenAI) em Configurações → Fornecedor de modelo é obrigatório na prática; sem créditos na OpenAI o salvamento da chave falha.
- **RLS bloqueia a escrita silenciosamente.** O nó Supabase de criar linha falha até existir uma política de segurança. A aula libera tudo com condição `true` para destravar o aprendizado — não é a configuração para produção.
- **Sem as condições isGroup = false e fromMe = false o bot entra em loop** respondendo às próprias mensagens ou atuando dentro de grupos.
- **O token de segurança da conta na Z-API é diferente do token da instância** e desaparece da tela depois de gerado.
- **Divisão de dados:** o histórico da conversa vive no Dify; o Supabase guarda só nome, celular, `conversation_id` e `user_id`. Sem esse registro não há como recuperar a conversa de um contato que volta.
- **Webhook de teste ≠ webhook de produção.** Ficar com a URL de teste faz o fluxo parar de responder quando você sai do modo de escuta.
- **Escrever o prompt em markdown hierárquico** (`#` / `##`) é a técnica recomendada para o modelo entender a estrutura da informação — e o prompt é apontado como a parte mais trabalhosa e mais importante do agente.
- **Custos observados:** plano gratuito do Dify (1 membro, 10 apps, 5 MB vetorial, 50 documentos), ~US$ 5 de crédito na OpenAI, US$ 0,04 gastos nos testes da aula, Z-API com 2 dias grátis, Supabase no plano free.
- **A interface do Dify muda com frequência** — o instrutor avisa que telas podem estar diferentes, mas a lógica permanece.
- **Autocrítica do instrutor:** o nó "informações manuais" (Set) é opcional, existe só para deixar o fluxo mais legível; os campos poderiam ser puxados direto do webhook.
