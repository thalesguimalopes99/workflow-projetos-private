---
name: briefing
description: Transforma um contexto raso sobre qualquer coisa que o usuário queira produzir — site, landing, app, criativo/peça gráfica, anúncio, brand book/identidade, projeto, automação, conteúdo, roteiro, copy — em um briefing rico e estruturado, fazendo perguntas inteligentes pra preencher lacunas antes de executar. Use SEMPRE que o usuário trouxer uma ideia ou tarefa incompleta/vaga e disser coisas como "quero produzir/criar/fazer X", "me ajuda a montar um brief", "tenho um briefing pra desenvolver", "me ajuda a tirar isso da cabeça", "preciso estruturar esse pedido", "/brief", ou pedir pra enriquecer/detalhar um pedido raso pra chegar num resultado não-vago. Também ative quando perceber que vai começar a produzir algo a partir de instruções superficiais.
---

# Briefing — de contexto raso a brief executável

Pega o pouco que a pessoa trouxe e devolve um brief estruturado o suficiente pra ser executado sem viagem — por você, por outra sessão do Claude Code, ou por outra pessoa. O valor está em **perguntar certo** e **preencher lacunas com defaults sensatos**, não em adivinhar.

## O princípio

Você recebe pouco, entrega muito — sem inventar. As perguntas enchem as lacunas. Para cada lacuna que a pessoa não responder, você propõe um default razoável e marca como `[suposição]` no brief. Assim a pessoa pode parar de responder a qualquer momento e ainda sair com um documento completo. **Brief com suposições explícitas é infinitamente melhor que nenhum brief.**

## Quando NÃO usar

- A pessoa só quer uma resposta rápida ou uma conversa — não vai produzir nada. Responda direto.
- O pedido já vem completo e específico. Não burocratize: confirme o entendimento em 2 linhas e siga.
- É tarefa de código dentro de um repositório existente com fluxo próprio (spec → plano). Aí a skill de brainstorming/planejamento dev encaixa melhor.

## Fluxo (siga em ordem)

1. **Capture o cru.** Leia tudo que a pessoa trouxe. Não peça nada ainda.
2. **Identifique o tipo de entregável.** Infira pelos sinais (tabela abaixo). Se não der pra inferir com confiança, pergunte numa única pergunta de múltipla escolha.
3. **Carregue a lente.** Leia o arquivo `references/<tipo>.md` correspondente. Se nenhum encaixar, use `references/generico.md`.
4. **Mapeie as lacunas.** Compare o cru contra o esqueleto universal + as dimensões específicas da lente. Liste mentalmente só o que falta.
5. **Entrevista progressiva.** Pergunte só as lacunas, em rounds curtos. Um tópico por vez, múltipla escolha sempre que der. Calibre a quantidade ao tamanho do entregável (ver "Disciplina de entrevista").
6. **Reflita o entendimento.** Em 3–5 linhas, devolva o que você entendeu e peça uma confirmação rápida ("é isso? quer ajustar algo?").
7. **Gere o brief.** Use o template universal + as seções extras da lente. Marque toda lacuna não confirmada como `[suposição]`.
8. **Entregue no ambiente certo.** Ver "Entrega por ambiente".

## Identificação de tipo + lentes

Infira o tipo pelos sinais. Na dúvida entre dois, pergunte.

| Sinais na fala da pessoa | Tipo | Lente a ler |
|---|---|---|
| site, landing page, página, web app, aplicativo, plataforma, dashboard | `site-app` | `references/site-app.md` |
| criativo, peça, post, anúncio, ad, banner, carrossel, vídeo curto, reel, story, tráfego | `criativo` | `references/criativo.md` |
| marca, brand book, identidade visual, logo, logotipo, símbolo, naming, posicionamento, tom de voz, rebranding, redesign de marca, refresh, atualizar marca | `brand` | `references/brand.md` |
| projeto, iniciativa, feature, automação, fluxo, sistema, processo, pipeline | `projeto` | `references/projeto.md` |
| texto, artigo, roteiro, copy, e-mail, newsletter, legenda, script | `conteudo` | `references/conteudo.md` |
| qualquer outra coisa não listada | `generico` | `references/generico.md` |

