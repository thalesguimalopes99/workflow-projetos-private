# F5.1 - Planejando seu Micro-SaaS

Trilha Nocode IA | 8 aulas | ~38 min (00:38:34) | nível iniciante

> Como planejar um micro-SaaS de ponta a ponta antes de programar: produto (desejado/viável/factível), software, camada de IA e monetização por assinatura — usando um app de finanças pessoais com IA como caso prático.

## O que você sai sabendo fazer

- Aplicar a tríade produto / SaaS no-code / IA no planejamento de um micro-SaaS próprio.
- Definir o JTBD (verbo + ação + contexto) e montar um mapa de empatia da persona com dores e necessidades.
- Preencher um Lean Canvas completo (problema, solução, alternativas, métricas-chave, proposta única de valor, vantagem injusta, canais, persona, custos, receita) e uma matriz SWOT com cruzamentos que geram ações estratégicas.
- Priorizar funcionalidades com o método MoSCoW para chegar num escopo de MVP realista.
- Desenhar a arquitetura técnica do app: front-end, back-end, banco de dados, automações e serviços via API.
- Planejar a integração de IA com function calling ligando chat e WhatsApp ao mesmo banco de dados.
- Mapear o fluxo de assinaturas (gateway + webhook) para liberar/cancelar acesso conforme o pagamento.

## Stack e ferramentas

- **FlutterFlow** — app multiplataforma (web, desktop, mobile); plano Pro citado em ~US$ 35/mês para domínio personalizado e publicação nas lojas.
- **Supabase** — banco de dados / back-end; plano pago citado em ~US$ 25/mês.
- **Make** — automações e webhooks (usado no lugar do back-end do Supabase, que exige código).
- **OpenAI** — camada de IA e function calling; estimativa de ~US$ 15/mês por consumo de créditos.
- **WhatsApp** — segunda interface do produto, conectada ao mesmo banco.
- **Stripe** — gateway de assinaturas (outros citados: Pagar.me, Mercado Pago).
- **Figma / Miro** — protótipo e wireframe de telas.
- **Dribbble / Behance** — mineração de referências visuais.
- Frameworks: Design Thinking, Jobs To Be Done, Mapa de Empatia, Teste da Mãe, Lean Canvas, SWOT, MoSCoW, MVP, PDCA.
- Menção a **Ollama** como alternativa open source/self-hosted à OpenAI (plano B contra encarecimento de IA).

## Pré-requisitos

As aulas assumem que você já viu a **Fase 1** da formação (teoria da tríade no-code + IA, produto desejado/viável/factível) e os módulos anteriores sobre **function calling** com OpenAI. O instrutor pede explicitamente que os módulos sejam feitos na ordem, porque cada app construído se conecta ao anterior.

## Aula a aula

### 1 - O que você irá aprender  (00:02:03)
- **Resumo:** Abertura da Fase 5. Apresenta o projeto-fio-condutor: um micro-SaaS de finanças pessoais integrado com IA, construído do zero juntando tudo o que foi visto nas fases anteriores. Este módulo específico cobre só o planejamento — produto, software e IA — antes de qualquer construção.
- **Pontos-chave:**
  - Projeto de referência: app de gestão de finanças pessoais com assistente de IA.
  - A tríade do no-code com IA (produto · SaaS no-code · IA) sai da teoria da Fase 1 e vira prática aqui.
  - Recomendação forte de seguir os módulos na ordem.
  - A metodologia serve para tirar qualquer ideia própria do papel e chegar nos primeiros clientes.
- **Link:** https://flix.nocodestartup.io/m/lessons/3348

### 2 - Mapa de Empatia  (00:05:21)
- **Resumo:** Primeiro pilar do produto: **desejado**. Antes de qualquer coisa, o produto precisa resolver um problema real. A aula define o JTBD do projeto e desenvolve um mapa de empatia completo de uma persona fictícia, mostrando na prática como sair da ideia genérica para dores concretas.
- **Pontos-chave:**
  - Fórmula do JTBD: verbo + ação + contexto (exemplo do Spotify: "escutar música em qualquer lugar").
  - JTBD do projeto: "gerir suas finanças em qualquer lugar" — praticidade é o valor central (computador, celular ou WhatsApp).
  - Persona: Marcos, 30 anos. Quadrantes preenchidos: o que ouve, o que pensa e sente, o que vê, o que fala e faz.
  - Dores mapeadas: não consegue criar o hábito de registrar gastos, falta de conhecimento sobre finanças, medo do tema.
  - Necessidades: sobrar dinheiro no fim do mês (viagem, investimento) e ganhar fundamentos de finanças pessoais.
  - Outras ferramentas do pilar citadas: Design Thinking, Jobs To Be Done, Canvas, Teste da Mãe.
- **Link:** https://flix.nocodestartup.io/m/lessons/3349

