# Task 3 Report — Rodar o gerador e versionar as saídas

## Step 1 — Rodar o script

Command: `bash scripts/gerar-inventario.sh` (invoked via `bash`, not `./scripts/...`, since the
executable bit was not preserved on Windows — matches the task instructions).

**Actual stdout final line:**
```
OK: INVENTARIO.md (108 skills) + relatorio-descriptions.md gerados.
```

This does **not** match the brief's expected line (`135 skills`). See "Concerns" below — this is
a real discrepancy, not a typo on my part.

## Step 2 — Coerência do INVENTARIO.md

```
$ grep -E '^\| skills' INVENTARIO.md
| skills | 108 | 136 |

$ grep -c '^- `' INVENTARIO.md
68

$ grep 'DRIFT' INVENTARIO.md || echo "sem drift — ok"
sem drift — ok
```

- Global (`~/.claude/skills`): script reports **108**, brief expected **135**.
- Biblioteca (`biblioteca/skills`): **136** (≥135 — OK, matches Task 1's resync).
- DRIFT warning: **absent** (OK — 0 skills missing from the biblioteca backup).

**Root cause of the global-count mismatch (investigated, not fixed — out of scope):**
`~/.claude/skills` has 135 entries total, but 27 of them are **symlinks**
(`~/.claude/skills/<name> -> ~/.agents/skills/<name>`, e.g. `algorithmic-art`, `frontend-design`,
`webapp-testing`, `xlsx`, `supabase`, `pdf`, `docx`, all `hf-*`, etc.). The script counts
`n_global` with `find "$GLOBAL_SKILLS" -mindepth 1 -maxdepth 1 -type d`, and `find -type d`
does **not** classify a symlink-to-a-directory as `-type d` (it's `-type l`) unless `-L` is
passed. That undercounts by exactly 27 (135 − 27 = 108, confirmed by
`find ... -mindepth 1 -maxdepth 1 | wc -l` = 135 vs `-type d` = 108, and
`-type l` count = 27).

Importantly, the **DRIFT** check and the **skill listing** (both built from `ls`, not
`find -type d`) are unaffected and correct — all 135 skill names (symlinks included) are listed
and correctly cross-referenced against the biblioteca backup, hence "sem drift" is trustworthy.
Only the **displayed summary count** in the "Resumo" table (108 vs the true 135) is wrong. The
biblioteca-side count (136, real directories, no symlinks there) is accurate.

This is a script bug in `scripts/gerar-inventario.sh` (Task 2 deliverable), not something within
Task 3's scope to fix. Per task instructions I did not modify the script. Flagging as a concern
for follow-up (e.g. swap `find -type d` → `find -L -type d`, or count via `ls -1 | wc -l`, for
`n_global`).

## Step 3 — Relatório de descriptions fracas

`docs/superpowers/relatorio-descriptions.md` flags **6 skills**, all with 1–2 char "descriptions":

| Skill | Chars | Note |
|---|---|---|
| `brand-landingpage` | 1 | False positive |
| `criativo-cliente` | 2 | False positive |
| `humanizer` | 1 | False positive |
| `instagram-creative-director` | 2 | False positive |
| `motion-design` | 1 | False positive |
| `video-extract` | 2 | False positive |

I inspected each skill's `SKILL.md` frontmatter directly. **All 6 are false positives** matching
the documented known limitation exactly: every one uses a YAML block-scalar description
(`description: >`, `description: >-`, or `description: |`) spanning multiple following lines,
and all have substantial, well-formed, long descriptions (150–500+ chars) once the block scalar
is read correctly. The parser (`awk -F'description:' '/^description:/{print $2; exit}'`) only
reads the same line, so it captures nothing but the block-scalar indicator character.
No genuinely weak descriptions were found among the 6 — the report is 100% false positives in
this run. Per instructions, not fixing the script.

## Step 4 — Commit

```
git add INVENTARIO.md docs/superpowers/relatorio-descriptions.md
git commit -m "docs(inventario): regenerar do filesystem (135 skills) + relatorio de descriptions fracas"
```

- Pre-commit hook (gitleaks) ran clean: "0 commits scanned... no leaks found".
- Commit: `63cce97ae2b289e87172a405e9db313dc8fe1b74` — "docs(inventario): regenerar do
  filesystem (135 skills) + relatorio de descriptions fracas"
- 2 files changed: `INVENTARIO.md` (modified), `docs/superpowers/relatorio-descriptions.md`
  (created).

## Concerns

1. **Global skill count in INVENTARIO.md's Resumo table is wrong (108, should be 135).**
   Root cause identified above (symlinks + `find -type d` not following them). This is
   pre-existing in `scripts/gerar-inventario.sh` from Task 2, reproducible on any environment
   where `~/.claude/skills` contains symlinked skills (common with plugin-provided skills
   linked from `~/.agents/skills`). The DRIFT/coherence guarantee itself is still correct
   (0 missing), but the headline number is misleading and should be fixed before this becomes
   the trusted source of truth. Recommend a follow-up task/patch: change `n_global` to either
   `find -L "$GLOBAL_SKILLS" -mindepth 1 -maxdepth 1 -type d | wc -l` or
   `ls -1 "$GLOBAL_SKILLS" | wc -l`.
2. Two untracked files unrelated to this task remain in the working tree
   (`curso-ripper.zip`, `yt-dlp.zip`) — not touched, not part of this commit.
3. Two plan/spec docs (`docs/superpowers/plans/...`, `docs/superpowers/specs/...`) are untracked
   and were left as-is (not part of Task 3's file scope).

## Fix — Task 3 follow-up: n_global undercounted symlinked skills

Root cause confirmed above (Concern 1) was fixed in a follow-up pass on branch
`sync-roteamento-inventario`.

### Change

In `scripts/gerar-inventario.sh`, `--- contagens ---` block: replaced `find ... -type d`-based
counts with `ls`-based counts (consistent with the DRIFT logic, which was already `ls`-based and
therefore already correct). `find -type d` does not classify a symlink-to-directory as `-type d`
without `-L`, undercounting `n_global` by exactly the 27 symlinked skills
(`~/.claude/skills/<name> -> ~/.agents/skills/<name>`).

```diff
-n_global=$(find "$GLOBAL_SKILLS" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
-n_bib=$(find "$BIB_SKILLS" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
-n_squads=$(find "$GLOBAL_CMDS" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
-n_agents=$(find "$GLOBAL_AGENTS" -maxdepth 1 -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
+n_global=$(ls -1 "$GLOBAL_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
+n_bib=$(ls -1 "$BIB_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
+n_squads=$(ls -1 "$GLOBAL_CMDS" 2>/dev/null | wc -l | tr -d ' ')
+n_agents=$(ls -1 "$GLOBAL_AGENTS" 2>/dev/null | grep -c '\.md$' || true)
```

`n_gsd` left untouched (already `ls`-based). No other logic (drift check, lists, weak-desc
report) was changed.

### Verification

```
$ bash -n scripts/gerar-inventario.sh
(no output — syntax OK)

$ bash scripts/gerar-inventario.sh
OK: INVENTARIO.md (135 skills) + relatorio-descriptions.md gerados.

$ grep -E '^\| skills' INVENTARIO.md
| skills | 135 | 136 |

$ grep 'DRIFT' INVENTARIO.md || echo "sem drift — ok"
sem drift — ok
```

Global now correctly shows **135** (matches biblioteca's ≥135), DRIFT check remains absent (still
0 missing).

### Commit

```
git add scripts/gerar-inventario.sh INVENTARIO.md docs/superpowers/relatorio-descriptions.md
git commit -m "fix(scripts): contar skills via ls (inclui symlinks) + regenerar INVENTARIO (135)"
```

- Pre-commit hook (gitleaks) ran clean: "0 commits scanned... no leaks found". No skill-name-list
  false positive encountered.
- Commit: `ff7e721` — "fix(scripts): contar skills via ls (inclui symlinks) + regenerar
  INVENTARIO (135)"
- 2 files changed: `scripts/gerar-inventario.sh` (+5/-5), `INVENTARIO.md` (+1/-1).
  `docs/superpowers/relatorio-descriptions.md` was staged per instructions but had no content
  diff (weak-description findings unchanged), so git recorded no change for it.

Concern 1 from the original Task 3 report is now resolved.
