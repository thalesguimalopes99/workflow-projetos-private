# Mapa de conhecimento — cursos transcritos

Cobre os **48 cursos já transcritos e resumidos** do catálogo NoCode StartUp (de um catálogo maior) — os 36 anteriores mais o lote de 12 recém-processado. Este mapa cresce a cada lote: agrupamentos, contagens e sugestões abaixo valem só para o que já está em `transcricoes/`.

---

## Por capacidade

### 1. Fundamentos: arquitetura, API, webhook e vocabulário técnico

Base obrigatória — separa front/back, ensina a ler documentação de API e a decidir entre API e webhook.

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F1.3 - Fundamentos Desenvolvimento de Software | 9 | Software = front + back; arquitetura de SaaS, JSON, chamada de API completa, API x webhook, modelagem de banco (1-N e N-N) e metodologia problema → PDCA | [ver](<transcricoes/Trilha Nocode IA/314 - F1.3 - Fundamentos Desenvolvimento de Software/RESUMO.md>) |
| 1 - O Poder das APIs - Fundamentos Essenciais | 10 | A API na prática dentro do FlutterFlow: método HTTP certo, headers e Bearer, teste no navegador/Postman, variável dinâmica entre colchetes, JSON Path salvo, ramos de sucesso/erro e proteção da chave tirando a chamada do client side | [ver](<transcricoes/Trilha FlutterFlow Geral/276 - 1 - O Poder das APIs - Fundamentos Essenciais/RESUMO.md>) |
| Fundamentos de Automações IA | 9 | Arquitetura em 4 camadas (WhatsApp → n8n → Supabase → agente/LLM), critério Zapier x Make x n8n, JSON, métodos HTTP, webhook como gatilho | [ver](<transcricoes/_sem-trilha/368 - Fundamentos de Automações IA/RESUMO.md>) |
| Fundamentos Essenciais de Desenvolvimento - Projetos IA | 11 | Classificar projeto (site/automação/software/agente), escolher stack, vocabulário de API, prompt de agente e rotas de monetização | [ver](<transcricoes/Trilha Agentes IA/450 - Fundamentos Essenciais de Desenvolvimento - Projetos IA/RESUMO.md>) |
| Fundamentos Essenciais de Desenvolvimento de Projetos \| Lovable | 11 | Mesmo conteúdo do anterior, com a lente de quem vai construir front no Lovable/Framer/FlutterFlow | [ver](<transcricoes/Trilha Lovable/459 - Fundamentos Essenciais de Desenvolvimento de Projetos -/RESUMO.md>) |
| F3.1 - Introdução da Trilha \| MasterClass NoCode | 6 | O mapa do NoCode: 7 categorias de projeto, qual ferramenta para cada uma ("melhor pra quê" x "pra quem"), arquitetura de SaaS, critérios de avaliação (integrações, custo, comunidade, código-fonte) e rotas de monetização | [ver](<transcricoes/Trilha Nocode IA/283 - F3.1 -Introdução da Trilha - MasterClass NoCode/RESUMO.md>) |
| 1.4 - Fundamentos (Para Não Técnicos) | 7 | Front/back/API, escolha de modelo por custo x profundidade, custo em tokens, quando usar MCP, Git/GitHub e escrita de PRD | [ver](<transcricoes/Trilha Agentic Builder Claude/538 - 1.4 - Fundamentos (Para Não Técnicos)/RESUMO.md>) |

### 2. Fundamentos de IA, LLM, RAG e agentes (teoria)

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F1.4 - Fundamentos Inteligência Artificial | 11 | Hierarquia IA ⊃ ML ⊃ Deep Learning ⊃ generativa ⊃ LLM; tokenização, embeddings, bancos vetoriais, fine-tuning x RAG, function calling | [ver](<transcricoes/Trilha Nocode IA/315 - F1.4 - Fundamentos Inteligência Artificial/RESUMO.md>) |
| Fundamentos de Agentes IA Nocode | 5 | Versão condensada do anterior + o que separa agente de chatbot: fluxo de RAG e de function calling, escolha de banco (relacional/não relacional/vetorial) | [ver](<transcricoes/_sem-trilha/367 - Fundamentos de Agentes IA Nocode/RESUMO.md>) |
| 1.1 - O Profissional Agentic Builder | 6 | Conceito de harness (modelo + tools + memória + permissões + loop), organização agentica, AI Business OS em 5 camadas e rotas de monetização | [ver](<transcricoes/Trilha Agentic Builder Claude/537 - 1.1 - O Profissional Agentic Builder/RESUMO.md>) |

### 3. Construir agentes de IA conversacionais (WhatsApp, Telegram, Instagram)

