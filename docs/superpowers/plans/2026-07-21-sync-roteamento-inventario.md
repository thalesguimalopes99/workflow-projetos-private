# Sync Roteamento + Inventário — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sincronizar a camada de roteamento da biblioteca (workflow skill, CLAUDE.md, ROUTING-MAP, INVENTARIO) com o inventário real instalado (135 skills), versionar as ~29 skills faltantes no backup, automatizar o índice contra drift, e instalar um hook que reforça "analise tudo e escolha a melhor ferramenta" antes de criar.

**Dois gaps distintos (não confundir):** (1) **Roteamento** — GSD (67) + ~28 soltas = ~95 skills instaladas mas não citadas em workflow/CLAUDE.md (Tasks 4-6). (2) **Versionamento** — só **29** skills (todas não-GSD) estão no global mas fora de `biblioteca/`; os 67 GSD já estão versionados (Task 1).

**Architecture:** Três categorias de mudança. **Factual** (o que existe) → gerado por script a partir do filesystem. **Decisão** (o que preferir) → curado à mão nos docs de roteamento. **Enforcement** (garantir que a regra rode) → hook `UserPromptSubmit`. Ordem obrigatória: resync biblioteca ANTES de gerar o índice.

**Tech Stack:** Bash (Git Bash no Windows), rsync, Node (validação JSON), Markdown, Claude Code hooks (settings.json).

## Global Constraints

- **Sem `jq`** no PATH — scripts e hook não podem depender de `jq`. Usar `node` p/ validar JSON, `awk`/`grep`/`sed` p/ texto.
- **Windows / Git Bash** — caminhos com espaço (`C:\Users\Thales Lopes\...`); sempre aspas.
- **Excluir lixo pesado** em qualquer cópia de skills: `node_modules`, `.venv`, `dist`, `build`, `cache`, `.git`, `__pycache__`, `*.mp4`, `*.dll`, `*.exe`, `*.node`.
- **Três cópias do workflow skill** devem ficar em sincronia: `.claude/skills/workflow/SKILL.md` (uso local), `biblioteca/skills/workflow/SKILL.md` (backup versionado / fonte do seed), `~/.claude/skills/workflow/SKILL.md` (global).
- **GSD é skill, não command** — invocação `/gsd-new-project` (hífen), nunca `/gsd:new-project`.
- **Commits atômicos** — um commit por task. Trabalhar em branch (não `main`) — criar branch na Task 1.
- **Não** alterar conteúdo/comportamento de nenhuma skill; só roteamento, índice, script e hook.

---

## File Structure

| Arquivo | Responsabilidade | Ação |
|---|---|---|
| `biblioteca/skills/*` | Backup versionado das skills | +~29 dirs não-GSD (resync) |
| `scripts/gerar-inventario.sh` | Gera índice + relatório descriptions fracas do filesystem | Criar |
| `INVENTARIO.md` | Índice exaustivo (saída do script) | Regerar |
| `docs/superpowers/relatorio-descriptions.md` | Lista de descriptions fracas (saída do script) | Criar (gerado) |
| `.claude/skills/workflow/SKILL.md` (+2 cópias) | Tabela de intake | Modificar |
| `CLAUDE.md` | Protocolo + tabela tarefa→recurso | Modificar |
| `ROUTING-MAP.md` | Roteamento fino DENTRO de squad + GSD | Modificar |
| `.claude/hooks/routing-reminder.json` | Payload do hook (additionalContext) | Criar |
| `.claude/settings.json` | Registra o hook UserPromptSubmit | Criar |
| `scripts/instalar-em-novo-projeto.sh` | Seed de novo projeto | Modificar (levar settings+hooks) |

---

### Task 1: Resync biblioteca — versionar as ~29 skills faltantes

**Files:**
- Create/Modify: `biblioteca/skills/*` (adiciona ~29 subpastas não-GSD vindas do global; os 67 GSD já estão lá)

**Interfaces:**
- Produces: `biblioteca/skills` com ≥135 subpastas (fonte do seed e do gerador); 0 skills do global fora do backup.

- [ ] **Step 1: Criar branch de trabalho**

