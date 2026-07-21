# Design — Sincronizar camada de roteamento com o inventário real

**Data:** 2026-07-21
**Autor:** Thales + Claude
**Status:** aprovado (aguardando review do spec)

## Problema

A biblioteca Workflow Projetos roteia ~107 skills, mas a realidade instalada é **135
skills · 14 squads · 33 agents**. **95 skills ficam invisíveis** no intake:

- **67 skills GSD** (`gsd-*`) — framework de projeto multi-fase, não roteado em lugar nenhum.
- **28 skills soltas** não-GSD instaladas no global além da biblioteca (docx, pdf, pptx,
  xlsx, mcp-builder, skill-creator, supabase, yt-dlp, ranquear, video-extract,
  webapp-testing, web-artifacts-builder, algorithmic-art, canvas-design, theme-factory,
  claude-api, doc-coauthoring, internal-comms, remotion-best-practices,
  instagram-creative-director (+workspace), distinctive-frontend, brand-guidelines,
  slack-gif-creator, curso-ripper, find-skills, template-skill,
  supabase-postgres-best-practices).

Os 4 artefatos de roteamento estão desalinhados entre si e do global:
`workflow` skill · `CLAUDE.md` · `ROUTING-MAP.md` · `INVENTARIO.md` (este último até
internamente inconsistente: diz "96" e "107" na mesma página).

### Os dois níveis de "aparecer" (diagnóstico que orienta a solução)

1. **Auto-disparo (Nível 1):** toda skill instalada já é visível ao Claude via o campo
   `description` do frontmatter — é o texto que dispara a invocação. Skill não some por
   estar fora do CLAUDE.md; mas `description` fraca/vaga nunca dispara. Esse é o gatilho real.
2. **Roteamento curado (Nível 2):** CLAUDE.md + workflow skill = camada que diz *qual
   preferir*, *como sequenciar*, *regra de desempate*, e torna a skill **descobrível pelo
   humano**. Sem isso a skill fica **subusada**, não zero-usada — no acaso da description.

Causa-raiz do drift: sincronização **manual**. Solução tem de atacar os dois níveis e
não re-apodrecer.

## Solução

Três categorias: **factual (o que existe) → gerado por script**; **decisão (o que
preferir) → curado à mão**; **enforcement (garantir que a regra rode sempre) → hook**.

### Componente 1 — Script gerador (anti-drift) `scripts/gerar-inventario.sh`

- Lê `~/.claude/skills`, `~/.claude/commands` (squads), `~/.claude/agents`, e `biblioteca/`.
- **Gera `INVENTARIO.md`** com: contagem real, todas as skills por cluster de domínio,
  e tag de origem `[biblio]` (versionada no backup) vs `[global-only]` (ainda não no backup).
- **Emite relatório de descriptions fracas** (`docs/superpowers/relatorio-descriptions.md`):
  skills cujo `description` do frontmatter é curto demais / sem triggers claros — candidatas
  a nunca disparar (ataca o Nível 1). Só lista pra decisão humana; não reescreve nada.
- Convenção: bash `.sh`, igual `instalar-em-novo-projeto.sh`. Idempotente, sem efeitos
  colaterais fora de gravar os 2 arquivos.

### Componente 2 — `INVENTARIO.md` (gerado)

Índice exaustivo das 135 skills por cluster, com contagem coerente e tags de origem.
Passa a ser **saída do script**, não editado à mão. Nada escondido.

### Componente 3 — `workflow` skill (`.claude/skills/workflow/SKILL.md`)

