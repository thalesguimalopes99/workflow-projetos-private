# Introdução: Planejamento do Projeto da Formação Lovable

Trilha Lovable | 6 aulas | ~27 min (00:27:10) | nível iniciante

> Como planejar, antes de escrever qualquer prompt, um app real (um CRM de leads) usando o framework de projeto da NoCode Startup — problema, solução, funcionalidades, usuários/permissões, benchmarking, wireframe e modelagem de dados.

## O que você sai sabendo fazer

- Aplicar o framework da NoCode Startup (visão estratégica → tendências de mercado → arquitetura técnica → criação interativa → lançamento/PDCA) para planejar um app com IA antes de começar a construir.
- Escrever a visão estratégica de um projeto: problema identificado, solução, funcionalidades principais tela a tela e escopo de V1/MVP.
- Mapear tipos de usuário, matriz de permissões (admin / vendedor / sem papel) e fluxo de cadastro-aprovação antes de tocar no back-end.
- Fazer benchmarking de concorrentes e levantar referências de design/UX para alimentar o prompt com contexto concreto.
- Rascunhar wireframes em dois níveis (papel → blocos em slides/Miro) e mapear os processos/automações do produto.
- Esboçar a modelagem de dados (tabelas, campos, tipos, chave primária, policies) e estimar custo/prazo do projeto.

## Stack e ferramentas

- **Lovable** — construção do front-end/interface (transcrito como "Lobo" pelo Whisper).
- **Supabase** — banco de dados, autenticação e back-end; descrito como "o coração de tudo".
- **n8n** — automações e integrações (formulário → CRM, WhatsApp → CRM).
- **ChatGPT** — apoio na pesquisa de mercado, referências de UX e modelagem de dados.
- **Notion** — documento do framework de planejamento (há botão de copiar o template).
- **Tally** — formulário de captação de leads (transcrito como "talhe").
- **Dribbble / Behance** — referências de design e UX.
- **Slides / PowerPoint / Miro** — wireframe de blocos; **UX Pilot / UI Wizard** citados como alternativas.
- **Replit** — citado no panorama de ferramentas de vibe code, junto com plataformas com editor de código e terminal.
- **Z-API / Mega API** — citadas como possíveis integrações de WhatsApp no futuro.
- Referências de CRM analisadas: **Pipedrive**, **Clint CRM** (usado internamente pela NoCode Startup) e um CRM minimalista transcrito como "Atch" (provavelmente Attio).

## Pré-requisitos

As aulas assumem que você já passou pelas fases anteriores da formação Lovable: noções de prompt/vibe code com Lovable e a aula de banco de dados no Supabase (o instrutor manda voltar atrás se você não souber o que é `int8`, chave primária ou script SQL). Também assume que o framework de projeto da NoCode Startup já foi apresentado antes.

## Aula a aula

### 1.1 - Introdução à Trilha  (00:03:12)
- **Resumo:** Abertura da última fase da trilha, em que o projeto é construído do zero até a publicação unindo front-end e back-end. O instrutor recapitula o panorama das ferramentas de AI coding/vibe code — plataformas conversacionais como Lovable e Replit versus plataformas mais complexas com editor de código e terminal — e recomenda começar por projetos simples. Apresenta o entregável: um CRM de leads com vendedores e admin. Avisa que a stack será Lovable + Supabase + n8n.
- **Pontos-chave:**
  - Lovable é a recomendação para a maioria dos tipos de projeto; complexidade maior vem de dominar o Supabase (back-end).
  - Saída é não-determinística: mesmo com prompt idêntico ao do instrutor, o resultado na tela pode diferir.
  - Foque nos fundamentos, boas práticas e no checklist, não em reproduzir pixel a pixel.
  - A combinação Lovable + n8n + Supabase é o que destrava projetos mais robustos.
- **Link:** https://flix.nocodestartup.io/m/lessons/5059

