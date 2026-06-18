# criar-proposta-comercial-premium — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir a skill `criar-proposta-comercial-premium` que gera proposta comercial premium (PPTX editável + PDF + pitch-kit) para o Thales ofertar serviços a clientes, usando a API do Gamma como motor de render.

**Architecture:** Skill de 7 fases (Brief+Discovery → Análise estratégica → Minerar → Direção → Build → Quality gate → Ship). O valor está nas fases 0-3 (estratégia/copy/ROI); a Fase 4 manda a copy final pro Gamma API (`textMode=preserve`) via um helper Node, com fallback `pptx`. Skill vive em `biblioteca/skills/` (fonte da verdade) e é espelhada em `.claude/skills/`.

**Tech Stack:** Claude Code Skill (SKILL.md + references markdown), Node 24 (helper `gamma-generate.mjs`, fetch nativo), Gamma Generate API, skills `pptx`/`design`/`pdf` (fallback), skill-creator (validação).

**Spec:** `docs/superpowers/specs/2026-06-03-criar-proposta-comercial-premium-design.md`

---

## File Structure

```
biblioteca/skills/criar-proposta-comercial-premium/
├── SKILL.md                       # orquestra as 7 fases; triggers; regra refactor 9+
├── scripts/
│   └── gamma-generate.mjs         # helper: POST→poll→export (1 formato/run)
└── references/
    ├── discovery-qualificacao.md  # gate de inputs core (Fase 0)
    ├── anatomia-proposta.md       # as 11 seções
    ├── fontes-mineracao.md        # minerar prospect + decks (Fase 2)
    ├── roi-custo-inacao.md        # cálculo custo de não-agir + ROI/payback
    ├── modelos-preco.md           # 4 modelos + quando usar
    ├── pitch-kit-followup.md      # talking points + objeções + follow-up
    ├── marca-thales.md            # identidade do Thales → tema Gamma + fallback
    ├── quality-gate.md            # checklist "fecharia?" (9+)
    ├── build-gamma.md             # uso do gamma-generate.mjs + pptx→pdf
    └── build-fallback-pptx.md     # build sem Gamma (API fora/quota)
```

Fora da pasta da skill:
- `biblioteca/skills/workflow/SKILL.md` — adicionar entrada de roteamento
- `.claude/skills/criar-proposta-comercial-premium/` — espelho (cópia) da skill
- `.env` (na raiz do projeto, gitignored) — `GAMMA_API_KEY`

---

## Task 1: Setup Gamma API + helper + smoke test

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/scripts/gamma-generate.mjs`
- Create/append: `.env` (gitignored), `.gitignore`

- [ ] **Step 1: Gerar a API key (manual — Thales)**

No Gamma: Account Settings → API Keys → criar key. No terminal desta sessão, rodar (substitua pela key real):

```
! setx GAMMA_API_KEY "sk-gamma-XXXX"
```

Para a sessão atual também: `$env:GAMMA_API_KEY = "sk-gamma-XXXX"` (PowerShell).

- [ ] **Step 2: Garantir `.env` ignorado**

Confirmar que `.gitignore` contém `.env`. Se não houver `.gitignore`, criar com a linha:

```
.env
```

Adicionar a key em `.env` (não commitar):

```
GAMMA_API_KEY=sk-gamma-XXXX
```

- [ ] **Step 3: Escrever o helper `gamma-generate.mjs`**

```js
#!/usr/bin/env node
// gamma-generate.mjs — gera um deck no Gamma e baixa o export.
// Uso:
//   node gamma-generate.mjs --input ./outline.md --export pptx --out ./proposta.pptx \
//        [--theme "Nome do Tema"] [--numCards 11] [--textMode preserve]
// Requer env GAMMA_API_KEY.

import fs from "node:fs";
import path from "node:path";

const API = "https://public-api.gamma.app/v1.0/generations";
const KEY = process.env.GAMMA_API_KEY;

function arg(name, def = undefined) {
  const i = process.argv.indexOf(`--${name}`);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}

