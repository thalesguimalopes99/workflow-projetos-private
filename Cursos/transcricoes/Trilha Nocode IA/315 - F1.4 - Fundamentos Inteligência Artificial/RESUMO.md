# F1.4 - Fundamentos Inteligência Artificial

Trilha Nocode IA | 11 aulas | ~40 min (00:39:49) | nível iniciante

> Curso conceitual que organiza o vocabulário de IA — IA → Machine Learning → Deep Learning → IA generativa → LLMs — e explica os mecanismos práticos por trás dos modelos: tokenização, embeddings, bancos vetoriais, fine-tuning, RAG e function calling.

## O que você sai sabendo fazer

- Situar corretamente qualquer termo de IA dentro da hierarquia IA ⊃ Machine Learning ⊃ Deep Learning ⊃ IA generativa ⊃ LLMs.
- Distinguir aprendizado supervisionado, não supervisionado e por reforço, e reconhecer qual problema cada um resolve.
- Explicar por que texto vira número: tokenização (token → ID) e embedding (token → vetor multidimensional).
- Estimar custo e limite de contexto de um modelo raciocinando em tokens, usando o tokenizador da OpenAI.
- Escolher entre fine-tuning e RAG quando precisar de um modelo que conheça dados próprios/específicos.
- Identificar quando um banco de dados vetorial é necessário e quais opções existem (pagas e open source).
- Reconhecer os principais LLMs do mercado, quem está por trás de cada um, e quais são open source (rodáveis localmente, sem custo de API).

## Stack e ferramentas

- **Modelos proprietários:** GPT (OpenAI, investida pela Microsoft), Gemini (Google), Claude (Anthropic, tendo a Amazon como principal investidora).
- **Modelos open source:** Llama 2 (Meta), Grok, Mistral AI.
- **Tokenizador da OpenAI** (ferramenta web) — visualizar contagem de tokens, caracteres e IDs de token.
- **API de embeddings da OpenAI** — passar um input de texto e receber o vetor.
- **Bancos de dados vetoriais:** Pinecone, Redis; open source: Qdrant, Milvus; e Supabase (backend com opção vetorial, usado ao longo da formação).
- **Chatbase** — ferramenta usada pela NoCode StartUp para montar RAG em cima de documentação.
- **Function calling** (OpenAI) — chamar APIs externas a partir do modelo.

## Pré-requisitos

Nenhum pré-requisito técnico. O instrutor posiciona o curso como a terceira perna da "tríade" da formação, depois das aulas de desenvolvimento de produtos e de fundamentos de software/SaaS NoCode — mas o conteúdo é autossuficiente.

## Aula a aula

### Intro / 001 - Fundamentos Ia  (00:02:00)
- **Resumo:** Abertura do módulo, apresentando o que será coberto e por que o instrutor considera essas aulas as mais importantes da formação. Ele contextualiza o curso como a terceira parte da tríade "desenvolvimento de produtos + SaaS NoCode + IA/agentes". O objetivo declarado é dar vocabulário para a pessoa parar de se perder entre tantos conceitos, ferramentas e modelos.
- **Pontos-chave:**
  - Roteiro do módulo: definições de IA, machine learning e deep learning; características dos LLMs; conceitos práticos (embedding, tokens).
  - Aviso: o módulo pode parecer difícil, mas basta captar o desenho geral para seguir adiante.
- **Link:** https://flix.nocodestartup.io/m/lessons/3170

### Fundamentos IA / 001 - Inteligência Artificial  (00:02:13)
- **Resumo:** Define IA como teoria e métodos para criar máquinas que pensam e agem como humanos, e apresenta o diagrama de círculos concêntricos que estrutura o curso inteiro. Mostra que machine learning é uma das áreas da IA, deep learning é uma subárea de ML, e as IAs generativas moram dentro de deep learning. Também lista as demais áreas de estudo da IA que o curso não vai aprofundar.
- **Pontos-chave:**
  - Hierarquia: IA ⊃ Machine Learning ⊃ Deep Learning ⊃ IA generativa (onde está o ChatGPT).
  - Machine Learning = habilidade da máquina aprender com os dados.
  - Deep Learning = redes neurais imitando o cérebro humano.
  - Outras áreas da IA citadas: processamento de linguagem natural, visão computacional, robótica, sistemas de recomendação, AGI.
- **Link:** https://flix.nocodestartup.io/m/lessons/3171

### Fundamentos IA / 002 - Machine Learning  (00:04:20)
- **Resumo:** Detalha os três tipos de aprendizado de máquina com exemplos visuais simples. O supervisionado é ilustrado com gorjeta versus valor da conta (dados rotulados por delivery ou consumo no restaurante) para prever o valor de uma nova gorjeta. O não supervisionado aparece como agrupamento de funcionários por salário e tempo de empresa, sem rótulo. O por reforço é apresentado como agente interagindo com ambiente via ações, recompensas e observações.
- **Pontos-chave:**
  - Supervisionado: dados rotulados; objetivo é prever resultado futuro a partir de dados passados (modelo preditivo).
  - Não supervisionado: sem rótulo; objetivo é descobrir padrões e organizar em grupos (clusters).
  - Por reforço: aprende por tentativa e erro, guiado por recompensa.
