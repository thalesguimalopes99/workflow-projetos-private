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

