# F4.2 - APIs de IA | Seu primeiro MicroSaaS com GPT Vision

Trilha Nocode IA | 12 aulas | ~55 min (00:54:56) | nível iniciante

> Case 100% prático: construir do zero um MicroSaaS de análise nutricional por foto — FlutterFlow no front, Supabase Storage para hospedar a imagem e a API Vision da OpenAI para descrever o prato e estimar calorias, proteínas, carboidratos e gorduras.

## O que você sai sabendo fazer

- Desenhar a arquitetura de um MicroSaaS simples separando front-end (FlutterFlow), back-end de mídia (Supabase Storage) e inteligência (API OpenAI).
- Montar duas telas no FlutterFlow do zero (container 100%, coluna, textos, imagem network, botão, padding, max width, safe area, scrollable).
- Configurar uma API Call POST no FlutterFlow com headers, variáveis dinâmicas, body JSON e JSON Path para extrair só o campo de resposta.
- Criar bucket público e policy no Supabase Storage e usar `Upload/Save Media` para subir a foto e recuperar a URL pública.
- Encadear um Action Flow completo: upload → chamada API → tratamento de sucesso/erro → gravação em Page State → exibição na tela.
- Escrever um prompt de sistema que força o formato de resposta desejado e bloqueia entradas fora do escopo.
- Publicar o app como Web App no FlutterFlow e instalá-lo no celular como PWA.

## Stack e ferramentas

