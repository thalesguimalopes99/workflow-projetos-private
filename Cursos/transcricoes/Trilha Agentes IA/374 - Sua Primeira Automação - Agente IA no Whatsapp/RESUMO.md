# Sua Primeira Automação - Agente IA no Whatsapp

Trilha Agentes IA | 14 aulas | ~1h11min | nível iniciante

> Constrói do zero, no n8n, um agente de IA que recebe mensagem no WhatsApp via ZAPI, identifica/cadastra o usuário no Supabase, responde com OpenAI e devolve a resposta no WhatsApp — o esqueleto reaproveitável de qualquer agente conversacional.

## O que você sai sabendo fazer

- Configurar um Webhook no n8n e plugá-lo no evento "ao receber mensagem" de uma API de WhatsApp (ZAPI).
- Blindar a automação com um node Filter para não responder grupo, newsletter, broadcast, encaminhada, edição nem mensagem gerada pela própria API (anti-loop).
- Normalizar o payload cru do webhook num node Set enxuto (nome, telefone, mensagem).
- Montar gestão de usuário no Supabase: buscar por número de WhatsApp, criar se não existir, e unificar os dois ramos num Merge que vira fonte única de verdade.
- Configurar o node AI Agent (Conversational Agent) com modelo OpenAI, system prompt e memória por número de WhatsApp.
- Enviar a resposta de volta via HTTP Request importando o cURL da documentação da ZAPI e autenticando por Header Auth.
- Virar a chave de teste para produção (webhook de produção + workflow ativo) e auditar pela aba de execuções.

## Stack e ferramentas

- **n8n** (versão cloud) — orquestrador; nodes usados: Webhook, Filter, Set (Edit Fields / Data Transformation), Supabase (Get a Row / Create a Row), If, Merge (modo append), AI Agent (LangChain), Simple Memory (memória interna), HTTP Request, No Operation.
- **ZAPI** — API não-oficial de WhatsApp (instância web, webhooks, endpoint `send-text`, Client-Token). Documentação em developers.zapi.io.
- **Supabase** — banco de dados, tabela `usuarios` com campos `id`, `created_at`, `nome`, `whatsapp`.
- **OpenAI** — modelo de LLM do agente (usado o "o mini"; o instrutor cita o 3.5 como alternativa barata para teste).
- Citadas mas **não usadas** neste módulo: API oficial da Meta, MegaAPI, Evolution API (self-host, fica para módulos futuros); memórias externas (Postgres, Redis).

## Pré-requisitos

- Curso **Fundamentos 80/20 de n8n** da mesma formação — o instrutor assume que você já sabe os nodes principais e já fez as integrações/credenciais de OpenAI, Supabase e ZAPI, além de já ter criado a tabela `usuarios` no Supabase.
- Uma conta ZAPI com instância conectada ao WhatsApp (o teste gratuito serve).

## Aula a aula

### 1.1 - Introdução Ao Módulo Nosso Primeiro Agente no WhatsApp  (00:02:10)
- **Resumo:** Abertura do módulo prático. O instrutor posiciona o case como o "envelope" de tudo que foi visto nos fundamentos: integrar uma API de WhatsApp, tratar as mensagens, passar pelo agente de IA nativo do n8n e responder no WhatsApp. Reforça que esse fluxo vira a base de todos os agentes conversacionais da formação, em qualquer canal.
- **Pontos-chave:**
  - Entregável do módulo: primeira automação = agente de IA no WhatsApp.
  - Usa a IA nativa do n8n + uma API de WhatsApp.
  - Pré-requisito explícito: ter assistido o Fundamentos 80/20 de n8n.
  - Materiais e templates da aula ficam no link da descrição.
- **Link:** https://flix.nocodestartup.io/m/lessons/3907