```bash
cd "C:/Users/Thales Lopes/Documents/wtf/Workflow Projetos"
git checkout -b sync-roteamento-inventario
```

- [ ] **Step 2: Contar baseline (antes)**

```bash
ls ~/.claude/skills | wc -l                 # esperado: 135 (global)
ls biblioteca/skills | wc -l                # esperado: 107 (antes)
```

- [ ] **Step 3: Rsync global → biblioteca (aditivo, sem --delete, excluindo lixo)**

```bash
cd "C:/Users/Thales Lopes/Documents/wtf/Workflow Projetos"
rsync -a \
  --exclude 'node_modules' --exclude '.venv' --exclude 'dist' \
  --exclude 'build' --exclude 'cache' --exclude '.git' \
  --exclude '__pycache__' \
  --exclude '*.mp4' --exclude '*.dll' --exclude '*.exe' --exclude '*.node' \
  ~/.claude/skills/ biblioteca/skills/
```

Nota: SEM `--delete` — preserva `criar-proposta-comercial-premium` (existe na biblioteca/local mas não no global). Rsync aditivo: adiciona faltantes + atualiza existentes.

- [ ] **Step 4: Verificar cobertura (depois)**

```bash
ls biblioteca/skills | wc -l                # esperado: >=135 (135 do global + 1 extra da biblioteca)
# O teste que importa — 0 skills do global fora do backup:
comm -23 <(ls ~/.claude/skills | sort) <(ls biblioteca/skills | sort) | wc -l   # esperado: 0
# Confirmar que as soltas chegaram:
ls biblioteca/skills | grep -E '^(docx|pdf|pptx|xlsx|mcp-builder|skill-creator|yt-dlp|supabase)$' | wc -l   # esperado: 8
```

Se o `comm` > 0: alguma skill do global ainda ficou fora. Investigar exclusões demais ou erro de rsync. NÃO prosseguir.

- [ ] **Step 5: Verificar que não entrou lixo pesado**

```bash
find biblioteca/skills -type d -name node_modules | head   # esperado: vazio
find biblioteca/skills -type f -name '*.exe' | head        # esperado: vazio
du -sh biblioteca/skills                                    # sanity: dezenas de MB, não GB
```

- [ ] **Step 6: Commit**

```bash
git add biblioteca/skills
git commit -m "chore(biblioteca): resync 95 skills faltantes do global (GSD + soltas) → 135 versionadas"
```

---

### Task 2: Script gerador `scripts/gerar-inventario.sh`

**Files:**
- Create: `scripts/gerar-inventario.sh`

**Interfaces:**
- Consumes: `~/.claude/skills`, `~/.claude/commands`, `~/.claude/agents`, `biblioteca/skills`.
- Produces: sobrescreve `INVENTARIO.md`; cria `docs/superpowers/relatorio-descriptions.md`. Exit 0 em sucesso.

- [ ] **Step 1: Escrever o script**