O núcleo prático do que já está transcrito.

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| Sua Primeira Automação - Agente IA no Whatsapp | 14 | Agente ponta a ponta no n8n: webhook ZAPI → filtro anti-loop → usuário no Supabase (Get/Create + Merge) → AI Agent com memória → resposta via HTTP Request. É o esqueleto reaproveitável | [ver](<transcricoes/Trilha Agentes IA/374 - Sua Primeira Automação - Agente IA no Whatsapp/RESUMO.md>) |
| M1 - Fundamentos Dify | 12 | Chatbot no Dify com prompt hierárquico, variáveis e parâmetros; LLM próprio; consumo da API do Dify; Supabase com RLS; publicação no WhatsApp via n8n + Z-API | [ver](<transcricoes/Trilha Dify/351 - M1 - Fundamentos Dify/RESUMO.md>) |
| API Instagram - Agente IA Direct e Comentários | 10 | App no Facebook Developers, token, webhook com hub.challenge, resposta no Direct via graph.instagram.com e migração teste → produção | [ver](<transcricoes/Trilha Agentes IA Conversacionais - Especiali/421 - API Instagram - Agente IA Direct e Comentários/RESUMO.md>) |
| Introdução: Projeto Final da Formação \| Do Zero ao Agente de IA | 3 | Arquitetura do agente comercial (WhatsApp + n8n + Supabase + Asaas + Trello), jornada do lead e quebra em workflows | [ver](<transcricoes/Trilha Do Zero ao Agente IA/479 - Introdução- Projeto Final da Formação - Do Zero ao Agen/RESUMO.md>) |
| Conclusão: Fechamento e Desafio Final \| Do Zero ao Agente de IA | 4 | Recapitulação da arquitetura, reaplicação em outros nichos, desafio final e framework de documentação do case | [ver](<transcricoes/Trilha Do Zero ao Agente IA/482 - Conclusão- Fechamento e Desafio Final - Do Zero ao Agen/RESUMO.md>) |
| Agente IA Telegram | 3 | Bot via BotFather, fluxo mínimo Trigger → AI Agent → Send, endereçamento por chat ID, memória por conversa e adaptação do template mestre (áudio/imagem/PDF) | [ver](<transcricoes/Trilha Agentes IA Conversacionais - Especiali/420 - Agente IA Telegram/RESUMO.md>) |

### 4. Conectar a IA aos seus dados (RAG e function calling)

É o que transforma um chatbot genérico em agente que sabe do seu negócio. Dois caminhos: **RAG** (documento → base vetorial) e **function calling** (IA chama a API do seu banco).

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F5.4 - Conectando Assistente de IA aos Dados do App | 18 | O ciclo completo de function calling com dados reais: JSON da função com parâmetros tipados/enum/required e `tool_choice auto`, system prompt anti-alucinação, extração dos parâmetros em custom functions, chamada REST ao Supabase com filtros (eq/gt/lt/gte/lte e período em `created_at`) e segunda chamada à OpenAI para responder em linguagem natural | [ver](<transcricoes/Trilha Nocode IA/308 - F5.4 - Conectando Assistente de IA aos Dados do App/RESUMO.md>) |
| Converse com um PDF, Planilhas e Arquivos \| RAG (OpenAI Assistants) | 4 | Assistant da OpenAI com File Search + Vector Store: hierarquia arquivo → Vector Store → Assistant, contorno da limitação de CSV/XLSX (converter em PDF), prompt que tira markdown/citação para ficar legível no WhatsApp e troca do assistant ID no fluxo n8n + Z-API | [ver](<transcricoes/Trilha Assistants Open AI/378 - Converse com um PDF, Planilhas e Arquivos - RAG/RESUMO.md>) |
| M2 - Converse com um PDF, Planilhas e Arquivos \| RAG (Dify) | 6 | Bases de conhecimento no Dify (CSV, PDF, site via Firecrawl), fragmentação, embedding, Top K/limiar e teste de recuperação | [ver](<transcricoes/Trilha Dify/364 - M2 - Converse com um PDF, Planilhas e Arquivos - RAG/RESUMO.md>) |

### 5. Automatizar processos e hospedar a automação (n8n, Make)

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| Infraestrutura Simplificada - Hostinger | 7 | Sair do n8n Cloud: VPS serverless na Hostinger com template n8n QMode (modo fila + Redis), atualização por docker-compose e OAuth do Google Cloud | [ver](<transcricoes/_sem-trilha/509 - Infraestrutura Simplificada - Hostinger/RESUMO.md>) |
| Push Notifications com Supabase e n8n | 11 | Push no Android ponta a ponta: projeto Firebase pelo FlutterFlow, chave de conta de serviço, custom action Dart com `firebase_messaging` para pegar o token FCM, token salvo na tabela `users` do Supabase e quatro fluxos de envio no n8n (manual, agendado, segmentado e reativo via Database Webhook) | [ver](<transcricoes/Trilha FlutterFlow Geral/325 - Push Notifications com Supabase e n8n/RESUMO.md>) |
| Make \| Sua Primeira Super Automação | 5 | Automação de 3 módulos: Google Forms/Sheets (Watch New Rows) → OpenAI (Create a Completion) → Update a Row com a saída da IA | [ver](<transcricoes/Trilha Automações Make/263 - Make - Sua Primeira Super Automação/RESUMO.md>) |

### 6. Operar um agente pessoal 24/7 (OpenClaw)

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| 3.2.5 - Ferramentas Avançadas e Dicas | 4 | O dia a dia do agente: comandos de barra no Telegram (/new, /reset, /compact, /model, /context, /skill, /plugins), envio e devolução de arquivos, voz (Groq Whisper large-v3-turbo na entrada + Edge TTS na saída), roteamento de modelo por tarefa para cortar custo, auditoria dos 10 erros de segurança (chave no chat, bot aberto, dashboard sem Tailscale, agente na máquina pessoal) e evolução da personalidade via soul.md/user.md/agents.md/lessons.md | [ver](<transcricoes/_sem-trilha/581 - 3.2.5 - Ferramentas Avançadas e Dicas/RESUMO.md>) |

