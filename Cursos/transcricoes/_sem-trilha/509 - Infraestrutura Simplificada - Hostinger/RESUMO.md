# Infraestrutura Simplificada - Hostinger

(sem trilha) | 7 aulas | ~26 min (00:26:12) | iniciante

> Como sair do n8n Cloud e hospedar o próprio n8n em VPS serverless na Hostinger, já em modo fila, sem mexer com código.

## O que você sai sabendo fazer
- Escolher entre n8n Cloud, hospedagem serverless (Hostinger, Railway, Cloudify) e VPS técnica (Hetzner, DigitalOcean) com base em custo, facilidade e nível técnico.
- Explicar a diferença entre modo padrão e modo fila (queue mode) do n8n e por que o modo fila é o padrão recomendado para escala.
- Contratar um plano de VPS na Hostinger já com o template "n8n QMode" (modo fila) e servidor no Brasil.
- Concluir o setup: criar senha, ativar malware scanner, criar a conta do n8n e ativar a licença gratuita por e-mail.
- Atualizar a versão do n8n hospedado via terminal do painel com três comandos Docker Compose.
- Criar credenciais OAuth do Google no Google Cloud Console para usar Drive, Sheets, Docs, Gmail e Calendar dentro do n8n.

## Stack e ferramentas
- **n8n** (Cloud e auto-hospedado), modo padrão e modo fila
- **Hostinger** — VPS com template de n8n, painel com Manage App / Manage VPS / Browse Terminal
- **Redis** — banco usado pelo n8n no modo fila (empilhamento de execuções)
- **Docker Compose** — `docker-compose pull`, `docker-compose down`, `docker-compose up -d`
- **Google Cloud Console** — APIs, tela de consentimento OAuth, cliente OAuth (Client ID + Client Secret)
- **APIs do Google**: Drive, Sheets, Calendar (mesmo processo para Docs e Gmail)
- Alternativas citadas para comparação: Railway, Cloudify, Hetzner, DigitalOcean

## Pré-requisitos
Saber o básico de n8n (criar workflows, adicionar nodes) — o curso trata só da infraestrutura, não do uso da ferramenta. Exige cartão/meio de pagamento para contratar o plano e uma conta Google para a parte de credenciais.

## Aula a aula

### 1.1 - Introdução à Infraestrutura Sem Servidor  (00:03:48)
- **Resumo:** Abre o curso justificando por que vale a pena tirar as automações do SaaS e colocá-las em infraestrutura própria. O instrutor apresenta um gráfico que posiciona as opções num eixo de "gasta mais dinheiro" versus "gasta mais tempo/conhecimento técnico". A conclusão é que a camada serverless é o meio-termo ideal para quem não é dev.
- **Pontos-chave:**
  - Ganhos citados: menor custo de operação, mais performance/escala e mais controle para investigar problemas.
  - n8n Cloud é bom para aprender rápido (dias gratuitos), mas fica caro na operação real.
  - Serverless (rápido, sem conhecimento técnico): Hostinger, Railway, Cloudify.
  - VPS técnica (mais barata pelo que entrega, mas exige código e manutenção): Hetzner, DigitalOcean.
  - n8n é open source — daí ser possível auto-hospedar.
- **Link:** https://flix.nocodestartup.io/m/lessons/5307

### 1.2 - Comparativo das Melhores Hospedagens  (00:04:57)
- **Resumo:** Comparação direta entre Hostinger, Railway e Hetzner em preço, hardware e facilidade. O instrutor mostra que os valores de entrada são parecidos e que o desempate real é a curva de aprendizado. Fecha recomendando a Hostinger como escolha padrão da NoCode Startup para quem está começando.
- **Pontos-chave:**
  - Faixas mensais citadas: Hostinger ~R$30 a R$80/90; Railway ~R$40 a R$100; Hetzner a partir de ~R$30 (com planos bem mais caros e melhor custo-benefício de performance).
  - Contrato anual dá desconto relevante em relação ao mensal.
  - Configuração considerada mínima para serviço profissional: 2 núcleos de CPU, 8 GB de RAM, 100 GB de disco.
  - Diferenciais da Hostinger citados: instalação "num botão", suporte brasileiro em português, servidor com baixa latência e possibilidade de hospedar outros produtos no mesmo ambiente.
  - Todas as opções comparadas oferecem modo fila do n8n.
- **Link:** https://flix.nocodestartup.io/m/lessons/5308

### 1.3 - Modo Padrão versus Modo Fila  (00:01:38)
- **Resumo:** Explica os dois modos de execução do n8n. No modo padrão o processamento das requisições acontece simultaneamente, o que é rápido com pouco volume mas cria gargalos. No modo fila as execuções são empilhadas e processadas de forma organizada, entregando muito mais escala. O instrutor mostra o diagrama da documentação oficial do n8n para ilustrar.
- **Pontos-chave:**
  - Modo padrão: bom só para poucas requisições; gera gargalo e limitação.
  - Modo fila: mais performático e escalável quando há muitos workflows rodando ao mesmo tempo.
  - O modo fila usa **Redis** para armazenar a fila antes da execução pelo n8n.
  - Na hospedagem, escolher o modo fila já provisiona n8n + Redis automaticamente.
  - Regra prática do instrutor: sempre escolher modo fila.
- **Link:** https://flix.nocodestartup.io/m/lessons/5309

