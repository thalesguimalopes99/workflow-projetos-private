# NOTA DE ARQUITETURA — AIOX é gerenciado FORA desta biblioteca

> Escrito em 2026-09-08 durante auditoria de sincronia. Leia antes de reinstalar,
> editar ou confiar nos arquivos desta pasta.

## O problema

AIOX é o único squad desta biblioteca cuja fonte da verdade **não é** `biblioteca/`.
Ele pertence ao repositório separado `~/aios-core` (git próprio, remoto próprio), e
mudou de arquitetura em **23/07/2026**.

Esta pasta esteve congelada em **16/04/2026** (personas monolíticas pré-refactor) até a
auditoria de 08/09/2026, quando os 12 arquivos foram re-espelhados da fonte canônica.
Hoje é **espelho de leitura**, não fonte — e volta a defasar sozinha a cada mudança no
`~/aios-core`.

## Como está hoje, nas três camadas

| Camada | Caminho | Formato | Tamanho típico |
|---|---|---|---|
| **Fonte canônica** | `~/aios-core/.aiox-core/development/agents/<id>.md` | persona completa, atual | ~25 KB |
| **Skill canônica** | `~/.claude/skills/AIOX/agents/<id>/SKILL.md` | payload de ativação | — |
| **Shim de compat.** | `~/.claude/commands/AIOX/agents/<id>.md` | `<!-- ACORE-CLAUDE-AGENT-COMMAND: legacy-shim -->` apontando pra Skill canônica | ~700 B |
| **Esta biblioteca** | `biblioteca/squads/AIOX/agents/<id>.md` | espelho da canônica (sync 08/09/2026) | ~25 KB |

## O que isso significa na prática

- **Não edite estes arquivos esperando efeito.** O que o Claude Code carrega são os shims
  em `~/.claude/commands/AIOX/` e as Skills em `~/.claude/skills/AIOX/agents/`. Editar
  aqui não muda comportamento nenhum — e o próximo sync sobrescreve.
- **Não reinstale o squad AIOX a partir desta pasta.** Instale do `~/aios-core`, que é
  onde o versionamento acontece.
- **Servem pra ler**: alimentam o `ROUTING-MAP.md` (seção `## AIOX`) e funcionam como
  backup portátil das personas. Não são backup *executável*.

## Como re-sincronizar quando defasar

```bash
C=~/aios-core/.aiox-core/development/agents
for f in biblioteca/squads/AIOX/agents/*.md; do cp "$C/$(basename "$f")" "$f"; done
```

## Onde editar de verdade

```
~/aios-core/.aiox-core/development/agents/<id>.md   # fonte
```

`~/aios-core` é repo git com remoto próprio — o versionamento do AIOX acontece lá, não aqui.

## Divergência conhecida com a regra da biblioteca

O `CLAUDE.md` deste projeto diz, em "Manutenção da biblioteca", que `biblioteca/` é a
fonte da verdade versionável de todo recurso. **AIOX é a exceção documentada.** Os outros
13 squads seguem a regra normalmente.
