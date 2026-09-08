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

# --- contagens ---
n_global=$(ls -1 "$GLOBAL_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
n_bib=$(ls -1 "$BIB_SKILLS" 2>/dev/null | wc -l | tr -d ' ')
# so DIRETORIOS contam como squad — $GLOBAL_CMDS tem arquivo solto (greet.md) e o dir synapse, ambos do aiox-core
n_squads=$(find "$GLOBAL_CMDS" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
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
