# 1.4 - Fundamentos (Para Não Técnicos)

Trilha Agentic Builder Claude | 7 aulas | ~33 min (00:32:49) | nível iniciante

> Aula teórica de base: o vocabulário mínimo (front/back, API, MCP, modelo, token, versionamento, PRD) que um profissional não técnico precisa antes de começar a construir software e agentes com Claude Code.

## O que você sai sabendo fazer

- Separar front-end, back-end e APIs ao descrever um projeto, e situar em qual camada cada problema mora.
- Escolher modelo de IA com consciência de trade-off (rápido/barato vs. raciocínio profundo/caro) e reconhecer que a maioria das "ferramentas de IA" é só interface sobre GPT/Gemini/Claude.
- Estimar e controlar custo de IA raciocinando em tokens de entrada e de saída — incluindo o que entra sem você perceber (system prompt, histórico, arquivos lidos).
- Decidir quando usar API e quando usar MCP para conectar um projeto a serviços externos.
- Explicar e usar o vocabulário de versionamento (commit, push, pull, branch, merge, PR) para acompanhar o que a IA faz no seu projeto.
- Escrever um PRD que dê contexto suficiente para a IA planejar o projeto em etapas em vez de "fazer qualquer coisa".

## Stack e ferramentas

- **Orquestração de agentes:** Claude Code (grafado "Cloud Code" na transcrição), OpenCode ("OpenCloud" na transcrição).
- **IDE:** Cursor (usado em conjunto com o agente do Claude Code), VS Code.
- **Front-end / framework:** Next.js + shadcn/ui (biblioteca de componentes).
- **Back-end:** Supabase — banco de dados, autenticação/segurança, functions, storage de arquivos, banco vetorial para IA.
- **Versionamento:** Git (local) + GitHub (nuvem).
- **Deploy:** Vercel para projetos Next.js; VPS da Hostinger em casos mais simples.
- **APIs citadas:** Stripe, Asaas, Pagar.me, Mercado Pago (pagamentos); Resend e SendGrid (e-mail); Google Maps (localização); API de WhatsApp; APIs das próprias LLMs.
- **Modelos citados:** OpenAI (GPT-5, GPT-5 Mini, GPT-Image); Google (Gemini 3 Pro, Gemini 3 Flash, Nano Banana para imagem, Veo 3 para vídeo); Anthropic (Claude Opus, Sonnet, Haiku); xAI (Grok 4, Grok Imagine); open source: Llama (Meta) e DeepSeek.
- **Planejamento:** framework/gerador de PRD da NoCode Startup (otimizado para colar no Claude Code) — link indicado na descrição da aula 2.4.
- **MCP:** Model Context Protocol, com exemplos de Slack, Notion, GitHub, Gmail, Google.

## Pré-requisitos

Nenhum. É o módulo de entrada da trilha, feito explicitamente para quem não tem formação técnica — não pede código, conta em nenhuma plataforma nem projeto anterior.

## Aula a aula

### 1.1 - Como um Projeto é Construído  (00:04:54)
- **Resumo:** Abre a formação estabelecendo o mapa mental de um projeto de software: a camada visual (front-end, com UI e UX), a camada onde a lógica acontece (back-end, com regras de negócio, banco e segurança) e as pontes com o mundo externo (APIs). Em seguida percorre o ciclo tradicional de desenvolvimento — descoberta, design, desenvolvimento, testes, lançamento, melhoria contínua — e mostra em quais dessas etapas a IA passa a fazer o trabalho pesado. Fecha delimitando o novo papel do profissional: orquestrador, não executor.
- **Pontos-chave:**
  - Front-end = tudo que o usuário vê (site, app, dashboard); back-end = lógica, banco de dados e segurança. Exemplo de fluxo: login digitado no front vai validar a senha no banco.
  - API é a conexão do seu projeto com serviços de terceiros (Stripe, Mercado Pago para pagamento; SendGrid ou Resend para e-mail, ex.: "esqueci minha senha").
  - Ciclo clássico: descoberta → design → desenvolvimento → testes → lançamento → melhoria contínua; com IA, o ciclo cai de meses para semanas e times menores entregam mais.
  - Teste continua exigindo humano: o ideal é teste da IA + teste humano.
  - A IA não substitui: entender o problema real, decidir o que vale a pena e assumir responsabilidade pelas decisões.
- **Link:** https://flix.nocodestartup.io/m/lessons/5507

