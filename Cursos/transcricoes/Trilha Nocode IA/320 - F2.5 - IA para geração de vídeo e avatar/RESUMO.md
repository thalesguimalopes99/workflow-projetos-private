# F2.5 - IA para geração de vídeo e avatar

Trilha Nocode IA | 7 aulas | ~20 min (00:20:29) | nível iniciante

> Tour prático pelas ferramentas de geração de vídeo por IA disponíveis no mercado, com foco em criar vídeos a partir de texto, de imagem e de outro vídeo usando Runway e Stable (Video) Diffusion via Replicate.

## O que você sai sabendo fazer

- Escolher entre Stable Video Diffusion, Runway e Pika Labs comparando custo, plataforma, acesso a API e funcionalidades.
- Gerar vídeo a partir de um prompt de texto dentro do Runway (Generate videos → text to video).
- Animar uma imagem estática e transformá-la em vídeo, mexendo nos controles de câmera (pan, zoom, rotação horizontal/vertical) e em interpolação.
- Aplicar Motion Brush: pintar até 5 áreas da imagem e definir direção de movimento (horizontal, vertical, aproximar) por área.
- Trocar o estilo de um vídeo existente com video-to-video, usando os presets e o botão de preview antes de gastar crédito.
- Rodar modelos de vídeo do Stable Diffusion pela interface do Replicate, ajustando parâmetros como tamanho, peso e frames por segundo.

## Stack e ferramentas

- **Runway** — ferramenta principal do curso. Text to video, image to video, video to video, text to image, image to image, Motion Brush, expandir/estender imagem, remover fundo, gerar áudio.
- **Stable Video Diffusion / Stability AI** — modelo aberto, sem interface própria; usado por meio de terceiros.
- **Replicate** — front-end para rodar os modelos da Stability AI (login via conta GitHub).
- **Pika Labs** — citada na comparação, mas não demonstrada na prática.
- **Sora (OpenAI)** — citada como promessa, sem acesso na época da gravação.
- **DALL·E / ChatGPT (GPT)** — origem das imagens usadas nos testes (barco pirata, robôs, dragão, astronauta).
- **HeyGen** ("Raygen" na transcrição) — citada só na conclusão como a ferramenta de avatares; **não é ensinada** neste curso.

## Pré-requisitos

- Ter visto os módulos anteriores da trilha sobre **Replicate** (o instrutor assume que a plataforma já é conhecida).
- Conta no GitHub (para logar no Replicate) e conta no Runway.
- Inglês básico para escrever prompts — as ferramentas funcionam melhor em inglês.

## Aula a aula

### 1 - Geração de videos com IA  (00:00:46)
- **Resumo:** Abertura curta do módulo. O instrutor apresenta a proposta: mostrar as principais ferramentas de geração de vídeo por IA do mercado e demonstrar Runway e Stable Diffusion na prática, para o aluno sair com um panorama de quais modelos e plataformas valem a pena no dia a dia.
- **Pontos-chave:**
  - Escopo: modelos + ferramentas de vídeo por IA, com demonstração prática.
  - As duas plataformas centrais anunciadas são Runway e Stable Diffusion.
- **Link:** https://flix.nocodestartup.io/m/lessons/3241

### 2 - Melhores Modelo do Mercado  (00:02:50)
- **Resumo:** Aula de comparação. Situa a geração de vídeo como um dos quatro quadrantes de IA (texto, imagem, áudio, vídeo) e confronta Stable Video Diffusion, Runway e Pika Labs em custo, interface, idioma de prompt, acesso a API e funcionalidades. Justifica por que o curso vai focar em Stable Video Diffusion e Runway, deixando Pika Labs de fora.
- **Pontos-chave:**
  - Ferramentas mapeadas: Sora (OpenAI, sem acesso na época), Stable Diffusion / Stable Video Diffusion, Runway e Pika Labs.
  - Preço citado: Runway a partir de US$ 12/mês; Pika Labs a partir de US$ 10/mês. Stability AI é open source e roda na própria máquina, além de ter créditos.
  - Interface: Stable Video Diffusion não tem plataforma própria (precisa de front-end de terceiro); Runway e Pika Labs têm.
  - API: Stability AI tem; Runway só nos planos Enterprise; Pika Labs não tinha.
  - Prompts devem ser escritos em inglês para funcionar bem.
  - Três funcionalidades-base do segmento: texto→vídeo, imagem→vídeo e vídeo→vídeo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3242