### 3 - Lean Canvas  (00:06:20)
- **Resumo:** Segundo pilar: **viável**. Verifica se o modelo de negócio se sustenta financeiramente e se encaixa em como o cliente quer usar e pagar. O instrutor preenche o Lean Canvas inteiro do app de finanças, bloco por bloco, incluindo custos reais de ferramentas e a matemática da meta de receita.
- **Pontos-chave:**
  - Regra: para cada problema listado, uma solução correspondente do outro lado do canvas.
  - Métricas-chave escolhidas: leads, MRR (receita recorrente mensal) e churn.
  - Proposta única de valor: gestão financeira multiplataforma + IA integrada + WhatsApp com IA conectado ao banco de dados.
  - Vantagem injusta (unfair advantage): finanças na palma da mão com assistente de IA personalizado.
  - Persona comercial: homens e mulheres de 25 a 40 anos, renda de R$ 5 a 10 mil/mês, interesse em tecnologia e IA; primeiros adotantes = amigos e familiares.
  - Custos: FlutterFlow Pro ~US$ 35/mês, Supabase ~US$ 25/mês, API OpenAI ~US$ 15/mês estimados, mais design e marketing.
  - Matemática da receita: assinatura de R$ 50/mês × 100 clientes pagantes = meta de R$ 5K de MRR.
  - Mapear concorrentes e alternativas existentes (papel, planilha, app bancário) evita construir algo que já existe.
- **Link:** https://flix.nocodestartup.io/m/lessons/3351

### 4 - Matriz Swot  (00:05:59)
- **Resumo:** Continuação do pilar viável com a SWOT aplicada ao projeto. Separa ambiente interno (forças e fraquezas) do externo (oportunidades e ameaças) e, principalmente, mostra o passo que muita gente pula: cruzar os quadrantes para extrair ações estratégicas concretas.
- **Pontos-chave:**
  - Forças do exemplo: domínio de ferramentas no-code, de IA e conhecimento de marketing.
  - Fraquezas: primeiro micro-SaaS, dificuldade de conseguir os primeiros clientes, capital limitado.
  - Oportunidades: crescimento exponencial da IA e demanda crescente por organização financeira.
  - Ameaças: surgimento de concorrente melhor e mais barato; encarecimento das APIs de IA.
  - Os quatro cruzamentos (força×oportunidade, oportunidade×fraqueza, força×ameaça, fraqueza×ameaça) convergem para a mesma dupla de ações: **no-code + IA para ganhar agilidade** e **MVP rápido para testar barato**.
  - Estratégia defensiva contra o custo de IA: entender os fundamentos para poder migrar de plataforma (ex.: Ollama, open source e self-hosted).
- **Link:** https://flix.nocodestartup.io/m/lessons/3350

### 5 - Método MoSCoW  (00:04:32)
- **Resumo:** Terceiro pilar: **factível** — se é tecnicamente possível construir. Reforça o ciclo lean (ideia → MVP → mensurar → aprender, num PDCA contínuo) e usa o MoSCoW para separar o que entra no MVP do que fica para depois.
- **Pontos-chave:**
  - Analogia do MVP: skate → patinete → bicicleta → moto → carro; cada etapa já entrega valor (transporte), diferente de entregar peças soltas de um carro.
  - **Precisa ter:** CRUD completo de finanças (adicionar, editar, deletar, visualizar), gastos por categoria, app multiplataforma (web e mobile), integração básica com IA.
  - **Bom ter:** IA que busca cotação de moedas; IA que acessa o banco de dados e responde perguntas sobre os dados (ambos serão feitos no curso).
  - **Poderia ter:** IA que registra lançamentos no banco a partir de comandos no WhatsApp ("adicione R$ 100 no supermercado"); IA de cotação de ações.
  - **Não precisa ter:** IA que manda e-mail para assessor de investimentos; Telegram.
  - Critério de corte: valor entregue versus trabalho necessário — o quadrante "não precisa ter" existe para conter a viagem de escopo.
- **Link:** https://flix.nocodestartup.io/m/lessons/3352

### 6 - Metodologia de Desenvolvimento  (00:06:45)
- **Resumo:** Vira a chave de negócio para técnico. Define a arquitetura (front-end, back-end, serviços por API), nomeia todas as ferramentas do projeto e percorre a metodologia de desenvolvimento da NoCode StartUp: estudar o problema → conceituar a solução → design de telas → banco de dados → desenvolvimento → mensurar e aprender.
- **Pontos-chave:**
  - Front-end: FlutterFlow (multiplataforma e com acesso ao código) + WhatsApp como segunda interface.
  - Back-end: Supabase como banco oficial, Make como camada de automação/integração.
  - Serviços: OpenAI para IA e Stripe para pagamentos.
  - Conceituação da solução: conceito, lista de funcionalidades (visualizar/editar/adicionar gastos, foto do gasto), tipos de usuário (só um) e mapa de telas.
  - Prototipagem: referências no Dribbble e Behance; wireframe de baixa fidelidade no Miro (mais simples) ou Figma; alta fidelidade direto no FlutterFlow.
  - Referência citada: CoinApp, app de finanças 100% construído em FlutterFlow.
  - Layout planejado: menu, saldo total, total de entradas, total de saídas e lista de gastos; no mobile o menu vira hambúrguer e um botão "+" adiciona lançamento.
  - Modelagem de dados: tabela **usuários** (nome, e-mail) e tabela **registros** (descrição, categoria, data de criação, tipo e valor) — depois conectada a uma tabela padrão do Supabase.
  - Fecha com PDCA (planejar, fazer, checar, agir) como ciclo de melhoria contínua.
