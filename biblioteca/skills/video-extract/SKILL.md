---
name: video-extract
description: >-
  Extrai TODO o conteúdo de um vídeo — a fala (transcrição) E o que aparece na tela
  (análise visual dos frames) — usando uma stack 100% gratuita e local (yt-dlp +
  faster-whisper + ffmpeg + leitura multimodal), SEM depender de Higgsfield, OpenAI
  ou qualquer API paga. Entrega um resumo estruturado em PT-BR + transcrição com
  timestamps, e então conecta o conteúdo às skills de produção (criar-site-premium,
  copywriting, instagram-creative-director, traffic-masters) pra virar template,
  briefing ou copy reusável. Use SEMPRE que o usuário mandar um link de vídeo
  (YouTube, Instagram, TikTok, Vimeo, etc.) ou um arquivo de vídeo local e quiser
  "entender o que é dito", "pegar a transcrição", "extrair o conteúdo", "resumir o
  vídeo", "saber o que tem nesse vídeo", "minerar essa referência", "transcrever",
  "o que esse vídeo ensina", ou reaproveitar o conteúdo de um vídeo pra outro
  entregável — mesmo que não diga "skill" ou "transcrição" explicitamente. Trigger
  também em inglês: "transcribe this video", "what does this video say", "extract
  video content", "summarize this youtube video", "get the transcript". NÃO é a skill
  de EDIÇÃO/corte de vídeo (essa é a video-use) — esta aqui é pra ENTENDER e REUSAR
  o conteúdo, não pra montar um corte.
---

# Video Extract — minerar o conteúdo de qualquer vídeo (grátis, local)

## Princípio

Um vídeo carrega dois canais de informação: **o que é DITO** (áudio/fala) e **o que
APARECE** (imagem na tela). Pra realmente entender e reusar o conteúdo você precisa
dos dois. Esta skill puxa os dois de graça, sem nenhuma API paga:

- **Fala** → áudio baixado com `yt-dlp`, transcrito **localmente** com `faster-whisper`.
- **Visual** → frames extraídos com `ffmpeg`, **lidos por você mesmo** (você é multimodal,
  então descrever a cena/texto/UI de um frame é grátis e tão bom quanto qualquer
  "video analysis" pago).

Nada de Higgsfield, nada de chave de API, nada sai da máquina. O único custo é tempo
de CPU na transcrição.

**Por que não usar a legenda automática do YouTube?** Porque ela é instável: sem um JS
runtime instalado, o endpoint de legenda do YT devolve `HTTP 429 Too Many Requests` e o
client `tv` cai em vídeos com DRM. O **áudio**, porém, baixa tranquilo pelo client padrão.
Então a regra é: **não depende de legenda — baixa o áudio e transcreve local.** É o
caminho que sempre funciona.

## Quando usar / quando não usar

- **USE** pra: entender, transcrever, resumir, ou reusar o conteúdo de um vídeo (link ou
  arquivo). Minerar uma referência de tutorial/aula/concorrente pra extrair o método.
- **NÃO use** pra cortar/editar/legendar um vídeo de entrega — isso é a **video-use**.
  Se a pessoa quer um *corte montado*, use video-use. Se quer *saber o que tem dentro*,
  é aqui.

## Setup (checar uma vez, não reinstalar)

Ferramentas necessárias (todas já costumam estar no PATH desta máquina):

- `ffmpeg` + `ffprobe` — extração de áudio e frames.
- `uv` / `uvx` — roda `yt-dlp` e o `faster-whisper` sem instalar nada global.
- Python disponível via `uv` (a transcrição roda em 3.12 pra ter wheels do ctranslate2).

Cheque rápido (não rode se já confirmou nesta sessão):

```bash
command -v ffmpeg && command -v ffprobe && command -v uv
```

Primeira transcrição baixa o modelo Whisper (`small` ≈ 460 MB, cacheado em
`~/.cache/huggingface`). Depois é instantâneo.

## Workspace