### 1.2 - IA, Modelos e Tokens  (00:07:06)
- **Resumo:** Organiza as "bonecas russas" do campo — IA contém machine learning, que contém deep learning, que contém a IA generativa (as LLMs) — só o suficiente para você se localizar numa conversa técnica. Depois separa empresa, modelo e interface, listando quem faz o quê no mercado, e distingue modelos fechados de open source. A segunda metade é sobre tokens: como o texto é fatiado, o que realmente entra na conta e por que a resposta custa mais que a pergunta.
- **Pontos-chave:**
  - Hierarquia: IA ⊃ machine learning ⊃ deep learning ⊃ IA generativa (LLMs). IA preditiva (recomendação de produto) é coisa antiga; a generativa cria conteúdo.
  - Empresa ≠ modelo ≠ interface: ChatGPT é só interface, o modelo é o GPT. Vale o mesmo para Gemini (Google), Claude (Anthropic) e Grok (xAI).
  - Cada modelo tem propósito: rápidos e baratos pensam menos; modelos para tarefa complexa demoram mais e custam mais; há modelos específicos de imagem e vídeo.
  - Open source (Llama, DeepSeek) tem código aberto e pode rodar na sua máquina, mas geralmente não compensa pelo peso — o normal é usar a nuvem das big techs.
  - Token = pedaço de palavra. ~4 caracteres em inglês (um pouco mais em português); 1 página de texto ≈ 750 tokens. Toda precificação é por token.
  - O token de entrada não é só a sua pergunta: inclui o system prompt, o resumo do projeto, o histórico inteiro da conversa e todos os arquivos lidos.
  - **Token de saída custa de 3 a 5 vezes mais caro** que o de entrada.
- **Link:** https://flix.nocodestartup.io/m/lessons/5508

### 1.3 - O que é possível criar  (00:03:34)
- **Resumo:** Panorama do escopo de entregas possíveis com IA agêntica, dividido em duas famílias. A primeira é software: da landing page em HTML até SaaS multi-empresa, ERP e API pública. A segunda são workflows agênticos: agentes pontuais, automações disparadas por evento, times de agentes por área e, no limite, a operação inteira da empresa rodando com agentes. O instrutor enfatiza que essa escalada é gradativa.
- **Pontos-chave:**
  - Software simples → complexo: site pessoal, landing page, blog, portfólio, dashboard, painel admin, CRM simples, gerador de documentos, área de membros, quiz, diretório, loja virtual, agendamento, marketplace, SaaS com login/pagamento/banco, ERP, API pública.
  - Workflows agênticos: agente único (pesquisador, escritor, executor) → automações inteligentes engatilhadas → times completos de agentes.
  - Exemplos de times: marketing (SEO + Ads + social media), operação, devs; substituição de áreas inteiras como SDR, suporte e financeiro.
  - Ferramentas citadas para isso: Claude Code e OpenCode.
  - O caminho é incremental: comece por um agente, teste, e só então avance para áreas e empresa agêntica.
- **Link:** https://flix.nocodestartup.io/m/lessons/5509

### 2.1 - Stack de Ferramentas  (00:04:44)
- **Resumo:** Apresenta o conjunto padrão de ferramentas adotado na formação, agrupado por função. Claude Code é o orquestrador central (um agente coordenando outros agentes), usado tanto para software quanto para automações. Cursor entra como IDE, e o instrutor mostra na tela o que é uma IDE para quem nunca viu. Para o produto em si a stack é Next.js + shadcn/ui no front e Supabase no back, com Git/GitHub, Vercel ou Hostinger no deploy e APIs para o resto.
- **Pontos-chave:**
  - A combinação recomendada é a IDE do Cursor + o agente do Claude Code (dá para rodar no terminal, no app ou dentro da IDE).
  - Next.js = framework React (pacote de funcionalidades para projetos robustos); shadcn/ui = biblioteca de componentes que melhora a interface.
  - Supabase concentra o back-end: banco de dados, autenticação, functions, arquivos/PDFs e banco vetorial para IA.
  - Versionamento local (Git) + nuvem (GitHub); deploy em Vercel para Next.js, ou VPS Hostinger em projetos mais simples.
  - Integrações por API ou MCP: Resend para e-mail transacional, Stripe ou Asaas para pagamento.
  - Você não precisa saber ler o código — precisa saber gerenciar o agente.
- **Link:** https://flix.nocodestartup.io/m/lessons/5510

### 2.2 - APIs e MCPs  (00:04:28)
- **Resumo:** Explica API pela metáfora do restaurante — você pede, o garçom (a API) leva à cozinha (o servidor) e traz a resposta, sem que você entre na cozinha — e mostra o fluxo prático: criar conta no serviço, gerar uma chave, chamar um endpoint e receber a resposta em JSON. Depois introduz MCP como a padronização que faltava: em vez de integrar cada API com sua documentação própria, existe um protocolo único desenhado para a IA usar. A conclusão é que API serve para você integrar e MCP serve para a IA agir.
- **Pontos-chave:**
  - Vantagem de API: você usa serviço pronto em vez de construir do zero, sem precisar entender o interior dele.
  - Fluxo prático: conta na plataforma → chave de API → chamada ao endpoint → resposta em JSON. Exemplo dado: perguntar ao Stripe se o boleto do usuário foi pago e cortar o acesso se não foi.
  - Categorias de API citadas: pagamento (Stripe, Asaas, Pagar.me), localização (Google Maps), LLM, WhatsApp.
  - MCP = Model Context Protocol, formato padrão para IAs se comunicarem com projetos e serviços.
  - Sem MCP: cada integração (Slack, Notion, GitHub) tem doc e formato próprios, tudo do zero. Com MCP: um padrão só, com ação autônoma e customizável.
  - Regra de bolso da aula: API é feita para o dev integrar; MCP é feito para a IA usar.