### 1.2 - O Fluxo da Nossa Automação e Agente  (00:05:40)
- **Resumo:** Passeio pelo fluxograma antes de codar. Explica nó a nó a lógica: webhook dispara ao receber mensagem, filtro decide se prossegue, busca no banco se o usuário existe, cria se não existir, manda pro agente com OpenAI e responde no WhatsApp. Fecha mostrando a arquitetura (WhatsApp como front, n8n como orquestrador, LangChain+OpenAI como cérebro, Supabase como banco) e um spoiler do canvas final.
- **Pontos-chave:**
  - Arquitetura: WhatsApp (front) → n8n (orquestração) → OpenAI via LangChain → Supabase (dados).
  - O filtro existe para não responder grupo/newsletter/mensagem da própria API.
  - Ramo condicional: usuário existe → segue; não existe → cria no banco → segue.
  - O instrutor avisa que haverá, no fim, uma aula de visão geral condensada para quem prefere revisar tudo de uma vez.
- **Link:** https://flix.nocodestartup.io/m/lessons/3906

### 1.3 - Recados Importantes! APIs De Whatsapp + A Importância Desse Módulo  (00:04:09)
- **Resumo:** Aula de recados sobre escolha de ferramenta. Defende começar tudo em versão cloud/gerenciada para não travar o aprendizado com infraestrutura, deixando self-host para um segundo momento. Compara as opções de WhatsApp (oficial da Meta vs. não oficiais) e justifica a escolha da ZAPI para as aulas iniciais.
- **Pontos-chave:**
  - Cloud primeiro, self-host depois — o que gera resultado é dominar automação e integração, não instalar servidor.
  - Opções de WhatsApp: API oficial da Meta; não oficiais ZAPI, MegaAPI, Evolution API.
  - ZAPI e MegaAPI cobram mensalidade mas oferecem teste gratuito; Evolution API é instalável em servidor próprio, sem custo de plataforma.
  - Escolha do curso: ZAPI. Evolution API e API oficial (Meta/Instagram/Telegram) virão em aulas futuras com templates próprios.
  - O agente desta trilha é a semente do "template mestre" de agentes conversacionais da NoCode StartUp.
- **Link:** https://flix.nocodestartup.io/m/lessons/4406

### 2.1 - Gatilho Webhook - Escutar Mensagens do WhatsApp  (00:05:09)
- **Resumo:** Primeiro nó na prática. Cria o node Webhook no n8n, renomeia, deixa o método POST e sem autenticação, copia a URL de teste e cola no painel da ZAPI, na opção de webhook "ao receber mensagem". Dispara uma mensagem real e dissecar o payload recebido.
- **Pontos-chave:**
  - No painel ZAPI: Instâncias web → sua instância → três pontinhos → Editar → Webhooks → "ao receber mensagem".
  - Marcar "notificar as enviadas por mim" quando você usa o mesmo número para enviar e receber nos testes.
  - O que interessa do payload está em `body`; `headers`/`query` são descartáveis.
  - Campos relevantes do body: flags booleanas (reply, edição, grupo, newsletter, broadcast, encaminhada, veio da API), telefone, nome do remetente, foto, status e o texto da mensagem.
- **Link:** https://flix.nocodestartup.io/m/lessons/3909

### 2.2 - Filtro de Bloqueio  (00:06:59)
- **Resumo:** Adiciona um node Filter como check de sanidade logo depois do webhook. Explica por que Filter e não If/Switch (aqui só interessa parar o fluxo, não desviá-lo) e monta condições booleanas encadeadas com "E". Termina ensinando a fixar (pin) o retorno do webhook e editar o JSON fixado para simular cenários sem precisar mandar mensagem no celular.
- **Pontos-chave:**
  - Condições: edição = false, grupo = false, newsletter = false, broadcast = false, encaminhada = false, veio da API = false.
  - A condição "veio da API = false" é o anti-loop: sem ela o agente responde à própria resposta infinitamente ao testar com o próprio número.
  - Filter para (não continua nada); If/Switch seriam a escolha se você quisesse tratar grupos por outro caminho.
  - Pin data no webhook + edição manual do JSON = teste rápido (ex.: forçar `isGroup: true` e ver o fluxo parar).