## Disciplina de entrevista

- **Pergunte só o que falta.** Nunca repita o que a pessoa já disse. Releia o cru antes de cada pergunta.
- **Múltipla escolha primeiro.** É mais fácil escolher do que redigir. Ofereça 2–4 opções + "outro".
- **Calibre a quantidade ao tamanho:**
  - Coisa pequena (um criativo, uma legenda): 2–3 perguntas, no máximo.
  - Coisa média (uma landing, um roteiro): 4–6 perguntas.
  - Coisa grande (um projeto, um brand book): 6–8 perguntas, em rounds, decompondo se for grande demais pra um brief só.
- **Não trave esperando perfeição.** Se a pessoa não souber ou pular, registre um default como `[suposição]` e siga.
- **Decomponha o grande.** Se o pedido junta vários subsistemas independentes (ex.: "uma plataforma com login, pagamento, chat e analytics"), avise antes de detalhar. Cada peça vira seu próprio brief.
- **Uma pergunta/round por mensagem** quando estiver no Claude Code (terminal). No Claude.ai, pode agrupar 2–3 perguntas relacionadas com botões, mas sem virar formulário gigante.

## Template universal do brief

Use SEMPRE esta espinha dorsal. A lente adiciona seções específicas (indicadas em cada `references/<tipo>.md`).

```markdown
# Brief — [nome do entregável]
_Tipo: [tipo] · Data: [AAAA-MM-DD]_

## 1. O quê
Uma frase: o que vamos produzir.

## 2. Objetivo
Qual resultado real isso precisa gerar. Como saberemos que deu certo.

## 3. Pra quem
Público / usuário / audiência. Quem usa, vê ou recebe isso.

## 4. Contexto
O que já existe e o que motivou. Materiais, links, histórico relevante.

## 5. Escopo
O que entra. Itens concretos a entregar.

## 6. Fora de escopo
O que NÃO entra. (Essencial pra não viajar.)

## 7. Referências e tom
Exemplos, inspirações, estilo, voz. O que copiar e o que evitar.

## 8. Restrições
Prazo, orçamento, técnicas, de marca, legais.

## 9. Suposições e decisões em aberto
Tudo que assumi por default (marcado [suposição]) e o que ainda falta decidir.

## 10. Critérios de aceite
Checklist do que precisa estar verdadeiro pra considerar "pronto".

---
## [Seções específicas do tipo — ver a lente]
```

## Entrega por ambiente

Detecte onde você está rodando:

- **Claude Code (terminal):** salve o brief como arquivo Markdown no diretório atual — `brief-[slug].md` — e diga o caminho. Assim ele já fica pronto pra alimentar a próxima sessão de execução.
- **Claude.ai (chat):** gere o brief como artefato/arquivo Markdown pra download e mostre o conteúdo inline também.

Em ambos: termine oferecendo o próximo passo ("quer que eu já comece a produzir a partir desse brief, ou prefere revisar primeiro?").

**Handoff pro especialista certo.** Quando o brief for de domínio (marca, copy, tráfego, narrativa, design, etc.) e o Thales topar produzir, consulte `ROUTING-MAP.md` na raiz da biblioteca (`C:\Users\Thales Lopes\Desktop\No Code Start-up\Workflow Projetos\ROUTING-MAP.md`) pra escolher **qual especialista DENTRO do squad** e **a sequência multi-agent** (ex: rebrand = kapferer→ries→neumeier→miller→wheeler→naming). Leia o mapa só na hora do handoff (lazy); invoque o agent nativo via `Skill` → `<squad-slug>:agents:<id>`. Não despeje as personas pesadas de `squad-prompts/` no contexto.

## Anti-padrões

- ❌ Despejar 15 perguntas de uma vez. → Rounds curtos, calibrados ao tamanho.
- ❌ Perguntar coisa que já está no cru. → Releia antes de perguntar.
- ❌ Travar porque a pessoa não respondeu algo. → Default + `[suposição]`.
- ❌ Entregar um brief vago com "a definir" em tudo. → Sempre proponha um default concreto.
- ❌ Aplicar lente de software (testes, arquitetura) num brand book ou criativo. → Carregue a lente certa.