### 7. Construir front-end, sites e apps (Lovable, Framer)

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F3.4 - Fundamentos Websites NoCode | 9 | Site x app, tipos de site, quando precisa de CMS, comparativo WordPress/Webflow/Framer, landing e portfólio no Framer + ofertas de serviço | [ver](<transcricoes/Trilha Nocode IA/284 - F3.4 - Fundamentos Websites NoCode/RESUMO.md>) |
| Desenvolvendo Front-end e Interfaces \| Lovable | 8 | Paleta 60/30/10, grid de 8pt, hierarquia tipográfica, fluxo baixa → alta fidelidade, referência virando prompt via ChatGPT e publicação com domínio próprio | [ver](<transcricoes/Trilha Lovable/460 - Desenvolvendo Front-end e Interfaces - Lovable/RESUMO.md>) |
| Criando Plataformas com Integração API \| Lovable | 7 | App de duas telas no Lovable consumindo visão da OpenAI (foto do prato → análise nutricional), API key, billing e depuração econômica | [ver](<transcricoes/Trilha Lovable/462 - Criando Plataformas com Integração API - Lovable/RESUMO.md>) |
| Conclusão: Fechamento e Desafio Final \| Formação Lovable | 2 | Desafio final da formação: evoluir o CRM ou criar case próprio, integrando WhatsApp/Instagram/e-mail via n8n e uma API de mercado | [ver](<transcricoes/Trilha Lovable/488 - Conclusão- Fechamento e Desafio Final - Formação Lovabl/RESUMO.md>) |

### 8. Construir app / micro-SaaS no FlutterFlow

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F3.5 - Fundamentos SaaS NoCode | 11 | SaaS x MicroSaaS, arquitetura (frontend, backend, CRUD), critérios para escolher Bubble x FlutterFlow x WeWeb e Supabase x Firebase x Xano, e a primeira conexão FlutterFlow + Supabase (API URL + Anon Key alimentando uma ListView) | [ver](<transcricoes/Trilha Nocode IA/285 - F3.5 - Fundamentos SaaS NoCode/RESUMO.md>) |
| F4.2 - APIs de IA \| Seu primeiro MicroSaaS com GPT Vision | 12 | MicroSaaS de análise nutricional por foto do zero: telas responsivas, bucket público + policy no Supabase Storage para hospedar a imagem, API Call POST para o GPT-4 Turbo Vision com JSON Path, action flow com ramo de erro (Raw Body Text) e publicação como Web App + PWA | [ver](<transcricoes/Trilha Nocode IA/304 - F4.2 - APIs de IA - Seu primeiro MicroSaaS com GPT Visi/RESUMO.md>) |
| Push Notifications com Supabase e n8n | 11 | (também no grupo 5) O canal de retenção do app: token FCM salvo no Supabase e disparo orquestrado pelo n8n | [ver](<transcricoes/Trilha FlutterFlow Geral/325 - Push Notifications com Supabase e n8n/RESUMO.md>) |

### 9. Backend e banco de dados com Supabase

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| 3 - Planejamento Backend Supabase | 9 | Backend completo de um app EAD do conceito ao físico: tipos de usuário e mapa de telas, as 4 etapas de modelagem (requisitos → conceitual → lógico/DER → físico), muitos-para-muitos com tabela auxiliar, FK com no action x cascade, policies RLS para destravar a API REST, views com um e dois JOINs e bucket de Storage com upload via API | [ver](<transcricoes/Trilha Supabase/249 - 3 - Planejamento Backend Supabase/RESUMO.md>) |
| 1.2 - Extra: Use IA como seu Super Funcionário | 7 | Gerar CREATE TABLE/INSERT em português no SQL Editor, Debug with Supabase AI, modelagem completa por prompt, JOINs e popular tabelas para teste | [ver](<transcricoes/Trilha Supabase/244 - 1.2 - Extra- Use IA como seu Super Funcionário/RESUMO.md>) |

### 10. Pagamentos, checkout e assinaturas

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| Pagamentos Stripe Bubble | 18 | Única implementação real do grupo: plugin Stripe by Bubble, cobrança avulsa, cartões de teste, planos recorrentes, cancelar, upgrade/downgrade e troca de cartão | [ver](<transcricoes/Trilha Bubble Geral/231 - Pagamentos Stripe Bubble/RESUMO.md>) |
| Pagamentos Supabase + Flutterflow - Intro | 6 | Teoria de gateway, assinatura recorrente e webhook antes de cobrar num app FlutterFlow com backend Supabase; Stripe x Asaas | [ver](<transcricoes/Trilha FlutterFlow Geral/331 - Pagamentos Supabase + Flutterflow - Intro/RESUMO.md>) |
| Introdução aos Pagamentos - bubble | 5 | Cadeia completa do pagamento, critérios de escolha de gateway (Pix, parcelamento, split, antifraude) e por que webhook é obrigatório em assinatura | [ver](<transcricoes/Trilha Bubble Geral/229 - Introdução aos Pagamentos - bubble/RESUMO.md>) |
| Introdução aos Pagamentos - FlutterFlow | 4 | Caminho do dinheiro, API x webhook e por que FlutterFlow sozinho não resolve recorrência (entram Firebase/Supabase ou automação) | [ver](<transcricoes/_sem-trilha/220 - Introdução aos Pagamentos - flutterflow/RESUMO.md>) |

### 11. Gerar mídia com IA (imagem, áudio, vídeo)

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F2.3 - IA para geração de imagem | 13 | DALL·E x Stable Diffusion x Midjourney, edição de região no ChatGPT, GPT Vision, endpoints da OpenAI/Stability e 3 caminhos de rodar SD (DreamStudio, Replicate, ComfyUI local) | [ver](<transcricoes/Trilha Nocode IA/318 - F2.3 - IA para geração de imagem/RESUMO.md>) |
| F2.4 - IA para geração de áudio | 9 | Whisper x OpenAI TTS x ElevenLabs, narração PT-BR, Voice Library, clonagem de voz, marcações de pausa, dublagem e os endpoints para embutir num SaaS | [ver](<transcricoes/Trilha Nocode IA/319 - F2.4 - IA para geração de áudio/RESUMO.md>) |
| F2.5 - IA para geração de vídeo e avatar | 7 | Runway e Stable Video Diffusion via Replicate: text-to-video, animar imagem com controle de câmera, Motion Brush e video-to-video | [ver](<transcricoes/Trilha Nocode IA/320 - F2.5 - IA para geração de vídeo e avatar/RESUMO.md>) |

