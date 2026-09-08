---
name: curso-ripper
description: >-
  Use quando o Thales quer baixar em lote as aulas (vídeo ou áudio) de um curso ou comunidade online protegido por login — enumerar todas as aulas de uma trilha/módulo e baixar de uma vez, não só 1 vídeo avulso. Plataformas já mapeadas: GoHighLevel/ClientClub/LeadConnector, Curseduca/nocodestartup. Players: Panda Video, Vimeo, HLS/m3u8, MP4 direto. Triggers: "baixa esse curso", "ripa essa trilha", "pega todas as aulas", "extrai os vídeos/áudios dessa plataforma", ou quando o yt-dlp sozinho não resolve porque as aulas estão atrás de login e precisam ser enumeradas.
---

# curso-ripper

## Overview

Baixar **todas** as aulas de um curso atrás de login. O truque: quase todo player entrega o vídeo por uma URL capturável na **camada de rede** (HLS aberto ou MP4 público), e a lista de aulas vem de uma **API** que você descobre logando 1 vez. Descobre a fonte + a API → enumera → baixa tudo no terminal.

A descoberta é **semi-manual** (cada plataforma tem auth/API própria); depois que acha a fonte, enumerar e baixar 60+ aulas é automático.

## Ferramenta de rede nesta máquina

Esta máquina tem o **playwright MCP** (o chrome-devtools MCP NÃO está instalado). Playwright lê a camada de rede — headers e corpos de resposta — que é tudo que o método precisa. Mapa das ferramentas usadas abaixo:

| Precisa | playwright (instalado) | chrome-devtools (se instalar depois) |
|---|---|---|
| Abrir página | `browser_navigate` | `navigate_page` |
| Listar requests de rede | `browser_network_requests` (`filter` regex, `static:false`) | `list_network_requests` |
| Ler headers/corpo de 1 request | `browser_network_request` (`part: response-body` \| `request-headers`) | `get_network_request` |
| Sondar API (fetch GET read-only) | `browser_evaluate` | `evaluate_script` |
| Salvar resposta grande em arquivo | `filename` em `browser_network_request`/`browser_network_requests` | `responseFilePath` |
| Ver abas abertas | `browser_tabs` | `list_pages` |

**NÃO usar claude-in-chrome** — trava na montagem do player (Plyr/hls.js). Playwright abre o próprio Chromium; o Thales loga nessa janela.

## O método (6 passos)

1. **Abrir a página com playwright (`browser_navigate`); o Thales faz o login.** Nunca digitar senha (regra fixa — o usuário loga). Não usar claude-in-chrome.
2. **Ler a camada de rede** (não injetar JS na página). Abrir 1 aula, `browser_network_requests` com `filter` pra `xhr`/`fetch`/`media` (`static:false`). Achar duas coisas:
   - a **API de conteúdo** (lista módulos/aulas) — e capturar os **headers de auth** de uma request real com `browser_network_request` (`part: request-headers`).
   - a **fonte do vídeo** (ver tabela abaixo).
3. **Sondar a API** com `browser_evaluate` (fetch **GET**, read-only) reusando os headers, até achar a enumeração completa: trilha → módulos → aulas, com a URL de vídeo de cada aula. Salvar respostas grandes com `filename`.
4. **Montar o manifesto** `manifest.json`: 1 entrada por aula `{source_type, url, dir, filename, extras}`. Roteamento de pastas espelhando o curso + sanitização Windows.
5. **Baixar em lote no terminal** com `batch_download.py` (sem browser — a CDN costuma ser pública).
6. **Verificar**: nº de arquivos == manifesto; `ffprobe` amostral (resolução/duração); sem órfãos (`.temp.mp4`) nem duplicatas.

## Duas decisões (onde se erra)

