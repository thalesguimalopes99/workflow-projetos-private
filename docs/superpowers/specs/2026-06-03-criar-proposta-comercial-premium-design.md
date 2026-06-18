# Spec — `criar-proposta-comercial-premium`

**Data:** 2026-06-03
**Autor:** Thales (NoCode StartUp) + Claude
**Status:** Aprovado para planejamento

---

## 1. Contexto e objetivo

A pasta `Workflow Projetos` é uma operação de agência premium multi-disciplinar:
porta de entrada única (`workflow`) → `briefing` → nível de qualidade → roteamento
para 14 squads (160+ tasks) e 86 skills, sob padrões inegociáveis (CREATIVE-OS para
web $100k+, BRANDING-OS para identidade $50k+).

Hoje só **sites** têm um pipeline premium ponta-a-ponta (`criar-site-premium`). Os
demais tipos de entrega dependem de squads soltos, sem o pipeline que força o tier
de agência.

Este spec define a **primeira skill de uma família** `criar-X-premium`: a
`criar-proposta-comercial-premium` — gera proposta comercial premium para ofertar os
serviços do Thales a clientes. Escolhida primeiro por valor direto (fecha cliente =
receita) e por servir de molde-referência para os outros pipelines.

### Família completa (contexto, NÃO escopo deste spec)

Pipelines planejados, todos clonando o esqueleto de 7 fases:
`criar-site-premium` (existe, refatorar), `criar-landing-premium`, `criar-saas-premium`,
`criar-brand-premium`, `criar-conteudo-premium`, `criar-video-premium`,
`criar-campanha-premium`, **`criar-proposta-comercial-premium`** (este),
`criar-boas-vindas`; + skill de discovery `pesquisa-mercado`.

Ordem de build acordada: pesquisa-mercado → brand → site(refactor)+landing → saas →
conteúdo → campanha → **proposta** → boas-vindas → vídeo. **Nota:** o Thales priorizou
construir a `proposta` primeiro; ela vira o molde-referência.

---

## 2. Esqueleto compartilhado da família (7 fases)

Toda skill `criar-X-premium` segue estas fases. Muda só o miolo de cada uma.

```
0 Brief              → puxa `briefing` na lente certa
1 Análise estratégica → convoca chiefs/AIOX/advisory + pesquisa-mercado (escala com o tier)
2 Minerar refs        → fontes top 1% do domínio (firecrawl / site-teardown)
3 Direção             → 2-3 rotas, escolhe critério do domínio
4 Build               → executa com squad/tool certo
5 Quality gate        → auto-crítica 9+, "parece genérico?"→refactor (OS doc do domínio)
6 Ship                → entrega na pasta do PROJETO ATIVO (nunca na biblioteca)
```

**Fase 1 — Análise Estratégica** é a regra transversal pedida pelo Thales: SEMPRE
convoca os especialistas relevantes antes de construir. Painel escala com o tier
(entrega pequena = painel enxuto; high-ticket = panel completo + advisory-board).

---

## 3. Especificação da skill `criar-proposta-comercial-premium`

### 3.1 Propósito

Transformar contexto de venda (cliente, dor, serviço a ofertar) em proposta comercial
premium que fecha high-ticket — em **PPTX editável** (fonte para pitch ao vivo) + **PDF
desenhado** (envio/impressão).

### 3.2 Triggers (frontmatter `description`)

Ativa quando o Thales quer ofertar/vender serviços a um cliente. Frases-gatilho:
"criar proposta comercial", "proposta pra cliente", "ofertar meus serviços",
"montar uma proposta", "deck de venda", "proposta high-ticket", "/proposta".
Também ativa dentro do roteamento da skill `workflow` quando o entregável é proposta
de venda.

### 3.3 Inputs em runtime (coletados na Fase 0 — Brief + Discovery)

**Core (obrigatório — sem isso a proposta sai genérica, a skill BLOQUEIA e pede):**
- Cliente (quem é, nicho, porte, contexto)
- Dor / situação atual do cliente
- **Números atuais do cliente** (faturamento/custo/métrica relevante — base do ROI)
- **Decisor / comitê de compra** — quem lê, quem assina (economic buyer vs campeão vs usuário)
- **Processo e critério de decisão** — como decidem, o que define "sim", prazo de decisão
- Serviço(s) a ofertar
- Cases/provas disponíveis (números reais)
- Sinal de budget / tier do deal

**Opcional:**
- Concorrência (outras agências no páreo)
- Restrições: prazo de entrega, sazonalidade, evento-âncora

> Quando o Thales não tem um item core, a skill oferece **minerar o prospect** (Fase 2)
> para preencher antes de prosseguir — nunca escreve no escuro.

### 3.4 Anatomia da proposta (deliverable — 10 seções)

Estrutura comprovada para fechar high-ticket:

1. **Capa + tese** — resultado prometido em uma frase
2. **Diagnóstico** — dor/situação atual + **custo de não-agir quantificado** (quanto perde parado)
3. **Destino** — onde o cliente chega depois
4. **Mecanismo único** — o método do Thales; por que só ele entrega (anti-comoditização)
5. **Escopo/entregáveis** — o que recebe + **fronteiras "o que NÃO está incluso"** (barra scope creep)
6. **Prova** — cases, números reais, social proof específico
7. **Investimento** — oferta ancorada + **ROI/payback projetado** (número do gap → retorno); modelo de preço escolhido na análise
8. **Por que agora** — urgência legítima (janela, custo crescente, sazonalidade) — nunca escassez falsa
9. **Bônus + garantia** — risk-reversal específico
10. **Próximos passos + CTA** — timeline, como começa
11. **FAQ/objeções** — antecipa e neutraliza

### 3.5 Modelos de preço suportados (Fase 1 escolhe)

A skill suporta os 4 e a análise (`hormozi-pricing` + contexto do deal) recomenda qual
usar — ou combina (ex: pacotes em camadas com opção retainer):

- **Pacotes em camadas** (Good/Better/Best) — ancora preço, sobe ticket médio
- **Preço único por valor** — ancorado em ROI/resultado, posiciona premium
- **Retainer/recorrente** — fee mensal, receita previsível
- **Por projeto/escopo** — orçamento fechado por entrega

### 3.6 Pipeline (as 7 fases instanciadas)

| Fase | O que faz nesta skill | Assets puxados |
|------|----------------------|----------------|
| 0 Brief+Discovery | coleta inputs 3.3 via `briefing`; **BLOQUEIA se faltar input core** (oferece minerar o prospect) | `briefing` |
| 1 Análise | define ângulo, modelo de preço, ROI/custo de não-agir, "por que agora", objeções | `hormozi-offers`, `hormozi-pricing`, `copy-master:copy-chief`, `advisory-board` (high-ticket), `pesquisa-mercado` (dado do nicho) |
| 2 Minerar | (a) **o próprio prospect** — site, números públicos, concorrentes, linguagem; (b) decks/propostas que fecham high-ticket | firecrawl, `site-teardown`, swipe files |
| 3 Direção | narrativa: diagnóstico→custo→mecanismo→oferta→prova→preço/ROI→por que agora→CTA; 2-3 ângulos | `storytelling:story-chief`, `copy-master` |
| 4 Build | monta outline + **copy final** das 11 seções → **Gamma API** (`textMode=preserve` p/ NÃO reescrever a copy; tema/marca do Thales) → poll → exporta `.pptx` + `.pdf`; **gera pitch-kit**. **Fallback:** skill `pptx`+`pdf` se API fora/quota | **Gamma API**, `copy-squad` (follow-up); fallback `pptx`/`design`/`pdf` |
| 5 Gate | checklist "fecharia?" (ver 3.7); score 9+ ou refatora | self-critique |
| 6 Ship | salva `.pptx` + `.pdf` + **pitch-kit** na pasta do projeto ativo + handoff | — |

### 3.6.1 Saídas (deliverables)

1. `proposta.pptx` — fonte editável (pitch ao vivo)
2. `proposta.pdf` — versão desenhada premium (envio/impressão)
3. `pitch-kit.md` — talking points por seção + respostas de objeção + sequência de
   follow-up (3-5 e-mails). O deal fecha no follow-up, não no envio.

### 3.7 Quality gate — checklist "fecharia?"

Refatora enquanto qualquer item falhar (alvo 9+/10):

- [ ] Diagnóstico mostra que entendeu a dor REAL do cliente (não genérico)
- [ ] **Custo de não-agir quantificado** (número, não adjetivo)
- [ ] Mecanismo é único — não comoditizável, não "mais uma agência"
- [ ] Preço ancorado ANTES do número + **ROI/payback explícito**
- [ ] Prova específica com números reais (não "ajudamos vários clientes")
- [ ] **Endereça o decisor certo** (linguagem do economic buyer, não só do usuário)
- [ ] **"Por que agora" legítimo** (não escassez falsa)
- [ ] Toda objeção principal antecipada e neutralizada
- [ ] **Fronteiras de escopo** presentes (o que não está incluso)
- [ ] CTA com próximo passo concreto (não "entre em contato")
- [ ] **Deck na marca do Thales** (não "premium genérico")
- [ ] Tom premium — passa no teste "parece proposta de agência top 1?" → senão refatora
- [ ] Coerência visual (PPTX e PDF na mesma direção de arte)
- [ ] **Pitch-kit gerado** (talking points + objeções + follow-up)

### 3.8 Estrutura de arquivos da skill

