# Runbook — atualizar a base do zero ao fim

Siga na ordem. Cada passo depende do anterior. Rode do diretório `scripts/` da skill.

## 1. Checar
```
python check_new.py
```
Leia `novos=N`. Se `N=0`, pare aqui — nada a fazer.

## 2. Baixar + converter
```
python update.py            # aba /videos
python update.py --shorts   # se também quiser varrer shorts (raro precisar)
```
Baixa legenda só dos ids novos, converte pra `.txt` com timestamps. Já pode já estar feito
pela tarefa agendada `AlfredoSoaresCaptions` (roda semanal, ver SKILL.md § Auto-atualização) —
rodar de novo é seguro e barato (não rebaixa o que já tem).

## 3. Destilar
```
python update.py --status
```
Lista os `.txt` sem ficha em `references/videos/`. Para cada lote de até 6 vídeos novos,
dispare 1 subagent em paralelo com `scripts/prompt-extracao.md` como instrução, apontando
pros `.txt` do lote. Cada subagent escreve `references/videos/<id>.md` (nunca edita os
arquivos de síntese diretamente).

## 4. Reindexar
```
python build_index.py
```
Regenera `references/indice-videos.md` do zero — seguro, é só tabela derivada das fichas.

## 5. Mesclar nas sínteses
```
python extract_sections.py <dir_temp>
```
Gera um `.md` por seção (`teses.md`, `frameworks-metodos.md` etc.) só com as fichas atuais,
num diretório temporário — **não** aponta pra `references/`. Compare cada arquivo gerado com
o equivalente em `references/*.md` e **mescle a mão** (ou via subagent) o que é novo: adicione
tese/framework/história/posição/diagnóstico/frase de voz que ainda não está lá, mantendo a
curadoria e organização existentes. Apague o `<dir_temp>` no final.

## 6. Atualizar a contagem
Edite a `description` do frontmatter de `SKILL.md`: número de vídeos long-form e de shorts.

## O que NÃO fazer
- **Não reescrever um arquivo de síntese inteiro** a partir do `extract_sections.py` — ele não
  tem a curadoria (agrupamento, priorização, remoção de redundância) que já existe nos arquivos
  de `references/`; sobrescrever perde isso.
- **Não deixar dado bruto entrar na skill.** `raw/*.txt`, `.vtt`, `.info.json` ficam fora
  (`~/Documents/wtf/mentor-alfredo-soares/raw/`), nunca copiados pra dentro de `references/`.
- **Não citar tese/framework/história/número sem `[<id> @ mm:ss]`.** Sem marcador, não entra
  na base — nem na ficha do vídeo, nem nos arquivos de síntese mesclados.