- **Ferramenta:** sempre a que lê **corpos de resposta na rede** (playwright aqui). O claude-in-chrome trava montando o player — não usar.
- **Áudio ou vídeo?** Conteúdo falado (office hours, calls, podcast) → **áudio** `.m4a` (leve). Tutorial de tela (código, dashboard) → **vídeo** `.mp4` 1080p — só áudio perde o essencial. Na dúvida, perguntar ao Thales.
- **Quer o TEXTO das aulas?** Cheque legenda primeiro (`yt-dlp --list-subs`): se a plataforma servir `.vtt`, é de graça. **Panda não serve** → ASR local. Com GPU, `faster-whisper large-v3-turbo` + `BatchedInferencePipeline(batch_size=16)` = **165x realtime** (458 h viram ~3-5 h com download em paralelo). Receita completa + armadilha das DLLs CUDA: `platforms.md`.

## Fonte de vídeo → receita

| Fonte | Como identificar na rede | Como baixar | Status |
|---|---|---|---|
| **Panda Video** | `*.tv.pandavideo.com.br/.../playlist.m3u8` | `yt-dlp --add-header "Referer:https://player-<lib>.tv.pandavideo.com.br/"` (HLS aberto, segmentos sem token) | ✅ testado |
| **MP4 direto** (Google Storage etc.) | URL `.mp4` pública; `curl -r 0-1` → 206 | `ffmpeg -i <url> -c copy out.mp4`, ou áudio `-vn -c:a copy` | ✅ testado |
| **Greenn Club** (api.greenn.club) | `source` embed Panda no `/watch` | Panda HLS 1080p + `.vtt` pt-BR de graça | ✅ testado |
| **HLS genérico** `.m3u8` | `application/vnd.apple.mpegurl` | `yt-dlp <m3u8>`; pode pedir `Referer`/`Origin`/cookies | ~ padrão |
| **Vimeo privado** | iframe `player.vimeo.com` | `yt-dlp --referer <página> <url>` | ~ padrão |
| **YouTube** priv/unlisted | iframe `youtube.com/embed` | → skill **`pica`** | ~ padrão |

Auth + endpoints de enumeração de cada plataforma: ver **`platforms.md`**.

## Gotchas

| Sintoma | Fix |
|---|---|
| Vídeo baixou vazio / `downloaded file is empty` em caminho fundo | **MAX_PATH 260 do Windows**: os fragmentos `.mp4.part-FragN.part` do yt-dlp estouram. `-P temp:` **não basta** em caminhos de 4 níveis (trilha/módulo/seção/aula) → **baixar num path CURTO e mover o `.mp4` final** pro destino (o `batch_download.py` já faz isso) + truncar nomes longos |
| API 401/403 com `Authorization: Bearer` | Auth **varia por plataforma** — ler o header exato de uma request real (`token-id`+`source`, ou `Bearer`+`api_key`+`x-tenant-id`). Não chutar |
| Mesma aula 2× | Dedup por **id do vídeo** (cts/uuid), não por título. Duração igual ≠ dupe (reunião de 1h colide por acaso) |
| Download 403 no terminal mas 200 no browser | Faltou header `Referer`/`Origin` do player, ou cookies |
| `.temp.mp4` sobrando | Órfão de merge do yt-dlp morto no meio → limpar na verificação |
| `browser_evaluate` "Execution context destroyed" | A página navegou → reconferir `browser_tabs` e repetir |
| Token expira (~1h a 30d) | Só afeta enumeração; os vídeos (CDN público) baixam sem token. Re-capturar via playwright |

## Aprendeu a rippar de um lugar novo? (autoalimentação)

**Se a plataforma OU a fonte de vídeo ainda não estava documentada aqui, registre ANTES de encerrar** — é isto que faz a skill crescer e ficar mais rápida a cada curso:

1. Anexe um playbook em **`platforms.md`** usando o template no topo daquele arquivo (**Auth · Enumeração · Fonte de vídeo · Download · Armadilhas**).
2. Adicione 1 linha na tabela **"fonte de vídeo → receita"** acima (marque `✅ testado`).

No campo **Armadilhas**, registre a **receita vencedora _e_ as 1-2 tentativas que custaram tempo** (ex: "`Authorization: Bearer` deu 401 → o certo era `token-id`"). Assim o próximo Claude não paga o mesmo pedágio.