### 12. Planejar produto, micro-SaaS e projeto de cliente

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| F5.1 - Planejando seu Micro-SaaS | 8 | JTBD + mapa de empatia, Lean Canvas com custo real e meta de MRR, SWOT, MoSCoW para o MVP, arquitetura técnica e fluxo de assinatura com webhook | [ver](<transcricoes/Trilha Nocode IA/307 - F5.1 - Planejando seu Micro-SaaS/RESUMO.md>) |
| Introdução: Planejamento do Projeto da Formação Lovable | 6 | Planejar um CRM de leads antes do primeiro prompt: framework da NoCode Startup (visão estratégica → tendências → arquitetura técnica → criação interativa → lançamento/PDCA), escopo de V1, matriz de permissões (admin/vendedor/sem papel), benchmarking, wireframe em dois níveis, modelagem de dados e estimativa de custo/prazo | [ver](<transcricoes/Trilha Lovable/485 - Introdução- Planejamento do Projeto da Formação Lovable/RESUMO.md>) |

### 13. Onboarding, comunidade, materiais e bônus

Conteúdo administrativo, 1–2 aulas cada — consumir por necessidade, não por ordem.

| Curso | Aulas | O que entrega | RESUMO |
|---|---|---|---|
| Comece sua jornada por aqui | 1 | As três plataformas (aulas, comunidade, NoCodeMatch), canais de suporte e o método fundamentos → cases guiados → projeto real | [ver](<transcricoes/_sem-trilha/353 - Comece sua jornada por aqui/RESUMO.md>) |
| 0.1 - Comece por aqui (Agentic Builder) | 1 | Ecossistema da formação Agentic Builder: ordem das trilhas (fundamentos → Claude Code → SaaS do zero → extra), comunidade como canal de suporte, portfólio na NoCodeMatch e o investimento mínimo em assinaturas de IA antes de começar | [ver](<transcricoes/Trilha Agentic Builder Claude/535 - 0.1 - Comece por aqui/RESUMO.md>) |
| Comunidade Open No-Code \| FlutterFlow | 2 | Como usar a comunidade: quais canais existem, como escrever post de dúvida que recebe resposta (título com palavras-chave, contexto, objetivo, prints), separação dúvida técnica x comercial e as IAs especialistas de FlutterFlow e Firebase embutidas | [ver](<transcricoes/_sem-trilha/186 - Comunidade Open No-Code - FlutterFlow/RESUMO.md>) |
| Plano de Estudos - FF | 1 | Plano de 30 dias da formação FlutterFlow, com checklist no Notion e escolha entre Firebase e Supabase | [ver](<transcricoes/Trilha FlutterFlow Geral/347 - Plano de Estudos - FF/RESUMO.md>) |
| Materiais - BB | 1 | Onde ficam os materiais no Drive, os links dos editores dos apps e os canais de suporte | [ver](<transcricoes/Trilha Bubble Geral/350 - Materiais - BB/RESUMO.md>) |
| Super Bônus \| U$S100 Créditos Bubble | 1 | Como resgatar US$ 100 em créditos pela Perk Application do Bubble | [ver](<transcricoes/_sem-trilha/216 - Super Bônus - U$S100 Créditos Bubble/RESUMO.md>) |
| Atomic Fusion \| Bubble io | 1 | Extensão com templates e componentes prontos para Bubble; 1 mês liberado para alunos | [ver](<transcricoes/_sem-trilha/212 - Atomic Fusion - Bubble io/RESUMO.md>) |
| Depoimentos Formações NoCode StartUp | 1 | Recado institucional de 35s pedindo avaliação — sem conteúdo técnico, pode pular | [ver](<transcricoes/_sem-trilha/278 - Depoimentos Formações NoCode StartUp/RESUMO.md>) |

---

## Por ferramenta

Só ferramentas que aparecem em 2+ dos 48 cursos, da mais frequente para a menos.