- **Link:** https://flix.nocodestartup.io/m/lessons/3908

### 2.3 - Simplificando e Normalizando Dados (SET)  (00:02:59)
- **Resumo:** Boa prática de arquitetura: logo após todo webhook, um node Set (Edit Fields, em Data Transformation) para reduzir o payload ao essencial. Mapeia apenas nome, telefone e mensagem em campos renomeados e batiza o node de "Simplificando dados".
- **Pontos-chave:**
  - Campos criados: nome do usuário, WhatsApp do usuário e mensagem.
  - Motivos: organização, facilidade de referenciar depois, possibilidade de renomear/tratar dados.
  - Motivo de performance: payload gordo trafegando por todos os nodes pesa no servidor conforme a automação cresce.
  - Nomear os nodes faz parte da boa prática ensinada.
- **Link:** https://flix.nocodestartup.io/m/lessons/3911

### 2.4 - Conectando Supabase para Gestão dos Usuários (parte1)  (00:04:43)
- **Resumo:** Entra o banco de dados. Adiciona o node Supabase na operação "Get a Row" apontando para a tabela `usuarios`, usando o número de WhatsApp como chave de busca (identificador único natural). Ao testar com o banco vazio, o fluxo morre — e aí vem o ajuste que destrava tudo.
- **Pontos-chave:**
  - Tabela `usuarios`: `id` e data de criação automáticos + `nome` e `whatsapp` (texto), criados na aula de fundamentos.
  - Filtro do Get a Row: campo `whatsapp` = valor vindo do node "Simplificando dados".
  - Sem resultado, o node não emite output e a automação para antes do If.
  - Correção: ativar nas configurações do node a opção de **sempre gerar output** (Always Output Data).
  - O ícone de interrogação em cada node traz a documentação inline.
- **Link:** https://flix.nocodestartup.io/m/lessons/3910

### 2.5 - Conectando Supabase para Gestão dos Usuários (parte2)  (00:05:31)
- **Resumo:** Configura o node If que bifurca entre usuário existente e novo. Para conseguir mapear os campos, cria manualmente um registro no Supabase com o próprio número, roda o fluxo, e usa a existência do `id` como condição. No ramo false, adiciona um segundo node Supabase para criar a linha.
- **Pontos-chave:**
  - Condição do If: o `id` retornado existe → true (usuário já cadastrado); senão → false.
  - Qualquer campo do retorno serviria, mas usar o `id` é o padrão recomendado.
  - Node "Criar usuário": Supabase → Create a Row → tabela `usuarios` → campos `nome` e `whatsapp`.
  - Pegadinha de origem do dado: os valores para criar o usuário têm que vir do node "Simplificando dados", nunca do If nem do "Buscar usuário" (que estão vazios justamente quando o usuário não existe).
  - Teste do ciclo completo: apagar o registro no Supabase → rodar (cai no false e cria) → rodar de novo (cai no true).
- **Link:** https://flix.nocodestartup.io/m/lessons/3913

### 2.6 - Centralizando Dados Usuário com Node Merge  (00:04:55)
- **Resumo:** Mostra de propósito o problema de plugar o AI Agent direto depois do If: os dados do usuário ficam ora no node "Buscar usuário", ora no "Criar usuário", e não há como referenciar um único lugar adiante no fluxo. A solução é um node Merge no modo append juntando os dois ramos.
- **Pontos-chave:**
  - Merge em modo **append** empilha os resultados dos dois ramos; como um deles está sempre vazio, sobra sempre exatamente um usuário.
  - O Merge vira a **fonte única de verdade** dos dados do usuário para todos os nodes seguintes.
  - Nomear os nodes ("Buscar usuário", "Criar usuário") facilita as referências.
  - Validação prática: rodar com usuário existente e com usuário novo e conferir que o Merge tem dado nos dois casos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3912

