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

