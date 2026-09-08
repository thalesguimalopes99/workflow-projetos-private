#!/usr/bin/env bash
# Converte os agents dos squads da biblioteca em skills nativas do Claude Code.
# Padrao espelhado do AIOX: ~/.claude/skills/<squad>/agents/<id>/SKILL.md
set -u

# Raiz derivada da localizacao do script — nao hardcodar caminho de maquina.
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$RAIZ/biblioteca/squads"
DST="$HOME/.claude/skills"

total=0
skipped=0

field() {
  # $1 = arquivo, $2 = nome do campo yaml
  grep -m1 -E "^[[:space:]]*$2:" "$1" 2>/dev/null \
    | sed -E "s/^[[:space:]]*$2:[[:space:]]*//; s/^\"//; s/\"$//; s/^'//; s/'$//" \
    | tr '"' "'" | tr -d '\r'
}

for squad in "$SRC"/*/; do
  s=$(basename "$squad")
  [ "$s" = "AIOX" ] && continue
  [ -d "${squad}agents" ] || { echo "sem agents: $s"; continue; }

  for f in "${squad}agents"/*.md; do
    [ -f "$f" ] || continue
    id=$(basename "$f" .md)
    out="$DST/$s/agents/$id"

    nome=$(field "$f" "name")
    titulo=$(field "$f" "title")
    quando=$(field "$f" "whenToUse")

    [ -z "$nome" ] && nome="$id"
    desc="Ativa $nome"
    [ -n "$titulo" ] && desc="$desc — $titulo"
    [ -n "$quando" ] && desc="$desc. Use quando: $quando"
    desc="[squad: $s] $desc"
    desc=$(printf '%s' "$desc" | cut -c1-420)

    mkdir -p "$out"
    {
      printf -- '---\n'
      printf 'name: %s-%s\n' "$s" "$id"
      printf 'description: "%s"\n' "$desc"
      printf 'user-invocable: true\n'
      printf -- '---\n\n'
      printf '> **Fonte da verdade:** `%s`\n' "$f"
      printf '> Persona completa abaixo. Sequencias multi-agent: `ROUTING-MAP.md` na raiz da biblioteca.\n\n'
      cat "$f"
    } > "$out/SKILL.md"

    if [ -s "$out/SKILL.md" ]; then
      total=$((total+1))
    else
      echo "FALHOU: $f"
      skipped=$((skipped+1))
    fi
  done
done

echo "---"
echo "instalados: $total"
echo "falhas: $skipped"
