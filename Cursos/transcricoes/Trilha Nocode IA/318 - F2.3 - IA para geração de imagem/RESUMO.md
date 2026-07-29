# F2.3 - IA para geração de imagem

Trilha Nocode IA | 13 aulas | ~39 min (0,65h) | nível iniciante

> Panorama prático dos principais modelos de geração de imagem por IA (DALL·E, Stable Diffusion, Midjourney), com mão na massa em DALL·E dentro do ChatGPT e nas várias formas de rodar o Stable Diffusion — sempre com o olho na API, porque a meta da formação é plugar essa inteligência em SaaS próprio.

## O que você sai sabendo fazer

- Escolher entre DALL·E, Stable Diffusion e Midjourney comparando custo, idioma do prompt, nível de customização e disponibilidade de API.
- Gerar, editar e reestilizar imagens no DALL·E dentro do ChatGPT, inclusive editando só uma região selecionada da imagem.
- Usar o ChatGPT como gerador de prompt e aproveitar o prompt em inglês que o próprio DALL·E reescreve por baixo dos panos.
- Extrair informação de imagens com GPT Vision (descrição de cena, estimativa nutricional, sugestões a partir de ingredientes).
- Localizar na documentação da OpenAI e da Stability AI os endpoints de geração, edição, variação e upscale de imagem.
- Rodar Stable Diffusion por três caminhos: interface oficial (DreamStudio), agregador de modelos (Replicate) ou instalação local (ComfyUI / ControlNet).

## Stack e ferramentas

- **Modelos:** DALL·E 2 e DALL·E 3 (OpenAI), Stable Diffusion / Stable Diffusion 3 (Stability AI), Midjourney (citado, não demonstrado), GPT Vision.
- **Interfaces e plataformas:** ChatGPT (plano Plus), GPTs personalizados da loja (Cartoonize Yourself, criadores de logo, GPT de fotos realistas), DreamStudio, Replicate, Hugging Face (citado), Leonardo AI (citado), Canva AI (citado), Discord (via Midjourney).
- **APIs e docs:** API de imagens da OpenAI (endpoint POST, payload JSON com model, prompt, n e size; chave de API; créditos), API da Stability AI (geração, upscale, edição; preço por crédito).
- **Local:** ComfyUI (fluxo por nós), ControlNet.

## Pré-requisitos

- Ter visto as aulas anteriores de prompt da trilha (as boas práticas são reaproveitadas, não reensinadas).
- Assinatura ChatGPT Plus para acompanhar a parte prática de DALL·E (o instrutor sugere ao menos usar o período de teste).
- Conta na OpenAI para acessar a documentação e conta no DreamStudio/Replicate para os testes.
- Noção básica de o que é uma API/endpoint ajuda, mas o curso não exige código.

## Aula a aula

### Intro / 001 - O que você irá aprender  (00:01:15)
- **Resumo:** Abertura do módulo com o mapa do que será coberto: comparativo dos principais modelos de geração de imagem, prática com DALL·E dentro do ChatGPT e exploração do Stable Diffusion. A promessa é que ao final o aluno consiga escolher a ferramenta certa para cada projeto.
- **Pontos-chave:**
  - Foco em três frentes: comparar modelos, praticar DALL·E, conhecer Stable Diffusion.
  - Objetivo declarado: saber escolher e usar o modelo mais adequado ao projeto, não decorar uma ferramenta.
- **Link:** https://flix.nocodestartup.io/m/lessons/3220

### Intro / 002 - Melhores Modelos do Mercado  (00:04:10)
- **Resumo:** Situa geração de imagem como uma das quatro categorias de IA generativa (texto, imagem, áudio, vídeo) e apresenta uma tabela comparativa entre DALL·E, Stable Diffusion e Midjourney. Cada modelo é avaliado por custo, forma de acesso, idioma do prompt, customização e API. A aula fecha justificando por que o curso vai priorizar DALL·E e Stable Diffusion.
- **Pontos-chave:**
  - Custos citados: DALL·E exige ChatGPT Plus (~US$ 20/mês na gravação); Stable Diffusion por créditos ou grátis se rodado localmente; Midjourney a partir de US$ 10/mês, sem plano gratuito.
  - Acesso: DALL·E pela plataforma da OpenAI; Stable Diffusion não tem front-end próprio (precisa de interface de terceiros ou instalação local); Midjourney roda dentro do Discord.
  - Idioma: DALL·E aceita bem português; Stable Diffusion funciona melhor em inglês; Midjourney aceita português mas rende mais em inglês.
  - API: OpenAI e Stability AI oferecem API; a do Midjourney é citada como a partir de US$ 30/mês.
  - Midjourney fica de fora da prática porque exige pagamento para testar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3221

