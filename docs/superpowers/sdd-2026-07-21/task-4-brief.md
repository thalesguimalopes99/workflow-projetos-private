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

