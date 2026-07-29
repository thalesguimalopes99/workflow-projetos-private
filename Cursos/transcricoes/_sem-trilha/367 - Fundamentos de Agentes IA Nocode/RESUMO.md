# Fundamentos de Agentes IA Nocode

(sem trilha) | 5 aulas | ~00:19:06 (0,32h) | nivel iniciante

> Aulas teoricas de nivelamento que explicam o vocabulario por tras de agentes de IA: onde a IA generativa se encaixa, quais sao os LLMs relevantes, como funcionam tokenizacao/embedding/bancos vetoriais, o que e RAG e o que diferencia um agente de um chatbot.

## O que voce sai sabendo fazer

- Situar IA generativa e LLM dentro do mapa IA > machine learning > deep learning, e escolher o **modelo** em vez de se perder na enxurrada de **ferramentas**.
- Escolher entre modelos proprietarios (GPT, Gemini, Claude) e open source (Llama, Mistral, Grok) sabendo o trade-off de hospedar por conta propria.
- Explicar o caminho texto -> tokens -> vetores -> banco vetorial e por que a busca por similaridade e rapida e escalavel.
- Decidir qual tipo de banco usar em cada caso: relacional (Postgres/Supabase), nao relacional (MongoDB/Firebase) ou vetorial (Pinecone, Supabase com vetores, banco nativo da plataforma).
- Desenhar mentalmente um fluxo de RAG (treinar o agente com PDF/planilha) e um fluxo de function calling (agente aciona API externa e devolve resposta estruturada).
- Diferenciar agente de IA de chatbot tradicional e justificar quando cada um cabe.

## Stack e ferramentas

Citados ao longo das aulas (a maior parte como referencia conceitual, sem hands-on nestas 5 aulas):

- **Modelos de texto/chat:** GPT (OpenAI), Gemini (Google), Claude (Anthropic), Llama, Mistral AI, Grok — o curso adota GPT como padrao por praticidade.
- **Modelos de imagem:** DALL-E, Stable Diffusion, Midjourney.
- **Audio:** OpenAI Text-to-Speech, OpenAI Whisper, ElevenLabs.
- **Video:** Sora, Runway, Pika Labs, Stable Diffusion.
- **Ferramentas de IA (interface, nao modelo):** ChatGPT, Jasper, Copy.ai, Leonardo AI, Notion AI.
- **Plataformas de agente/fluxo:** n8n, Dify, Langflow (multimodelo — voce escolhe o LLM).
- **Chatbots tradicionais:** Typebot, ManyChat, Botpress, Voiceflow.
- **Bancos de dados:** PostgreSQL, MySQL, Supabase (BaaS sobre Postgres), MongoDB, Firebase (BaaS), Pinecone e demais bancos vetoriais; Supabase tambem suporta vetores.
- **Tokenizacao/embedding:** tokenizer da OpenAI (demo no navegador) e modelo de embedding da OpenAI (text-embedding-3-small).

## Pre-requisitos

Nenhum formal — as aulas partem do zero conceitual. O instrutor assume que voce esta seguindo a formacao na ordem e ja passou pelos fundamentos de automacao; ele tambem indica a formacao de SaaS com IA para quem quiser aprofundar imagem/audio/video.

## Aula a aula

### 1 - O que voce vai aprender  (00:00:53)
- **Resumo:** Abertura do modulo. Lista os tres blocos teoricos que serao cobertos — modelos e LLMs, embeddings e bancos vetoriais, fundamentos de agentes — e explica que esta e a parte conceitual antes da pratica.
- **Pontos-chave:**
  - Recomenda assistir na ordem, porque os conceitos se encadeiam.
  - A promessa e sair com base suficiente para tocar um projeto sozinho e voltar a aulas especificas quando travar.
  - Menciona acesso a comunidade da formacao.
- **Link:** https://flix.nocodestartup.io/m/lessons/3827

### 2 - IA, LLM e Melhores Modelos  (00:05:21)
- **Resumo:** Desenha o encaixe dos campos: IA contem machine learning, que contem deep learning, que contem a IA generativa. A partir dai define LLM como modelo de deep learning treinado em larga escala para lidar com linguagem natural, e apresenta o panorama de modelos por modalidade. Fecha com a distincao central entre ferramenta e modelo.
- **Pontos-chave:**
  - ChatGPT e **interface**; o modelo se chama GPT. Nao confunda os dois.
  - Modelos proprietarios de referencia: GPT (OpenAI/Microsoft), Gemini (Google), Claude (Anthropic/Amazon).
  - Open source: Llama, Mistral, Grok — dificil rodar em maquina propria, exige hardware pesado.
  - Quatro frentes generativas: texto/chat, imagem, audio, video — cada uma com seus modelos de ponta.
  - Nao caca a "melhor ferramenta": olhe o modelo por tras dela. n8n e Dify aceitam multiplos modelos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3826