### 1.2 - Conhecendo o Projeto que Vamos Construir  (00:02:44)
- **Resumo:** Demo do produto final já pronto, gravada depois da construção. O instrutor navega pelo CRM No Code mostrando dashboard com métricas e filtros de período, pipeline Kanban com drag and drop, CRUD e busca de leads, e o painel de administrador para aprovar perfis. Também mostra o formulário externo de captação que, via n8n, faria o lead cair automaticamente no CRM.
- **Pontos-chave:**
  - Dashboard: total de leads, taxa de conversão, negócios ganhos, valor ganho, leads por negócio, leads por origem, performance dos vendedores.
  - Filtros de 7 e 30 dias que recalculam o dashboard dinamicamente.
  - Pipeline com arrastar e soltar entre etapas; criar, editar e deletar leads.
  - Lista completa de leads com busca por pessoa ou empresa.
  - Painel admin aprova perfis (vendedor ou não-aprovado); autenticação e segurança ficam no Supabase.
  - A automação do formulário ainda não está ligada na demo — é feita mais adiante na formação.
- **Link:** https://flix.nocodestartup.io/m/lessons/5077

### 1.3 - Planejamento do Projeto  (00:02:37)
- **Resumo:** Aula que estabelece o método de trabalho da trilha. Reforça o conceito de MVP e alerta contra tentar construir de cara um app complexo com muitas telas via vibe code. Define a divisão do projeto em duas grandes partes — primeiro a interface, depois dados e inteligência — e apresenta as etapas do framework da NoCode Startup que serão percorridas uma a uma no documento.
- **Pontos-chave:**
  - MVP = produto mínimo viável: pense no problema, não na solução; poucas telas, funcionalidades essenciais, V1 antes de V2.
  - Nunca jogar front-end e back-end num prompt só — o Lovable se perde.
  - Etapas do framework: visão estratégica, insights de mercado, arquitetura técnica, criação interativa e lançamento/PDCA.
  - A criação interativa é subdividida em interface e back-end/dados, totalizando 6 etapas.
  - Há um documento pronto e detalhado para baixar, mas a recomendação é preencher junto, ativamente.
- **Link:** https://flix.nocodestartup.io/m/lessons/5060

### 2.1 - Etapa 1: Visão Estratégica  (00:08:32)
- **Resumo:** A aula mais longa e densa do curso: o instrutor preenche ao vivo a primeira etapa do framework para o CRM. Detalha o problema (leads espalhados entre planilha, WhatsApp e papel; processo comercial sem padronização; falta de visão de resultados), a solução, a lista de funcionalidades com o layout desejado do dashboard, os três tipos de usuário com suas permissões, o fluxo de cadastro e as ferramentas envolvidas com estimativa de custo e prazo.
- **Pontos-chave:**
  - Funcionalidades definidas: dashboard de resultados, pipeline comercial, CRUD de leads, lista de contatos, gestão de admin/usuários e integrações com n8n.
  - Dashboard descrito por linhas — linha 1: leads, taxa de conversão, quantidade de negócios; linha 2: gráficos de ganhos por dia e leads por origem; linha 3: performance por vendedor.
  - Etapas do Kanban mantidas simples: novo, atendimento, ganho, perdido.
  - Campos do lead: nome, empresa, telefone, origem, data de criação, detalhes — sem histórico do lead, para simplificar.
  - Permissões: admin vê/cria/edita/deleta qualquer lead e acessa a gestão de usuários; vendedor vê todos os leads, cria novos, mas só edita os que criou e não acessa a gestão de usuários; papel "nenhum" é o estado inicial, sem acesso a nada até o admin liberar.
  - Custo estimado: Lovable no plano de 100 créditos (projeto deve consumir ~20 a 30), Supabase no plano gratuito, e cerca de R$100 a R$300/mês num cenário real com integrações. Prazo estimado: uma semana.
  - Quanto mais detalhado o documento, melhor a IA constrói — pergunta rasa gera coisas que você não pediu.
- **Link:** https://flix.nocodestartup.io/m/lessons/5061

### 2.2 - Etapa 2: Tendências de Mercado  (00:03:17)
- **Resumo:** Etapa de benchmarking. O instrutor mostra a pesquisa que fez sobre CRMs existentes, os padrões funcionais que se repetem no mercado e as referências de design e UX levantadas com apoio do ChatGPT e de galerias de design. Fecha com prints de CRMs bonitos para extrair a estrutura visual padrão.
- **Pontos-chave:**
  - Vale mesmo para projeto interno ou pessoal — serve como referência de design e de funcionalidades que já se provaram.
  - Padrões identificados no mercado: pipeline visual com Kanban arrastável, gestão de contatos, relatórios básicos (inclusive PDF) e integrações simples com e-mail e calendário.
  - A gestão de contatos não estava na V1 e entrou depois de a pesquisa mostrar que fazia sentido.
  - Diretrizes de UX coletadas: Kanban limpo, hierarquia visual clara no dashboard, uso de cards, paleta suave, tipografia legível, painel responsivo.
  - Não invente um design novo: siga a estrutura consagrada (menu lateral, lista, cards de resultado, Kanban).
  - Quanto mais lapidada a ideia antes, menos crédito gasto e menos erro depois.
