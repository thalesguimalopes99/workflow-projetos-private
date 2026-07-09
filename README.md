# Workflow Projetos — Biblioteca de Skills, Squads e Agents do Claude Code

Kit pronto pro [Claude Code](https://claude.com/claude-code): **107 skills · 14 squads · 33 agents**.
Clona, abre o Claude Code na pasta e roda `/workflow`. Funciona em **Windows, macOS e Linux** —
sem symlink, sem caminho fixo de máquina, sem instalar nada global.

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
claude                                # abre o Claude Code nesta pasta
```

O `git config core.hooksPath` é **por clone** — o git não ativa hooks sozinho ao clonar.
Sem esse comando, nada impede um `git add -A` de commitar seu `.env`.

Dentro do Claude Code, rode:

```
/workflow
```

As skills, squads (commands) e agents carregam **automaticamente** de `.claude/` porque
o Claude Code lê os recursos no nível do projeto. Nada precisa ser copiado pra `~/.claude`.

> **macOS / Linux:** funciona direto.
> **Windows:** funciona direto também — todos os recursos são arquivos reais (sem symlink).

## O que tem

```
.claude/
  skills/      107 skills (workflow, briefing, GSD, design/marketing, SEO/GEO, motion, etc.)
  commands/    14 squads (cada um com agents/, tasks/, checklists/)
  agents/      33 agents
CLAUDE.md      regras de roteamento (qual recurso pra cada tarefa)
ROUTING-MAP.md índice fino de roteamento por squad
INVENTARIO.md  lista completa de skills, squads e agents
CREATIVE-OS.md padrão de qualidade criativa
biblioteca/    backup versionável da fonte da verdade (mesmo conteúdo)
remotion-video/ projeto Remotion opcional (rode `npm install` se for usar)
```

Veja `INVENTARIO.md` pra lista detalhada.

## Variáveis de ambiente

Copie `.env.example` → `.env`. Só `GAMMA_API_KEY` (geração de slides) é usada, e é **opcional**.
O `.env` real **nunca** vai pro git: está no `.gitignore` e o hook `pre-commit` o barra.

> `.gitignore` não protege arquivo **já rastreado**. Se algum segredo entrar no índice,
> `git rm --cached <arquivo>` — só ignorar depois não adianta.

Reforço opcional: instale [`gitleaks`](https://github.com/gitleaks/gitleaks) e o hook passa
a usá-lo no lugar da varredura por regex, que é mais rasa.

## Semear `.claude/` em OUTRO projeto

Quer levar esses recursos pro `.claude/` de um projeto diferente:

```bash
# macOS / Linux / Git Bash no Windows
./scripts/instalar-em-novo-projeto.sh "/caminho/do/projeto/destino"
```

## Licença / uso

Use à vontade. Os recursos em `.claude/skills/` incluem skills de terceiros (cada uma com
sua própria licença/origem nos respectivos `SKILL.md` / `LICENSE`).
