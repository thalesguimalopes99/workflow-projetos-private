#!/usr/bin/env bash
set -euo pipefail

# ============================================================================
# instalar-em-novo-projeto.sh
# Semeia a pasta .claude/ de um projeto destino com os recursos reutilizaveis
# guardados nesta biblioteca (skills, squads/commands e agents).
#
# Uso:
#   ./scripts/instalar-em-novo-projeto.sh "/caminho/do/projeto/destino"
#
# O script copia:
#   biblioteca/skills  ->  DESTINO/.claude/skills
#   biblioteca/squads  ->  DESTINO/.claude/commands
#   biblioteca/agents  ->  DESTINO/.claude/agents
# ============================================================================

# --- 1) Checagem de argumento ------------------------------------------------
if [ "$#" -lt 1 ]; then
  echo "ERRO: faltou o caminho do projeto destino."
  echo "Uso:  $0 \"/caminho/do/projeto/destino\""
  exit 1
fi

DESTINO="$1"

# Diretorio raiz desta biblioteca (a pasta acima de scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(cd "$SCRIPT_DIR/.." && pwd)"
BIB="$RAIZ/biblioteca"

# --- 2) Validacoes -----------------------------------------------------------
if [ ! -d "$BIB" ]; then
  echo "ERRO: pasta biblioteca/ nao encontrada em: $BIB"
  exit 1
fi

if [ ! -d "$DESTINO" ]; then
  echo "Aviso: o destino \"$DESTINO\" nao existe. Criando..."
  mkdir -p "$DESTINO"
fi

echo "==> Semeando .claude/ em: $DESTINO"
mkdir -p "$DESTINO/.claude"

# --- 3) Copia de cada bloco --------------------------------------------------
copiar_bloco () {
  local origem="$1"
  local alvo="$2"
  local rotulo="$3"
  if [ ! -d "$origem" ]; then
    echo "  [pular] $rotulo: origem inexistente ($origem)"
    return 0
  fi
  echo "  [copiar] $rotulo -> $alvo"
  mkdir -p "$alvo"
  # -a preserva estrutura; cp -r com '/.' copia o conteudo para dentro do alvo
  cp -a "$origem/." "$alvo/"
}

copiar_bloco "$BIB/skills" "$DESTINO/.claude/skills"   "skills"
copiar_bloco "$BIB/squads" "$DESTINO/.claude/commands" "squads (commands)"
copiar_bloco "$BIB/agents" "$DESTINO/.claude/agents"   "agents"

# --- 4) Resumo ---------------------------------------------------------------
echo ""
echo "==> Concluido. Resumo:"
echo "    skills   : $(find "$DESTINO/.claude/skills"   -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l) subpastas"
echo "    commands : $(find "$DESTINO/.claude/commands" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l) squads"
echo "    agents   : $(find "$DESTINO/.claude/agents"   -maxdepth 1 -name '*.md' 2>/dev/null | wc -l) arquivos .md"
echo ""
echo "Pronto! Abra o projeto no Claude Code e os recursos locais estarao disponiveis."