- **Nova linha GSD** na tabela de roteamento (entregável: "Projeto de software
  multi-fase / autônomo").
- **Novo bloco "Clusters de skills utilitárias"** — docs, mídia, dev-infra, meta — pra
  o intake achar docx/pdf/yt-dlp/mcp-builder/skill-creator etc. sem inchar a tabela principal.
- **Regra de desempate GSD ↔ AIOX** (ver abaixo).

### Componente 4 — `CLAUDE.md`

- **Linha GSD** na "Tabela de roteamento — tarefa → recurso".
- **Mini-seção "Roteamento de dev — GSD vs AIOX"** (espelha o padrão da seção SEO existente).
- **Atualiza contagem** no topo: 107 → 135 skills, com nota do gap biblioteca↔global.

### Componente 5 — `ROUTING-MAP.md`

- **Seção GSD:** as 67 skills agrupadas em 8 clusters, com gatilho por cluster +
  sequência do ciclo canônico + nota do track leve `gsd-ns-*`.

### Componente 6 — Resync `biblioteca/` (fecha o buraco de versionamento)

Hoje `biblioteca/skills` tem 107; global tem 135. As **29 faltantes** (todas não-GSD)
estão só no global — fora do repo. **Os 67 GSD já estão versionados** na biblioteca (o
gap de versionamento ≠ gap de roteamento). Sem copiar as 29, o seed via
`instalar-em-novo-projeto.sh` não leva essas skills soltas.

- **Copiar** as ~29 skills de `~/.claude/skills` para `biblioteca/skills/` → repo passa a
  ter todas as **135** (rsync aditivo, sem `--delete`, preserva extras da biblioteca).
- **Excluir lixo pesado** na cópia (mesma política do INVENTARIO): `node_modules`,
  `.venv`, `dist`, `build`, `cache`, `.git`, binários (`.mp4`, `.dll`, `.exe`, `.node`).
- Depois do resync, quase tudo vira `[biblio]` no INVENTARIO; a tag `[global-only]`
  continua útil pra detectar drift futuro.
- **Ordem:** resync ANTES de rodar o gerador, pra o INVENTARIO já refletir 135 versionadas.

### Componente 7 — Hook de enforcement `UserPromptSubmit` (regra "sempre a melhor ferramenta")

Pedido do Thales: *sempre que for criar algo, analisar tudo do projeto e escolher as
melhores ferramentas*. Isso é comportamento automático por-evento → exige **hook** (o
harness executa; memória/CLAUDE.md é mole e "esvanece" em sessão longa), não instrução.

- **Evento:** `UserPromptSubmit`. Injeta `additionalContext` (system-reminder) a cada turno.
- **Mecanismo:** sem `jq`/`node` (não há `jq` no PATH). O comando só faz `echo` de um JSON
  fixo com `hookSpecificOutput.additionalContext`. **Auto-gatilhado**: o texto diz "SE for
  criar entregável, primeiro consulte o roteamento" — a condição fica no texto (avaliada
  pelo modelo), não na lógica shell. Reinjeta todo turno → mantém a Regra de Ouro saliente.
- **Conteúdo injetado (curto, ~60 tokens):** "Antes de criar/produzir qualquer entregável:
  consulte INVENTARIO.md + ROUTING-MAP.md, analise os recursos do projeto
  (skills/squads/agents/MCP) e escolha as MELHORES ferramentas. Não entregue genérico.
  Processo antes do especialista (workflow/briefing/superpowers)."
- **Escopo:** `.claude/settings.json` (projeto, versionado) — vale nesta biblioteca e em
  projetos semeados via `instalar-em-novo-projeto.sh`, onde ROUTING-MAP/INVENTARIO existem.
- **Seed:** garantir que `instalar-em-novo-projeto.sh` leve `.claude/settings.json` (ou o
  bloco de hook) pro projeto destino — senão o hook não segue no seed.
- **Verificação:** pipe-test do comando (`echo '{}' | <cmd>` → JSON válido) + `node`
  de validação de sintaxe do settings + confirmar que o hook carrega (abrir `/hooks` ou
  restart, pois o watcher só observa `.claude/` que já tinha settings no start da sessão).

## Regra de desempate GSD ↔ AIOX