- **FlutterFlow** — construção de telas, API Calls, Actions, Page State, publicação web e PWA (plano gratuito: até 2 API calls e até 3 domínios; marca d'água e publicação nas lojas exigem plano pago).
- **OpenAI API** — endpoint `chat/completions`, modelo GPT-4 Turbo com Vision; chave API via header `Authorization`; `max_tokens` ajustado para 1200.
- **Supabase** — apenas o módulo Storage (bucket público + policy liberada) como hospedagem das fotos, para gerar a URL pública que vai no payload da API.
- Documentação da OpenAI (seção Vision) como referência de URL, headers e estrutura do JSON.

## Pré-requisitos

- Noções básicas de FlutterFlow (o instrutor assume que o aluno já viu a ferramenta em aulas anteriores da formação).
- Conceito de chamada de API (método, endpoint, header, body JSON) já apresentado antes na trilha.
- Conta na OpenAI com crédito: o instrutor recomenda colocar 3 a 4 dólares — não dá para testar no plano gratuito.
- Conta no Supabase (pode ser projeto novo, do zero).

## Aula a aula

### Intro 01 - O que você irá aprender  (00:03:07)
- **Resumo:** Apresenta o projeto do módulo: um app em que a pessoa fotografa o prato e recebe de volta peso por ingrediente, calorias, proteínas, carboidratos e gorduras. Define o que é um MicroSaaS e por que o nicho de dieta/emagrecimento foi escolhido. Conecta as três frentes da formação — produto, SaaS nocode e IA — como método de criação.
- **Pontos-chave:**
  - MicroSaaS = serviço para um nicho específico, resolve 1 ou 2 problemas, escala menor, time enxuto.
  - A tese do produto é a interseção entre uma dor real (dificuldade de calcular macros da dieta) e a tecnologia disponível (GPT Vision).
  - GPT Vision descreve o conteúdo de uma imagem — é isso que viabiliza o app.
  - Objetivo do módulo: sair com o app pronto e saber replicar o padrão para outra ideia.
- **Link:** https://flix.nocodestartup.io/m/lessons/3260

### Intro 02 - Planejamento do App  (00:01:45)
- **Resumo:** Desenha a arquitetura antes de codar. Front-end fica no FlutterFlow (visual e fluxo do usuário), back-end no Supabase servindo só como armazenamento de mídia, e a inteligência vem da OpenAI via API. Fecha o escopo em duas telas.
- **Pontos-chave:**
  - Supabase entra exclusivamente para guardar a foto e devolver uma URL acessível — não há banco de dados no projeto.
  - Tela 1: boas-vindas. Tela 2: upload da foto + exibição das informações nutricionais.
  - Escopo mínimo proposital: app didático, dois passos de usuário.
- **Link:** https://flix.nocodestartup.io/m/lessons/3259

### Design 01 - Layout da Tela Boas Vindas  (00:05:27)
- **Resumo:** Cria o projeto "App Food AI" no FlutterFlow sem Firebase e monta a home. A estrutura é container em 100% de largura e altura, com uma coluna dentro contendo título, subtítulo, imagem e botão. Ajusta tipografia, cores e espaçamento até a tela ficar apresentável.
- **Pontos-chave:**
  - Desabilitar Firebase na criação do projeto; clicar em Start Building.
  - Remover o fill do container principal (conta-gotas → Clear Color) e desligar a Safe Area.
  - Paleta: marrom `#844D3A` para o título; subtítulo no mesmo marrom com opacidade reduzida (~70).
  - Título em 24px bold, alinhado ao centro; subtítulo em 12–14px; padding de 12 na imagem.
  - Imagem inserida via opção **Network** com Box Fit ajustado para encaixar.
- **Link:** https://flix.nocodestartup.io/m/lessons/3261

### Design 02 - Layout da Tela AnaliseFoto  (00:07:21)
- **Resumo:** Cria a segunda tela (Create Blank, "Analisador de imagem") com o card de upload e a área de resposta. Aplica um limite de largura no container para o app ficar centralizado e legível também no desktop. Monta dentro do card a imagem placeholder, o texto de instrução e o botão de tirar foto, além do texto que depois receberá a descrição da IA.
- **Pontos-chave:**
  - `max width` de 550 no container + alinhamento central = responsividade barata para desktop.
  - Regra de espaçamento do instrutor: sempre múltiplos de 8 (padding 24 vertical, 16 horizontal, 16 e 8 entre elementos).
  - Card interno: fill branco (`FFF`), border radius 12, elevation 2, altura ~260.
  - Ordem de montagem sempre igual: container → coluna → elementos.
  - Texto de resposta alinhado à esquerda, com conteúdo provisório "descrição da foto".
- **Link:** https://flix.nocodestartup.io/m/lessons/3262

### Design 03 - Precisamos do seu feedback!  (00:00:43)
- **Resumo:** Aula institucional, sem conteúdo técnico. O instrutor pede um feedback de um minuto sobre a formação pelo link abaixo do vídeo, com foto de perfil e comentário detalhado sobre estrutura e didática.
- **Pontos-chave:**
  - Não há passo de construção nesta aula.
- **Link:** https://flix.nocodestartup.io/m/lessons/3257

### API GPT 01 - Configurar chamada API no Flutterflow  (00:07:24)
- **Resumo:** Parte da documentação Vision da OpenAI para entender o formato da requisição e replica isso numa API Call do FlutterFlow. Configura método, endpoint, headers, chave como variável, body JSON copiado da doc, e testa até receber status 200. Termina salvando um JSON Path para isolar só o texto da resposta.
- **Pontos-chave:**
  - Método **POST**, endpoint `chat/completions`; headers `Content-Type` e o header de autorização com a chave.
  - A chave vira variável dinâmica (`API Key`, tipo string) em vez de ficar hardcoded no header.
  - Body do tipo JSON com `role: user`, o texto da pergunta e a `image_url`.
  - Em **Advanced Settings**, marcar o decode UTF-8 — sem isso acentos e til não são lidos corretamente.
  - Response & Test: retorno **200** = sucesso; depois usar **Add JSON Path** salvando `$.choices[...].message.content` com o nome "resposta".
  - Plano gratuito do FlutterFlow permite 2 API calls; mais que isso exige plano pago.
- **Link:** https://flix.nocodestartup.io/m/lessons/3263

### API GPT 02 - Configurar Action Flutterflow  (00:08:16)
- **Resumo:** Cria a infraestrutura de storage no Supabase e conecta tudo no Action Flow do botão. Sobe o bucket público com policy liberada, habilita a integração Supabase no FlutterFlow com URL e chave do projeto, e encadeia upload → chamada API → tratamento de erro/sucesso → atualização do Page State que alimenta o texto da tela.
- **Pontos-chave:**
  - Supabase → Storage → **New Bucket** "imagens" com **Public bucket** marcado; em Policies, criar política via *Powerful Customization* liberando select/insert/update/delete.
  - Habilitar Supabase no FlutterFlow (engrenagem → Supabase) colando URL e chave de **Project Settings → API**, depois **Get Schema**.
  - Ação 1: **Upload/Save Media** com Upload Type = Supabase, bucket "imagens", pasta "testes OpenAI", origem câmera ou galeria, largura máxima reduzida para acelerar.
  - Ação 2: **API Call** apontando para a chamada GPT Vision, com output nomeado.
  - Ramo de falha: Informational Dialog exibindo o **Raw Body Text** do output para depurar, seguido de Terminate.
  - Ramo de sucesso: **Update Page State** gravando o JSON Path "resposta" numa variável de página tipo string (valor padrão nulo), que o texto da tela lê dinamicamente.
- **Link:** https://flix.nocodestartup.io/m/lessons/3264

### API GPT 03 - Atualizações Chamada API  (00:05:21)
- **Resumo:** Torna a URL da imagem dinâmica no body (variável string em vez de link fixo) e substitui a pergunta genérica por um prompt de nutricionista com formato de saída definido. Ajusta o limite de tokens e corrige o JSON antes de testar com uma foto real achada no Google.
- **Pontos-chave:**
  - Nova variável `URL da imagem` (string) arrastada para dentro do body no lugar do link fixo.
  - Prompt persona: nutricionista que descreve o prato em até 5 linhas e depois lista, por ingrediente, peso aproximado + calorias, proteínas, carboidratos e gorduras, com somatório final.
  - Guarda-corpo no prompt: se a foto não for de comida, responder "só sei analisar foto de alimentos".
  - `max_tokens` = **1200**, porque a resposta formatada é longa.
  - O prompt precisa ficar tudo numa linha só e com as aspas corretas, senão o JSON quebra.
  - Teste feito colando a URL de uma imagem pública (botão direito → copiar endereço da imagem) — retorno 200 com a análise formatada.
- **Link:** https://flix.nocodestartup.io/m/lessons/3265

### API GPT 04 - Testes Finais  (00:05:57)
- **Resumo:** Amarra as pontas soltas e testa o fluxo ponta a ponta no preview. Passa a URL do arquivo recém-enviado para a variável da API, faz o placeholder da imagem virar a foto do usuário, adiciona a navegação que faltava no botão da home e corrige o corte do texto de resposta.
- **Pontos-chave:**
  - Valor da variável `URL imagem` = **Uploaded File URL**, gerado pelo Supabase logo após o upload.
  - Mesma referência aplicada à imagem do card (Network + Uploaded File URL), com uma URL fixa como valor de fallback quando não há upload.
  - Faltava a Action **Navigate to** no botão "Começar" da home apontando para o Analisador de Imagens.
  - Marcar **scrollable** na coluna principal — sem isso a resposta longa estoura e não é lida.
  - No preview do FlutterFlow, manter o zoom em 100% para evitar bug de renderização.
  - Testes com prato de comida e com frutas retornaram peso, calorias, proteínas, carboidratos, gorduras e somatório.
- **Link:** https://flix.nocodestartup.io/m/lessons/3266

### Publicação App 01 - Web App  (00:04:03)
- **Resumo:** Publica o app na web pelo FlutterFlow. Configura URL, metadados de SEO, ícone e a opção PWA, além de forçar o app a abrir sempre em light mode. Mostra também que cada teste vai empilhando arquivos no bucket do Supabase e valida o app rodando no desktop.
- **Pontos-chave:**
  - **Settings → Web Publishing**: definir subdomínio, título e descrição SEO; marcar a opção PWA (obrigatória para instalar no celular depois).
  - Marcar a inicialização alternativa do engine para carregar mais rápido.
  - Action `Set Dark Mode Settings → Light Mode` colada em ambas as páginas para ignorar o tema do dispositivo.
  - Ícone do app definido em **App Details → Assets**.
  - Plano gratuito do FlutterFlow: limite de 3 domínios (foi preciso remover domínios antigos para publicar) e a marca d'água só sai no plano Pro.
  - Cada upload de teste fica guardado na pasta do bucket, já que a API precisa do link público da imagem.
- **Link:** https://flix.nocodestartup.io/m/lessons/3267

### Publicação App 02 - PWA  (00:04:45)
- **Resumo:** Instala o app publicado no celular como PWA e testa a captura pela câmera, que é o uso real do produto. Valida o guard-rail do prompt fotografando algo que não é comida e depois roda a análise num prato montado, conferindo a resposta completa em tela cheia.
- **Pontos-chave:**
  - No iPhone: botão de compartilhar do Safari → **Adicionar à Tela de Início**; no Android o caminho equivalente existe e é análogo.
  - PWA não é app nativo, mas roda em tela cheia sem a interface do navegador — usabilidade bem melhor.
  - Publicar nas lojas (Apple/Google Play) é possível no FlutterFlow, mas exige plano pago; seria o caminho ideal para acessar recursos nativos.
  - No celular o botão passa a oferecer tirar foto na hora, não só upload da galeria.
  - Foto fora do escopo retornou exatamente a mensagem definida no prompt, confirmando o guard-rail.
  - Uma chamada falhou e funcionou na repetição — a resposta demorar um pouco é sinal de que está processando.
  - Ideia de evolução sugerida: acrescentar meta de calorias e acompanhar o consumo ao longo do tempo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3268

### Conclusão 01 - Aprendizados  (00:00:47)
- **Resumo:** Fecha o módulo reforçando que o padrão aprendido (FlutterFlow + chamada de API OpenAI) serve para qualquer funcionalidade de IA, não só análise de imagem. Reposiciona o foco em resolver a dor de um nicho e anuncia cases mais completos nas aulas seguintes.
- **Pontos-chave:**
  - O mesmo esqueleto vale para gerador de texto, gerador de imagem e outros serviços da OpenAI.
  - A escolha do problema do nicho importa mais que a tecnologia usada.
- **Link:** https://flix.nocodestartup.io/m/lessons/3269

## Pegadinhas e insights

- **Custo obrigatório:** a API da OpenAI não tem tier gratuito utilizável aqui; o instrutor orienta colocar 3–4 dólares de crédito antes de testar.
- **Acentuação quebrada:** sem marcar o decode UTF-8 em Advanced Settings da API Call, a resposta em português vem com caracteres corrompidos.
- **JSON quebra fácil:** o prompt colado no body precisa ficar em uma linha só e com as aspas intactas — espaços e quebras de linha geram erro de formato.
- **Texto cortado:** a resposta do GPT é longa; sem `scrollable` na coluna principal ela fica ilegível na tela.
- **Preview com bug:** manter o zoom do preview do FlutterFlow em 100% (o zoom do navegador não é o mesmo controle).
- **Por que Supabase:** a API Vision consome a imagem por URL pública, então é preciso hospedar a foto antes de chamar a API — daí o bucket público como pré-requisito técnico, não como banco de dados.
- **Segurança do bucket:** a policy criada libera tudo (select/insert/update/delete) para simplificar a aula — não é configuração de produção.
- **Debug embutido:** exibir o Raw Body Text no ramo de erro da API Call é o atalho para descobrir o que a OpenAI devolveu quando algo falha.
- **Limites de plano do FlutterFlow:** 2 API calls e 3 domínios no gratuito; remoção da marca d'água e publicação nas lojas só no pago.
- **Instabilidade esperada:** uma chamada pode falhar e funcionar na tentativa seguinte; latência maior costuma indicar sucesso a caminho.
- **Formato de saída é prompt, não código:** toda a estrutura da resposta (descrição em 5 linhas, ingrediente como título, macros um embaixo do outro, somatório final) e o guard-rail de "só analiso alimentos" vêm do prompt, não da lógica do app.