- **Link:** https://flix.nocodestartup.io/m/lessons/3353

### 7 - Integração IA + FF + WhatsApp  (00:04:45)
- **Resumo:** Planejamento da camada de IA. Mostra como o chat do app vai conversar com o banco de dados via function calling e como essa mesma capacidade é estendida para o WhatsApp, com as duas interfaces lendo o mesmo Supabase.
- **Pontos-chave:**
  - Fluxo de function calling: prompt do usuário → OpenAI avalia se precisa de função → se não, resposta padrão; se sim, dispara a função, chama API externa com request estruturado e devolve saída estruturada.
  - Caminho no app: FlutterFlow (interface) → OpenAI (function "checar banco") → API do Supabase → resposta de volta ao app.
  - Exemplo de consulta: "quanto gastei em março?" com parâmetros mês = março e categoria = supermercado.
  - Caminho no WhatsApp: mesma lógica, mas o **Make** recebe um webhook, consulta o Supabase e devolve a resposta ao WhatsApp em vez do FlutterFlow.
  - Make é escolhido no lugar do Supabase para automação porque o Supabase exige programação.
  - Diferencial do produto: duas interfaces distintas conversando com o mesmo banco de dados.
- **Link:** https://flix.nocodestartup.io/m/lessons/3355

### 8 - Gerindo Assinaturas e Finalização  (00:02:49)
- **Resumo:** Fecha o planejamento com a parte de monetização. Explica por que um SaaS de assinatura precisa de um gateway de pagamento e como o webhook mantém o status do usuário sincronizado com o banco, liberando ou cortando o acesso ao app.
- **Pontos-chave:**
  - Gateway é obrigatório para processar pagamentos e repassar o dinheiro ao dono do micro-SaaS — não dá para receber direto.
  - Gateways citados: Stripe (o escolhido), Pagar.me, Mercado Pago, Asaas.
  - Arquitetura de cobrança: Stripe conversa com o Supabase via Make; o app checa se o usuário está em plano pago antes de liberar ações.
  - Webhook no Make fica escutando o evento de pagamento: assinatura paga → libera acesso; não paga → cancela assinatura e acesso.
  - Também será construída uma landing page padrão para a compra.
  - Encerramento: micro-SaaS 100% planejado nas quatro frentes (produto/negócio, software, IA, assinaturas); os próximos módulos são de execução no FlutterFlow.
- **Link:** https://flix.nocodestartup.io/m/lessons/3354

## Pegadinhas e insights

- **Planejar não é opcional.** O recado final do instrutor é direto: muita gente sai construindo sem nenhum estudo de mercado. Todos os passos deste módulo devem preceder a primeira tela.
- **Todo problema no Lean Canvas precisa de uma solução pareada.** Bloco de problema sem contrapartida é sinal de canvas mal feito.
- **A SWOT só vale pelo cruzamento.** Listar os quatro quadrantes e parar aí não produz nada — o valor está nas ações que saem do cruzamento interno × externo. Quando a mesma ação aparece em vários quadrantes, ela é altamente estratégica (aqui: no-code + IA e MVP rápido).
- **Não faça a SWOT em 5 minutos.** O instrutor avisa que o exemplo da aula é didático e comprimido; o real exige sentar, discutir e registrar.
- **Mapeie os concorrentes antes de construir.** Existem apps de finanças muito robustos; descobrir isso depois é desperdício de tempo.
- **Escopo é o inimigo.** O quadrante "não precisa ter" do MoSCoW existe justamente para barrar funcionalidades caras de produzir e de baixo retorno. Registrar lançamentos pelo WhatsApp ficou em "poderia ter" porque a complexidade sobe bastante.
- **MVP tem que entregar valor em cada etapa**, não peças de um produto incompleto — daí a analogia skate → carro.
- **Decisão de arquitetura: Make em vez do back-end do Supabase.** O Supabase daria conta das automações, mas exige código; o Make mantém o fluxo no-code. Esse trade-off aparece duas vezes (IA e assinaturas).
- **Custo real de operação:** ~US$ 35/mês (FlutterFlow Pro, necessário para domínio próprio e publicação nas lojas) + ~US$ 25/mês (Supabase pago, ao ultrapassar o mínimo) + ~US$ 15/mês estimados de OpenAI, que na prática varia com o consumo de créditos.
- **Risco de encarecimento de IA** é tratado como ameaça explícita na SWOT; a mitigação é dominar os fundamentos para poder trocar de provedor (ex.: Ollama, open source, hospedado na própria máquina).
- **Meta modesta e alcançável:** R$ 5K de MRR com apenas 100 assinantes de R$ 50/mês — a matemática do micro-SaaS é o argumento central da viabilidade.
- **As aulas seguintes dependem umas das outras.** Cada módulo constrói sobre o app do anterior; pular quebra a sequência. Function calling, em particular, é pré-requisito assumido.