Tudo de uma sessão vai pra uma pasta de trabalho, fora de qualquer pasta de skill.
Padrão: `C:\Users\<user>\video-work\` (ou uma subpasta por vídeo se forem vários).
Layout:

```
video-work/
├── audio.webm / audio.wav      ← áudio baixado + wav 16k mono pro whisper
├── video.mp4                   ← vídeo low-res só pros frames
├── frames/f_###.jpg            ← 1 frame a cada N segundos
├── transcript.txt              ← saída do faster-whisper (com timestamps)
├── <vid>.info.json             ← metadata (título, duração, canal)
└── RESUMO.md                   ← ENTREGÁVEL: resumo estruturado em PT-BR
```

## Processo

### 1. Intake — entender o pedido antes de baixar

Pergunte (curto) duas coisas se não estiverem claras:
- **Fonte**: link (qual plataforma?) ou arquivo local (caminho)?
- **Objetivo**: só entender? resumir? ou **virar o quê** (site, copy, post, briefing)?
  Isso decide a fase de Reuso lá no fim — já pergunte agora.

### 2. Download (yt-dlp via uvx)

Primeiro a metadata, pra saber a duração (decide modelo do whisper e intervalo de frame):

```bash
cd "<workspace>" && uvx --with curl_cffi yt-dlp --skip-download --no-warnings \
  --print "%(title)s :: %(duration)s sec :: %(uploader)s" "<URL>"
```

Baixa **áudio** (o que sempre funciona — client padrão, sem DRM) e a metadata:

```bash
uvx --with curl_cffi yt-dlp -f bestaudio --impersonate chrome \
  --write-info-json -o "audio.%(ext)s" "<URL>"
```

Baixa um **vídeo low-res** só pros frames (720p é legível pra texto na tela; 360p se for
só pra ver a cena). Só o stream de vídeo, áudio você já tem:

```bash
uvx --with curl_cffi yt-dlp -f "bv*[height<=720]" --impersonate chrome \
  -o "video.%(ext)s" "<URL>"
```

**Arquivo local?** Pula o yt-dlp inteiro. Use o arquivo direto como `video.mp4` e extraia o
áudio dele (passo 3).

**Gotchas (aprendidos na prática):**
- Sempre `--with curl_cffi --impersonate chrome` → passa por throttling/anti-bot.
- **Não** force `--extractor-args player_client=tv` → DRM. O client padrão (android vr)
  serve áudio e vídeo de boa.
- Se um download der 429, espere e re-tente; raramente é permanente pro áudio/vídeo
  (só pra legenda, que a gente nem usa).

### 3. Transcrição (faster-whisper local — `scripts/transcribe.py`)

Converta o áudio pra wav 16k mono (whisper gosta, e ffmpeg lê webm/m4a sem dor):

```bash
ffmpeg -y -i audio.webm -ar 16000 -ac 1 -c:a pcm_s16le audio.wav
```

(Arquivo local: `ffmpeg -y -i video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le audio.wav`.)

Rode a transcrição. **Modelo por necessidade:**
- `small` — padrão, rápido, ótimo pra captar a ideia. Comece por ele.
- `medium` / `large-v3` — quando a redação exata importa (nomes, números, idioma não-inglês).

```bash
uv run --python 3.12 --with faster-whisper python \
  "<skill-dir>/scripts/transcribe.py" audio.wav --model small --out transcript.txt