- **Link:** https://flix.nocodestartup.io/m/lessons/5511

### 2.3 - Versionamento  (00:04:57)
- **Resumo:** Parte do caos conhecido do "relatorio_final_v2_agora_vai" para justificar versionamento: um único arquivo com histórico de snapshots em vez de cópias soltas. Separa Git (local, offline, na sua máquina) de GitHub (nuvem, colaboração) e percorre o ciclo commit → push → pull. Fecha explicando branch e merge com dois cenários — correção de bug e três pessoas desenvolvendo em paralelo — tranquilizando que o Claude Code executa os comandos por você.
- **Pontos-chave:**
  - Versionamento = linha do tempo de fotos do projeto, com controle total das mudanças.
  - Git: local, funciona offline, rastreia mudanças, cria e gerencia branches, salva snapshots. GitHub: plataforma online, backup na nuvem, colaboração, rastreio de bugs e melhorias, automações.
  - Analogia da aula: Git é o diário pessoal do projeto; GitHub é a biblioteca compartilhada.
  - Ciclo: editar local → **commit** (agrupar e salvar mudanças) → **git push** (empurrar para a nuvem) → **git pull** (puxar a versão mais atual). Pull request (PR) é o pedido de atualização.
  - Branch = ramificação onde você experimenta, quebra e conserta sem tocar na versão que funciona; merge = unir de volta na branch principal quando a tarefa está pronta.
  - Cenários mostrados: hotfix de bug via branch e três devs em paralelo, cada merge acontecendo quando a respectiva tarefa fica pronta.
- **Link:** https://flix.nocodestartup.io/m/lessons/5512

### 2.4 - PRD para Planejar um Projeto  (00:03:06)
- **Resumo:** Fecha o módulo com o documento que traduz sua intenção para a IA. O PRD reúne dor, solução, funcionalidades, usuários, stack e referências de design. O instrutor demonstra o gerador de PRD da NoCode Startup, campo a campo, e explica que a saída é feita para ser colada no Claude Code. O princípio central: contexto é seu trabalho, execução técnica é da IA — e o resultado deve virar um plano em etapas.
- **Pontos-chave:**
  - PRD = documento que comunica à IA o problema, o projeto, os usuários e as funcionalidades.
  - Campos do gerador: nome do projeto, problema identificado, solução, funcionalidades principais (botões prontos ou texto livre), tipos de usuário, stack tecnológica e referência de design → botão "gerar documentação".
  - Exemplo de stack preenchida na demonstração: React, shadcn/ui, Supabase.
  - A saída é otimizada para colar no Claude Code e servir de base para o plano do projeto.
  - Referência de design importa: puxe de empresas e sites já existentes para não cair no genérico.
  - O trabalho sempre avança em etapas — a IA monta o plano por fases e você executa parte por parte para garantir qualidade.
- **Link:** https://flix.nocodestartup.io/m/lessons/5513

## Pegadinhas e insights

- **Não pule os fundamentos.** O instrutor abre a aula 1.1 avisando explicitamente que quem pular a teoria para "sair fazendo" vai dar ruim — o aprendizado prático depende desse vocabulário.
- **O custo escondido está no contexto, não na sua pergunta.** O token de entrada carrega system prompt, resumo do projeto, histórico completo da conversa e todo arquivo lido. É por isso que gerenciar contexto vira disciplina de custo, tema retomado nas aulas seguintes da trilha.
- **Saída custa 3 a 5x mais que entrada.** Pedir para a IA gerar muito texto/código é sistematicamente mais caro do que dar muito contexto.
- **Pedir para resumir um livro inteiro é caro.** Exemplo usado para ilustrar que volume de input vira dinheiro.
- **Modelo não é ferramenta.** Muita "empresa de IA" é só interface sobre GPT/Gemini/Claude — saber disso evita pagar duas vezes pela mesma inteligência.
- **Rodar open source local pode não compensar.** Llama e DeepSeek são abertos, mas o instrutor alerta que rodar na própria máquina "queima o computador"; o padrão é usar a nuvem dos provedores.
- **Sem contexto, a IA faz qualquer coisa.** Justificativa direta do PRD: quanto mais direcionamento, melhor o resultado — mas a decisão técnica deve ficar com a IA.
- **Decisão de arquitetura da formação:** IDE do Cursor + agente do Claude Code em conjunto, Next.js/shadcn no front e Supabase como back-end único (banco + auth + storage + vetorial), Vercel para deploy de Next.js e VPS Hostinger como alternativa mais simples.
- **Sempre em etapas.** A orientação repetida é fazer a IA planejar em fases e executar parte por parte, em vez de pedir o projeto inteiro de uma vez.
- **Teste humano continua obrigatório** mesmo com IA gerando e testando.
- **Nota de transcrição:** o ASR grafa "Cloud Code" (Claude Code), "Antrofic" (Anthropic), "ChatCN"/"ShedCN" (shadcn/ui), "Verticell" (Vercel), "Recend" (Resend), "Asus"/"Asas" (Asaas), "Grock" (Grok), "Deep Sea" (DeepSeek) e "PNI" (OpenAI). Nenhum valor ou passo foi alterado neste resumo.