| Ferramenta | Nº | Cursos que usam |
|---|---|---|
| OpenAI / GPT / ChatGPT | 32 | M1 Dify · M2 RAG Dify · RAG Assistants OpenAI · F5.4 Function Calling · F4.2 MicroSaaS Vision · Poder das APIs · Push Notifications · Primeira Automação WhatsApp · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · API Instagram · Agente IA Telegram · F1.4 Fundamentos IA · F1.3 Fundamentos Software · F3.1 MasterClass NoCode · F2.3 imagem · F2.4 áudio · F2.5 vídeo · F5.1 Micro-SaaS · Planejamento Lovable · Fundamentos Automações IA · Fundamentos Agentes IA · 1.1 Agentic Builder · 1.4 Fundamentos não técnicos · 3.2.5 OpenClaw · Front-end Lovable · Plataformas com API Lovable · Conclusão Lovable · IA Super Funcionário · Make Primeira Automação · Projeto Final Intro · Projeto Final Conclusão |
| Supabase | 29 | M1 Dify · RAG Assistants OpenAI · F5.4 Function Calling · F4.2 MicroSaaS Vision · F3.5 Fundamentos SaaS · Poder das APIs · Backend Supabase · Push Notifications · Primeira Automação WhatsApp · Agente IA Telegram · API Instagram · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · Fundamentos Automações IA · F1.3 · F1.4 · F3.1 MasterClass NoCode · F5.1 Micro-SaaS · Planejamento Lovable · 1.4 Fundamentos não técnicos · Front-end Lovable · Fundamentos Agentes IA · IA Super Funcionário · Pagamentos Supabase+FlutterFlow · Intro Pagamentos FlutterFlow · Projeto Final Intro · Projeto Final Conclusão · Conclusão Lovable · Plano de Estudos FF |
| n8n | 19 | M1 Dify · RAG Assistants OpenAI · Push Notifications · Poder das APIs · Primeira Automação WhatsApp · Agente IA Telegram · API Instagram · Infra Hostinger · Fundamentos Automações IA · Fundamentos Agentes IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · F1.3 · F3.1 MasterClass NoCode · Planejamento Lovable · 0.1 Comece por aqui · Projeto Final Intro · Projeto Final Conclusão · Conclusão Lovable |
| FlutterFlow | 16 | F5.4 Function Calling · F4.2 MicroSaaS Vision · F3.5 Fundamentos SaaS · Poder das APIs · Push Notifications · Backend Supabase · Comunidade Open No-Code · Intro Pagamentos FlutterFlow · Pagamentos Supabase+FlutterFlow · Plano de Estudos FF · F1.3 · F3.1 MasterClass NoCode · F5.1 Micro-SaaS · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · Materiais BB |
| Stripe | 13 | Pagamentos Stripe Bubble · Intro Pagamentos Bubble · Intro Pagamentos FlutterFlow · Pagamentos Supabase+FlutterFlow · Poder das APIs · F3.1 MasterClass NoCode · Comunidade Open No-Code · F1.3 · F5.1 Micro-SaaS · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · 1.4 Fundamentos não técnicos |
| Asaas | 11 | Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · Fundamentos Automações IA · F1.3 · 1.4 Fundamentos não técnicos · Pagamentos Supabase+FlutterFlow · Intro Pagamentos FlutterFlow · Intro Pagamentos Bubble · Projeto Final Intro · Projeto Final Conclusão · Conclusão Lovable |
| Bubble | 11 | Pagamentos Stripe Bubble · Intro Pagamentos Bubble · Bônus US$100 Bubble · Atomic Fusion · Materiais BB · F3.5 Fundamentos SaaS · F3.1 MasterClass NoCode · Backend Supabase · F1.3 · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Make | 11 | Make Primeira Automação · F3.5 Fundamentos SaaS · Poder das APIs · F3.1 MasterClass NoCode · Pagamentos Supabase+FlutterFlow · Intro Pagamentos FlutterFlow · F1.3 · F5.1 Micro-SaaS · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| WhatsApp (como canal) | 11 | M1 Dify · RAG Assistants OpenAI · Primeira Automação WhatsApp · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · Fundamentos Automações IA · F5.1 Micro-SaaS · 1.4 Fundamentos não técnicos · Projeto Final Intro · Projeto Final Conclusão · Conclusão Lovable |
| Claude (Anthropic) | 9 | F1.4 · F3.1 MasterClass NoCode · 0.1 Comece por aqui · Fundamentos Agentes IA · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · 1.4 Fundamentos não técnicos · Projeto Final Conclusão |
| Gemini (Google) | 9 | F1.3 · F1.4 · F3.1 MasterClass NoCode · 3.2.5 OpenClaw (Gemini Live) · Fundamentos Agentes IA · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) · 1.4 Fundamentos não técnicos |
| Firebase | 8 | Push Notifications (FCM) · F3.5 Fundamentos SaaS · Poder das APIs · F3.1 MasterClass NoCode · Comunidade Open No-Code · Intro Pagamentos FlutterFlow · Fundamentos Agentes IA · Plano de Estudos FF |
| Redis | 7 | API Instagram · Infra Hostinger · RAG Assistants OpenAI · F1.4 · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Framer | 7 | F3.4 Websites NoCode · F3.5 Fundamentos SaaS · F3.1 MasterClass NoCode · Front-end Lovable · Pagamentos Supabase+FlutterFlow · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Z-API / Mega API / Evolution API | 7 | M1 Dify · RAG Assistants OpenAI · Planejamento Lovable · Primeira Automação WhatsApp · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Lovable | 6 | Front-end Lovable · Plataformas com API Lovable · Conclusão Lovable · Planejamento Lovable · Fundamentos Projetos (Lovable) · Fundamentos Projetos IA |
| Postgres / PostgreSQL / SQL | 6 | Backend Supabase · F3.5 Fundamentos SaaS · IA Super Funcionário · Fundamentos Agentes IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Google Sheets | 6 | Make Primeira Automação · F5.4 Function Calling · F3.1 MasterClass NoCode · Infra Hostinger · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Miro | 6 | Backend Supabase · Planejamento Lovable · F1.3 · F5.1 Micro-SaaS · Front-end Lovable · Projeto Final Intro |
| Dify | 5 | M1 Dify · M2 RAG Dify · F3.1 MasterClass NoCode · Fundamentos Automações IA · Fundamentos Agentes IA |
| Zapier | 5 | F3.1 MasterClass NoCode · Intro Pagamentos FlutterFlow · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| PokéAPI (API de treino) | 5 | Poder das APIs · F1.3 · Fundamentos Automações IA · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Notion | 5 | 3.2.5 OpenClaw · Planejamento Lovable · Front-end Lovable · Plano de Estudos FF · Projeto Final Conclusão |
| Postman | 4 | Poder das APIs · Backend Supabase · F1.3 · Fundamentos Automações IA |
| Mercado Pago | 4 | Intro Pagamentos Bubble · Intro Pagamentos FlutterFlow · F1.3 · 1.4 Fundamentos não técnicos |
| Llama | 4 | F1.4 · Fundamentos Agentes IA · Fundamentos Automações IA · 1.4 Fundamentos não técnicos |
| Dribbble | 4 | Planejamento Lovable · F1.3 · F5.1 Micro-SaaS · Front-end Lovable |
| Behance | 4 | Planejamento Lovable · F1.3 · F5.1 Micro-SaaS · Front-end Lovable |
| Webflow | 4 | F3.4 Websites NoCode · F3.1 MasterClass NoCode · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Google Drive | 4 | F5.4 Function Calling · Materiais BB · Infra Hostinger · Intro Pagamentos Bubble |
| Tally | 4 | Planejamento Lovable · Conclusão Lovable · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| WeWeb | 3 | F3.5 Fundamentos SaaS · F3.1 MasterClass NoCode · Backend Supabase |
| Xano | 3 | F3.5 Fundamentos SaaS · F3.1 MasterClass NoCode · Poder das APIs |
| Claude Code | 3 | 1.1 Agentic Builder · 1.4 Fundamentos não técnicos · 0.1 Comece por aqui |
| GitHub | 3 | F2.5 vídeo · 1.4 Fundamentos não técnicos · 0.1 Comece por aqui |
| Pinecone | 3 | F1.4 · Fundamentos Agentes IA · RAG Assistants OpenAI |
| Mistral AI | 3 | F1.4 · Fundamentos Agentes IA · 3.2.5 OpenClaw |
| ElevenLabs | 3 | F2.4 áudio · Fundamentos Agentes IA · 3.2.5 OpenClaw |
| Whisper (OpenAI/Groq/local) | 3 | F2.4 áudio · Fundamentos Agentes IA · 3.2.5 OpenClaw |
| TTS (OpenAI / Edge TTS) | 3 | F2.4 áudio · Fundamentos Agentes IA · 3.2.5 OpenClaw |
| WordPress | 3 | F3.4 Websites NoCode · F3.1 MasterClass NoCode · Fundamentos Projetos (Lovable) |
| Airtable | 3 | F3.1 MasterClass NoCode · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Replit | 3 | Planejamento Lovable · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Google Docs | 3 | F5.4 Function Calling · Materiais BB · Intro Pagamentos Bubble |
| Railway | 3 | M1 Dify · Infra Hostinger · Fundamentos Automações IA |
| Hostinger | 3 | Infra Hostinger · Front-end Lovable (domínio) · 1.4 Fundamentos não técnicos |
| Pagar.me | 3 | Intro Pagamentos Bubble · F1.3 · 1.4 Fundamentos não técnicos |
| Figma | 3 | F1.3 · F3.4 Websites NoCode · F5.1 Micro-SaaS |
| Cursor | 3 | 1.4 Fundamentos não técnicos · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Grok | 3 | F1.4 · Fundamentos Agentes IA · 1.4 Fundamentos não técnicos |
| DALL·E | 3 | F2.3 imagem · F2.5 vídeo · Fundamentos Agentes IA |
| Stable Diffusion / Stability AI | 3 | F2.3 imagem · F2.5 vídeo · Fundamentos Agentes IA |
| Sora | 3 | F2.4 áudio · F2.5 vídeo · Fundamentos Agentes IA |
| Google Calendar | 3 | Infra Hostinger · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Gmail | 3 | Infra Hostinger · Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| LinkedIn | 3 | Projeto Final Conclusão · Conclusão Lovable · Fundamentos Projetos (Lovable) |
| Softr | 2 | F3.5 Fundamentos SaaS · F3.1 MasterClass NoCode |
| Dart / Flutter | 2 | F3.5 Fundamentos SaaS · Push Notifications |
| Telegram | 2 | Agente IA Telegram · 3.2.5 OpenClaw |
| Google Cloud | 2 | Push Notifications (conta de serviço) · Infra Hostinger (OAuth) |
| Wix | 2 | F3.1 MasterClass NoCode · Fundamentos Projetos (Lovable) |
| Carrd | 2 | F3.1 MasterClass NoCode · Fundamentos Projetos (Lovable) |
| Trello | 2 | Projeto Final Intro · Projeto Final Conclusão |
| Replicate | 2 | F2.3 imagem · F2.5 vídeo |
| Midjourney | 2 | F2.3 imagem · Fundamentos Agentes IA |
| Leonardo AI | 2 | F2.3 imagem · Fundamentos Agentes IA |
| Runway | 2 | F2.5 vídeo · Fundamentos Agentes IA |
| Pika Labs | 2 | F2.5 vídeo · Fundamentos Agentes IA |
| Langflow | 2 | Fundamentos Automações IA · Fundamentos Agentes IA |
| DigitalOcean | 2 | Infra Hostinger · Fundamentos Automações IA |
| Hetzner | 2 | Infra Hostinger · Fundamentos Automações IA |
| v0 | 2 | Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| Windsurf | 2 | Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| SerpAPI | 2 | Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| ActiveCampaign | 2 | Fundamentos Projetos IA · Fundamentos Projetos (Lovable) |
| PayPal | 2 | Intro Pagamentos Bubble · Intro Pagamentos FlutterFlow |
| Yuno / Juno | 2 | Intro Pagamentos Bubble · Intro Pagamentos FlutterFlow |