### 2.1 - Introdução ao Plano Hostinger  (00:02:09)
- **Resumo:** Tour pela página de planos de VPS para n8n da Hostinger. A diferença entre os planos está basicamente em núcleos de CPU e memória RAM. O instrutor indica qual plano escolher conforme o estágio (aprendendo versus atendendo clientes) e destaca o que vem incluso.
- **Pontos-chave:**
  - Planos variam em 1, 2, 4 e 8 núcleos de CPU, com RAM proporcional.
  - Para projetos profissionais/atendimento a clientes: mínimo de 4 núcleos e 16 GB de RAM.
  - Para começar/testar: o plano mais barato já entrega n8n hospedado.
  - Incluso: workflows ilimitados (limitação que existe no n8n Cloud), nodes da comunidade e n8n em modo fila.
  - Contratação mensal ou anual, com o anual mais barato.
- **Link:** https://flix.nocodestartup.io/m/lessons/5310

### 2.2 - Instalando o N8N em Modo Fila na Hostinger Passo a Passo  (00:04:51)
- **Resumo:** Instalação completa acompanhada na tela, do checkout até o n8n rodando. O ponto crítico é escolher o template "n8n QMode" em vez do n8n padrão sugerido pela plataforma. Depois do provisionamento, o instrutor cria a conta do n8n e ativa a licença gratuita recebida por e-mail.
- **Pontos-chave:**
  - No checkout: escolher período (24 ou 12 meses dão mais desconto; ele usa 1 mês só para testar — total de 43 na demo) e, com 12 meses, ganha domínio grátis.
  - Backups automáticos diários: opcional, recomendado para uso profissional.
  - Localização do servidor: escolher **Brasil** pela latência.
  - Sistema operacional/template: a plataforma sugere o n8n padrão — trocar para **n8n QMode** (modo fila).
  - Pós-compra: definir senha, ativar o malware scanner, clicar em "Finish setup" e aguardar o provisionamento.
  - No painel: **Manage App** abre o n8n; **Manage VPS** dá overview, gestão e manutenção da máquina.
  - Dentro do n8n: criar conta, pedir "Send me a free license key", pegar o código no e-mail e ativar a licença.
- **Link:** https://flix.nocodestartup.io/m/lessons/5311

### 2.3 - Como Atualizar sua Versão do N8N  (00:01:38)
- **Resumo:** Mostra a rotina de atualização do n8n auto-hospedado, que não é automática — quem hospeda precisa rodar o update. O caminho é o terminal embutido no painel da Hostinger e três comandos de Docker Compose em sequência. No fim, dá para conferir a versão ativa dentro do próprio n8n.
- **Pontos-chave:**
  - Acesso pelo botão **Browse Terminal** no painel (abre um terminal preto no navegador).
  - Sequência: `docker-compose pull` → `docker-compose down` → `docker-compose up -d`.
  - O efeito é remover a versão antiga e subir a nova imagem.
  - Se já estiver na última versão, o `pull` não muda nada.
  - Conferir a versão pelo **What's New** no rodapé do n8n.
- **Link:** https://flix.nocodestartup.io/m/lessons/5312

### 2.4 - [Extra] Integrando os Serviços Google ao N8N  (00:07:11)
- **Resumo:** Aula extra com o passo a passo de criação das credenciais OAuth do Google para usar Drive, Sheets, Docs, Gmail e Calendar no n8n. Todo o trabalho acontece no Google Cloud Console: criar projeto, ativar as APIs, montar a tela de consentimento, gerar o cliente OAuth e publicar o app. No fim, a credencial é conectada de volta no n8n e testada com um trigger do Drive.
- **Pontos-chave:**
  - O processo é idêntico para n8n Cloud e auto-hospedado (a demo é no Cloud).
  - Google Cloud Console → criar novo projeto → **APIs e serviços** → ativar uma API por serviço (Google Drive API, Google Sheets API, Google Calendar API...).
  - Criar a **tela de permissão/consentimento**: nome do app, e-mail de suporte e público **externo**.
  - Criar **cliente OAuth** do tipo "aplicativo da web" e colar a URI de redirecionamento que o n8n fornece no campo de URIs autorizadas.
  - Copiar **Client ID** e **Client Secret** do Google para a credencial no n8n.
  - Antes de logar, ir em público-alvo → **publicar app** → enviar para produção; senão o login falha.
  - No login, passar pelo aviso de app não verificado (avançado → acessar) e marcar todos os escopos.
- **Link:** https://flix.nocodestartup.io/m/lessons/5313

## Pegadinhas e insights
- **A pegadinha central do curso:** na hora de escolher o template do servidor, a Hostinger sugere o n8n padrão. Trocar manualmente para **n8n QMode** — se passar batido, você fica sem modo fila e sem Redis, e vai ter gargalo quando o volume subir.
- Migrar do n8n Cloud para VPS troca R$150–R$300/mês por algo a partir de ~R$30/mês, e ainda remove o limite de workflows.
- O trade-off da infra é sempre dinheiro versus tempo/conhecimento: Hetzner e DigitalOcean saem mais baratas pela performance, mas cobram em curva de aprendizado e manutenção — o instrutor só as recomenda para quem já é desenvolvedor.
- Régua de hardware: 2 núcleos + 8 GB de RAM é o piso para serviço profissional; 4 núcleos + 16 GB é o recomendado para quem atende cliente com agentes de IA.
- Escolher servidor no Brasil por latência, mesmo que a diferença de preço exista.
- Auto-hospedar significa assumir a atualização: não há update automático, é você quem roda `pull` / `down` / `up -d`.
- Backups automáticos diários são opcionais e ficam de fora se você não marcar — para uso profissional, ative.
- No Google Cloud, dois pontos que costumam quebrar a integração: escolher público **externo** na tela de consentimento e **publicar o app em produção** antes de tentar autenticar.
- Ativar a licença gratuita do n8n exige e-mail correto no cadastro — a chave chega por e-mail.