```

Deixe `--lang` de fora pra auto-detectar (ele imprime o idioma + confiança no stderr).

**Vídeo longo (> ~6 min) ou modelo grande?** Rode em **background** e leia o
`transcript.txt` crescendo — não bloqueie. (No harness: `run_in_background: true`, depois
`Read` no arquivo de saída.) Você é notificado quando termina.

**Cache:** nunca re-transcreva o mesmo áudio. Se `transcript.txt` já existe pra essa fonte,
reuse.

### 4. Análise visual (ffmpeg frames → você lê)

Extraia frames. Intervalo conforme o tipo de vídeo:
- Tutorial / aula / talking-head → 1 frame a cada **15–20s** (telas mudam devagar).
- Conteúdo visual rápido / clipe / montagem → cada **5–10s**.

Escala 1280 de largura mantém texto/UI legível:

```bash
mkdir -p frames && ffmpeg -y -i video.mp4 -vf "fps=1/20,scale=1280:-1" -q:v 3 frames/f_%03d.jpg
```

**Leia os frames em lotes** (várias imagens por mensagem, via `Read`). Pra cada frame
relevante anote: cena, texto na tela, UI/produto, e qualquer coisa reusável (paleta,
fonte, layout, número, prompt). **Pule frames repetidos** — slides estáticos aparecem em
vários frames seguidos; descreva uma vez. Cruze com o `transcript.txt` pelos timestamps
(frame_N ≈ N × intervalo em segundos) pra casar "o que ela falava" com "o que estava na
tela".

### 5. Síntese → `RESUMO.md` (o entregável)

Escreva um markdown estruturado **em PT-BR** (mesmo que o vídeo seja em outro idioma —
traduza; mantenha citações-chave no original quando o fraseado importar). Template:

```markdown
# Resumo — "<título>"

**Fonte:** <URL ou caminho>
**Canal/Autor:** <…> · <duração> · idioma: <detectado>

## Tese central
<1 parágrafo: a ideia/promessa do vídeo>

## O que é DITO (transcrição destilada)
<bullets dos pontos faladoss, em ordem; cite trechos fortes verbatim>

## O que TEM na tela (visual)
<o que aparece: telas, produtos, código, UI, paletas, fontes, números>

## Ouro reusável
<os ativos concretos: prompts, frameworks, táticas, hex, nomes — o que dá pra REUSAR>

## Resultado / conclusão
```

Salve `transcript.txt` (já está) e `RESUMO.md` lado a lado. Esses dois são a entrega.

### 6. Reuso — conectar à produção

Aqui o conteúdo vira ação. Olhe o tema do vídeo e **encaminhe pra skill certa**, levando
o "Ouro reusável" como insumo:

| Tema do vídeo | Skill pra onde levar |
|---|---|
| Site / landing / web design | `criar-site-premium` · `site-teardown` (se for minerar referência) |
| Copy / oferta / VSL / headline | `copywriting` · `copy-master` |
| Anúncio pago / tráfego | `traffic-masters` |
| Post / carrossel / reel | `instagram-creative-director` · `criativo-cliente` |
| Marca / identidade | `brand` · `brand-squad` |
| Pedido vago "quero fazer algo com isso" | `briefing` pra estruturar, depois rotear |

Antes de rotear, pergunte ao usuário **em que formato ele quer o reuso** (template
parametrizado? briefing? copy pronta?) e então **invoque a skill de produção** passando o
material extraído. Se ele só queria entender, pare no RESUMO.md.

## Regras firmes (onde desviar quebra silenciosamente)

1. **Não dependa de legenda** — baixe áudio e transcreva local. Legenda do YT é instável (429).
2. **Áudio pelo client padrão** (`-f bestaudio --impersonate chrome`). Nunca `player_client=tv` (DRM).
3. **wav 16k mono** antes do whisper.
4. **Transcrição longa = background**, depois lê o arquivo. Nunca trave a sessão esperando.
5. **Cache** — não re-baixa nem re-transcreve a mesma fonte.
6. **Leia frames em lotes e pule repetidos** — não gaste leitura em slide estático repetido.
7. **Entrega em PT-BR**, traduzindo o que for preciso, mas preservando citações onde o
   fraseado original tem valor.
8. **Workspace fora das pastas de skill** — escreva em `video-work/`, nunca dentro de
   `.claude/skills/`.

## Recursos

- `scripts/transcribe.py` — wrapper do faster-whisper (offline). Args: `INPUT --model
  --lang --out`. Veja o docstring no topo do arquivo.