### Intro / 003 - Prompts e funcionalidades para imagens  (00:01:30)
- **Resumo:** Revisão rápida de que as boas práticas de prompt já vistas na trilha valem igual para imagem: detalhar bastante, dar passo a passo, atribuir persona e especificar características do resultado. Em seguida lista as três funcionalidades que se espera de uma ferramenta de imagem.
- **Pontos-chave:**
  - Quanto mais detalhe no prompt, melhor a imagem.
  - Funcionalidade 1: geração do zero (qualquer estilo, de vetor a cena).
  - Funcionalidade 2: edição (trocar background, trocar personagens).
  - Funcionalidade 3: upscale, para aumentar a definição da imagem.
- **Link:** https://flix.nocodestartup.io/m/lessons/3222

### Dall-E / 001 - Como criar imagens incríveis  (00:06:56)
- **Resumo:** Aula prática mais longa do módulo. O instrutor gera uma imagem de guerreiro com dragão no DALL·E dentro do ChatGPT e vai iterando: refina por conversa, edita região selecionada, troca personagem, adiciona elementos ao fundo e muda o estilo. Também mostra como recuperar o prompt em inglês gerado pelo modelo e como pedir ao ChatGPT que escreva o prompt para você.
- **Pontos-chave:**
  - Acesso: DALL·E direto no chat do Plus, ou via **Explore GPTs** procurando o GPT oficial "DALL·E".
  - No ícone de informação da imagem aparece o prompt em inglês que o modelo reescreveu — dá para copiar, traduzir e ajustar como base de novos prompts.
  - Edição conversacional: pedir alterações em linguagem natural e o modelo parte da imagem anterior (ex.: dragão de fogo → dragão de gelo).
  - Edição por seleção: pintar uma área da imagem e descrever a troca, mantendo o resto intacto (funcionou para trocar o guerreiro por uma guerreira e adicionar dragões ao fundo).
  - Mudança de estilo por prompt (ex.: mangá japonês) e escolha de formato: quadrado, widescreen ou vertical.
  - Para realismo, citar detalhes de câmera e tamanho no prompt.
  - Se travar no prompt, peça ao próprio ChatGPT um prompt detalhado e cole no DALL·E.
- **Link:** https://flix.nocodestartup.io/m/lessons/3223

### Dall-E / 002 - GPTVision e Descrição de Imagens  (00:03:59)
- **Resumo:** Inverte o fluxo: em vez de gerar imagem a partir de texto, envia imagem e pede interpretação. Dois exemplos práticos — um prato de comida, do qual o modelo descreve os alimentos e estima calorias e proteína, e uma foto de ingredientes, da qual o modelo sugere drinks com passo a passo. A aula posiciona isso como matéria-prima para ideias de produto.
- **Pontos-chave:**
  - Fluxo: subir a foto no chat e pedir "descreva o que tem nessa foto".
  - Estimativas retornadas no exemplo: cerca de 300 a 450 calorias no prato e 24 a 29 g de proteína considerando ~100 g de carne.
  - O modelo erra identificações (confundiu batata doce com berinjela) — a leitura visual não é confiável ao pé da letra.
  - Sem informação de peso, os números nutricionais são aproximações.
  - Caso de uso sugerido: app que calcula calorias a partir da foto do prato.
- **Link:** https://flix.nocodestartup.io/m/lessons/3225

### Dall-E / 003 - GPTs Personalizados  (00:03:31)
- **Resumo:** Explora a loja de GPTs focados em imagem, tanto os oficiais da OpenAI quanto os criados pela comunidade. Testa um GPT que transforma foto em cartoon e outro especializado em fotos realistas, mostrando que cada GPT tem comportamento e qualidade próprios porque foi ajustado para uma tarefa específica.
- **Pontos-chave:**
  - A categoria DALL·E dentro dos GPTs concentra ferramentas só de imagem.
  - Exemplos testados/citados: Cartoonize Yourself (foto → cartoon), GPT de fotos realistas, GPTs de criação de logo, de tatuagem e de gerar imagem similar a partir de uma referência.
  - A nota/avaliação do GPT ajuda a escolher qual usar.
  - Prompt em português funciona; alguns GPTs traduzem o pedido para inglês antes de gerar.
  - Alguns GPTs entregam a imagem via link que demora a carregar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3224