---

## Sobreposição

O catálogo repete muito fundamento. Onde escolher um e pular os outros:

**1. `Fundamentos Essenciais - Projetos IA` (450) x `Fundamentos Essenciais ... | Lovable` (459)**
São o mesmo curso, 11 aulas cada, mesmos outcomes (front/back, 4 categorias de projeto, anatomia de agente, API x webhook, prompt, monetização). Diferença: a lista de ferramentas do 459 puxa mais para front (Wix, Carrd, NoCode Match). **Assista um só** — 450 se o destino é agente/n8n, 459 se o destino é Lovable.

**2. Escolha de ferramenta e categoria de projeto — 283 (F3.1) x 450/459 x 285 (F3.5)**
283 é o **mapa mais completo** (7 categorias, ~40 ferramentas, critérios de avaliação, arquitetura de SaaS, monetização) — use como panorama antes de fechar stack. 450/459 dizem a mesma coisa em 4 categorias, dentro de outra formação. 285 só repete a parte de SaaS, mas **acrescenta o que os outros não têm: a conexão prática FlutterFlow + Supabase**. Panorama: 283. Mão na massa: 285.

**3. Teoria de API x webhook — aparece em 9 cursos**
314, 368, 450, 459, 538, 331, 220, 229 e 276 ensinam a mesma coisa. **Use 314 (F1.3)** se o objetivo é software/app: é o mais completo em teoria. **Use 368** se o objetivo é automação: acrescenta as 4 camadas e o cURL indo direto pro n8n. **Use 276 (O Poder das APIs)** se o objetivo é *executar* — é o único que monta a chamada de verdade (variável dinâmica, JSON Path salvo, ramo de erro, proteção de chave via Cloud Function). Nos outros, pule a parte de API.