### 3 - Diffusion com Replicate  (00:02:55)
- **Resumo:** Demonstra como acessar modelos de vídeo do Stable Diffusion sem interface própria, usando o Replicate como front-end. O instrutor navega pelo painel, busca por "Stability AI" na área de explorar e mostra dois modelos: um que gera vídeo animado a partir de texto e outro que anima uma imagem enviada. É uma passada rápida — ele avisa que vai aprofundar mesmo no Runway.
- **Pontos-chave:**
  - Login no Replicate é feito com conta do GitHub.
  - Caminho: painel → Explorar/Explore → buscar "Stability AI" → listar modelos.
  - O modelo oficial de imagem→vídeo tinha sido retirado no momento da gravação; o instrutor achou modelos alternativos.
  - Parâmetros ajustáveis nos modelos: ângulo/rotação, tamanho do vídeo, peso e frames por segundo.
  - Aula deliberadamente superficial — a profundidade fica no Runway.
- **Link:** https://flix.nocodestartup.io/m/lessons/3243

### 4 - Criar vídeos a partir de Texto ou Imagem  (00:06:12)
- **Resumo:** Aula mais densa do curso. Passeia primeiro pela home do Runway mostrando o leque de funcionalidades e depois entra na plataforma logada para gerar vídeos na prática. Testa texto→vídeo com um prompt em inglês (guerreiro voando num dragão vermelho cuspindo fogo), depois sobe uma imagem de dragão feita no DALL·E para animá-la, e por fim explora o painel de configurações de câmera com uma imagem de astronauta.
- **Pontos-chave:**
  - Menu à esquerda: criativos/assets, edição, separação por vídeos, imagens e outros, e saldo de créditos.
  - Fluxo: Generate videos → text to video (dá para só escrever o prompt ou subir uma imagem).
  - Previews gratuitos existem, mas ficam indisponíveis quando o servidor está sobrecarregado.
  - Config geral: **interpolate** (suaviza a transição entre frames), **upscale** (aumenta resolução) e **remover marca d'água** — os dois últimos exigem plano pago superior.
  - Controles de câmera: pan (dá sensação de 3D), esquerda/direita, rotação vertical (cima/baixo) e zoom.
  - O modelo erra a interpretação do prompt com frequência: é normal gerar de novo e ajustar o texto.
- **Link:** https://flix.nocodestartup.io/m/lessons/3245

### 5 - Videos a partir de Videos  (00:02:26)
- **Resumo:** Mostra o modo video-to-video do Runway, que reestiliza um vídeo existente. O instrutor reaproveita o vídeo do dragão gerado na aula anterior e vai testando presets de estilo — espaço, abstrato, pet cartoon, neon, green, vibrante, ilustração, sci-fi — usando o preview para inspecionar antes de gerar. O resultado final sai distorcido, e ele conclui que a cena era detalhada demais.
- **Pontos-chave:**
  - Caminho: Videos → gerar vídeos → opção vídeo para vídeo → upload do vídeo base.
  - À direita ficam o prompt de estilo personalizado e a biblioteca de presets.
  - O botão **preview** simula o estilo antes de gastar crédito na geração — use sempre.
  - O preview trava/bugga às vezes; o jeito é ir testando estilos diferentes.
  - Vídeos com muito detalhe reestilizam mal; o instrutor sugere que vídeos com pessoas/humanos funcionam melhor.
- **Link:** https://flix.nocodestartup.io/m/lessons/3244