### Dall-E / 004 - Open AI API  (00:03:27)
- **Resumo:** Passeio pela documentação da OpenAI focada em imagem, com o argumento de que é pela API que essa inteligência entra num SaaS. Mostra onde ficam os modelos, o guia de capabilities de geração de imagem e a API reference, além da parte de Vision.
- **Pontos-chave:**
  - Modelos disponíveis na doc: DALL·E 3 e DALL·E 2; é preciso ter créditos na conta.
  - Requisição: POST com `application/json`, chave de API no header e corpo com modelo, prompt, quantidade de imagens e tamanho.
  - A doc cobre três operações: criar imagem, editar imagem (ex.: inserir um flamingo numa foto) e gerar variações.
  - Vision recebe a URL da imagem e devolve a descrição.
  - A resposta da API traz URLs das imagens geradas, prontas para consumo no app.
  - A construção da API na prática fica para módulos posteriores da formação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3226

### Stable Diffusion / 001 - Precisamos do seu feedback!  (00:00:43)
- **Resumo:** Recado institucional, sem conteúdo técnico. O instrutor pede que o aluno deixe um feedback detalhado sobre a formação no link da aula, incluindo foto de perfil.
- **Pontos-chave:**
  - Pedido de feedback de ~1 minuto, com comentário sobre estrutura e didática.
  - Sem relação com o conteúdo de geração de imagem.
- **Link:** https://flix.nocodestartup.io/m/lessons/3256

### Stable Diffusion / 002 - Conhecendo o Modelo  (00:04:27)
- **Resumo:** Apresenta a Stability AI como empresa por trás do Stable Diffusion e navega pelo site: modelos de imagem, vídeo, áudio e 3D, documentação de API e pricing por crédito. O ponto central é entender que o Stable Diffusion é só o modelo, sem interface própria, e que o ecossistema de ferramentas ao redor é que dá acesso a ele.
- **Pontos-chave:**
  - Diferencial do modelo: ser open source, o que explica a adoção ampla.
  - Funcionalidades da API da Stability: geração, upscale (alta definição) e edição (trocar pessoas, trocar fundos), com recursos ainda por lançar.
  - Cobrança por crédito, consumido em cada operação (gerar, upscalar, editar).
  - Não há um "chat padrão" como na OpenAI — é preciso escolher uma interface.
  - Ferramentas que rodam o modelo: Stable Diffusion Web, DreamStudio (oficial), Leonardo AI, Canva AI, além de Hugging Face e Replicate para rodar modelos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3227

### Stable Diffusion / 003 - Dream Studio  (00:02:57)
- **Resumo:** Demonstração prática do DreamStudio, a interface oficial da Stability AI. O instrutor cria conta, escolhe estilo, escreve o prompt em inglês e gera imagens, comparando o resultado com o que havia feito no DALL·E. Mostra também os campos de controle disponíveis.
- **Pontos-chave:**
  - A conta nova vem com créditos iniciais; depois é preciso comprar mais.
  - Prompt deve ser escrito em inglês.
  - Campos principais: estilo (anime, fotográfico, digital, punk e outros), prompt, **prompt negativo** (o que não deve aparecer), upload de imagem, tamanho e quantidade de imagens.
  - Em opções avançadas há controle de proporção e de **steps**.
  - Botão **Dream** dispara a geração.
  - O maior grau de personalização do Stable Diffusion só aparece na instalação local.
- **Link:** https://flix.nocodestartup.io/m/lessons/3228