```
criar-proposta-comercial-premium/
├── SKILL.md                      # frontmatter + 7 fases + triggers + regra refactor
└── references/
    ├── discovery-qualificacao.md # checklist do que TEM que saber antes (gate de bloqueio)
    ├── anatomia-proposta.md      # as 11 seções + por que cada uma
    ├── fontes-mineracao.md       # minerar o prospect + decks high-ticket
    ├── roi-custo-inacao.md       # como calcular custo de não-agir + ROI/payback
    ├── modelos-preco.md          # 4 modelos + quando usar cada
    ├── pitch-kit-followup.md     # talking points + objeções + sequência follow-up
    ├── marca-thales.md           # identidade do Thales → tema/brand do Gamma (e fallback)
    ├── quality-gate.md           # checklist "fecharia?" detalhado
    ├── build-gamma.md            # chamar Gamma API: payload, textMode=preserve, tema, poll, export pptx+pdf
    └── build-fallback-pptx.md    # fallback: montar pptx+pdf sem Gamma (API fora/quota)
```

---

## 4. Integração com o sistema existente

- **Roteamento:** adicionar entrada na skill `workflow` → pedido de proposta/oferta
  roteia para `criar-proposta-comercial-premium`.
- **Onde salvar a skill:** `biblioteca/skills/criar-proposta-comercial-premium/`
  (fonte da verdade versionável) + disponibilizar em `.claude/skills/` do projeto
  (cópia ou symlink, seguindo o padrão atual da pasta).
- **Saídas do deliverable:** sempre na pasta do PROJETO ATIVO do cliente, nunca na
  biblioteca (regra do CLAUDE.md).
- **Ferramenta de criação:** usar `skill-creator` (instalado) para gerar e validar a
  skill contra `template-skill`.

### 4.1 Integração Gamma API (motor de build da Fase 4)

- **Plano:** requer Pro/Ultra/Teams/Business — Thales já tem pago.
- **Auth:** header `X-API-KEY`. Chave em **variável de ambiente `GAMMA_API_KEY`**
  (`.env` local / secret), **nunca commitada** no repo.
- **Fluxo (assíncrono):**
  1. `POST https://public-api.gamma.app/v1.0/generations` com payload:
     `inputText` = outline + copy final das 11 seções; `format=presentation`;
     `textMode=preserve` (Gamma diagrama, NÃO reescreve); `numCards` ≈ nº de seções;
     tema/brand = identidade do Thales; `exportAs` = `pptx`.
  2. Pollar `GET /v1.0/generations/{generationId}` a cada ~5s até `completed`.
  3. Resposta traz `gammaUrl` (link editável), `exportUrl` (download), `gammaId`.
  4. Repetir export para `pdf` (1 formato por call) → guardar `.pptx` + `.pdf`.
- **Marca:** aplicar tema/brand do Gamma com cor/tipo/logo do Thales (ver `marca-thales.md`).
  Se ainda não há tema configurado, mini-intake na 1ª run e salvar referência.
- **Fallback:** se a API falhar, retornar erro, ou estourar quota → cair para
  `build-fallback-pptx.md` (skills `pptx`+`design`+`pdf`), sem travar a entrega.
- **Robustez:** tratar timeout/`failed` do poll; logar `gammaId` para arquivar/deletar depois.

---

## 5. Fora de escopo (YAGNI) e refator futuro

Fora de escopo agora:
- Os outros 8 pipelines da família + `pesquisa-mercado` (specs próprios depois).
  EXCEÇÃO: a Fase 1 referencia `pesquisa-mercado`; se ela ainda não existir no momento
  do build, a skill faz a pesquisa inline (firecrawl + análise) e marca como ponto de
  refator futuro quando `pesquisa-mercado` existir.
- Refactor do `criar-site-premium` para o padrão da família.
- Geração automática de contrato/assinatura (a proposta para no aceite + próximos passos).
- Integração CRM/envio automático.

Anotado para refator futuro (secundários que decidimos não fazer agora):
- **Banco de provas reutilizável** — biblioteca de cases/depoimentos para não re-coletar
  a cada proposta.
- **Frame competitivo explícito** — seção "por que você vs a outra agência".
- **Loop de feedback "fechou ou não"** — registrar desfecho para melhorar a skill.

**Premissa (marca do Thales):** a Fase 4 aplica a identidade do Thales no deck. Se ainda
não existir um arquivo de brand tokens dele na biblioteca, a skill faz um mini-intake de
marca na primeira execução (cor/tipo/voz/logo) e salva em
`biblioteca/config/` para reuso — não re-pergunta toda vez.

---

## 6. Critérios de sucesso

1. Rodar a skill com um caso real (um serviço do Thales + um cliente-alvo) produz
   `.pptx` editável + `.pdf` premium (11 seções) + `pitch-kit.md`.
2. A Fase 0 bloqueia se faltar input core; oferece minerar o prospect para preencher.
3. A Fase 1 efetivamente convoca os chiefs/agentes certos e a saída reflete as decisões
   deles (ângulo, modelo de preço, ROI, "por que agora", objeções).
4. O quality gate roda e rejeita rascunho genérico (refatora até 9+), incluindo custo
   de não-agir quantificado e deck na marca do Thales.
5. `workflow` roteia corretamente um pedido de proposta para esta skill.
6. A skill serve de molde claro para clonar os próximos `criar-X-premium`.
```
