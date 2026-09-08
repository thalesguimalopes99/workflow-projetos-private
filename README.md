# Workflow Projetos — Biblioteca de Skills, Squads e Agents do Claude Code

Kit pronto pro [Claude Code](https://claude.com/claude-code): **139 skills · 14 squads · 34 agents**.
Clona, instala os recursos no perfil global, abre o Claude Code na pasta e roda `/workflow`.
Funciona em **Windows, macOS e Linux** — sem symlink, sem caminho fixo de máquina.

## Pré-requisitos

- [Claude Code](https://claude.com/claude-code) instalado (`npm i -g @anthropic-ai/claude-code` ou app desktop).
- `git`.
- (Opcional) [`git-lfs`](https://git-lfs.com) — só pra baixar 6 PNGs de teste do skill `hyperframes`. Sem ele tudo funciona; esses assets vêm como ponteiro.
- (Opcional) Node.js — só se for usar o `remotion-video/`.

## Como usar (qualquer SO)

```bash
git clone https://github.com/<seu-usuario>/workflow-projetos.git
cd workflow-projetos
git config core.hooksPath .githooks   # ativa o hook que barra commit de segredo
cp .env.example .env                  # preencha as chaves se for usar (ex.: GAMMA_API_KEY)

# instala skills e agents no perfil global (passo obrigatório — ver nota abaixo)
mkdir -p ~/.claude/skills ~/.claude/agents
cp -r biblioteca/skills/*  ~/.claude/skills/
cp -r biblioteca/agents/*  ~/.claude/agents/

claude                                # abre o Claude Code nesta pasta
```

O `git config core.hooksPath` é **por clone** — o git não ativa hooks sozinho ao clonar.
Sem esse comando, nada impede um `git add -A` de commitar seu `.env`.

Dentro do Claude Code, rode:

```
/workflow
```

**O que carrega de onde** (mudou no commit `67a0a6f` — as cópias locais de skills e agents
foram removidas de propósito, e o `.gitignore` impede que voltem):

| Recurso | Origem | Carrega sozinho ao clonar? |
|---|---|---|
| **14 squads** | `.claude/commands/` (versionado no repo) | ✅ sim, nível de projeto |
| **139 skills** | `~/.claude/skills/` (perfil global) | ❌ não — precisa do passo de instalação acima |
| **34 agents** | `~/.claude/agents/` (perfil global) | ❌ não — precisa do passo de instalação acima |

A fonte da verdade versionada de skills e agents é **`biblioteca/`**, não `.claude/`. Editou um
recurso no global? Sincronize de volta pra `biblioteca/` — é ela que vai pro git.

> **macOS / Linux:** funciona direto.
> **Windows:** funciona direto também — todos os recursos são arquivos reais (sem symlink).

## O que tem

```
biblioteca/            FONTE DA VERDADE versionada — é daqui que você instala
  skills/              139 skills (workflow, briefing, GSD, design/marketing, SEO/GEO, motion, etc.)
  agents/              34 agents (33 GSD + executor)
  squads/              14 squads (backup limpo; cada um com agents/, tasks/, checklists/)
.claude/
  commands/            14 squads — o ÚNICO bloco que carrega automático, no nível do projeto
  hooks/               routing-reminder.json (lembrete de roteamento a cada prompt)
  settings.json        config do projeto (a .local.json é pessoal, fica fora do git)
CLAUDE.md              regras de roteamento (qual recurso pra cada tarefa)
ROUTING-MAP.md         índice fino: qual especialista DENTRO de cada squad + sequências
INVENTARIO.md          lista completa — GERADO por scripts/gerar-inventario.sh, não editar à mão
CREATIVE-OS.md         padrão de qualidade criativa (régua $1M / awwwards)
CLAUDE-BRANDING-OS.md  padrão de qualidade de marca/identidade
Cursos/                acervo de transcrições de curso + CONHECIMENTO.md (mapa por capacidade)
scripts/               gerar-inventario.sh · instalar-em-novo-projeto.sh
remotion-video/        projeto Remotion opcional (rode `npm install` se for usar)
```

Veja `INVENTARIO.md` pra lista detalhada.

## Variáveis de ambiente

Copie `.env.example` → `.env`. Só `GAMMA_API_KEY` (geração de slides) é usada, e é **opcional**.
O `.env` real **nunca** vai pro git: está no `.gitignore` e o hook `pre-commit` o barra.

> `.gitignore` não protege arquivo **já rastreado**. Se algum segredo entrar no índice,
> `git rm --cached <arquivo>` — só ignorar depois não adianta.

O hook usa **defesa em camadas**: uma regex de formatos conhecidos (roda sempre) mais o
[`gitleaks`](https://github.com/gitleaks/gitleaks) (700+ regras) quando instalado — ambos
precisam passar. Instalar o gitleaks amplia a cobertura:

```bash
winget install Gitleaks.Gitleaks   # Windows
brew install gitleaks              # macOS
```

A config fica em `.gitleaks.toml` (allowlist de falsos positivos conhecidos). Scan manual do
histórico inteiro: `gitleaks git .`

## Semear `.claude/` em OUTRO projeto

Quer levar esses recursos pro `.claude/` de um projeto diferente:

```bash
# macOS / Linux / Git Bash no Windows
./scripts/instalar-em-novo-projeto.sh "/caminho/do/projeto/destino"
```

## Licença / uso

Use à vontade. Os recursos em `.claude/skills/` incluem skills de terceiros (cada uma com
sua própria licença/origem nos respectivos `SKILL.md` / `LICENSE`).
