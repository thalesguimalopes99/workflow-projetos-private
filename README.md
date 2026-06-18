# Workflow Projetos — Biblioteca Central de Recursos do Claude Code

Esta pasta e a **fonte da verdade / kit inicial** dos recursos reutilizaveis do
Claude Code do Thales: skills, squads (chiefs/agents/tasks) e agents. Sempre que
voce comecar um projeto novo, e daqui que voce puxa tudo.

## O que tem aqui

```
Workflow Projetos/
  biblioteca/
    skills/      <- 107 skills (GSD, HyperFrames, design/marketing, marketing skills.sh, SEO/GEO, workflow, briefing, site-teardown, motion-design, etc.)
    squads/      <- 14 squads (cada um com agents/, tasks/, checklists/, workflows/)
    agents/      <- 33 agents globais GSD (.md)
    config/      <- settings.global.referencia.json (copia do ~/.claude/settings.json)
  scripts/
    instalar-em-novo-projeto.sh   <- semeia o .claude/ de um projeto destino
  README.md
  INVENTARIO.md  <- lista completa de skills, squads e agents
```

Conteudo limpo: ~41,5 MB de texto (.md/.yaml). Todo o lixo pesado
(`node_modules`, `.venv`, `dist`, `build`, `.git`, `.mp4`, `.dll`, `.exe`)
foi **excluido** da copia — as fontes originais somavam ~1,6 GB.

Veja o `INVENTARIO.md` para a lista detalhada de cada skill, squad e agent.

## Como semear um projeto novo

No git-bash (Windows), a partir desta pasta:

```bash
./scripts/instalar-em-novo-projeto.sh "/caminho/do/projeto/destino"
```

O script copia:

| Biblioteca           | Destino no projeto         |
|----------------------|----------------------------|
| `biblioteca/skills`  | `DESTINO/.claude/skills`   |
| `biblioteca/squads`  | `DESTINO/.claude/commands` |
| `biblioteca/agents`  | `DESTINO/.claude/agents`   |

Ele cria as pastas (`mkdir -p`), copia tudo e mostra um resumo no final.

## NOTA IMPORTANTE — global x local

As skills, commands (squads) e agents **ja estao instalados GLOBALMENTE** em
`~/.claude/` (`C:/Users/Thales Lopes/.claude/`). Por isso eles **ja valem para
todos os projetos automaticamente** — voce nao precisa copiar nada so para
usa-los no dia a dia.

Entao para que serve esta pasta?

1. **Backup versionavel da fonte da verdade.** Se algo for apagado ou corrompido
   no `~/.claude/` global, voce restaura daqui. E como esta tudo em texto leve,
   da para versionar em git sem peso.

2. **Kit para semear `.claude/` LOCAL de um projeto especifico** — util quando
   voce quer travar a versao dos recursos junto com o repositorio do projeto, ou
   levar o conjunto para **outra maquina** que ainda nao tem o `~/.claude/`
   global configurado. Para isso, use o script acima.

## Sobre o config de referencia

`biblioteca/config/settings.global.referencia.json` e uma copia do
`~/.claude/settings.json` global. Ele contem hooks do GSD com **caminhos
absolutos** desta maquina, plugins habilitados, statusLine e permissoes. Use-o
apenas como referencia; nao copie cru por cima do settings de um projeto novo
sem antes revisar os caminhos.