Create `scripts/gerar-inventario.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

# ============================================================================
# gerar-inventario.sh
# Gera INVENTARIO.md (índice exaustivo) + relatorio-descriptions.md
# a partir do filesystem real. Anti-drift: a parte factual nunca é editada à mão.
#
# Uso:  ./scripts/gerar-inventario.sh
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(cd "$SCRIPT_DIR/.." && pwd)"
GLOBAL_SKILLS="$HOME/.claude/skills"
GLOBAL_CMDS="$HOME/.claude/commands"
GLOBAL_AGENTS="$HOME/.claude/agents"
BIB_SKILLS="$RAIZ/biblioteca/skills"
OUT="$RAIZ/INVENTARIO.md"
REL="$RAIZ/docs/superpowers/relatorio-descriptions.md"
WEAK_MIN=40   # description < WEAK_MIN chars (ou ausente) = fraca
trap 'rm -f /tmp/inv_global.txt /tmp/inv_bib.txt' EXIT

# --- contagens (ls-based: ~/.claude/skills tem symlinks; find -type d não os conta) ---
n_global=$(ls -1 "$GLOBAL_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
n_bib=$(ls -1 "$BIB_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
n_squads=$(ls -1 "$GLOBAL_CMDS" 2>/dev/null | wc -l | tr -d ' ')
n_agents=$(ls -1 "$GLOBAL_AGENTS" 2>/dev/null | grep -c '\.md$' || true)
n_gsd=$(ls "$GLOBAL_SKILLS" | grep -c '^gsd-' || true)

# --- listas ---
ls "$GLOBAL_SKILLS" | sort > /tmp/inv_global.txt
ls "$BIB_SKILLS" | sort > /tmp/inv_bib.txt

# origem: [biblio] se está na biblioteca, senão [global-only]
origem_tag () {
  local name="$1"
  if grep -qxF "$name" /tmp/inv_bib.txt; then echo "[biblio]"; else echo "[global-only]"; fi
}

# --- gerar INVENTARIO.md ---
{
  echo "# Inventario da Biblioteca"
  echo ""
  echo "> GERADO por scripts/gerar-inventario.sh — NAO editar a mao (re-rode o script)."
  echo "> Fonte: filesystem real (~/.claude + biblioteca/)."
  echo ""
  echo "## Resumo"
  echo ""
  echo "| Bloco | Global (~/.claude) | Biblioteca (versionada) |"
  echo "|---|---|---|"
  echo "| skills | $n_global | $n_bib |"
  echo "| squads (commands) | $n_squads | - |"
  echo "| agents (.md) | $n_agents | - |"
  echo "| das quais GSD | $n_gsd | - |"
  echo ""
  # Drift real = skills do global fora do backup (NÃO igualdade de contagem —
  # a biblioteca pode ter extras locais que não estão no global).
  n_missing=$(comm -23 /tmp/inv_global.txt /tmp/inv_bib.txt | wc -l | tr -d ' ')
  if [ "$n_missing" -gt 0 ]; then
    echo "> ⚠️ DRIFT: $n_missing skill(s) do global fora da biblioteca. Rode o resync (rsync)."
    comm -23 /tmp/inv_global.txt /tmp/inv_bib.txt | awk '{printf "> - %s\n", $0}'
    echo ""
  fi

  echo "## Skills GSD ($n_gsd) — framework de projeto multi-fase"
  echo ""
  echo "### Track principal"
  echo ""
  ls "$GLOBAL_SKILLS" | grep '^gsd-' | grep -v '^gsd-ns-' | sort | awk '{printf "%s, ", $0}' | sed 's/, $//' || true
  echo ""
  echo ""
  echo "### Track leve \`gsd-ns-*\`"
  echo ""
  ls "$GLOBAL_SKILLS" | grep '^gsd-ns-' | sort | awk '{printf "%s, ", $0}' | sed 's/, $//' || true
  echo ""
  echo ""

  echo "## Skills não-GSD (alfabético, com origem)"
  echo ""
  while read -r s; do
    case "$s" in gsd-*) continue;; esac
    echo "- \`$s\` $(origem_tag "$s")"
  done < /tmp/inv_global.txt
  echo ""

  echo "## Squads ($n_squads)"
  echo ""
  ls "$GLOBAL_CMDS" | sort | awk '{printf "%s, ", $0}' | sed 's/, $//'
  echo ""
} > "$OUT"

# --- relatório de descriptions fracas ---
{
  echo "# Relatorio — descriptions fracas (candidatas a nunca disparar)"
  echo ""
  echo "> GERADO por gerar-inventario.sh. description < ${WEAK_MIN} chars ou ausente."
  echo "> Nivel 1 (auto-disparo): description fraca = skill instalada que nao aciona."
  echo ""
  echo "| Skill | Chars | Description (inicio) |"
  echo "|---|---|---|"
  while read -r s; do
    f="$GLOBAL_SKILLS/$s/SKILL.md"
    [ -f "$f" ] || continue
    # extrai a linha 'description:' do frontmatter (primeira ocorrencia)
    desc=$(awk -F'description:' '/^description:/{print $2; exit}' "$f" | sed 's/^[[:space:]]*//')
    len=${#desc}
    # bloco escalar YAML (> ou |) = description longa proposital, não é fraca
    case "$desc" in
      ''|'>'|'|'|'>-'|'|-'|'>+'|'|+') continue ;;
    esac
    if [ "$len" -lt "$WEAK_MIN" ]; then
      echo "| \`$s\` | $len | ${desc:0:60} |"
    fi
  done < /tmp/inv_global.txt
} > "$REL"

echo "OK: INVENTARIO.md ($n_global skills) + relatorio-descriptions.md gerados."
```