**4. Micro-SaaS "foto do prato → análise nutricional" — 304 (FlutterFlow) x 462 (Lovable)**
É **o mesmo projeto em duas ferramentas**: GPT Vision analisando a foto. 304 é mais completo (12 aulas: Supabase Storage com bucket e policy, action flow com tratamento de erro, publicação Web App + PWA); 462 (7 aulas) chega ao mesmo resultado com prompt no Lovable. **Escolha pela stack de destino** — não faça os dois.

**5. RAG — 378 (OpenAI Assistants) x 364 (Dify)**
Mesmo objetivo: dar conhecimento próprio ao agente. 378 usa File Search + Vector Store da própria OpenAI e é o caminho mais curto se o fluxo já é n8n + Z-API (troca só o assistant ID). 364 dá mais controle sobre o retrieval (fragmentação, Top K, limiar) e aceita site via Firecrawl. **Se já usa OpenAI no n8n, vá de 378**; se quer entender e ajustar a recuperação, 364. Ambos esbarram na mesma limitação: planilha precisa virar PDF.

**6. RAG x function calling — 378/364 x 308**
Não são alternativas, são problemas diferentes. **RAG** responde sobre *documento estático* (manual, política, catálogo em PDF). **Function calling (308)** responde sobre *dado vivo do banco* ("quanto gastei em março"), porque a IA extrai parâmetros e vira filtro de API no Supabase. Se a pergunta muda com o banco, é 308 — nenhum outro curso transcrito implementa esse ciclo.

**7. Fundamentos de IA — 315 (F1.4) x 367 (Fundamentos de Agentes IA)**
367 é a versão condensada (5 aulas) de 315 (11 aulas) + o que separa agente de chatbot. **Comece por 315** (tokenização, embedding, fine-tuning x RAG, custo por token) e use **367 só para o final**: fluxo de RAG e function calling. 538 repete o raciocínio de custo em tokens numa lente não técnica.

**8. Panorama de mídia por IA**
367 lista todas as ferramentas de imagem/áudio/vídeo em panorama; 318, 319 e 320 são mão na massa. **Use 367 como mapa** e vá para o F2.x correspondente só quando o projeto precisar do output. Para voz *dentro de um agente rodando* (STT na entrada, TTS na saída, custo por modelo), o material é 581 — não os F2.x.

**9. Agentes conversacionais por canal — 374 (WhatsApp) x 420 (Telegram) x 421 (Instagram)**
374 (14 aulas) constrói o esqueleto completo; 420 (3 aulas) e 421 (10 aulas) apenas trocam o trigger e o envio sobre o mesmo "template mestre". **Faça 374 primeiro** — sem ele, 420 e 421 não fazem sentido. 421 é o mais trabalhoso dos canais por causa do app na Meta e do token.

**10. Dify (351/364) x n8n AI Agent (374/420/421)**
Dois caminhos para o mesmo resultado (agente com memória e conhecimento próprio). **Dify entrega RAG pronto** com menos montagem; **n8n entrega controle e integrações** (Supabase, Asaas, Trello, roteamento por tipo de mídia). Escolha um; se for pelo n8n, ainda vale ver 364 pelo raciocínio de fragmentação e recuperação.

**11. Modelagem de banco no Supabase — 249 x 244 x 314**
314 dá a teoria (1-N, N-N). **249 é o curso completo de backend**: as 4 etapas de modelagem, FK pela UI com no action x cascade, RLS destravando a API REST, views com JOIN e bucket de Storage — faça este. **244 é acelerador, não substituto**: gera o SQL por prompt em português. Ideal: entender em 249, executar rápido com 244.

**12. Planejamento de projeto — 307 (F5.1) x 485 (Lovable)**
307 é o lado **negócio** (JTBD, mapa de empatia, Lean Canvas, meta de MRR, SWOT, MoSCoW) — use quando o app vira produto pago. 485 é o lado **execução** (visão estratégica, permissões por perfil, benchmarking, wireframe, modelagem, custo e prazo) — use quando vai construir com IA e o prompt precisa de contexto concreto. Complementares: 485 antes de prompt, 307 antes de cobrar.