### 2.7 - Criando Nosso Agente Integrado a OpenAI  (00:07:09)
- **Resumo:** Configura o node AI Agent (baseado em LangChain) no tipo Conversational Agent. Define de onde vem o prompt do usuário, escreve o system message, conecta o modelo da OpenAI e, ao perceber que o agente não lembra de nada, pluga a memória interna do n8n usando o número de WhatsApp como chave de sessão.
- **Pontos-chave:**
  - Tipo de agente: Conversational Agent — o mais versátil e recomendado pela documentação para a maioria dos casos.
  - Prompt do usuário: opção "definir abaixo", puxando a mensagem do node "Simplificando dados".
  - System message do exemplo: agente que é "o melhor vendedor do mundo" e tenta vender algo relacionado ao que o usuário falou, de forma engraçada e persuasiva.
  - Modelo: OpenAI ("o mini"), com 3.5 citado como alternativa barata; opções de provedor incluem Groq, Google Gemini, Azure, Anthropic e Ollama.
  - Memória: memória interna do n8n com chave = número de WhatsApp do usuário, garantindo uma conversa por contato.
  - Sem memória o agente não lembra da mensagem anterior; a memória interna atende o teste mas não é o recomendado em produção.
  - Ferramentas (tools) do agente ficam para módulos futuros.
- **Link:** https://flix.nocodestartup.io/m/lessons/3915

### 2.8 - HTTP Resquest - Enviando Resposta no WhatsApp  (00:07:01)
- **Resumo:** Fecha o ciclo devolvendo a resposta ao WhatsApp. Vai à documentação da ZAPI, copia o cURL do endpoint de envio de texto e usa o "Import cURL" do node HTTP Request para pré-preencher método, URL, header e body. Depois troca as credenciais por uma autenticação gerenciada pelo n8n e mapeia telefone e mensagem.
- **Pontos-chave:**
  - Documentação em developers.zapi.io → Mensagens → enviar texto simples; método POST, endpoint termina em `send-text` (para imagem seria `send-image`, mesmo padrão).
  - A URL leva o ID da instância e o token da instância — dá para copiar o endpoint já montado no painel da ZAPI.
  - O header `Client-Token` com o token de segurança da conta (painel ZAPI → Segurança) é obrigatório em **todas** as chamadas.
  - Em vez de digitar o header na mão, criar uma credencial genérica do tipo **Header Auth** no n8n — mais seguro e reutilizável.
  - Body obrigatório: `phone` (do Merge ou do "Simplificando dados") e `message` (output do AI Agent). Opcionais: delay de mensagem, delay type, edit message ID.
  - Um node No Operation no final serve só de marcação visual de fim de fluxo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3914

### 2.9 - Colocando nosso Agente em Produção  (00:03:49)
- **Resumo:** Passa o agente do modo teste para produção. Explica que a URL cadastrada na ZAPI ainda era a de teste, copia a URL de produção do node Webhook, atualiza na instância da ZAPI, ativa e salva o workflow. Conversa com o bot direto pelo celular e revisa a aba de execuções.
- **Pontos-chave:**
  - Trocar a URL de teste pela de **produção** no webhook da ZAPI (Instâncias web → Editar → Webhook) — sem isso, workflow ativo não roda.
  - Remover o pin do webhook e salvar o workflow antes de usar.
  - Aba de execuções mostra o histórico: uma execução completa (mensagem do humano) e outra que para no Filter (mensagem gerada pela própria API).
  - Esse par de execuções por mensagem é comportamento esperado quando você testa conversando consigo mesmo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3916

### 3.1 - Visão Geral da Nossa Automação Agente de IA  (00:07:22)
- **Resumo:** Aula de revisão consolidada: percorre o fluxo já pronto, node por node, mostrando as configurações finais e reexplicando o porquê de cada decisão. É a alternativa para quem prefere revisar tudo de uma vez em vez de voltar às aulas passo a passo.
- **Pontos-chave:**
  - Blocos do canvas (organizados com notas/sticky notes): gatilho → gestão de usuários e conversas → agente de IA → resposta à API de WhatsApp.
  - Recapitula as seis condições do Filter e por que "veio da API" evita o agente conversar sozinho.
  - Recapitula o Set como redução de carga e o Merge como fonte de verdade.
  - Recapitula o agente: prompt de vendedor, mensagem vinda do "Simplificando dados", OpenAI, buffer de memória chaveado pelo telefone.
  - Recapitula a chamada final: POST em `send-text`, Client-Token na credencial (não no header manual), body com `phone` e `message`.
  - Argumento de modularidade: em outra API de WhatsApp muda pouca coisa; o bloco do agente é plugável.