- [ ] **Step 2: Tornar executável**

```bash
cd "C:/Users/Thales Lopes/Documents/wtf/Workflow Projetos"
chmod +x scripts/gerar-inventario.sh
```

- [ ] **Step 3: Checar sintaxe bash (não roda ainda)**

Run: `bash -n scripts/gerar-inventario.sh`
Expected: sem saída, exit 0.

- [ ] **Step 4: Commit**

```bash
git add scripts/gerar-inventario.sh
git commit -m "feat(scripts): gerador anti-drift de INVENTARIO + relatorio de descriptions fracas"
```

---

### Task 3: Rodar o gerador e versionar as saídas

**Files:**
- Modify: `INVENTARIO.md` (regerado)
- Create: `docs/superpowers/relatorio-descriptions.md`

**Interfaces:**
- Consumes: `scripts/gerar-inventario.sh` (Task 2), `biblioteca/skills` resincronizada (Task 1).

- [ ] **Step 1: Rodar o script**

Run: `cd "C:/Users/Thales Lopes/Documents/wtf/Workflow Projetos" && ./scripts/gerar-inventario.sh`
Expected: `OK: INVENTARIO.md (135 skills) + relatorio-descriptions.md gerados.`

- [ ] **Step 2: Conferir coerência do INVENTARIO**

```bash
grep -E '^\| skills' INVENTARIO.md          # global 135 | biblioteca >=135
grep -c '^- `' INVENTARIO.md                # linhas de skills não-GSD listadas
grep 'DRIFT' INVENTARIO.md || echo "sem drift — ok"
```

Expected: global 135, biblioteca ≥135, **sem** aviso de DRIFT (0 skills do global fora do backup).

- [ ] **Step 3: Conferir o relatório de descriptions**

Run: `cat docs/superpowers/relatorio-descriptions.md`
Expected: tabela (pode estar vazia se todas as descriptions são fortes). Revisar quais skills aparecem — são candidatas a reescrever depois (fora do escopo deste plano).

- [ ] **Step 4: Commit**

```bash
git add INVENTARIO.md docs/superpowers/relatorio-descriptions.md
git commit -m "docs(inventario): regenerar do filesystem (135 skills) + relatorio de descriptions fracas"
```

---

### Task 4: Atualizar a skill `workflow` (GSD + clusters utilitárias + desempate)

**Files:**
- Modify: `.claude/skills/workflow/SKILL.md`
- Sync: `biblioteca/skills/workflow/SKILL.md`, `~/.claude/skills/workflow/SKILL.md`

**Interfaces:**
- Consumes: nada de código; edição de markdown.

- [ ] **Step 1: Adicionar linha GSD na tabela de roteamento**

Em `.claude/skills/workflow/SKILL.md`, na tabela "Entregável → recurso", logo após a linha `**Software (analyst→dev→qa→devops)**`, inserir:

```markdown
| **Projeto de software multi-fase / autônomo (ciclo com artefatos)** | projeto | framework **GSD** (`/gsd-new-project` → `/gsd-plan-phase` → `/gsd-execute-phase` → `/gsd-verify-work` → `/gsd-code-review` → `/gsd-ship`). Ver desempate GSD↔AIOX abaixo. | Sketch/Spike · MVP (`/gsd-mvp-phase`) · Produção (ciclo completo + secure/ui/eval-review) |
```

- [ ] **Step 2: Adicionar regra de desempate GSD↔AIOX**

Logo após a tabela de roteamento (antes de "## Regras de processo"), inserir:

```markdown
### Desempate GSD ↔ AIOX (ambos fazem software)

