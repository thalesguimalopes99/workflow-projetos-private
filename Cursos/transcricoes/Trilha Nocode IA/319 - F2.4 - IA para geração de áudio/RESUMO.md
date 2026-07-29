# F2.4 - IA para geração de áudio

Trilha Nocode IA | 9 aulas | ~22 min (00:21:56) | iniciante

> Panorama prático das IAs de áudio (OpenAI Whisper, OpenAI TTS e ElevenLabs) com foco em gerar voz, transcrever e dublar para usar em vídeos, conteúdos e SaaS no-code.

## O que você sai sabendo fazer

- Escolher entre Whisper, OpenAI TTS e ElevenLabs conforme o caso de uso (transcrever, gerar voz, clonar voz, dublar).
- Gerar narração em português com sotaque brasileiro no ElevenLabs, ajustando estabilidade, similaridade e exagero de estilo.
- Garimpar e adicionar vozes prontas da Voice Library filtrando por idioma (português) e testá-las com texto próprio.
- Clonar a própria voz via Instant Voice Cloning (gravando ou subindo um áudio) no plano pago mais barato.
- Inserir pausas controladas no texto para o áudio não sair robótico.
- Dublar vídeos automaticamente para outros idiomas (dubbing do ElevenLabs ou Rask) e avaliar se a qualidade serve.
- Localizar na documentação da OpenAI os endpoints de speech-to-text, tradução e TTS para plugar áudio num SaaS.

## Stack e ferramentas

- **OpenAI Whisper** — reconhecimento de voz / transcrição de áudio para texto em qualquer idioma; modelo precisa ser baixado, uso mais técnico (via código); também disponível por API.
- **OpenAI TTS (Text to Speech)** — texto para áudio via plataforma/API da OpenAI; consumo por créditos.
- **ChatGPT (app da OpenAI)** — comando de voz virando texto e upload de arquivos de áudio para transcrição, sem código.
- **Documentação da OpenAI (API)** — seções de speech-to-text, transcriptions, translations e idiomas suportados.
- **ElevenLabs** — plataforma principal do curso: Text to Speech, Speech to Speech, Voice Design, Voice Library, Voice Lab, Instant Voice Cloning, clone profissional, Projects, Dubbing e API própria. 29 idiomas, incluindo português com sotaque brasileiro. Freemium + planos a partir de US$ 3/mês (Starter); Projects exige plano Creator.
- **Rask** — ferramenta bônus de dublagem automática de vídeos (planos de US$ 50 e US$ 120/mês, com teste gratuito).
- **Sora (OpenAI)** — citada como fonte dos vídeos que o ElevenLabs sonorizou na demo do Twitter/X.

## Pré-requisitos

Nenhum pré-requisito técnico. Conta na OpenAI e conta no ElevenLabs (gratuita para explorar; plano Starter pago para clonar voz). Microfone decente se for gravar a amostra para o clone. O curso é continuação de uma trilha que já cobriu IA para texto, imagem e vídeo, mas as aulas se sustentam sozinhas.

## Aula a aula

### Intro / 001 - IA para Geração de Áudio  (00:00:50)
- **Resumo:** Abertura do módulo. O instrutor apresenta o escopo: modelos de IA generativa para áudio nos dois sentidos (texto→áudio e áudio→texto) e uma parte prática dedicada ao ElevenLabs. O objetivo declarado é habilitar o aluno a plugar funcionalidades de áudio em SaaS e projetos.
- **Pontos-chave:**
  - Dois fluxos centrais: text-to-speech e speech-to-text.
  - ElevenLabs é a ferramenta escolhida para a demonstração prática.
  - Foco de aplicação: SaaS e projetos com camada de áudio.
- **Link:** https://flix.nocodestartup.io/m/lessons/3233

### Intro / 002 - Melhores Modelos e Ferramentas  (00:02:16)
- **Resumo:** Aula de mapa do território. Situa o áudio dentro do quadrante texto/imagem/áudio/vídeo e compara três opções: Whisper, OpenAI TTS e ElevenLabs. A comparação cobre finalidade, custo e forma de uso (local, API ou interface própria).
- **Pontos-chave:**
  - Whisper: transcrição e tradução de áudio em qualquer idioma; casos como tradução de palestras e assistentes de voz; exige baixar o modelo.
  - OpenAI TTS: texto→áudio para assistentes virtuais e acessibilidade; pago por créditos, usado via plataforma/API.
  - ElevenLabs: TTS + speech-to-speech + vozes personalizadas + clone de voz; freemium e planos a partir de US$ 3/mês.
  - As três oferecem API — o critério de escolha é o caso de uso, não a disponibilidade.