- **Link:** https://flix.nocodestartup.io/m/lessons/3172

### Fundamentos IA / 003 - Deep Learning  (00:04:49)
- **Resumo:** Explica redes neurais no nível mais básico: camada de input, nós intermediários com pesos e camada de output com probabilidades. Usa a classificação de foto de cachorro/pássaro/gato como exemplo — cada nó carrega uma "pergunta" ponderada (tem focinho, tem bico, tem asas) até chegar numa probabilidade final. Fecha diferenciando IA discriminativa (classifica/prediz) de IA generativa (cria dados novos parecidos com os de treino).
- **Pontos-chave:**
  - Estrutura: input layer → camadas de cálculo (nós com pesos) → output com probabilidades.
  - Números citados para o modelo da OpenAI/ChatGPT: ~175 bilhões de parâmetros e 96 camadas.
  - Caixa-preta: só se enxerga input e saída; o que acontece nas camadas internas não é conhecido.
  - Discriminativa = classificação treinada com dados rotulados; generativa = gera um cachorro novo, com outras características, a partir de milhares de exemplos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3173

### Fundamentos IA / 004 - Ias Generativas  (00:04:11)
- **Resumo:** Recapitula a hierarquia e foca no funcionamento das IAs generativas: dados (rotulados ou não) → treino do modelo → geração de conteúdo novo. Diferencia modelo (o que a OpenAI criou) de interface (o ChatGPT). Mapeia a matriz de combinações input→output e o leque de aplicações práticas monetizáveis.
- **Pontos-chave:**
  - Nomenclatura padrão: text-to-text, text-to-image, text-to-video, image-to-text, image-to-video, image-to-image.
  - De um input de texto saem tradução, resumo, resposta, correção gramatical, imagem, vídeo, áudio, até decisões.
  - De um input de imagem saem texto, busca dentro da imagem, upscale/completação, animação.
  - Aplicações citadas: texto para marketing/vendas/suporte, código e documentação, SQL, apps, imagens para social e design, voz, vídeo, 3D, jogos, música.
- **Link:** https://flix.nocodestartup.io/m/lessons/3174

### LLM / 001 - Large Language Models  (00:05:24)
- **Resumo:** Define LLM como modelo de deep learning treinado com grande volume de dados para compreender, gerar e interagir em linguagem natural em escala. Lista os problemas que resolve, as características do modelo (tamanho, parâmetros, restrição de fontes, fine-tuning) e os benefícios de reaproveitar um mesmo modelo em domínios diferentes. Encerra mapeando o mercado: quem é dono/investidor de cada modelo e quais são open source.
- **Pontos-chave:**
  - Casos de uso: classificação de texto, chat de perguntas e respostas, resumo, geração de texto.
  - Benefícios: um mesmo modelo serve várias áreas; ajuste exige poucos dados; performance cresce com mais dados e parâmetros.
  - Proprietários pagos: GPT/OpenAI (Microsoft), Gemini (Google), Claude/Anthropic (Amazon como principal investidora).
  - Open source: Llama 2 (Meta), Grok, Mistral AI — baixáveis para máquina ou servidor próprio, sem pagar pelo serviço.
  - Definição de open source dada em aula: código-fonte público, qualquer um pode ver, modificar e contribuir.
- **Link:** https://flix.nocodestartup.io/m/lessons/3176

### LLM / 002 - Tokenização  (00:04:00)
- **Resumo:** Mostra por que o texto precisa virar número: o computador só entende números, então textos longos são quebrados em unidades menores (tokens), cada uma com um ID único. Usa "bebendo" como exemplo de palavra que vira dois tokens porque o sufixo se repete em vários verbos. Faz uma demonstração prática no tokenizador da OpenAI, colando frases e observando contagem de tokens, caracteres e IDs.
- **Pontos-chave:**
  - Token = pedaço recorrente de texto; cada token tem um ID numérico, como um dicionário.
  - Exemplos medidos na aula: "bebendo" = 7 caracteres / 2 tokens; "Bebe uma água gelada" = 20 caracteres / 6 tokens; a frase completa com "para ficar bem hidratado" = 43 caracteres / 13 tokens.
  - IDs citados no tokenizador: "Be" = 1395, "bi" = 8385.
  - Duas consequências práticas: cada modelo tem limite de tokens por requisição, e a cobrança da OpenAI é por token.
- **Link:** https://flix.nocodestartup.io/m/lessons/3175