**13. Introduções de pagamento — 220 (FlutterFlow), 229 (Bubble), 331 (Supabase+FlutterFlow)**
Os três ensinam a mesma teoria (cadeia do pagamento, escolha de gateway, webhook para recorrência) trocando só a ferramenta de destino. **Veja 229** (o mais completo dos três) e vá direto para a implementação. **A única implementação real transcrita é `Pagamentos Stripe Bubble` (231, 18 aulas)**.

**14. Prompt de agente (persona, objetivo, exemplos, restrições, passos, formato)**
Idêntico em 450, 459 e 368; 308 e 378 mostram a versão aplicada (system prompt anti-alucinação com lista fechada e prompt que limpa markdown para WhatsApp). Veja a teoria uma vez, depois só os aplicados.

**15. Onboarding e bônus (353, 535, 186, 350, 347, 216, 212, 278)**
1–2 aulas cada, conteúdo administrativo. **353** e **535** são o mesmo tipo de aula (plataformas, comunidade, NoCodeMatch, suporte) em formações diferentes — veja um. **186** é o único com conteúdo útil de verdade: como escrever post que recebe resposta e as IAs especialistas de FlutterFlow/Firebase. **278 pode ser pulado**.

---

## Sugestão de ordem de estudo

Rota enxuta para sair construindo agentes de IA e apps, usando só o que já está transcrito.

**Base conceitual (não pule, mas não repita)**
1. `F3.1 - Introdução da Trilha | MasterClass NoCode` (283) — o mapa: classificar o projeto e escolher a stack antes de tudo.
2. `F1.3 - Fundamentos Desenvolvimento de Software` (314) — arquitetura, API, webhook, modelagem de banco.
3. `F1.4 - Fundamentos Inteligência Artificial` (315) — token, embedding, RAG x fine-tuning, custo.
4. `Fundamentos de Automações IA` (368) — as 4 camadas do projeto e o cURL indo pro n8n.
5. `Fundamentos Essenciais - Projetos IA` (450) — fecha prompt de agente e monetização. *(pule 459, 538, 367 aqui — são repetição)*

**Primeiro agente funcionando**
6. `Sua Primeira Automação - Agente IA no Whatsapp` (374) — o esqueleto reaproveitável. É o curso mais importante da lista.
7. `3 - Planejamento Backend Supabase` (249) — modelar o banco direito: FK, RLS, views com JOIN, Storage.
8. `1.2 - Extra: Use IA como seu Super Funcionário` (244) — acelerar o mesmo trabalho por prompt.
9. `Converse com um PDF... | RAG` (378) — conhecimento próprio no agente via Assistants + Vector Store. *(se for pelo Dify, veja 351 e 364)*

**Expandir canais e virar projeto de verdade**
10. `Agente IA Telegram` (420) — canal novo em 3 aulas, prova que o template se replica.
11. `API Instagram - Agente IA Direct e Comentários` (421) — o canal mais burocrático (Meta, token, webhook).
12. `Introdução: Projeto Final` (479) → `Conclusão: Desafio Final` (482) — agente comercial com Asaas, Trello, follow-up e fallback humano; sai case de portfólio.
13. `Infraestrutura Simplificada - Hostinger` (509) — tirar do n8n Cloud e rodar em modo fila com Redis.
14. `3.2.5 - Ferramentas Avançadas e Dicas` (581) — operar o agente no dia a dia: voz, roteamento de modelo por custo e auditoria de segurança. Feche o ciclo aqui antes de colocar em cliente.

**Quando o projeto virar app com interface**
15. `1 - O Poder das APIs` (276) — a chamada de API montada de verdade dentro do FlutterFlow, com proteção de chave.
16. `F3.5 - Fundamentos SaaS NoCode` (285) — SaaS x MicroSaaS e a primeira conexão FlutterFlow + Supabase.
17. `F4.2 - Seu primeiro MicroSaaS com GPT Vision` (304) — MicroSaaS completo com Storage, IA e publicação em PWA. *(se a stack for Lovable, troque 285+304 por 460 + 462)*
18. `F5.4 - Conectando Assistente de IA aos Dados do App` (308) — o salto: a IA consultando o banco por function calling. Requer 276 e 249 antes.
19. `Push Notifications com Supabase e n8n` (325) — retenção: token FCM no Supabase e envio orquestrado no n8n.

**Antes de vender / cobrar**
20. `Introdução: Planejamento do Projeto` (485) — planejar o app (permissões, wireframe, modelagem, custo e prazo) antes do primeiro prompt.
21. `F5.1 - Planejando seu Micro-SaaS` (307) — JTBD, Lean Canvas, meta de MRR e MoSCoW.
22. `Introdução aos Pagamentos - bubble` (229) — teoria de gateway e recorrência (vale para qualquer stack).
23. `Pagamentos Stripe Bubble` (231) — a implementação completa: avulso, assinatura, cancelamento, upgrade, troca de cartão. Se sua stack é FlutterFlow, veja 331/220 no lugar da teoria.

**Sob demanda**
- `F3.4 - Fundamentos Websites NoCode` (284) + `Front-end Lovable` (460) — quando o entregável for site/interface.
- `Make | Sua Primeira Super Automação` (263) — só se o cliente já usa Make.
- `F2.3` (318) / `F2.4` (319) / `F2.5` (320) — quando o projeto pedir imagem, áudio ou vídeo.
- `1.1 - O Profissional Agentic Builder` (537) + `1.4 - Fundamentos (Para Não Técnicos)` (538) + `0.1 - Comece por aqui` (535) — se quiser migrar de no-code para Claude Code e orquestração de agentes.
- `Comunidade Open No-Code` (186) — quando travar: como perguntar direito e usar as IAs especialistas.