| Use **GSD** quando | Use **AIOX** quando |
|---|---|
| Projeto real multi-fase; quer ciclo disciplinado com artefatos (`.planning/`, PLAN/RESEARCH/VERIFICATION); execução autônoma/checkpointada; commits atômicos | Quer personas de time sob demanda (analyst/architect/dev/qa/devops) pra consultar/decidir, sem o overhead do ciclo de fases |
| Invoca skills `gsd-*` via `/gsd-new-project`, `/gsd-plan-phase`... | Invoca o chief `AIOX:agents:aiox-master` (roteia os agentes internos) |

> GSD é instalado como **skills** (`gsd-*`), não command namespace. `/gsd-new-project` (hífen).
```

- [ ] **Step 3: Adicionar bloco de clusters de skills utilitárias**

Após o bloco de desempate, inserir:

```markdown
### Clusters de skills utilitárias (fora da tabela principal, mas disponíveis)

Não são entregáveis de marca, mas o intake deve lembrar delas:

- **Docs/Office:** `docx`, `pdf`, `pptx`, `xlsx`, `doc-coauthoring`, `internal-comms`
- **Mídia:** `video-extract`, `yt-dlp`, `slack-gif-creator`, `curso-ripper`
- **Dev-infra:** `claude-api`, `mcp-builder`, `supabase`, `supabase-postgres-best-practices`, `webapp-testing`, `web-artifacts-builder`, `remotion-best-practices`, `distinctive-frontend`
- **Criativo extra:** `algorithmic-art`, `canvas-design`, `theme-factory`, `criativo-cliente`, `instagram-creative-director`, `brand-guidelines`
- **Growth:** `ranquear` (rankear no Google + citação por IA + crescer no Instagram — filtro cético de táticas SEO/GEO)
- **Meta/infra:** `skill-creator`, `template-skill`, `find-skills`

> Índice exaustivo de TODAS as skills: `INVENTARIO.md` (gerado). GSD: ver `ROUTING-MAP.md`.
```

- [ ] **Step 4: Sincronizar as 3 cópias**

```bash
cd "C:/Users/Thales Lopes/Documents/wtf/Workflow Projetos"
cp ".claude/skills/workflow/SKILL.md" "biblioteca/skills/workflow/SKILL.md"
cp ".claude/skills/workflow/SKILL.md" "$HOME/.claude/skills/workflow/SKILL.md"
# conferir iguais:
diff ".claude/skills/workflow/SKILL.md" "biblioteca/skills/workflow/SKILL.md" && echo "biblioteca OK"
diff ".claude/skills/workflow/SKILL.md" "$HOME/.claude/skills/workflow/SKILL.md" && echo "global OK"
```

Expected: "biblioteca OK" e "global OK" (sem diffs).

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/workflow/SKILL.md biblioteca/skills/workflow/SKILL.md
git commit -m "feat(workflow): rotear GSD + clusters utilitarios + desempate GSD/AIOX"
```

---

### Task 5: Atualizar `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Atualizar contagem no topo**

Substituir a linha (perto do topo):
`107 skills · 14 squads · 33 agents.`
por:
`135 skills (das quais 67 GSD) · 14 squads · 33 agents. Índice exaustivo: INVENTARIO.md (gerado).`

- [ ] **Step 2: Adicionar linha GSD na "Tabela de roteamento — tarefa → recurso"**

Após a linha `| Desenvolvimento de software (analyst→architect→dev→qa→devops) | squad **AIOX** (`aiox-master`) |`, inserir:

```markdown
| Projeto de software multi-fase / autônomo (ciclo com artefatos `.planning/`) | framework **GSD** (skills `/gsd-*`) — ver desempate GSD↔AIOX abaixo |
```

- [ ] **Step 3: Adicionar mini-seção de desempate dev (espelha a seção SEO)**

Após a seção "## Roteamento SEO — qual recurso usar", inserir:

```markdown
## Roteamento de dev — GSD vs AIOX (evita sobreposição)

Ambos cobrem software. Regra de desempate:

- **Ciclo de projeto multi-fase, autônomo, com artefatos** (`.planning/`, PLAN/RESEARCH/VERIFICATION), commits atômicos e checkpoints → framework **GSD**. Skills `gsd-*`, invocadas via `/gsd-new-project` → `/gsd-plan-phase` → `/gsd-execute-phase` → `/gsd-verify-work` → `/gsd-code-review` → `/gsd-ship`. Track leve: `gsd-ns-*`.
- **Personas de time sob demanda** (analyst/architect/dev/qa/devops) pra consultar/decidir, sem o overhead do ciclo → squad **AIOX** (`aiox-master`), que roteia os agentes internos.
- **Correção:** GSD é instalado como **skills** (`gsd-*`), não command namespace `/gsd:`. Invocação: `/gsd-new-project` (hífen).
```

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(claude-md): rotear GSD, desempate GSD/AIOX, contagem 135"
```

---

### Task 6: Atualizar `ROUTING-MAP.md` (seção GSD)

**Files:**
- Modify: `ROUTING-MAP.md`

- [ ] **Step 1: Adicionar seção GSD ao fim do arquivo**

Anexar em `ROUTING-MAP.md`:

```markdown
---

## GSD — framework de projeto multi-fase (67 skills `gsd-*`)

Não é squad; é ciclo. Regra de desempate com AIOX: GSD = ciclo disciplinado com artefatos (`.planning/`), autônomo; AIOX = personas de time sob demanda. Invocação: `/gsd-<skill>` (hífen — é skill, não command).

**Ciclo canônico:** `new-project` → `plan-phase` → `execute-phase` → `verify-work` → `code-review` → `ship`.

**8 clusters:**

1. **Início/Projeto** — `new-project`, `new-milestone`, `complete-milestone`, `milestone-summary`
2. **Planejar** — `plan-phase`, `discuss-phase`, `spec-phase`, `ultraplan-phase`, `plan-review-convergence`, `sketch`, `spike`
3. **Executar** — `execute-phase`, `mvp-phase`, `phase`, `fast`, `quick`, `autonomous`
4. **Verificar/QA** — `verify-work`, `validate-phase`, `code-review`, `secure-phase`, `ui-review`, `eval-review`, `audit-fix`, `audit-milestone`, `audit-uat`, `add-tests`
5. **Debug/Forense** — `debug`, `forensics`, `health`
6. **Docs/Contexto** — `docs-update`, `map-codebase`, `ingest-docs`, `capture`, `explore`, `graphify`, `surface`, `thread`
7. **Manutenção/Estado** — `cleanup`, `resume-work`, `pause-work`, `undo`, `update`, `config`, `settings`, `workspace`, `progress`, `stats`, `ship`, `pr-branch`, `import`, `inbox`, `review-backlog`, `manager`, `workstreams`, `extract-learnings`, `profile-user`, `help`, `review`
8. **Track leve `gsd-ns-*`** — `ns-context`, `ns-ideate`, `ns-project`, `ns-review`, `ns-manage`, `ns-workflow`

> Lista sempre atual: `INVENTARIO.md` (gerado). Prefixo `gsd-` = 67; `gsd-ns-` = track leve.
```

- [ ] **Step 2: Commit**

```bash
git add ROUTING-MAP.md
git commit -m "docs(routing-map): adicionar secao GSD (8 clusters + ciclo + track ns)"
```

---

### Task 7: Hook de enforcement `UserPromptSubmit` + seed

**Files:**
- Create: `.claude/hooks/routing-reminder.json`
- Create: `.claude/settings.json`
- Modify: `scripts/instalar-em-novo-projeto.sh`

**Interfaces:**
- Produces: hook que injeta `additionalContext` todo turno; seed que leva settings+hooks.

- [ ] **Step 1: Criar o payload do hook**

Create `.claude/hooks/routing-reminder.json` (JSON de UMA linha lógica, válido):

```json
{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"REGRA DE OURO (biblioteca Workflow Projetos): antes de criar/produzir QUALQUER entregável, analise os recursos do projeto e escolha as MELHORES ferramentas — invoque a skill `workflow` (intake) ou `briefing`, consulte `INVENTARIO.md`/`ROUTING-MAP.md` se presentes, e processo antes do especialista (superpowers). Nao entregue generico."}}
```

- [ ] **Step 2: Pipe-test do comando do hook (sem jq — só cat)**

Run:
```bash
cd "C:/Users/Thales Lopes/Documents/wtf/Workflow Projetos"
cat ".claude/hooks/routing-reminder.json" | node -e "let s='';process.stdin.on('data',d=>s+=d).on('end',()=>{JSON.parse(s);console.log('JSON valido')})"
```
Expected: `JSON valido`.

- [ ] **Step 3: Criar `.claude/settings.json` com o hook**

Create `.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "cat \"$CLAUDE_PROJECT_DIR/.claude/hooks/routing-reminder.json\"",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 4: Validar sintaxe do settings.json**

