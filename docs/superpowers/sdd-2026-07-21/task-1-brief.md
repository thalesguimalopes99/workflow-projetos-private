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