### 6 - Motion Brush  (00:04:35)
- **Resumo:** Ensina o Motion Brush, recurso de animação seletiva do Runway. Partindo de uma imagem de barco pirata feita no DALL·E, o instrutor pinta áreas separadas (mar, ambiente, barco) e define a direção de movimento de cada uma — horizontal, vertical, aproximar — gerando uma cena animada convincente. Repete o exercício com uma imagem de robôs e obtém um resultado pior, ilustrando o limite da técnica. Fecha citando ferramentas de expandir imagem no Runway.
- **Pontos-chave:**
  - Fluxo: imagem→vídeo → upload da imagem → Motion Brush → pintar a área → definir o movimento.
  - Cada área pintada tem controles próprios: horizontal, vertical, aproximar/zoom e "ambiente" (movimento ambiente da região).
  - Limite prático: só **5 áreas** de pintura por imagem.
  - Regra de ouro: movimentos **sutis**. Exagerar deixa o resultado poluído e desconfigura rostos e formas.
  - Bônus citado: ferramentas de imagem do Runway para expandir a imagem e criar imagem infinita, gerando conteúdo novo para os lados.
- **Link:** https://flix.nocodestartup.io/m/lessons/3247

### 7 - Aprendizados  (00:00:45)
- **Resumo:** Fechamento rápido recapitulando o que foi visto: o filtro das melhores ferramentas do mercado e as demonstrações práticas de Runway e Stable Diffusion para criar vídeo a partir de texto e de imagem. O instrutor reconhece que a parte de avatares não foi coberta e a deixa como possível conteúdo futuro.
- **Pontos-chave:**
  - Recap: melhores modelos + Runway na prática + Stable Diffusion na prática.
  - Criação de avatares fica de fora — a ferramenta indicada para isso é o HeyGen, mencionado como assunto de uma aula futura.
- **Link:** https://flix.nocodestartup.io/m/lessons/3246

## Pegadinhas e insights

- **O "avatar" do título não é ensinado.** Avatares aparecem só na aula de conclusão, como promessa de conteúdo futuro, com indicação da ferramenta HeyGen. Não espere tutorial de avatar aqui.
- **Curso datado.** Sora ainda não tinha acesso público na gravação, e um dos modelos de imagem→vídeo da Stability AI já havia sumido do Replicate durante a própria produção. Preços (Runway US$ 12/mês, Pika US$ 10/mês) e disponibilidade de API mudaram desde então.
- **Prompt em inglês.** O instrutor é explícito: essas ferramentas funcionam bem em inglês, é o idioma oficial delas.
- **Créditos acabam.** No Runway o saldo inicial é limitado e depois é pago. Por isso o preview do video-to-video é economicamente relevante: testa o estilo sem queimar geração.
- **Preview pode não estar disponível** quando o servidor está sobrecarregado — não é bug da sua conta.
- **Upscale e remover marca d'água são paywall**, exigem plano superior ao inicial.
- **O modelo erra o prompt.** No teste texto→vídeo o Runway confundiu "guerreiro voando num dragão" e fundiu os dois; regenerar e reescrever o prompt faz parte do processo.
- **Video-to-video odeia cenas detalhadas.** Quanto mais complexo o vídeo de origem, mais desconfigurado o resultado. Cenas com pessoas tendem a sair melhor.
- **Motion Brush: sutileza > intensidade.** Movimento forte demais em rostos deforma completamente a imagem (visível no teste com os robôs). Limite de 5 áreas por imagem também força priorização.
- **Stable Video Diffusion depende de front-end de terceiro.** Não tem interface própria; ou você usa Replicate/similar, ou roda localmente por ser open source.
- **Pipeline implícito do curso:** gerar a imagem base no DALL·E/ChatGPT → subir no Runway → animar com image-to-video ou Motion Brush. As imagens dos exercícios (dragão, barco pirata, robôs, astronauta) vieram todas de geração de imagem prévia.
