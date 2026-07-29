# M2 - Converse com um PDF, Planilhas e Arquivos | RAG

Trilha Dify | 6 aulas | ~28 min (00:28:11) | nível iniciante

> Como alimentar um agente do Dify com conhecimento externo (planilha, PDF e site) usando RAG, e testar se ele realmente responde com base nesses dados.

## O que você sai sabendo fazer

- Criar uma base de conhecimento no Dify a partir de CSV/planilha, PDF e páginas de site.
- Escolher a estratégia de fragmentação (automática vs. personalizada com delimitador) para que cada bloco fique bem estruturado.
- Configurar modelo de embedding, modo de índice e tipo de pesquisa (vetorial, por texto ou híbrida).
- Ajustar Top K e limiar de pontuação para deixar a recuperação mais precisa ou mais aberta.
- Usar o teste de recuperação para validar se a pergunta bate nos blocos certos antes de plugar no bot.
- Conectar o Firecrawl ao Dify para rastrear um site e transformar o conteúdo em base vetorial.
- Anexar as bases ao contexto do agente e ajustar o prompt para ele acionar o conhecimento externo na hora certa.

## Stack e ferramentas

- **Dify** — criação do agente, base de conhecimento e banco vetorial (tudo dentro da plataforma).
- **Embedding da OpenAI** — modelo `large` usado para vetorizar o conhecimento.
- **GPT-4o / GPT-4o mini** — modelo de resposta do bot (o mini é citado como opção mais barata).
- **Firecrawl** — scraper de sites integrado ao Dify via API Key (plano gratuito com 500 créditos).
- **Planilha em CSV** (exportada do Google Sheets/Excel) e **PDF** de perguntas e respostas como fontes.
- Tokenizador da OpenAI (usado só para demonstrar contagem de tokens e IDs).
- Formatos aceitos pelo upload do Dify citados na aula: PDF, HTML, XLS, CSV, PowerPoint; sincronização com Notion e com site.

## Pré-requisitos

O módulo assume que você **já criou o agente de atendimento no Dify em um módulo anterior**, inclusive com integração ao WhatsApp — aqui o trabalho é só treiná-lo com conhecimento externo. Também assume conta na OpenAI configurada no Dify e conta no Firecrawl (gratuita) para a aula de sites. A teoria de tokenização/embedding é revisada na aula 2, então não é pré-requisito.

## Aula a aula

### 1 - Introdução e Planejamento do Projeto  (00:02:00)
- **Resumo:** Abertura do módulo, que apresenta o objetivo de turbinar o agente com conhecimentos personalizados vindos de planilhas, PDFs e sites externos. O instrutor introduz o conceito de RAG (Retrieval Augmented Generation) e adianta que o Dify simplifica bastante o processo. O projeto do módulo é evoluir o agente de atendimento já criado e integrado ao WhatsApp para que ele consulte esses materiais antes de responder.
- **Pontos-chave:**
  - RAG = Retrieval Augmented Generation (o instrutor pronuncia "reg" ao longo do curso).
  - Fluxo do projeto: dúvida do usuário → instruções do prompt → consulta a planilha, PDF e site → resposta personalizada.
  - Casos de uso citados: agentes de suporte treinados com material da empresa e agentes de vendas.
  - Continuação direta do agente montado em módulo anterior, não parte do zero.
- **Link:** https://flix.nocodestartup.io/m/lessons/3799

### 2 - Revisão Embedding, Banco de Dados Vetorial e RAG  (00:05:48)
- **Resumo:** Aula teórica de revisão, marcada como pulável para quem já domina os conceitos. Explica tokenização (texto virando IDs numéricos, que é o que a IA cobra como input/output), embedding como representação vetorial multidimensional onde palavras similares ficam próximas, e o papel dos bancos de dados vetoriais. Fecha amarrando os três conceitos na definição de RAG: em vez de responder só com o conhecimento da LLM, a busca passa pelo modelo de embedding e pelo banco vetorial para trazer contexto próprio.
- **Pontos-chave:**
  - Demonstração no tokenizador: "Eu sou aluno da NoCode Startup" gera 7 tokens e 30 caracteres; cada token tem um ID fixo (ex.: "eu" = 55218).
  - Embedding é multidimensional — a aula cita ordens de grandeza de centenas até 4.096 dimensões, não apenas eixos X e Y.
  - Banco vetorial serve para texto, imagem, áudio e vídeo; vantagens citadas: indexação rápida, busca por similaridade e escalabilidade.
  - Exemplos de bancos vetoriais mencionados: Pinecone e Redis — mas no curso o embedding é feito pelo modelo da OpenAI e o banco vetorial é criado pelo próprio Dify.
- **Link:** https://flix.nocodestartup.io/m/lessons/3798

### 3 - Planilhas  (00:07:24)
- **Resumo:** Primeira aula prática: subir uma planilha real (mapa de aulas da formação, com trilha, módulo, descrição, palavras-chave e link) como base de conhecimento no Dify. Percorre o menu Conhecimento, o upload em CSV, a tela de fragmentação, o modo de índice, o modelo de embedding e o tipo de pesquisa. Termina no teste de recuperação, mostrando como ler a pontuação de cada bloco e como Top K e limiar mudam o resultado.
- **Pontos-chave:**
  - Planilha é a melhor fonte para RAG porque **cada linha vira um bloco limpo** — blocos bem estruturados são o que faz o modelo achar a resposta certa.
  - Configuração usada: fragmentação **automático**, modo de índice **alta qualidade**, embedding OpenAI `large`, pesquisa **vetorial** (as outras opções são por texto e híbrida).
  - Cada bloco pode ser aberto e editado, inclusive acrescentando palavras-chave.
  - Teste de recuperação retorna score por bloco: perto de 0 = match fraco, perto de 1/100 = match forte (exemplo real: 0,51 para "matriz SWOT"; 0,39/0,38/0,31 para "Flutter Flow").
  - **Top K** = quantos blocos são retornados; **limiar de pontuação** = filtro mínimo de score. Configuração final da aula: Top K 3 e limiar 0,2.
  - Upload também é possível via API.