### Stable Diffusion / 004 - Replicate  (00:03:19)
- **Resumo:** Mostra o Replicate como agregador que dá interface e API para centenas de modelos abertos que, sozinhos, exigiriam código para rodar. Faz login, explora o catálogo, busca modelos da Stability AI e abre um text-to-image para ver os parâmetros e o exemplo de chamada.
- **Pontos-chave:**
  - Catálogo cobre modelos de texto, imagem e vídeo, incluindo Google, Meta e projetos open source.
  - Exemplos de uso vistos: transformar estilo de imagem, remover fundo, animar imagem, gerar imagens novas.
  - Cada modelo expõe prompt, tamanho e demais parâmetros na própria página, além de README com tutorial.
  - A página mostra chamadas em HTTP, Node e Python — o instrutor recomenda usar o formato de endpoint HTTP, coerente com a pegada no-code da formação.
  - Alternativas de front-end para o mesmo modelo: DreamStudio, Canva, Leonardo AI.
- **Link:** https://flix.nocodestartup.io/m/lessons/3229

### Stable Diffusion / 005 - Ferramentas para Instalação Local  (00:01:39)
- **Resumo:** Fecha o bloco apontando o caminho avançado: rodar o Stable Diffusion na própria máquina para ganhar personalização total e parar de pagar por geração. Apresenta as duas ferramentas principais desse caminho, sem tutorial de instalação.
- **Pontos-chave:**
  - **ComfyUI**: interface por nós conectados, permite montar fluxos que geram e alteram imagem, estilo e background.
  - **ControlNet**: guia a geração a partir de um desenho/estrutura (ex.: rascunho de tartaruga vira várias versões com fundos diferentes), usando Stable Diffusion por trás.
  - Rodando local não há gasto por imagem.
  - A instalação em si fica fora do módulo para não alongá-lo; conteúdo prometido para o futuro.
- **Link:** https://flix.nocodestartup.io/m/lessons/3231

### Conclusão / 001 - Aprendizados do Módulo  (00:01:11)
- **Resumo:** Recapitulação do módulo: modelos comparados, funcionalidades de imagem, prática com DALL·E, papel da API da OpenAI para alimentar SaaS, conceitos de Stable Diffusion e opções de execução local. Encerra incentivando a explorar outras ferramentas construídas sobre esses modelos.
- **Pontos-chave:**
  - DALL·E é reforçado como o mais prático e o caminho natural para integração via API.
  - Stable Diffusion é a via de personalização, inclusive local com ControlNet e ComfyUI.
  - Muitas ferramentas de mercado são apenas front-ends de modelos já vistos.
- **Link:** https://flix.nocodestartup.io/m/lessons/3230

## Pegadinhas e insights

- **DALL·E reescreve seu prompt.** O prompt em inglês que o modelo realmente usou fica no ícone de informação da imagem. Copiar esse texto e editá-lo é o atalho mais rápido para prompts bons — vale mais do que escrever do zero.
- **Editar por seleção preserva o resto.** Pintar só a região a alterar e descrever a troca mantém composição e estilo da imagem original, ao contrário de gerar tudo de novo.
- **Iteração é conversacional.** Cada novo pedido parte da imagem anterior; é assim que se refina, não com prompts isolados.
- **GPT Vision erra.** No exemplo do prato ele trocou batata doce por berinjela, e sem peso os valores nutricionais são estimativa. Não trate a leitura como dado confiável.
- **Idioma importa.** DALL·E vai bem em português; para Stable Diffusion escreva em inglês.
- **Prompt negativo existe no DreamStudio, não no DALL·E.** É onde você lista o que não quer ver na imagem — recurso que muda o resultado e não tem equivalente direto no fluxo de chat.
- **Créditos acabam.** DreamStudio dá créditos iniciais e o instrutor avisa explicitamente para não torrar tudo nos primeiros testes; depois é compra. A API da OpenAI também exige créditos na conta.
- **Midjourney não é testável de graça.** Por isso ficou de fora da prática — hoje é pago a partir de US$ 10/mês e roda dentro do Discord.
- **Stable Diffusion é modelo, não produto.** Leonardo AI, Canva AI, DreamStudio e Replicate são camadas por cima do mesmo motor; escolha a interface pelo fluxo de trabalho, não pela qualidade do modelo.
- **Replicate resolve o problema de "modelo sem interface".** Dá endpoint HTTP pronto para modelos que, de outro modo, exigiriam código — encaixe direto na lógica no-code de consumir API.
- **Rodar local é a saída para custo e controle.** ComfyUI (nós) e ControlNet dão personalização máxima e custo zero por imagem, mas o módulo não ensina a instalar.
- **O módulo é panorâmico e orientado a API.** A construção real do SaaS com essas APIs fica para módulos seguintes da formação.