| Use **GSD** quando | Use **AIOX** quando |
|---|---|
| Projeto real multi-fase; quer ciclo disciplinado com artefatos (`.planning/`, PLAN/RESEARCH/VERIFICATION); execução autônoma/checkpointada; commits atômicos | Quer personas de time sob demanda (analyst/architect/dev/qa/devops) pra consultar/decidir, sem o overhead do ciclo de fases |
| Invoca via `/gsd-new-project`, `/gsd-plan-phase`, `/gsd-execute-phase`... (skills `gsd-*`) | Invoca via chief `AIOX:agents:aiox-master` (que roteia os agentes internos) |

> **Correção de fato:** GSD é instalado como **skills** (`gsd-*`), não como command
> namespace `/gsd:` — houve migração command→skill (existe `~/.claude/gsd-migration-journal`).
> Invocação correta: `/gsd-new-project` (hífen), não `/gsd:new-project`.

## Clusters GSD (67 → 8 grupos)

1. **Início/Projeto** — new-project, new-milestone, complete-milestone, milestone-summary
2. **Planejar** — plan-phase, discuss-phase, spec-phase, ultraplan-phase,
   plan-review-convergence, sketch, spike
3. **Executar** — execute-phase, mvp-phase, phase, fast, quick, autonomous
4. **Verificar/QA** — verify-work, validate-phase, code-review, secure-phase, ui-review,
   eval-review, audit-fix, audit-milestone, audit-uat, add-tests
5. **Debug/Forense** — debug, forensics, health
6. **Docs/Contexto** — docs-update, map-codebase, ingest-docs, capture, explore, graphify,
   surface, thread
7. **Manutenção/Estado** — cleanup, resume-work, pause-work, undo, update, config, settings,
   workspace, progress, stats, ship, pr-branch, import, inbox, review-backlog, manager,
   workstreams, extract-learnings, profile-user, help, review
8. **Track leve `ns-*`** — ns-context, ns-ideate, ns-project, ns-review, ns-manage, ns-workflow

## Clusters skills soltas (28)

- **Docs/Office** — docx, pdf, pptx, xlsx, doc-coauthoring, internal-comms
- **Mídia** — video-extract, yt-dlp, slack-gif-creator, curso-ripper
- **Dev-infra** — claude-api, mcp-builder, supabase, supabase-postgres-best-practices,
  webapp-testing, web-artifacts-builder, remotion-best-practices, distinctive-frontend
- **Criativo** — algorithmic-art, canvas-design, theme-factory, criativo-cliente,
  instagram-creative-director (+workspace), brand-guidelines
- **Growth** — ranquear
- **Meta/infra** — skill-creator, template-skill, find-skills

## Fora de escopo (confirmado)

- **Não** altero o conteúdo/comportamento de nenhuma skill — só roteamento, índice,
  o novo script e a cópia dos arquivos pro backup.
- **Não** reescrevo descriptions fracas — só as listo no relatório pra decisão humana.
- **Não** mexo no que já está em `biblioteca/` além de adicionar as 95 faltantes.

## Critérios de sucesso

1. `biblioteca/skills` passa de 107 → **≥135** (as ~29 faltantes não-GSD copiadas, sem lixo pesado).
2. `gerar-inventario.sh` roda e produz INVENTARIO.md coerente (contagem = filesystem real)
   + relatório de descriptions fracas.
3. As 4 fontes de roteamento (workflow, CLAUDE.md, ROUTING-MAP, INVENTARIO) concordam
   entre si e com o global E com a biblioteca.
4. GSD e as 28 skills soltas ficam descobríveis pelo intake, com regra de desempate
   GSD↔AIOX explícita.
5. Rodar o script de novo no futuro reflete instalações/remoções sem edição manual.
6. `instalar-em-novo-projeto.sh` passa a levar todas as 135 (backup completo) + o hook.
7. Hook `UserPromptSubmit` ativo: a cada turno reforça "analise tudo, escolha a melhor
   ferramenta antes de criar"; segue nos projetos semeados.