- **Link:** https://flix.nocodestartup.io/m/lessons/3917

### 3.2 - A Grande Importância desse Módulo  (00:03:33)
- **Resumo:** Fechamento conceitual. Defende que a estrutura construída é o gabarito de praticamente qualquer agente futuro: gatilho por webhook de WhatsApp, filtro, normalização, gestão de usuário em banco, bloco de IA e resposta pela API. O bloco de IA é o único trecho realmente intercambiável.
- **Pontos-chave:**
  - Estrutura base repetível: webhook → filtro → normalização → gestão de usuários → agente → resposta.
  - O banco de dados é a fonte de verdade sobre usuários, produtos e clientes usados pelo agente.
  - O node de AI Agent do n8n pode ser trocado por outro motor (ex.: Assistants da OpenAI, Dify) sem mexer no resto do fluxo.
  - Nos módulos seguintes esse bloco de agente cresce com novas funções e ferramentas.
- **Link:** https://flix.nocodestartup.io/m/lessons/3918

## Pegadinhas e insights

- **Anti-loop é obrigatório.** Sem a condição "mensagem veio da API = false" no Filter, testar com o próprio número faz o agente responder à própria resposta em looping infinito.
- **Supabase Get a Row mata o fluxo quando não acha nada.** Precisa ligar "sempre gerar output" (Always Output Data) nas configurações do node, senão o If nunca recebe dados e a automação para silenciosamente.
- **De onde puxar o dado ao criar o usuário:** só do node de normalização (Set). Referenciar o If ou o "Buscar usuário" resulta em campos vazios, porque justamente naquele ramo eles não existem.
- **Por que Merge e não ligar o If direto no agente:** com dois ramos, o dado do usuário fica ora num node ora noutro e não há endereço fixo para referenciar depois. O Merge em append resolve porque um dos ramos sempre chega vazio.
- **Filter vs. If/Switch:** use Filter quando o cenário indesejado deve simplesmente encerrar o fluxo; If/Switch quando cada cenário tem um tratamento próprio.
- **Pin data economiza teste manual.** Fixar o retorno do webhook e editar o JSON à mão (ex.: virar `isGroup` para true) permite simular cenários sem mandar mensagem no celular a cada rodada.
- **Webhook de teste ≠ webhook de produção.** É o erro clássico do fim do módulo: ativar o workflow e nada acontecer porque a ZAPI ainda aponta para a URL de teste.
- **Client-Token em toda chamada da ZAPI**, e o certo é guardá-lo numa credencial Header Auth do n8n — mais seguro e reaproveitável do que colar o header em cada node.
- **Memória interna do n8n não é recomendada para produção** — serve para teste (e para cenários pequenos), mas o instrutor sinaliza opções externas.
- **Normalizar dados não é só estética:** carregar o payload inteiro do webhook por todos os nodes pesa no servidor à medida que a automação cresce.
- **Decisão de ferramenta:** cloud primeiro (ZAPI, n8n cloud, Supabase), self-host depois (Evolution API). ZAPI e MegaAPI cobram mensalidade mas têm teste gratuito; Evolution API é gratuita mas exige servidor próprio.
- **Custo do modelo:** o instrutor escolhe deliberadamente um modelo barato ("o mini", com o 3.5 como alternativa) porque a fase é de teste.
- **Reaproveitamento:** este workflow é declaradamente a base do "template mestre" de agentes conversacionais da formação — vale salvá-lo como template antes de evoluir.
