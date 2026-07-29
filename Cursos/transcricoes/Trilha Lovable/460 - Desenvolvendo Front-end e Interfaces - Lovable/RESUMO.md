# Desenvolvendo Front-end e Interfaces | Lovable

Trilha Lovable | 8 aulas | ~32 min (00:31:54) | nível iniciante

> Fundamentos rápidos de design (cor, espaçamento, tipografia, padrões) somados ao fluxo completo de criar e publicar uma landing page de portfólio no Lovable, do planejamento estratégico ao domínio próprio.

## O que você sai sabendo fazer

- Montar uma paleta de cores coerente aplicando roda de cores, relações (complementar/análoga/tríade) e a regra 60/30/10.
- Aplicar grid de 8 pontos, hierarquia tipográfica (H1/H2/body/botão) e a Lei de Jacob para não inventar padrões que confundem o usuário.
- Percorrer o fluxo baixa fidelidade → wireframe → alta fidelidade, validando com o cliente a cada etapa.
- Usar o framework NoCode Startup (Notion) para planejar visão estratégica, insights de mercado e arquitetura técnica antes de gerar código.
- Transformar uma referência de site em prompt detalhado usando o ChatGPT e gerar a página no Lovable.
- Iterar a página gerada (imagens, cores, textos, links) economizando créditos e publicar com domínio próprio via Custom Domains.

## Stack e ferramentas

- **Lovable** — geração da interface/landing page, preview responsivo, publicação (`*.lovable.app`) e Custom Domains.
- **ChatGPT** — refino do escopo da página, geração do wireframe e construção do prompt final (recomendado em inglês).
- **Notion** — template duplicável do framework NoCode Startup (5 etapas).
- **Dribbble / Behance** — mineração de referências de design e benchmark; a referência escolhida no case era um template Framer.
- **Geradores de paleta** — gerador de paleta de cores (nova paleta com a tecla espaço), roda de cores da Adobe, UI Colors.
- **Guias de design** — Material Design, Human Interface Guidelines, Bootstrap.
- **Tipografia** — Roboto / Roboto Mono (antiga da NoCode Startup) → Inter (atual).
- **Wireframe de baixa/média fidelidade** — papel, PowerPoint ou Miro.
- **Hostinger** (ou registrador brasileiro para `.com.br`) — compra e gestão do domínio.
- Supabase é citado só como integração nativa do Lovable; não é usado neste curso.

## Pré-requisitos

- Conta no Lovable (o instrutor usa conta de embaixador; o plano gratuito serve, com créditos limitados que renovam).
- Conta no Notion para duplicar o template do framework.
- Módulo anterior da trilha, onde o framework NoCode Startup de 5 etapas é ensinado — o curso o trata explicitamente como pré-requisito e pede para não pular.
- Domínio próprio (opcional) e plano pago do Lovable, se quiser publicar fora do subdomínio `lovable.app`.

## Aula a aula

### 1.1 - Introdução  (00:01:36)
- **Resumo:** Abertura do módulo, explicando que a trilha cobre primeiro fundamentos de design e depois a construção da primeira interface no Lovable. O escopo é deliberadamente só front-end: banco de dados e back-end ficam para módulos futuros.
- **Pontos-chave:**
  - Lovable é apresentado como a melhor opção para interfaces e projetos simples; ferramentas para projetos complexos vêm depois.
  - Tem integração nativa com Supabase (não usada aqui) e é a ferramenta que mais cresce no mercado.
  - Entregável do módulo: um site/página criado do zero, com passo a passo replicável.
- **Link:** https://flix.nocodestartup.io/m/lessons/4796

### 2.1 - Cores e Identidade Visual  (00:05:53)
- **Resumo:** Explica por que entender design importa mesmo com a IA gerando telas: é o vocabulário para dialogar com ela e pedir melhorias certas. Separa UI (cor, tipografia, hierarquia, design gráfico) de UX (design de interação, wireframe, arquitetura da informação, pesquisa de usuário) e mergulha na parte de cores.
- **Pontos-chave:**
  - Roda de cores: primárias → secundárias → terciárias; relações complementar, análoga, tríade, semicomplementar, tetraédrica/quadrada.
  - Regra 60/30/10: 60% cor primária, 30% secundária, 10% cor de destaque (botões, CTAs).
  - Exemplo prático com a paleta da NoCode Startup (escuros, verde brilhante, azul turquesa + secundárias de destaque) e variações por marca/formação.
  - Ferramentas para gerar paleta: gerador que sorteia cores conectadas com a tecla espaço, roda de cores da Adobe e UI Colors (já entrega a escala pronta para aplicar).
  - O objetivo não é decorar teoria e sim ter noção suficiente para formular o pedido certo para a IA.
