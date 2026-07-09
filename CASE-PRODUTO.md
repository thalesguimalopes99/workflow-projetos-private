# Workflow Projetos — Sistema operacional de IA para uma agência criativa

## Contexto
Esse é o projeto-meta: a infraestrutura que opera todos os outros. O desafio era escalar produção criativa de alta qualidade **sem multiplicar o time de especialistas**. A agência opera em vários domínios ao mesmo tempo — marca, copy, tráfego pago, design, narrativa, oferta, dados — cada um exigindo expertise diferente. Sem orquestração, pedido raso virava entrega genérica e o melhor recurso (o especialista certo) era ignorado.

## Problema
Gerir produção criativa em escala com IA exige resolver cinco coisas que, sem sistema, cada projeto reinventava do zero:
- Transformar briefing raso ("preciso de um site") em brief executável.
- Rotear o pedido para o **especialista certo** entre 14 squads.
- Executar com padrão de qualidade alto (awwwards/Pentagram), não template.
- Documentar e repetir — portabilidade entre projetos.
- Não desperdiçar contexto carregando personas pesadas que não serão usadas.

## Quem era o usuário?
Eu mesmo — como diretor criativo que gerencia os próprios projetos (sites premium, rebrandings, ofertas) e as contas da agência, precisando de velocidade e qualidade ao mesmo tempo, trabalhando dentro do Claude Code como IDE.

## Como você descobriu esse problema?
Iterativamente, rodando vários projetos grandes (sites, identidades, sequências de copy, campanhas). Os padrões que se repetiam: pedidos chegavam vagos e exigiam adivinhação; os recursos certos não eram acionados (copy sem a expertise de um Gary Halbert ou David Ogilvy); cada projeto recomeçava o roteamento do zero; a qualidade flutuava sem critério; e o contexto era desperdiçado carregando personas e skills desnecessárias.

## Hipóteses
1. Uma **porta de entrada estruturada** (skill `/workflow`) converteria pedido vago em brief afiado via intake interativo.
2. **Squads com especialistas nomeados** (personas clonadas de mestres reais) + roteamento fino escalariam expertise.
3. **Padrões de qualidade explícitos** (um "Creative OS" e "Branding OS") como lei, não sugestão, elevariam o piso de entrega.
4. Um **índice de roteamento leve** (ROUTING-MAP) em vez de despejar todas as personas no contexto economizaria muito token.

## Solução
Uma biblioteca central no Claude Code com 3 camadas:
- **Skills (107):** porta de entrada (`workflow`), briefing com 6 lentes, execução (`criar-site-premium`, `brand`, `slides`, `motion-design`, `site-teardown`) e um metaprocesso (GSD) de planejamento, debugging, testes e review.
- **Squads (14 squads, ~155 agentes):** Brand Squad (David Aaker, Marty Neumeier, Alina Wheeler…), Copy Master (Gary Halbert, Eugene Schwartz, David Ogilvy…), Hormozi (oferta, pricing, escala), Traffic Masters (ads, pixel, scaling), Storytelling, Design, Data, C-Level, Advisory Board (Ray Dalio, Naval, Munger), AIOX (software), entre outros.
- **Operacionalização:** `ROUTING-MAP.md` (índice fino problema → squad → especialista → sequência), `CLAUDE.md` (regra de ouro + protocolo de roteamento), `CREATIVE-OS.md` / `CLAUDE-BRANDING-OS.md` (a lei de qualidade), e separação entre biblioteca global e `.claude/` local por projeto.

## Como funciona?
1. Disparo `/workflow` com o pedido.
2. A skill pergunta **qual entregável** (site, brand, logo, copy, tráfego…).
3. Invoca a skill `briefing` na lente certa, extraindo 8 dimensões (objetivo nº1, público + estado mental, sucesso medível, referências, ângulo/diferencial, restrições, o que já existe, não-objetivos).
4. Pergunta o **nível de qualidade** desejado.
5. Lê o ROUTING-MAP, identifica o squad e roteia para o **chief** dele.
6. O chief diagnostica e roteia internamente para o especialista exato, em sequência (ex: Gary Halbert → Stefan Georgi → Todd Brown).
7. Executa e devolve o output, com gate de qualidade ao final (nota abaixo do alvo → refatora).

## Stack
- **Plataforma:** Claude Code (registry de skills/commands/agents)
- **MCP:** firecrawl (mineração de referências), playwright (UI/teste/regressão), github, sequential-thinking, context7, e conectores (Figma, Notion, Supabase, Vercel)
- **Web:** Next.js, React, Tailwind, shadcn/ui, GSAP/Lenis/Three.js
- **Vídeo/motion:** Remotion (opcional), HyperFrames
- **Referências de qualidade:** Awwwards, FWA, Behance, Pentagram, Collins, Landor

## Minhas decisões
- **`/workflow` como porta única** — evita que pedido raso vire genérico; força brief antes de rotear.
- **Briefing com 6 lentes** — a mesma pergunta não serve para logo e newsletter.
- **Personas clonadas de mestres reais** — fidelidade e clareza: "Gary Halbert pra sales letter" é melhor que "agente genérico de copy".
- **ROUTING-MAP leve + personas lazy** — decisões rápidas com economia grande de contexto.
- **Padrão de qualidade explícito** — "se a nota interna for baixa, refatora" elimina o "suficiente".
- **Squads multi-nível (chief → especialista → subespecialista)** — escalabilidade do roteamento.
- **Biblioteca global + local, sem symlink** — portabilidade entre máquinas e sistemas.

## Resultado
Operacionalmente: todo entregável começa estruturado, o roteamento é automático para o especialista certo, a qualidade tem lei clara e auditável, e tudo é portável entre projetos. Para o negócio: a agência opera expertise via IA sem duplicar headcount — eu produzo sites, marcas, ofertas e campanhas sozinho com qualidade de agência, e um novo projeto é "clonar o `.claude/` e rodar `/workflow`". É menos uma aplicação e mais uma biblioteca operacional de inteligência coletiva.

## O que eu faria diferente hoje
- **Council multi-agente em paralelo por padrão** — orquestrar squads concorrentes em paralelo quando faz sentido, convergindo o resultado, em vez de chamar em sequência manual.
- **Artefatos de handoff persistentes** — YAML formal com flag de "consumido" e resultados cacheados para reusar em projetos similares.
- **Auto-upgrade das skills via git** — pull automático das últimas versões sem restart manual.
- **Loop de feedback no gate de qualidade** — quando a nota é baixa, o sistema apontar qual agente falhou em vez de só dizer "refatora".
- **Detecção de clones** — sugerir "encontrei um padrão parecido no Projeto X; quer clonar e customizar?".
- **Orçamento de contexto por squad** — alocação máxima de tokens por squad para forçar foco.