Run:
```bash
node -e "JSON.parse(require('fs').readFileSync('.claude/settings.json','utf8'));console.log('settings.json OK')"
```
Expected: `settings.json OK`.

- [ ] **Step 5: Confirmar que o schema do hook está correto (sem jq → node)**

Run:
```bash
node -e "const s=JSON.parse(require('fs').readFileSync('.claude/settings.json','utf8'));const c=s.hooks.UserPromptSubmit[0].hooks[0].command;if(!c.includes('routing-reminder.json'))throw new Error('comando errado');console.log('hook schema OK:',c)"
```
Expected: `hook schema OK: cat "$CLAUDE_PROJECT_DIR/.claude/hooks/routing-reminder.json"`.

- [ ] **Step 6: Fazer o seed levar settings.json + hooks/**

Em `scripts/instalar-em-novo-projeto.sh`, após o bloco "3b) Hook anti-segredo" (linha ~80), inserir novo bloco:

```bash
# --- 3c) Hook de roteamento (regra "melhor ferramenta") ----------------------
# Leva settings.json (registra o hook) + o payload .claude/hooks/.
if [ -f "$RAIZ/.claude/settings.json" ]; then
  cp -a "$RAIZ/.claude/settings.json" "$DESTINO/.claude/settings.json"
  echo "  [copiar] settings.json (hook UserPromptSubmit) -> $DESTINO/.claude/"
fi
if [ -d "$RAIZ/.claude/hooks" ]; then
  mkdir -p "$DESTINO/.claude/hooks"
  cp -a "$RAIZ/.claude/hooks/." "$DESTINO/.claude/hooks/"
  echo "  [copiar] .claude/hooks/ -> $DESTINO/.claude/hooks/"
fi
```

- [ ] **Step 7: Checar sintaxe do seed alterado**

Run: `bash -n scripts/instalar-em-novo-projeto.sh`
Expected: sem saída, exit 0.

- [ ] **Step 8: Garantir que `.claude/settings.json` não está gitignored**

```bash
git check-ignore .claude/settings.json && echo "IGNORADO — ajustar .gitignore" || echo "versionavel — ok"
```
Se "IGNORADO": adicionar exceção `!.claude/settings.json` no `.gitignore`. (`.claude/settings.local.json` continua ignorado.)

- [ ] **Step 9: Commit**

```bash
git add .claude/settings.json .claude/hooks/routing-reminder.json scripts/instalar-em-novo-projeto.sh
git add .gitignore 2>/dev/null || true
git commit -m "feat(hook): UserPromptSubmit reforca 'melhor ferramenta' + seed leva settings/hooks"
```

- [ ] **Step 10: Provar que o hook carrega (fora do turno)**

O watcher de settings só observa `.claude/` que já tinha settings no início da sessão. Como `.claude/settings.json` é novo, abrir `/hooks` (menu do usuário) uma vez OU reiniciar a sessão pra carregar. Depois, no próximo prompt, confirmar que o system-reminder de roteamento aparece. (Passo manual do Thales — não automatizável neste turno.)

---

## Notas de execução

- **Task 7 Step 10** exige ação do Thales (`/hooks` ou restart) — o hook não dispara na sessão atual até o config recarregar.
- **Ordem obrigatória:** Task 1 (resync) antes de Task 3 (gerar índice), senão INVENTARIO reporta drift.
- **Merge final:** ao terminar, usar `superpowers:finishing-a-development-branch` pra decidir merge/PR da branch `sync-roteamento-inventario`.