async function main() {
  if (!KEY) throw new Error("GAMMA_API_KEY ausente no ambiente.");

  const inputPath = arg("input");
  if (!inputPath) throw new Error("--input <arquivo> é obrigatório.");
  const inputText = fs.readFileSync(inputPath, "utf8");

  const exportAs = arg("export", "pptx"); // pptx | pdf | png
  const out = arg("out", `./out.${exportAs}`);
  const textMode = arg("textMode", "preserve"); // preserve não reescreve a copy
  const numCards = Number(arg("numCards", "11"));
  const theme = arg("theme"); // opcional

  const body = {
    inputText,
    format: "presentation",
    textMode,
    numCards,
    exportAs,
  };
  if (theme) body.themeName = theme;

  // 1) cria a geração
  const createRes = await fetch(API, {
    method: "POST",
    headers: { "X-API-KEY": KEY, "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!createRes.ok) {
    throw new Error(`POST falhou ${createRes.status}: ${await createRes.text()}`);
  }
  const { generationId } = await createRes.json();
  if (!generationId) throw new Error("Resposta sem generationId.");
  console.log(`generationId=${generationId} (poll a cada 5s)`);

  // 2) poll até completed/failed (timeout 5 min)
  const deadline = Date.now() + 5 * 60 * 1000;
  let result;
  while (Date.now() < deadline) {
    await new Promise((r) => setTimeout(r, 5000));
    const res = await fetch(`${API}/${generationId}`, {
      headers: { "X-API-KEY": KEY },
    });
    if (!res.ok) throw new Error(`GET falhou ${res.status}: ${await res.text()}`);
    result = await res.json();
    if (result.status === "completed") break;
    if (result.status === "failed") throw new Error(`Geração falhou: ${JSON.stringify(result)}`);
    console.log(`status=${result.status}...`);
  }
  if (!result || result.status !== "completed") throw new Error("Timeout no poll.");

  // 3) baixa o export
  const url = result.exportUrl;
  if (!url) throw new Error("Sem exportUrl na resposta completed.");
  const fileRes = await fetch(url);
  if (!fileRes.ok) throw new Error(`Download falhou ${fileRes.status}`);
  const buf = Buffer.from(await fileRes.arrayBuffer());
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  fs.writeFileSync(out, buf);

  console.log(JSON.stringify({ ok: true, out, gammaUrl: result.gammaUrl, gammaId: result.gammaId }));
}

main().catch((e) => {
  console.error(`ERRO: ${e.message}`);
  process.exit(1);
});
```

- [ ] **Step 4: Smoke test com input mínimo**

Criar arquivo temporário e rodar de verdade contra a API:

```
node -e "require('fs').writeFileSync('smoke.md','# Proposta Teste\n\nDiagnóstico: cliente perde tempo.\n\nMecanismo: nosso método X.\n\nInvestimento: R$ 10k.')"
node "biblioteca/skills/criar-proposta-comercial-premium/scripts/gamma-generate.mjs" --input smoke.md --export pptx --out out/smoke.pptx --numCards 3
```

Expected: imprime `generationId=...`, depois `status=...` até `{"ok":true,"out":"out/smoke.pptx",...}` e o arquivo `out/smoke.pptx` existe.

- [ ] **Step 5: Verificar o arquivo gerado**

Run:
```
node -e "const s=require('fs').statSync('out/smoke.pptx');console.log('bytes', s.size)"
```
Expected: `bytes` > 0 (deck real). Apagar smoke: `node -e "require('fs').rmSync('smoke.md');require('fs').rmSync('out/smoke.pptx')"`

- [ ] **Step 6: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/scripts/gamma-generate.mjs .gitignore
git commit -m "feat(proposta): helper gamma-generate + smoke test"
```

> Se a pasta não for repo git, pular o commit e seguir (avisar o Thales).

---

## Task 2: Scaffold da skill (SKILL.md)

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/SKILL.md`

- [ ] **Step 1: Escrever o SKILL.md**

```markdown
---
name: criar-proposta-comercial-premium
description: Use quando o Thales quer ofertar/vender serviços a um cliente e precisa de uma proposta comercial premium que FECHA high-ticket. Gatilhos "criar proposta comercial", "proposta pra cliente", "ofertar meus serviços", "deck de venda", "proposta high-ticket", "/proposta". Também ativa pelo roteamento da skill workflow quando o entregável é proposta de venda. Produz PPTX editável + PDF desenhado + pitch-kit (talking points, objeções, follow-up). NÃO use para brand book, site, conteúdo de IG ou campanha de tráfego — há pipelines próprios.
---

# criar-proposta-comercial-premium

Pipeline de 7 fases. Regra-mãe: o valor está nas fases 0-3 (estratégia, copy, ROI). O Gamma só renderiza. Nada de proposta genérica — se o quality gate < 9, refatora.

## Fase 0 — Brief + Discovery
Coletar inputs core. Se faltar algum, BLOQUEAR e oferecer minerar o prospect.
→ ver `references/discovery-qualificacao.md`. Use a skill `briefing` (lente venda/oferta).

## Fase 1 — Análise estratégica
Convocar especialistas (escala com o tier do deal):
- `hormozi-offers` + `hormozi-pricing` → oferta + modelo de preço (ver `references/modelos-preco.md`)
- `copy-master:copy-chief` → ângulo de copy
- `advisory-board` → só se high-ticket / decisão estratégica
- pesquisa de mercado do nicho (inline via firecrawl até a skill `pesquisa-mercado` existir)
Definir: ângulo, modelo de preço, custo de não-agir + ROI (ver `references/roi-custo-inacao.md`), "por que agora", objeções.

## Fase 2 — Minerar
(a) O PRÓPRIO prospect: site, números públicos, concorrentes, linguagem (firecrawl, `site-teardown`).
(b) Decks/propostas que fecham high-ticket.
→ ver `references/fontes-mineracao.md`.

## Fase 3 — Direção
Montar a narrativa nas 11 seções com COPY FINAL (não rascunho): diagnóstico→custo→mecanismo→oferta→prova→preço/ROI→por que agora→CTA. Gerar 2-3 ângulos, escolher 1.
→ ver `references/anatomia-proposta.md`. Use `storytelling:story-chief` + `copy-master`.

## Fase 4 — Build
1. Salvar a copy final das 11 seções em `outline.md`.
2. Rodar `scripts/gamma-generate.mjs` com `--textMode preserve` e o tema da marca do Thales.
3. Exportar `.pptx` (fonte) e derivar `.pdf`. → ver `references/build-gamma.md`.
4. Aplicar identidade do Thales → ver `references/marca-thales.md`.
5. Gerar `pitch-kit.md` → ver `references/pitch-kit-followup.md` (usa `copy-squad`).
Fallback se Gamma falhar/quota → `references/build-fallback-pptx.md`.

## Fase 5 — Quality gate
Rodar o checklist "fecharia?" (`references/quality-gate.md`). Score < 9 em qualquer item → refatora a fase responsável e re-renderiza.

## Fase 6 — Ship
Salvar `proposta.pptx` + `proposta.pdf` + `pitch-kit.md` na pasta do PROJETO ATIVO do cliente (NUNCA na biblioteca). Entregar resumo + próximos passos.
```

- [ ] **Step 2: Validar frontmatter**

Run:
```
node -e "const f=require('fs').readFileSync('biblioteca/skills/criar-proposta-comercial-premium/SKILL.md','utf8');if(!/^---[\s\S]*?name:\s*criar-proposta-comercial-premium[\s\S]*?description:[\s\S]*?---/.test(f))throw new Error('frontmatter inválido');console.log('frontmatter OK')"
```
Expected: `frontmatter OK`

- [ ] **Step 3: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/SKILL.md
git commit -m "feat(proposta): SKILL.md com as 7 fases"
```

---

## Task 3: Reference — discovery-qualificacao.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/discovery-qualificacao.md`

- [ ] **Step 1: Escrever o conteúdo**

Conteúdo (gate de inputs core — a skill bloqueia sem eles):

```markdown
# Discovery / Qualificação — gate antes de escrever

NÃO escrever proposta sem os itens CORE. Faltou? Oferecer minerar o prospect (Fase 2) ou perguntar ao Thales.

## Core (obrigatório)
- Cliente: quem é, nicho, porte, contexto
- Dor / situação atual (na linguagem do cliente)
- Números atuais (faturamento / custo / métrica relevante) — base do ROI
- Decisor / comitê: quem lê, quem assina (economic buyer × campeão × usuário)
- Processo e critério de decisão: como decidem, o que define "sim", prazo
- Serviço(s) a ofertar
- Cases/provas disponíveis (números reais)
- Sinal de budget / tier do deal

## Opcional
- Concorrência (outras agências no páreo)
- Restrições: prazo, sazonalidade, evento-âncora

## Saída desta fase
Um bloco "Contexto do Deal" preenchido, marcando o que veio do Thales × o que foi minerado.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/discovery-qualificacao.md
git commit -m "docs(proposta): reference discovery-qualificacao"
```

---

## Task 4: Reference — anatomia-proposta.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/anatomia-proposta.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Anatomia da proposta — 11 seções

1. Capa + tese — resultado prometido em uma frase
2. Diagnóstico — dor/situação atual + custo de não-agir QUANTIFICADO
3. Destino — onde o cliente chega depois
4. Mecanismo único — o método do Thales; por que SÓ ele entrega (anti-comoditização)
5. Escopo/entregáveis — o que recebe + fronteiras "o que NÃO está incluso"
6. Prova — cases, números reais, social proof específico (nada de "vários clientes")
7. Investimento — oferta ancorada + ROI/payback; modelo de preço da Fase 1
8. Por que agora — urgência legítima (janela, custo crescente, sazonalidade); nunca falsa
9. Bônus + garantia — risk-reversal específico
10. Próximos passos + CTA — timeline, como começa (passo concreto)
11. FAQ/objeções — antecipa e neutraliza as 3-5 principais

Regra: cada seção fala a linguagem do DECISOR, não só do usuário.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/anatomia-proposta.md
git commit -m "docs(proposta): reference anatomia-proposta"
```

---

## Task 5: Reference — fontes-mineracao.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/fontes-mineracao.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Mineração (Fase 2)

## (a) O PRÓPRIO prospect — prioridade
- Site do cliente (firecrawl / site-teardown): proposta de valor, tom, ofertas
- Números públicos: faturamento estimado, tráfego, redes, reviews
- Concorrentes diretos do cliente (3): o que eles fazem melhor/pior
- Linguagem própria do cliente: termos que ele usa (devolver na proposta = espelho)

## (b) Decks/propostas que fecham high-ticket
- Swipe files de propostas premium do nicho de serviço
- Estruturas de oferta (Hormozi value stack, grand slam offer)
- Referências visuais de deck premium (para o tema do Gamma)

## Saída
Bullets de insights por fonte + 3-5 termos do cliente para reusar na copy.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/fontes-mineracao.md
git commit -m "docs(proposta): reference fontes-mineracao"
```

---

## Task 6: Reference — roi-custo-inacao.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/roi-custo-inacao.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Custo de não-agir + ROI/payback

## Custo de não-agir (usar na seção Diagnóstico)
Fórmula simples: `perda_mensal = métrica_atual × gap_estimado`.
Ex: "Sem isso, você perde ~R$ X/mês em [conversão/eficiência/churn]."
Sempre número, nunca adjetivo. Basear no número atual do cliente (Discovery).

## ROI/payback (usar na seção Investimento)
- Ganho projetado (conservador) = resultado esperado × preço/unidade
- Payback (meses) = investimento / ganho_mensal_projetado
- Mostrar: "Investimento R$ I → retorno R$ G em N meses (ROI Xx)."
- Ancorar SEMPRE antes do número do preço.

## Regra
Usar premissas conservadoras e explícitas (o cliente confia mais).
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/roi-custo-inacao.md
git commit -m "docs(proposta): reference roi-custo-inacao"
```

---

## Task 7: Reference — modelos-preco.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/modelos-preco.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Modelos de preço (Fase 1 escolhe; pode combinar)

| Modelo | Quando usar | Mecânica |
|--------|-------------|----------|
| Pacotes em camadas (Good/Better/Best) | cliente indeciso, quer ancorar e subir ticket | 3 opções, recomendar a do meio |
| Preço único por valor | resultado claro, posicionamento premium | 1 preço ancorado em ROI, não em horas |
| Retainer/recorrente | gestão contínua, squad dedicado | fee mensal + escopo recorrente |
| Por projeto/escopo | entrega fechada e bem definida | orçamento por escopo, marcos de pagamento |

## Heurística de escolha
- Deal alto + decisor financeiro → valor único com ROI forte
- Relação longa / operação contínua → retainer
- Cliente comparando fornecedores → camadas (ancora)
- Escopo único e finito → por projeto

Sempre: ancorar valor ANTES do número. Oferecer no máx. 3 opções (paradoxo da escolha).
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/modelos-preco.md
git commit -m "docs(proposta): reference modelos-preco"
```

---

## Task 8: Reference — pitch-kit-followup.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/pitch-kit-followup.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Pitch-kit + follow-up (saída `pitch-kit.md`)

Gerar junto com o deck. O deal fecha no follow-up, não no envio.

## 1. Talking points (por seção do deck)
Para cada uma das 11 seções: 1-2 frases que o Thales fala ao apresentar.

## 2. Banco de objeções (3-5)
Para cada objeção provável: resposta curta + prova/reframe.
Ex: "Tá caro" → reframe custo de não-agir + ROI + payback.

## 3. Sequência de follow-up (3-5 e-mails) — usar copy-squad
- D+0: envio + resumo da tese + próximo passo
- D+2: prova/case relevante ao caso dele
- D+5: responder a objeção mais provável
- D+9: urgência legítima ("por que agora")
- D+14: break-up educado (reabre porta)

## Saída
Arquivo `pitch-kit.md` com as 3 seções, na pasta do projeto do cliente.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/pitch-kit-followup.md
git commit -m "docs(proposta): reference pitch-kit-followup"
```

---

## Task 9: Reference — marca-thales.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/marca-thales.md`
- Read-if-exists: `biblioteca/config/` (brand tokens do Thales)

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Marca do Thales → tema do Gamma

Objetivo: o deck sai com a identidade do Thales, não "premium genérico".

## Onde estão os tokens
Procurar em `biblioteca/config/` por um arquivo de marca do Thales (cores, tipografia, logo, voz).
- Existe → usar como `--theme` (tema custom do Gamma) e na camada visual.
- NÃO existe → mini-intake na 1ª run: perguntar cor primária, tipografia, logo, tom de voz;
  salvar em `biblioteca/config/marca-thales.json` para reuso (não re-perguntar depois).

## Mapear para o Gamma
- Criar/selecionar um tema no Gamma com as cores/fontes do Thales; passar `--theme "<nome>"`.
- Logo: inserir na capa e rodapé.
- Voz: refletida na copy (Fases 0-3), não no tema.

## Fallback (sem Gamma)
Aplicar os mesmos tokens via skills `design`/`pptx`.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/marca-thales.md
git commit -m "docs(proposta): reference marca-thales"
```

---

## Task 10: Reference — quality-gate.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/quality-gate.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Quality gate — checklist "fecharia?" (alvo 9+/10)

Refatora a fase responsável enquanto QUALQUER item falhar:

- [ ] Diagnóstico mostra a dor REAL do cliente (não genérico)
- [ ] Custo de não-agir QUANTIFICADO (número, não adjetivo)
- [ ] Mecanismo único — não comoditizável
- [ ] Preço ancorado ANTES do número + ROI/payback explícito
- [ ] Prova específica com números reais
- [ ] Endereça o DECISOR certo (linguagem do economic buyer)
- [ ] "Por que agora" legítimo (não escassez falsa)
- [ ] Objeções principais antecipadas e neutralizadas
- [ ] Fronteiras de escopo presentes (o que NÃO está incluso)
- [ ] CTA com próximo passo concreto
- [ ] Deck na marca do Thales (não premium genérico)
- [ ] Passa no teste "parece proposta de agência top 1?"
- [ ] PPTX e PDF coerentes (mesma direção)
- [ ] pitch-kit.md gerado (talking points + objeções + follow-up)

Score < 9 → identificar a fase culpada, corrigir, re-renderizar, re-checar.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/quality-gate.md
git commit -m "docs(proposta): reference quality-gate"
```

---

## Task 11: Reference — build-gamma.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/build-gamma.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Build via Gamma (Fase 4)

Pré: `GAMMA_API_KEY` no ambiente. Copy final das 11 seções salva em `outline.md`
(markdown: um H1 de tese + um H2 por seção com a copy pronta).

## Passos
1. Gerar o PPTX (fonte editável):
   `node scripts/gamma-generate.mjs --input outline.md --export pptx --out <projeto>/proposta.pptx --textMode preserve --numCards 11 --theme "<tema do Thales>"`
2. Derivar o PDF mantendo o MESMO deck:
   - Se LibreOffice instalado: `soffice --headless --convert-to pdf --outdir <projeto> <projeto>/proposta.pptx`
   - Senão: 2ª chamada do helper com `--export pdf` (aceitar leve variação visual).
3. Guardar `gammaUrl` e `gammaId` (log) para editar/arquivar depois.

## Regras
- SEMPRE `--textMode preserve` — Gamma diagrama, não reescreve nossa copy.
- `numCards` ≈ nº de seções (11). Ajustar se alguma seção virar 2 cards.
- Erro/timeout/quota → seguir `build-fallback-pptx.md`.
```

- [ ] **Step 2: Verificar referência ao script existe**

Run:
```
node -e "const fs=require('fs');if(!fs.existsSync('biblioteca/skills/criar-proposta-comercial-premium/scripts/gamma-generate.mjs'))throw new Error('helper ausente');console.log('helper OK')"
```
Expected: `helper OK`

- [ ] **Step 3: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/build-gamma.md
git commit -m "docs(proposta): reference build-gamma"
```

---

## Task 12: Reference — build-fallback-pptx.md

**Files:**
- Create: `biblioteca/skills/criar-proposta-comercial-premium/references/build-fallback-pptx.md`

- [ ] **Step 1: Escrever o conteúdo**

```markdown
# Build fallback (sem Gamma)

Quando: API fora, `failed`, timeout, ou quota estourada.

## Passos
1. Usar a skill `pptx` para montar o deck com as 11 seções (copy já pronta).
2. Aplicar a marca do Thales via skill `design` (cores/tipo/logo de `marca-thales.md`).
3. Exportar PDF: skill `pdf` (ou `soffice --headless --convert-to pdf`).
4. Mesmo quality gate (`quality-gate.md`).

## Regra
Fallback não pode travar a entrega: se Gamma falhar, avisar o Thales e seguir por aqui.
```

- [ ] **Step 2: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium/references/build-fallback-pptx.md
git commit -m "docs(proposta): reference build-fallback-pptx"
```

---

## Task 13: Roteamento na skill `workflow`

**Files:**
- Modify: `biblioteca/skills/workflow/SKILL.md`

- [ ] **Step 1: Localizar a tabela/lista de roteamento**

Run:
```
node -e "const f=require('fs').readFileSync('biblioteca/skills/workflow/SKILL.md','utf8');const i=f.toLowerCase().indexOf('roteamento');console.log(i>=0?f.slice(i,i+600):'secao de roteamento nao encontrada')"
```
Expected: trecho da seção de roteamento (para saber o formato exato a seguir).

- [ ] **Step 2: Adicionar a entrada de roteamento**

No formato existente da tabela/lista, adicionar uma linha mapeando intenção → skill. Exemplo (ajustar ao formato real encontrado no Step 1):

```markdown
| Proposta comercial / ofertar serviços a cliente / deck de venda | `criar-proposta-comercial-premium` |
```

- [ ] **Step 3: Verificar a entrada**

Run:
```
node -e "const f=require('fs').readFileSync('biblioteca/skills/workflow/SKILL.md','utf8');if(!f.includes('criar-proposta-comercial-premium'))throw new Error('roteamento nao adicionado');console.log('roteamento OK')"
```
Expected: `roteamento OK`

- [ ] **Step 4: Commit**

```
git add biblioteca/skills/workflow/SKILL.md
git commit -m "feat(workflow): rotear proposta comercial para criar-proposta-comercial-premium"
```

---

## Task 14: Validar a skill com skill-creator + espelhar em .claude/skills

**Files:**
- Create (cópia): `.claude/skills/criar-proposta-comercial-premium/`

- [ ] **Step 1: Validar estrutura da skill**

Run (confere SKILL.md + todas as 10 references + script):
```
node -e "const fs=require('fs');const b='biblioteca/skills/criar-proposta-comercial-premium';const need=['SKILL.md','scripts/gamma-generate.mjs','references/discovery-qualificacao.md','references/anatomia-proposta.md','references/fontes-mineracao.md','references/roi-custo-inacao.md','references/modelos-preco.md','references/pitch-kit-followup.md','references/marca-thales.md','references/quality-gate.md','references/build-gamma.md','references/build-fallback-pptx.md'];const miss=need.filter(p=>!fs.existsSync(b+'/'+p));if(miss.length)throw new Error('faltando: '+miss.join(', '));console.log('estrutura completa OK')"
```
Expected: `estrutura completa OK`

- [ ] **Step 2: Rodar avaliação do skill-creator**

Invocar a skill `skill-creator` no modo de validação/eval apontando para
`biblioteca/skills/criar-proposta-comercial-premium`. Corrigir o que ela apontar
(description triggers, clareza das fases). Re-rodar até passar.

- [ ] **Step 3: Espelhar em `.claude/skills` (cópia, padrão da pasta)**

Run:
```
node -e "require('fs').cpSync('biblioteca/skills/criar-proposta-comercial-premium','.claude/skills/criar-proposta-comercial-premium',{recursive:true,force:true});console.log('espelhado em .claude/skills')"
```
Expected: `espelhado em .claude/skills`

- [ ] **Step 4: Commit**

```
git add biblioteca/skills/criar-proposta-comercial-premium .claude/skills/criar-proposta-comercial-premium
git commit -m "chore(proposta): validar skill e espelhar em .claude/skills"
```

---

## Task 15: Teste end-to-end (caso real)

**Files:**
- Temp: pasta de um projeto-cliente de teste (ex: `out/teste-proposta/`)

- [ ] **Step 1: Rodar a skill num caso real**

Invocar a skill com um serviço real do Thales + um cliente-alvo real. Deixar as 7 fases
rodarem. Conferir que a Fase 0 bloqueia se faltar input core.

- [ ] **Step 2: Verificar as 3 saídas**

Run (ajustar caminho do projeto de teste):
```
node -e "const fs=require('fs');const d='out/teste-proposta';for(const f of ['proposta.pptx','proposta.pdf','pitch-kit.md']){if(!fs.existsSync(d+'/'+f))throw new Error('faltou '+f);console.log('OK '+f,fs.statSync(d+'/'+f).size,'bytes')}"
```
Expected: `OK proposta.pptx`, `OK proposta.pdf`, `OK pitch-kit.md`, todos > 0 bytes.

- [ ] **Step 3: Rodar o quality gate manualmente**

Conferir a proposta gerada contra `references/quality-gate.md`. Se algum item < 9,
identificar a fase culpada, corrigir a skill, re-rodar.

- [ ] **Step 4: Limpar artefatos de teste**

Run:
```
node -e "require('fs').rmSync('out/teste-proposta',{recursive:true,force:true});console.log('limpo')"
```

- [ ] **Step 5: Commit final**

```
git add -A
git commit -m "test(proposta): e2e validado, skill pronta"
```

---

## Notas de execução

- **Pré-requisito Task 1:** Thales gera a `GAMMA_API_KEY` antes de tudo.
- **Git:** se a pasta `Workflow Projetos` não for repo git, pular os commits (ou rodar `git init` se o Thales pedir).
- **Saídas reais sempre** na pasta do projeto do CLIENTE, nunca na biblioteca.
- **Molde:** ao terminar, esta skill vira referência para clonar os próximos `criar-X-premium` (brand, conteúdo, saas, campanha, vídeo).