- **Link:** https://flix.nocodestartup.io/m/lessons/3232

### Open AI / 001 - Text to Speech  (00:01:50)
- **Resumo:** Passeio pelas capacidades de áudio da OpenAI, primeiro pelo app do ChatGPT (falar e receber transcrição, enviar arquivos de áudio) e depois pela documentação da API. O instrutor navega pelas seções de speech-to-text, transcrições, traduções e idiomas suportados, mostrando onde achar o que é preciso para conectar áudio a um SaaS.
- **Pontos-chave:**
  - Dá para transcrever sem código direto no ChatGPT, inclusive enviando arquivos de áudio (MP3).
  - Na doc da API existem endpoints separados de transcription e translation — este último viabiliza apps de tradução.
  - A lista de idiomas suportados inclui português.
  - Os exemplos de Whisper na doc são mais técnicos, baseados em código.
  - Recomendação explícita: sempre ler a documentação antes de escolher a abordagem.
- **Link:** https://flix.nocodestartup.io/m/lessons/3235

### Eleven Labs / 001 - Conhecendo a Plataforma  (00:02:11)
- **Resumo:** Tour pelo site institucional do ElevenLabs antes de entrar na conta. Mostra os usos vendidos pela ferramenta (vídeo, jogos, audiobooks, chat), as vozes de demonstração, o suporte a idiomas e a página de preços. Termina olhando a documentação da API, que é o caminho para embutir a geração de voz num produto próprio.
- **Pontos-chave:**
  - 29 idiomas; escolhendo português, a voz sai com sotaque brasileiro.
  - Blocos principais anunciados: text to speech, speech to speech, voice cloning e projects.
  - Existe camada gratuita e planos pagos baratos — vale conferir o pricing antes de começar.
  - A API segue o padrão requisição com dados → resposta; ler a doc é pré-requisito para integrar num SaaS.
- **Link:** https://flix.nocodestartup.io/m/lessons/3234

### Eleven Labs / 002 - Efeitos de Som em Vídeos  (00:01:31)
- **Resumo:** Aula curta e conceitual sobre sonorização de vídeos gerados por IA. O instrutor mostra a publicação do ElevenLabs no Twitter/X em que sons naturais foram adicionados aos vídeos da Sora, da OpenAI. A ideia é que vídeo gerado por IA + camada de áudio gerada por IA permite produzir peças completas sozinho.
- **Pontos-chave:**
  - Funcionalidade de efeitos sonoros aplicados sobre vídeo existente.
  - Combinação sugerida: gerar o vídeo (Sora ou outra ferramenta do módulo anterior) e depois adicionar o som.
  - Argumento central: dá para "fazer filmes por conta própria" empilhando as IAs.
- **Link:** https://flix.nocodestartup.io/m/lessons/3236

### Eleven Labs / 003 - Principais funcionalidades  (00:06:26)
- **Resumo:** Aula prática mais longa do curso, já dentro da conta logada. O instrutor gera fala a partir de um texto em português, troca de voz, mexe nos sliders do modelo e explora as áreas de vozes: Voice Lab, Voice Design, Voice Library e Dubbing. Testa vozes brasileiras da biblioteca e faz uma dublagem automática de um vídeo próprio para inglês, avaliando o resultado com honestidade.
- **Pontos-chave:**
  - Painel oferece text-to-speech e speech-to-speech (upload de um áudio para regerar com outra voz).
  - Configurações da voz: estabilidade, similaridade e exagero de estilo; trocar de modelo (ex.: V2) pode mudar o sotaque resultante.
  - Voice Library: filtrar por idioma "português" e adicionar vozes prontas ao Voice Lab (ex.: Brazilian Dude, Borges BR).
  - Voice Design monta uma voz do zero por atributos (gênero, faixa etária, sotaque) — mais orientado a inglês.
  - Clone de voz exige plano Starter; Projects exige plano Creator.
  - Dubbing traduz vídeo automaticamente, mas o teste em português→inglês travou no início e ficou apenas razoável.
  - Caso de uso apontado: narração de vídeo de marketing/YouTube/e-book sem contratar locutor ou dublador.