- **Link:** https://flix.nocodestartup.io/m/lessons/4797

### 2.2 - Padrões de Design  (00:05:23)
- **Resumo:** Cobre espaçamento, tipografia e convenções de layout. Usa Apple/Samsung como exemplo de respiro visual e defende seguir padrões consolidados em vez de inventar. Fecha com a Lei de Jacob e a anatomia padrão de uma landing page.
- **Pontos-chave:**
  - Espaço em branco = interface mais clean; grid de 8 pontos (8, 16, 24, 32, 48) como régua de espaçamento.
  - Tipografia: buscar referências e manter consistência de hierarquia (H1, H2, body, botão). Case da NoCode Startup migrando de Roboto/Roboto Mono para Inter.
  - Lei de Jacob: o usuário passa a maior parte do tempo em outros sites e espera que o seu funcione igual.
  - Estrutura padrão de landing: Hero (título + explicação do que a empresa faz + CTA), seções, rodapé. Em apps: sidebar ou barra superior, dark/light mode.
  - Materiais de estudo indicados: Material Design, Human Interface Guidelines, Bootstrap.
  - Se o projeto precisa de identidade visual completa e consistente, contrate um designer; aqui o foco é MVP e telas rápidas.
- **Link:** https://flix.nocodestartup.io/m/lessons/4798

### 2.3 - Fluxos de Criação de Telas  (00:02:05)
- **Resumo:** Apresenta a escada de fidelidade no desenho de telas: rascunho no papel, wireframe em blocos, média fidelidade e alta fidelidade. Enfatiza validação incremental com o cliente e mostra como esse artefato alimenta a IA.
- **Pontos-chave:**
  - Baixa fidelidade (papel) → wireframe em blocos brancos/cinzas (PowerPoint, Miro ou similar) → média → alta fidelidade.
  - Nunca pular etapas sem feedback do cliente; validar a cada nível evita retrabalho caro no fim.
  - Wireframe serve para visualizar a organização das telas antes de qualquer pixel.
  - Truque com IA: mandar um print da alta fidelidade para o ChatGPT descrever cores e elementos, e usar essa descrição como base do prompt no Lovable.
- **Link:** https://flix.nocodestartup.io/m/lessons/4799

### 3.1 - Visão Estratégica do Projeto  (00:05:24)
- **Resumo:** Começa o case prático: um portfólio pessoal só de front-end. Retoma o framework NoCode Startup de 5 etapas (visão estratégica, insights de mercado, arquitetura técnica, criação iterativa, lançamento/PDCA) e preenche a primeira etapa no template do Notion.
- **Pontos-chave:**
  - Framework em 5 etapas; num projeto simples de uma página, várias sub-etapas (modelagem de dados, agentes, integrações) são puladas.
  - Etapa 1 preenche: problema identificado, solução, personas/usuários, requisitos funcionais e custo das ferramentas.
  - Case: centralizar identidade profissional numa landing com o que faz, principais projetos e um CTA de contato.
  - Personas do case: empresas que precisam de soluções de IA e empresas que querem educação em IA para funcionários.
  - Custos levantados: créditos do Lovable + hospedagem/domínio (~R$50 por ano no exemplo).
  - O template do Notion tem botão de duplicar; o framework é ensinado no módulo anterior.
- **Link:** https://flix.nocodestartup.io/m/lessons/4800

### 3.2 - Tendências de Mercado  (00:04:17)
- **Resumo:** Etapa 2 do framework: pesquisar benchmark e referências de design antes de construir. Escolhe um portfólio minimalista como referência única e usa o ChatGPT para converter essa referência em um prompt estruturado para o Lovable.
- **Pontos-chave:**
  - Fontes de referência: Dribbble e Behance; a referência escolhida era um projeto feito em Framer.
  - Critério de escolha: simples, clean, direto ao ponto — com foto, CTAs de redes, experiência, projetos, formação, ferramentas e contato.
  - Pedido ao ChatGPT: gerar um prompt bem detalhado para o Lovable com o objetivo de copiar aquele site, passando o link.
  - Complemento decisivo do pedido: "vou incluir minhas próprias informações de cada seção, vá me perguntando que eu vou preenchendo" — a IA entrevista seção por seção.
  - É possível remover seções que não interessam durante a entrevista; o resultado final é um prompt único pronto para colar.