### LLM / 003 - Embeddings  (00:04:50)
- **Resumo:** Explica embedding como a representação de palavras/tokens em um espaço vetorial, onde a posição carrega o significado. Usa um plano cartesiano didático (cachorro em 0.5, 8; gato em 1, 8; cavalo em 1, 7) para mostrar que palavras semanticamente próximas ficam agrupadas e que a distância entre vetores mede a dissimilaridade. Alerta que o exemplo 2D é só didático e que embeddings reais são multidimensionais, e mostra a chamada de API de embeddings da OpenAI.
- **Pontos-chave:**
  - Palavras similares ficam próximas no espaço; animais longe de frutas, de móveis, de finanças.
  - O contexto resolve ambiguidade: "banco" pode cair perto de dinheiro/cofre ou perto de cadeira/sofá.
  - Dimensionalidade real citada: normalmente de 512 a 4096 dimensões (n dimensões, não visualizáveis).
  - Na API da OpenAI: passa-se o input de texto e o modelo de embedding, e recebe-se o vetor como resposta.
  - Esses vetores são o que se armazena em bancos de dados vetoriais.
- **Link:** https://flix.nocodestartup.io/m/lessons/3178

### LLM / 004 - Bancos De Dados Vetoriais  (00:02:05)
- **Resumo:** Apresenta bancos vetoriais como sistemas feitos para armazenar, consultar e manipular dados em formato vetorial multidimensional. O argumento é que dados do mundo real (áudio, texto, vídeo) não são estruturados, e virar vetor é o que permite buscá-los. Lista as propriedades que tornam esses bancos adequados a IA e os principais players do mercado.
- **Pontos-chave:**
  - Áudio, texto e vídeo viram vetores; vídeo é fracionado em partes antes de vetorizar.
  - Propriedades: indexação eficiente, busca por similaridade, escalabilidade e velocidade.
  - Opções de mercado: Pinecone e Redis; open source: Qdrant e Milvus.
  - Supabase é destacado como backend com opção de banco vetorial e será muito usado ao longo da formação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3177

### LLM / 005 - Outros Conceitos Importantes  (00:05:16)
- **Resumo:** Fecha o módulo com três conceitos operacionais. Fine-tuning é ajustar um LLM já treinado com dados e regras específicas para gerar um modelo especializado (exemplos: reconhecimento de fala adaptado a sotaques e dialetos brasileiros; diagnóstico médico a partir de ressonância e tomografia). RAG é enriquecer a resposta consultando fonte externa antes de chamar o modelo, usando banco vetorial como contexto. Function calling é o modelo acionar uma API externa para trazer dado que ele não tem.
- **Pontos-chave:**
  - Fluxo do RAG descrito: pergunta → busca no banco de dados vetorial externo → pergunta + contexto recuperado → modelo → resposta.
  - Caso real citado: as IAs da comunidade NoCode StartUp (Bubble, FlutterFlow) foram feitas com Chatbase, ingerindo a documentação completa da ferramenta como base vetorial.
  - Function calling: exemplo do clima em Boston — o modelo chama uma API externa e devolve a resposta já resumida ("22 graus"); serve também para enviar e-mails e consultar outros bancos.
  - Function calling é anunciado como conteúdo prático dos próximos módulos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3179

### Conclusão / 001 - Aprendizados  (00:00:41)
- **Resumo:** Encerramento curto recapitulando o objetivo do módulo: dar clareza sobre IA, machine learning, deep learning, LLMs, tokenização e embeddings, para que a pessoa não fique perdida no vocabulário. Libera o aluno para avançar para as próximas aulas da formação.
- **Pontos-chave:**
  - Nenhum conceito novo; apenas recapitulação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3180

## Pegadinhas e insights

- **Custo e limite são medidos em token, não em palavra.** Uma palavra pode virar 2+ tokens ("bebendo" = 2). Isso afeta tanto o teto de contexto do modelo quanto a fatura da OpenAI — dimensione prompts pensando em tokens.
- **O modelo é caixa-preta por dentro.** O instrutor é explícito: sabe-se o input e o output, mas não como os pesos das ~96 camadas / 175 bilhões de parâmetros chegam ao resultado.
- **Fine-tuning ≠ RAG.** Fine-tuning altera o modelo com dados e regras específicas; RAG deixa o modelo intacto e injeta contexto recuperado de uma fonte externa. Para "ensinar" dados do próprio negócio, a aula aponta o RAG como o caminho prático.
- **Embedding não é 2D.** O plano cartesiano da aula é só didático — na prática são de 512 a 4096 dimensões, e a intuição visual quebra acima de 3.
- **Contexto desambigua.** O mesmo termo ("banco") ocupa posições diferentes no espaço vetorial conforme o contexto — por isso busca por similaridade funciona melhor que busca por palavra-chave.
- **Modelo open source como alavanca de custo.** O instrutor sugere explicitamente considerar Llama 2 / Grok / Mistral rodando em máquina ou servidor próprio para baratear um SaaS, já que GPT, Gemini e Claude são serviços pagos.
- **Supabase é a aposta da formação** para backend, incluindo o banco vetorial — vale já contar com ele nas decisões de arquitetura das próximas aulas.
- **Aviso de expectativa:** o instrutor reconhece que o módulo é denso e pede para não travar nos detalhes — o objetivo é o desenho geral, não domínio profundo de redes neurais.