- **Link:** https://flix.nocodestartup.io/m/lessons/3237

### Eleven Labs / 004 - Clone de Voz + dica extra  (00:04:35)
- **Resumo:** O instrutor assina o plano Starter e executa o Instant Voice Cloning ao vivo: nomeia a voz, grava a amostra pelo microfone, adiciona descrição e testa o resultado com frases de exemplo. Ajusta a similaridade para maximizar a semelhança e comenta as limitações de qualidade percebidas. Fecha com a dica de pausas no texto.
- **Pontos-chave:**
  - Clone instantâneo aceita arquivo enviado ou gravação feita na hora — qualidade do microfone importa.
  - Preencher nome e descrição (idioma, nacionalidade) ajuda a organizar o Voice Lab; etiquetas são opcionais.
  - Subir slider de similaridade aproxima mais o resultado da voz original.
  - Com a voz clonada dá para regerar áudios de terceiros na própria voz e traduzir vídeos próprios.
  - Dica extra: existe uma marcação de tempo (break/timing) inserida no texto para criar pausas de meio segundo ou um segundo entre falas — sem isso o áudio fica robótico.
  - Combinação sugerida para o futuro: voz clonada + avatar = vídeos "infinitos".
- **Link:** https://flix.nocodestartup.io/m/lessons/3238

### Bônus / 001 - Ferramenta Rask  (00:01:42)
- **Resumo:** Apresentação rápida do Rask como alternativa mais forte que o dubbing do ElevenLabs para dublar vídeos automaticamente. O instrutor abre o site, roda a demo de tradução e comenta os planos. Menciona que a própria escola avalia usar a ferramenta para publicar a formação em outros idiomas.
- **Pontos-chave:**
  - Dublagem automática de vídeo para inglês, espanhol e outros idiomas.
  - Planos citados: US$ 50/mês e US$ 120/mês, com opção de teste gratuito.
  - Atenção ao limite de duração de vídeo permitido em cada plano.
  - Posicionada como a melhor opção de dublagem vista até então pelo instrutor.
- **Link:** https://flix.nocodestartup.io/m/lessons/3239

### Conclusão / 001 - Aprendizados do Módulo  (00:00:35)
- **Resumo:** Fechamento curto recapitulando o escopo: melhores modelos e ferramentas para gerar áudio com IA nos dois sentidos. O instrutor lembra que mostrou apenas as ferramentas mais conhecidas e incentiva a pesquisar outras, inclusive soluções focadas em nichos específicos.
- **Pontos-chave:**
  - Recapitula texto→áudio e áudio→texto como os dois eixos do módulo.
  - O mercado tem muitas outras ferramentas além das demonstradas, algumas de nicho.
- **Link:** https://flix.nocodestartup.io/m/lessons/3240

## Pegadinhas e insights

- **Clone de voz é pago.** O Instant Voice Cloning só libera no plano Starter; o instrutor pagou US$ 3 para gravar a aula. Projects exige o plano Creator, mais caro.
- **Dubbing do ElevenLabs decepcionou em português.** No teste do próprio instrutor (PT→EN) o áudio travou no começo e ficou "mais ou menos"; a hipótese dele é que funcione melhor com locução original em inglês. Para dublagem séria, ele indica o Rask.
- **Trocar o modelo pode mudar o sotaque.** Ao alternar para o modelo V2 a voz passou a sair com sotaque inglês, mesmo com texto em português — vale revalidar o áudio depois de mexer no modelo.
- **Sem marcação de pausa o áudio soa robótico.** A dica de inserir os códigos de timing (meio segundo / um segundo) entre as frases é apontada como uma das mais importantes do módulo.
- **Voice Design é enviesado para inglês.** Os atributos de sotaque servem melhor a vozes em inglês; para português, o caminho mais rápido é filtrar a Voice Library por idioma e adotar uma voz pronta.
- **Qualidade da amostra manda no clone.** O instrutor reconhece que a qualidade final do áudio clonado não ficou boa, ainda que a semelhança tenha ficado alta — gravar com microfone decente é decisivo.
- **Whisper não é plug-and-play.** Exige baixar o modelo e usar código; para transcrição rápida sem trabalho, o próprio app do ChatGPT resolve.
- **Ler a documentação da API é regra recorrente.** Aparece tanto na aula da OpenAI quanto na do ElevenLabs, sempre com o mesmo argumento: é o que permite plugar áudio dentro de um SaaS próprio.
