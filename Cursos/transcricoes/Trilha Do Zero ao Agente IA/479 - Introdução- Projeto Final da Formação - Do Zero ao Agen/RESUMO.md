# Introdução: Projeto Final da Formação | Do Zero ao Agente de IA

Trilha Do Zero ao Agente IA | 3 aulas | ~15min (00:15:18) | nível intermediário

> Aula de abertura do projeto final da formação: apresenta o escopo, a arquitetura e os workflows de um agente comercial de IA construído no n8n com Supabase, Asaas e Trello — antes de qualquer construção prática.

## O que você sai sabendo fazer

- Enxergar a arquitetura completa de um agente comercial (front-end WhatsApp → orquestração n8n → banco Supabase → APIs Trello/Asaas) e saber onde cada ferramenta entra.
- Mapear a jornada do lead em macro-etapas: entrada, registro, CRM, qualificação/proposta, cobrança, follow-up, reconhecimento de pagamento e fallback humano.
- Identificar quais workflows do n8n precisam existir e por que eles são separados em vez de um só fluxo gigante.
- Definir a modelagem mínima do banco: tabelas de leads, produtos e pedidos, e os campos que sustentam o follow-up.
- Checar se você tem os pré-requisitos da formação antes de entrar na parte prática do case.

## Stack e ferramentas

- **n8n** — orquestrador central de todos os fluxos e agentes.
- **Supabase** — banco de dados (tabelas de leads, produtos e pedidos).
- **Asaas** — criação de clientes, geração de cobranças e link de pagamento.
- **Trello** — CRM visual em colunas (funil de vendas por cartão).
- **OpenAI / ChatGPT** — modelo de linguagem dos agentes dentro do n8n.
- **WhatsApp** — canal de conversa do agente (via "template mestre" da formação).
- **Chat Trigger (n8n)** — interface provisória de teste antes de plugar o WhatsApp.
- **Webhook do Asaas** — confirmação de pagamento.
- **Miro** — mapa mental usado pelo instrutor para destrinchar a jornada do lead.

## Pré-requisitos

O instrutor lista módulos anteriores da formação que devem estar vistos antes deste case:

- Fundamentos de automações, fundamentos de agentes de IA e engenharia de prompt.
- Módulo "8020" e agente de IA no WhatsApp.
- Dominando tools, APIs e MCP Agents.
- Conversando com PDFs, planilhas e arquivos.
- Template mestre para agentes (conexão com WhatsApp).
- Módulo de gerenciamento de pagamentos (Asaas).

## Aula a aula

### 1.1 - O que Você Vai Aprender na Trilha  (00:06:39)
- **Resumo:** Abertura da fase. O instrutor define o entregável: um agente comercial construído do zero que conversa com o lead, registra dados, gera cobrança e cobra de volta sozinho. Explica que este módulo é a costura de tudo que já foi ensinado na formação e lista os pré-requisitos e as ferramentas do case. Fecha com o resultado esperado: um case funcional para portfólio, entrevista ou proposta comercial.
- **Pontos-chave:**
  - Sete blocos do projeto: entrada do lead, registro no Supabase, organização no CRM, qualificação e proposta, cobrança, follow-up automático + reconhecimento de pagamento, e fallback humano.
  - O n8n é o maestro; o Supabase é onde tudo fica registrado; Asaas e Trello são apoio.
  - A fase termina em um desafio prático — o conteúdo é a preparação para ele.
  - Habilidades declaradas: estruturar base no Supabase, automatizar cobrança no Asaas, usar Trello como funil e orquestrar tudo no n8n.
- **Link:** https://flix.nocodestartup.io/m/lessons/4955

### 1.2 - Arquitetura do Projeto  (00:02:59)
- **Resumo:** Aula curta que abre o diagrama de arquitetura em três camadas: front-end/interface, back-end e integrações via API. Mostra que a conversa começa pelo Chat Trigger do n8n e só depois migra para o WhatsApp via template mestre. Detalha o papel de cada peça, incluindo as colunas do quadro do Trello e o que o Asaas assume na parte financeira.
- **Pontos-chave:**
  - Front-end: WhatsApp (destino final); Chat Trigger do n8n serve de front provisório durante a construção.
  - Supabase guarda leads, produtos e pedidos — é de lá que o agente tira contexto para conversar.
  - Modelo de linguagem: OpenAI (ChatGPT), rodando dentro dos nós de agente do n8n.
  - Colunas do funil no Trello: novo lead, aguardando pagamento, pago, perdido — cada lead vira um cartão.
  - Asaas elimina boleto manual e planilha: cria o cliente e gera a cobrança automaticamente.
- **Link:** https://flix.nocodestartup.io/m/lessons/4956

### 1.3 - Apresentando os Fluxos  (00:05:40)
- **Resumo:** O instrutor abre um mapa mental no Miro e dá zoom em cada macro-etapa da jornada do lead, quebrando-a em micro-etapas concretas. Em seguida mostra, dentro do n8n, os workflows já prontos que serão reconstruídos ao longo da fase. Encerra avisando que o próximo módulo é de planejamento, usando o framework da NoCode Startup, antes de qualquer construção.
- **Pontos-chave:**
  - Captura de dados do lead: nome, e-mail, telefone e CPF; verificação de duplicidade no Supabase antes de cadastrar.
  - CRM: criar cartão no Trello → associar o cartão ao lead no Supabase → atualizar status (novo, pago, perdido).
  - Fluxo Asaas em 4 micro-etapas: verificar se o cliente existe → criar se não existir → gerar a cobrança → atualizar o pedido no Supabase.
  - Follow-up: monitorar o campo "última mensagem" no Supabase para disparar lembretes e recuperar leads inativos.
  - Reconhecimento de pagamento: webhook no Asaas → atualiza Supabase → move o cartão no Trello.
  - Workflows a construir: (1) agente no Chat Trigger com as tools de Supabase/Asaas/Trello, (2) criar cartão no Trello (fluxo separado), (3) template mestre com as tools, (4) template mestre com desativação do agente para fallback humano, (5) follow-up, (6) webhook de checagem de pagamento.
- **Link:** https://flix.nocodestartup.io/m/lessons/4957

## Pegadinhas e insights

- **Nada é construído aqui.** As 3 aulas são 100% apresentação/slides/Miro. A mão na massa começa só no módulo seguinte, que é de planejamento com o framework da NoCode Startup — não pule a etapa de planejar achando que já dá pra montar o fluxo.
- **Construir primeiro no Chat Trigger, WhatsApp por último.** Decisão de arquitetura deliberada: testa-se o agente e as tools num canal simples antes de plugar o template mestre do WhatsApp. Reduz o custo de depurar dois problemas ao mesmo tempo.
- **Verificação de duplicidade é passo explícito.** Antes de cadastrar o lead, consultar o Supabase — o instrutor cita a duplicação como o erro a evitar na entrada.
- **Criar cartão no Trello vira workflow separado**, não um nó dentro do agente. Isso é escolha de arquitetura, não detalhe: o agente chama esse workflow como tool.
- **O fallback humano é implementado desativando o agente** numa variante do template mestre, com alerta por WhatsApp em situações críticas — não é só "avisar alguém".
- **O follow-up depende de um campo do banco**: sem manter "última mensagem" atualizado no Supabase, o fluxo de recuperação de inativos não tem em que se apoiar.
- O curso não cita preços, limites de plano ou custos das ferramentas.