### 3 - Tokenizacao e Embedding  (00:04:10)
- **Resumo:** Explica que o computador so opera com numeros, entao o texto e quebrado em tokens, cada um com ID unico. Demonstra no tokenizer da OpenAI como uma frase curta vira uma lista de numeros. Em seguida introduz embedding como representacao vetorial em espaco multidimensional, onde termos semanticamente proximos ficam agrupados.
- **Pontos-chave:**
  - Token nao e palavra: uma palavra pode ser fatiada em varios pedacos ("form" + "acao").
  - Na demo do tokenizer, uma frase curta da formacao resulta em 11 tokens e 42 caracteres.
  - O grafico 2D (animais, moveis, frutas agrupados) e so didatico — embeddings reais tem entre 512 e 4096 dimensoes.
  - O LLM resolve ambiguidade pelo contexto (exemplo: "banco" como movel vs. instituicao).
  - Qualquer midia — texto, audio, video — pode ser vetorizada; na OpenAI isso passa pelo modelo de embedding (text-embedding-3-small).
- **Link:** https://flix.nocodestartup.io/m/lessons/3829

### 4 - Bancos de Dados Vetoriais  (00:03:57)
- **Resumo:** Compara os tres tipos de banco (relacional, nao relacional, vetorial) e explica por que o vetorial e o padrao em aplicacoes de IA: indexacao eficiente, consulta por proximidade e escalabilidade. Termina apresentando RAG como a tecnica que conecta o agente a documentos proprios.
- **Pontos-chave:**
  - Relacional = tabelas e relacoes (PostgreSQL, MySQL); Supabase e um BaaS sobre Postgres, com auth, storage e seguranca alem do banco.
  - Nao relacional = colecoes e documentos flexiveis (MongoDB, Firebase).
  - Vetorial = embeddings; Pinecone e citado, e o Supabase tambem pode virar banco vetorial. Dify ja traz banco vetorial nativo.
  - Escolha do curso: Supabase para o relacional, banco vetorial nativo da plataforma de agente para os embeddings.
  - RAG = Retrieval Augmented Generation: a consulta busca no banco vetorial antes de o modelo responder, permitindo treinar o agente com PDF e planilha.
- **Link:** https://flix.nocodestartup.io/m/lessons/3828

### 5 - Fundamentos Agentes IA  (00:04:45)
- **Resumo:** Fecha o modulo mostrando as duas capacidades que tornam um agente poderoso: RAG (conhecimento externo) e function calling (acionar APIs). Detalha o fluxo completo de uma chamada de funcao e lista os componentes de um agente. Encerra contrastando agente e chatbot.
- **Pontos-chave:**
  - Categorias de projeto nocode: SaaS/apps, automacoes, websites (front-end) e agentes de IA.
  - Fluxo de function calling: prompt -> LLM decide se precisa de funcao -> monta request estruturado -> API responde -> resposta devolvida em linguagem natural. Exemplo dado: consultar gasto de uma categoria em um mes especifico no banco de dados.
  - Anatomia do agente: modelo + prompt base + memoria (curto e longo prazo, para retomar conversas em outro dia) + RAG + tools.
  - Tools tipicas: enviar WhatsApp, enviar e-mail, consultar clima, buscar no Google, ler/criar registros no banco.
  - Agente conversa em linguagem natural e raciocina; chatbot segue script e botoes. Typebot, ManyChat, Botpress e Voiceflow ficam do lado chatbot (com integracao a IA); n8n, Dify e Langflow do lado agente.
- **Link:** https://flix.nocodestartup.io/m/lessons/3830

## Pegadinhas e insights

- **Ferramenta != modelo.** O erro mais repetido pelo instrutor: gente que fica cacando "a melhor ferramenta de IA" quando o que decide a qualidade e o modelo por tras. Jasper, Copy.ai, Notion AI, Leonardo e o proprio ChatGPT sao camadas de interface.
- **ChatGPT nao e o nome do modelo.** GPT e o modelo; ChatGPT e a interface da OpenAI sobre ele.
- **Open source nao roda na sua maquina.** O instrutor desaconselha auto-hospedagem de LLM: exige supercomputador ou VM cara, e os modelos pagos so ficam mais baratos com o tempo.
- **Token nao e palavra.** Uma unica palavra pode consumir varios tokens — impacta direto custo e limite de contexto.
- **Grafico 2D de embedding e ficcao didatica.** Na pratica sao 512 a 4096 dimensoes; nao pense em "duas coordenadas".
- **Supabase entra por dois motivos diferentes.** No curso ele e usado como banco relacional/BaaS, nao como banco vetorial — mesmo tendo suporte a vetores. O vetorial fica com Pinecone ou o banco nativo do Dify.
- **A escolha de GPT no curso e por praticidade, nao por dogma.** Como n8n, Dify e Langflow sao multimodelo, da para trocar o LLM sem refazer o fluxo.
- **Chatbot com IA nao vira agente.** Roteiro com botoes e resposta pre-definida continua sendo chatbot; agente pressupoe linguagem natural, memoria e capacidade de acionar funcoes.
- Estas 5 aulas sao 100% teoricas — a pratica (RAG e function calling no n8n e no Dify) e prometida para modulos posteriores da formacao.
