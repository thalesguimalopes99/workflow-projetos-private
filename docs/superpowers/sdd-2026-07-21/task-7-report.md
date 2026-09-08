# Task 7 Report — Hook de enforcement `UserPromptSubmit` + seed

> Nota: `.superpowers/sdd/task-7-brief.md` não existia no filesystem no início desta
> task. Trabalhei a partir do conteúdo completo da Task 7 em
> `docs/superpowers/plans/2026-07-21-sync-roteamento-inventario.md` (idêntico ao que
> a descrição da task já continha) — mesma fonte, sem divergência de conteúdo.

## Arquivos

- Criado: `.claude/hooks/routing-reminder.json`
- Criado: `.claude/settings.json`
- Modificado: `scripts/instalar-em-novo-projeto.sh` (bloco `3c` inserido logo após o
  bloco `3b) Hook anti-segredo`, antes de `# --- 4) Resumo`)

## Verificações (Steps 1-9)

**Step 1 — payload criado** (`.claude/hooks/routing-reminder.json`), conteúdo verbatim
do brief/plano (uma linha lógica de JSON).

**Step 2 — pipe-test (sem jq, node valida):**
```
cat ".claude/hooks/routing-reminder.json" | node -e "let s='';process.stdin.on('data',d=>s+=d).on('end',()=>{JSON.parse(s);console.log('JSON valido')})"
```
Saída: `JSON valido` ✅

**Step 3 — `.claude/settings.json` criado** (verbatim do brief/plano — hook
`UserPromptSubmit` → `command: cat "$CLAUDE_PROJECT_DIR/.claude/hooks/routing-reminder.json"`,
`timeout: 5`). Confirmado que não havia `settings.json` prévio (só `settings.local.json`,
que já era ignorado e não foi tocado).

**Step 4 — parse do settings.json (node):**
```
node -e "JSON.parse(require('fs').readFileSync('.claude/settings.json','utf8'));console.log('settings.json OK')"
```
Saída: `settings.json OK` ✅

**Step 5 — schema do comando do hook (node):**
```
node -e "const s=JSON.parse(...);const c=s.hooks.UserPromptSubmit[0].hooks[0].command;if(!c.includes('routing-reminder.json'))throw new Error('comando errado');console.log('hook schema OK:',c)"
```
Saída: `hook schema OK: cat "$CLAUDE_PROJECT_DIR/.claude/hooks/routing-reminder.json"` ✅

**Step 6 — bloco 3c inserido no seed script**, imediatamente após o bloco 3b (hook
anti-segredo) e antes de `# --- 4) Resumo ---`. Copia `settings.json` + `.claude/hooks/`
para o destino semeado, condicional a existirem na biblioteca (mesmo padrão defensivo
dos blocos anteriores).

**Step 7 — sintaxe bash do script alterado:**
```
bash -n scripts/instalar-em-novo-projeto.sh
```
Sem saída, exit 0 ✅

**Step 8 — `.claude/settings.json` gitignored?**
```
git check-ignore .claude/settings.json && echo "IGNORADO — ajustar .gitignore" || echo "versionavel — ok"
```
Resultado: **"versionavel — ok"** — `settings.json` NÃO está ignorado (só
`.claude/settings.local.json` está, linha 22 do `.gitignore` raiz, intocada).
**`.gitignore` NÃO precisou ser tocado.**

**Step 9 — commit.** Staged apenas os 3 arquivos do escopo da task (não incluí os
arquivos soltos não relacionados `curso-ripper.zip`, `yt-dlp.zip`, docs de plano/spec
que já estavam untracked no working tree antes desta task).

Pre-commit hook (gitleaks) rodou limpo: `0 commits scanned`, `no leaks found`. Sem
bloqueio, sem falso positivo — nenhum `--no-verify` foi necessário.

## Commit

```
290a0fdb3393210d9fb79827479dd6e9a2603b93
feat(hook): UserPromptSubmit reforca 'melhor ferramenta' + seed leva settings/hooks
```

Arquivos no commit:
- `.claude/hooks/routing-reminder.json` (novo)
- `.claude/settings.json` (novo)
- `scripts/instalar-em-novo-projeto.sh` (modificado, bloco 3c)

3 files changed, 28 insertions(+)

## Step 10 — pendente (ação do Thales)

**NÃO tentado**, conforme instrução explícita da task. O watcher de settings só
observa pastas `.claude/` que já tinham `settings.json` no início da sessão; como o
arquivo é novo nesta sessão, é preciso o Thales abrir `/hooks` (menu do usuário) ou
reiniciar a sessão para o hook carregar e disparar no próximo prompt.

## Preocupações

Nenhuma. Todas as verificações da task passaram de primeira; nenhum ajuste de
`.gitignore` foi necessário; gitleaks não sinalizou nada no payload (é prosa de
roteamento, sem segredos).