- **Link:** https://flix.nocodestartup.io/m/lessons/5062

### 2.3 - Etapa 3: Arquitetura Técnica  (00:06:48)
- **Resumo:** Fecha o planejamento com um checklist técnico em quatro frentes: wireframe, mapeamento de processos, modelagem de dados e melhorias futuras. O instrutor mostra o rascunho em papel das telas, a evolução para blocos em slides, o passo a passo de uma automação de captação e o esboço das tabelas do banco. Termina anunciando os próximos módulos: design/front-end, depois back-end e inteligência, depois fechamento com desafio final.
- **Pontos-chave:**
  - Wireframe em dois níveis: primeiro rabisco em papel (menu lateral, dash, pipeline, colunas do Kanban), depois blocos de maior fidelidade em slides, Miro ou PowerPoint.
  - Telas do app: dashboard, pipeline, leads, admin e meu perfil.
  - Mapeamento de processos exemplificado: usuário preenche formulário no Tally → webhook → cadastra lead no Supabase → lead aparece no Kanban. Mesma lógica para leads vindos do WhatsApp.
  - Modelagem de dados feita conversando com o ChatGPT: só duas tabelas, usuários e leads, com campos e tipos definidos (ex.: `int8` como chave primária, referência ao id da tabela de users, nome como texto).
  - Policies (quem acessa qual tabela) e o script SQL de criação das tabelas ficam para o módulo de back-end — o Lovable gera isso.
  - Melhoria futura citada: agente de IA que qualifica leads antes de passar para vendedores humanos.
  - Não pule etapas do checklist: sem elas o ChatGPT e as ferramentas de vibe code não constroem o que você quer.
- **Link:** https://flix.nocodestartup.io/m/lessons/5063

## Pegadinhas e insights

- **Separar front-end e back-end em prompts distintos é lei.** Jogar tudo num prompt só faz o Lovable se perder — a trilha inteira é organizada em torno dessa separação.
- **Resultado não é determinístico.** Prompt igual ao do instrutor pode gerar tela diferente; a régua de aprendizado são os fundamentos e o checklist, não o pixel.
- **Complexidade cedo mata o projeto.** O aviso é explícito: construir um app com muitas telas e funcionalidades de cara em vibe code "vai dar ruim". V1 enxuta primeiro, V2 depois.
- **Planejar é economizar crédito.** Documento raso → IA constrói o que você não pediu → retrabalho → mais créditos gastos e mais erro.
- **Decisões de arquitetura tomadas para simplificar:** sem histórico do lead na V1; apenas duas tabelas (usuários e leads); apenas quatro etapas no Kanban.
- **Modelo de permissão com estado inicial vazio:** todo usuário que se cadastra entra com papel "nenhum" e não vê nada até o admin promovê-lo a vendedor. Vendedor só edita os leads que ele mesmo criou. Isso precisa estar decidido no planejamento porque é a parte mais complexa do app.
- **Custos citados:** Supabase no plano gratuito atende; no Lovable, o plano de 100 créditos cobre o projeto, com consumo estimado de 20 a 30 créditos; num cenário real com integrações (Z-API, Mega API, GPT), algo entre R$100 e R$300 para iniciar. Dá para construir de graça se você distribuir o trabalho ao longo dos dias.
- **A pesquisa de mercado muda o escopo.** A lista de contatos de leads não estava prevista e entrou na V1 depois do benchmarking.
- **Supabase é o centro de gravidade do projeto** — ele une front-end, automações e dados; dominá-lo é o que permite projetos mais complexos.
- **Nota de transcrição:** o Whisper transcreve "Lovable" como "Lobo", "n8n" como "N2N/N8N/N20", "wireframe" como "iframe" e "CRUD" como "crude". A ferramenta de formulário citada como "talhe" é o Tally.