- **Link:** https://flix.nocodestartup.io/m/lessons/3800

### 4 - PDFs  (00:03:08)
- **Resumo:** Repete o processo com um PDF de perguntas e respostas frequentes do atendimento. O foco é a fragmentação personalizada: como o PDF foi escrito com `#` antes de cada pergunta, esse caractere é usado como identificador de segmento para o Dify cortar os blocos exatamente onde se quer. No fim, o teste de recuperação mostra a busca cruzando resultados da planilha e do PDF.
- **Pontos-chave:**
  - PDF bagunçado ou muito grande faz o Dify misturar/desorganizar as informações — funciona, mas performa pior.
  - Solução: preparar o PDF com um delimitador (aqui `#`) e usar o modo **personalizado** informando esse identificador.
  - Também se define o número máximo de tokens por bloco na fragmentação personalizada (o instrutor cita 1.000 como teto usado).
  - Demais configurações mantidas iguais às da planilha (alta qualidade, mesmo embedding), depois "Salvar e processar".
  - Busca por "link formação" retornou bloco com 0,64 de score, puxando conteúdo da planilha e do PDF.
- **Link:** https://flix.nocodestartup.io/m/lessons/3801

### 5 - Sites  (00:04:26)
- **Resumo:** Terceira fonte: conteúdo de site, via integração do Dify com o Firecrawl. Mostra como criar a conta, pegar a API Key no dashboard e configurar a integração dentro do Dify. Depois roda o scraping de um post de blog, decide não rastrear subpáginas e processa o resultado como nova base. Também corrige uma organização da aula anterior, separando perguntas e respostas e mapa de aulas em bases distintas.
- **Pontos-chave:**
  - Firecrawl é serviço à parte: exige conta e API Key (campo de URL base é opcional); o plano gratuito dá 500 créditos, aproximadamente 500 páginas.
  - Ao rodar, o Dify pergunta se quer rastrear subpáginas, com controle de profundidade máxima de camadas e regras para incluir/excluir caminhos.
  - Cuidado com o consumo de créditos: rastrear documentação inteira de uma ferramenta estouraria o plano gratuito.
  - Blocos vindos de site ficam naturalmente mais desorganizados que os de planilha — aula usa automático + alta qualidade mesmo assim.
  - Teste de recuperação com "webflow" confirmou que o texto da página foi indexado.
- **Link:** https://flix.nocodestartup.io/m/lessons/3802

### 6 - Teste Final e Aprendizados  (00:05:25)
- **Resumo:** Fecha o módulo plugando as bases criadas no agente. Atualiza o prompt do bot para separar tipos de dúvida e instruir quando acionar a base externa, adiciona as bases no bloco de contexto, ajusta modelo e faz uma bateria de perguntas reais para validar. Termina apontando o uso comercial: treinar bots com o material do próprio negócio ou de clientes.
- **Pontos-chave:**
  - Prompt atualizado separa "dúvidas gerais" de "temos aula sobre esse tema?" e manda acionar a base de conhecimento externo quando necessário, com exemplo de pergunta e resposta padrão embutido.
  - No **contexto** do agente foram adicionadas só as bases de perguntas e respostas e de módulos das aulas — a base do site ficou de fora por não ser útil nesse caso.
  - Ajuste do chat para modo **preciso**; modelo GPT-4o ou GPT-4o mini (o mini é a opção mais barata).
  - Testes feitos: marketplace (respondeu corretamente que não existe módulo), matriz SWOT (achou o módulo certo e devolveu o link), prompts (apontou a masterclass de engenharia de prompt) e link de compra da formação (veio do PDF).
  - Fechamento: a mesma mecânica serve para vender o serviço, usando os materiais do cliente para treinar o bot dele. Próximo módulo entra em funções personalizadas.
- **Link:** https://flix.nocodestartup.io/m/lessons/3803

## Pegadinhas e insights

- **Qualidade do bloco > volume de dados.** O recado central do módulo: garantir que cada bloco esteja bem estruturado é o que determina se a LLM acha a resposta certa. Planilha bem organizada ganha de PDF corrido.
- **Prepare o documento antes do upload.** O truque do `#` no PDF mostra que vale editar a fonte para inserir delimitadores e então usar fragmentação personalizada, em vez de confiar no corte automático.
- **PDF gigante ou bagunçado degrada o RAG** — o instrutor avisa que funciona, mas o Dify pode misturar informações.
- **Top K e limiar são os dois botões de precisão.** Top K baixo (1 a 3) para respostas cirúrgicas; limiar alto corta blocos com score fraco. A aula testa 0,35 e acaba deixando 0,2 para não ficar restritivo demais.
- **Uma base por assunto.** Na aula 5 o instrutor conta que tinha jogado dois conhecimentos na mesma base vetorial e refez, separando em duas — decisão de arquitetura que depois permite escolher quais bases entram no contexto do agente.
- **Nem toda base precisa ir para o bot.** A base do site foi criada mas deliberadamente não anexada ao agente de atendimento.
- **Firecrawl tem custo real.** 500 créditos no plano gratuito, cada página consumindo crédito; rastrear subpáginas com profundidade alta estoura rápido.
- **Alta qualidade no índice custa quase nada** para documentos normais, segundo o instrutor — só documentos muito grandes podem pesar.
- **Custo de modelo:** GPT-4o entrega bem, mas o mini é indicado como alternativa mais barata para o agente de atendimento.
