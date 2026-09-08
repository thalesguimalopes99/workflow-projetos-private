---
name: pica
description: >-
  Use quando o Thales quer baixar coisas do YouTube ou de outro site de vídeo — vídeo, áudio, legenda/transcrição salva em texto (.txt), título/metadata, playlist. Roda em cima do yt-dlp. Triggers válidos: invocação explícita `/pica` (nome antigo: `/yt-dlp`); ou linguagem natural tipo "baixa esse vídeo", "pega a transcrição/legenda desse vídeo", "salva o áudio", "extrai o texto desse vídeo". Também é o fallback quando o NotebookLM falha ao processar fonte do YouTube (a skill notebooklm referencia esta).
---

# pica — download de vídeo/áudio/legenda (yt-dlp)

## Invocação nesta máquina

Sem `yt-dlp.exe` no PATH e sem deno — usar **módulo Python + runtime node** (Node v24 instalado). O `--remote-components ejs:github` baixa o solver de JS challenge do YouTube (sem ele, formatos somem e aparece warning "n challenge solving failed"):

```powershell
$env:PYTHONIOENCODING='utf-8'; py -m yt_dlp --js-runtimes node --remote-components ejs:github <args>
```

Todos os exemplos abaixo assumem esse prefixo (abreviado como `ytdlp`).

**ffmpeg ESTÁ instalado** nesta máquina (v8.1, no PATH) — o yt-dlp acha sozinho. Merge de 1080p+, extração pra mp3, `--convert-subs`, `--download-sections` e `--embed-*` todos funcionam aqui.

## Receitas (todas verificadas nesta máquina)

### Transcrição em texto — .txt com o título do vídeo no nome

Duas etapas: baixar legenda .vtt nomeada pelo título, converter pra texto limpo (sem timestamps, sem duplicatas do ASR):

```powershell
# vídeo em português; se for em inglês usar --sub-langs "en,en-orig"
ytdlp --skip-download --write-subs --write-auto-subs --sub-langs "pt,pt-orig" --sub-format vtt --sleep-subtitles 2 -o "%(title)s.%(ext)s" <URL>
Get-ChildItem *.vtt        # nome real sai sanitizado (`?`→`？`, `|`→`｜`) — pegar o caminho daqui
py C:\Users\"Thales Lopes"\.claude\skills\pica\vtt2txt.py "<caminho-do-vtt>"
```

- `--write-subs` pega legenda manual; `--write-auto-subs` a automática (`pt-orig`/`en-orig` = trilha ASR original). Vem o que existir; se vierem as duas, **converter a manual (sem `-orig`)** — a ASR é mais suja.
- **Pedir só as línguas prováveis do vídeo, exatas, nunca wildcard** — `pt.*` puxa dezenas de traduções automáticas, e cada request de legenda conta pro rate limit do YouTube (HTTP 429). O `--sleep-subtitles 2` espaça os requests.
- **No primeiro 429 o yt-dlp ABORTA as línguas restantes** (exit 1, mesmo com arquivos já gravados). Conferir `Get-ChildItem *.vtt` antes de retentar — e retentar só com a língua que faltou, ou esperar uns minutos.
- O vtt2txt.py imprime o caminho do .txt gerado. Conversão não precisa de ffmpeg.

### Título / metadata (sem baixar nada)

```powershell
ytdlp --print "%(title)s" --skip-download <URL>
ytdlp -J <URL>                # JSON completo (duration, uploader, chapters...)
ytdlp --list-subs <URL>       # quais legendas existem
```

### Áudio

```powershell
# m4a puro, sem re-encode (mais rápido, mantém qualidade original):
ytdlp -f "ba[ext=m4a]/b" -o "%(title)s.%(ext)s" <URL>

# mp3 (re-encode via ffmpeg — usar só se precisar de mp3 mesmo):
ytdlp -x --audio-format mp3 --audio-quality 0 -o "%(title)s.%(ext)s" <URL>
```

### Vídeo

```powershell
# progressivo (rápido, 1 arquivo, tipicamente ≤720p, sem merge):
ytdlp -f "b[ext=mp4]/b" -o "%(title)s.%(ext)s" <URL>

# melhor qualidade (1080p+ — junta vídeo+áudio com ffmpeg):
ytdlp -f "bv*+ba/b" --merge-output-format mp4 -o "%(title)s.%(ext)s" <URL>
```

`b[ext=mp4]` = formato progressivo (vídeo+áudio num arquivo só). `bv*+ba` = melhor vídeo + melhor áudio separados, merge automático com ffmpeg (necessário pra 1080p+).

### Playlist

```powershell
ytdlp -o "%(playlist_index)02d - %(title)s.%(ext)s" <URL-da-playlist>
# só alguns itens: --playlist-items 1-5
```

### Recortar trecho (ffmpeg disponível)

```powershell
ytdlp --download-sections "*00:01:30-00:04:00" -f "b[ext=mp4]/b" -o "%(title)s.%(ext)s" <URL>
```

## Erros comuns

| Sintoma | Causa → Fix |
|---|---|
| `yt-dlp não é reconhecido` | exe fora do PATH → sempre `py -m yt_dlp` |
| HTTP 429 baixando legendas | rate limit do YouTube (acontece até com línguas exatas, e aborta as línguas restantes) → conferir o que já baixou, retentar só o que falta com `--sleep-subtitles 2`, ou esperar uns minutos |
| "n challenge solving failed" / formato faltando | faltou `--js-runtimes node --remote-components ejs:github` |
| `UnicodeEncodeError` / `�` no output | faltou `$env:PYTHONIOENCODING='utf-8'` |
| `？ ｜` no nome do arquivo | sanitização Windows normal; `--restrict-filenames` se precisar ASCII puro |
| Exit code ≠ 0 mas arquivos baixados | falha parcial (ex: 1 idioma de legenda deu 429) — conferir `Get-ChildItem` antes de retentar |
| `ffmpeg not found` (não deve acontecer aqui) | ffmpeg está no PATH; se sumir: `winget install ffmpeg` e reabrir o shell |

## Manutenção

YouTube quebra extractors velhos — se aparecer erro de extração novo: `py -m pip install -U yt-dlp`. Flags raros: `py -m yt_dlp --help`.