- **Link:** https://flix.nocodestartup.io/m/lessons/4801

### 3.3 - Criação no Lovable  (00:04:37)
- **Resumo:** Etapa 3 (arquitetura técnica, aqui reduzida a fluxo de telas e prompts) e a geração efetiva da página. Cola o prompt final no Lovable, avalia o resultado e começa o ciclo de refinamento conversacional.
- **Pontos-chave:**
  - Num site sem back-end não há mapeamento de processos, modelagem de dados, agentes nem integrações de API — só fluxo de telas e prompts.
  - Teste do instrutor: o prompt em inglês com o conteúdo em português deu o melhor equilíbrio de resultado.
  - O Lovable entregou a estrutura completa, escolheu imagem sozinho (nenhuma foi enviada) e já saiu responsivo — dá para conferir nas visões desktop, tablet e celular.
  - Refinamentos feitos por conversa: trocar imagem de perfil, ajustar textos, corrigir links, subir logos, acertar o verde da paleta.
  - Economia de créditos: fazer uma lista das melhorias e mandar tudo de uma vez, em vez de pedidos avulsos.
  - Mesmo prompt pode gerar resultados diferentes entre pessoas; ajuste por conversa até chegar no desejado.
- **Link:** https://flix.nocodestartup.io/m/lessons/4802

### 3.4 - Publicação com Domínio Próprio  (00:02:39)
- **Resumo:** Fecha o case publicando o site. Mostra o link gratuito do Lovable e o caminho para conectar um domínio personalizado, além de indicar onde comprar o domínio. Encerra apontando que os próximos módulos unem front-end e back-end.
- **Pontos-chave:**
  - Publicação gratuita sai no subdomínio `*.lovable.app`; domínio próprio exige plano pago.
  - Caminho no Lovable: **Custom Domains** — dá para comprar domínio ali ou conectar um existente.
  - O Lovable detecta automaticamente o provedor de hospedagem e faz a integração; no exemplo detectou a Hostinger sem configuração manual extra.
  - Onde comprar: Hostinger (barato e fácil de manter) ou registrador brasileiro para `.com.br`.
  - Resultado final já responsivo em desktop e celular; é possível fazer sites de múltiplas páginas no Lovable.
- **Link:** https://flix.nocodestartup.io/m/lessons/4803

## Pegadinhas e insights

- **Prompt em inglês, conteúdo em português.** Após testes, foi o formato com melhor consistência de resposta no Lovable. Se o padrão de saída estiver ruim, traduzir o prompt para inglês é a primeira tentativa.
- **Créditos são o recurso escasso.** Agrupe todas as correções numa lista e envie de uma vez; pedidos fragmentados queimam crédito. Créditos zeram no dia seguinte no plano usado.
- **Domínio próprio é feature de plano pago.** No plano gratuito você fica no `lovable.app`.
- **A referência é o que determina o resultado.** "Tudo depende da referência" — não tentar inovar do zero; minerar Dribbble/Behance, escolher uma referência forte e pedir ao ChatGPT para transformá-la em prompt.
- **Não pule a validação com o cliente entre níveis de fidelidade.** Confirmar rascunho antes do wireframe e wireframe antes da alta fidelidade evita retrabalho.
- **Lei de Jacob acima da criatividade solta.** Padrão de mercado (Hero + CTA, sidebar, dark/light mode) mantém o usuário mais tempo; design "diferentão" atrapalha.
- **A IA já segue bons padrões (8pt grid, hierarquia) sozinha** — mas sem o vocabulário de design você não consegue pedir a correção certa quando ela erra.
- **Planejar antes de construir.** O framework existe justamente para não gerar retrabalho depois; mesmo num projeto de uma página, preencha a visão estratégica.
- **Saída não determinística.** O mesmo prompt pode produzir layouts bem diferentes; conte com rodadas de ajuste conversacional.
- **Escopo do curso:** só front-end. Nada de banco, autenticação ou back-end — isso vem nos módulos seguintes da trilha.
