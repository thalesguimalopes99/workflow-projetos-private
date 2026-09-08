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

