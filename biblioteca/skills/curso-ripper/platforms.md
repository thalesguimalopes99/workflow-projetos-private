# Playbooks por plataforma — curso-ripper

Detalhe de **auth + enumeração + fonte de vídeo** de cada plataforma já rippada. Consumido pelo método em `SKILL.md`. Cresce com o tempo (ver "autoalimentação" no SKILL.md).

## Template (copie ao registrar um caso novo)

```markdown
## <Plataforma> / <front-end/marca> (visto em: <curso>)

- **Auth:** <headers exatos que funcionaram na API de conteúdo>
- **Enumeração:** <endpoints em ordem: trilha → módulos → aulas; o que cada um devolve>
- **Fonte de vídeo:** <Panda/Vimeo/MP4/HLS> — <como a URL aparece / como construir>
- **Download:** <comando exato que funcionou>
- **Armadilhas:** <receita vencedora + as 1-2 tentativas que custaram tempo e o fix>
```

Regra de ouro da descoberta: **leia o header/URL de uma request real** na camada de rede (playwright `browser_network_request`, `part: request-headers`) em vez de adivinhar. Toda plataforma abaixo foi decifrada assim. (Mapa playwright ↔ chrome-devtools no SKILL.md.)

---

## GoHighLevel / ClientClub / LeadConnector (visto em: High Ticket Clube)

Front "comunidade" (Vue SPA) sobre o backend GoHighLevel. Cursos = *memberships*; canais = *communities*.

- **Auth:** `token-id: <firebase-JWT>` + `source: PORTAL_USER` + `channel: APP` + `version: 2021-07-28`. **Não** é `Authorization: Bearer`. Origin/referer da comunidade.
- **Enumeração:**
  - Cursos: `GET services.leadconnectorhq.com/membership/locations/{CID}/user-purchase/categories?product_id={pid}&source=communities` → `categories[]` (módulos) → `posts[]` (aulas) → `video.transcoderWorkerVideoId` = `cts-id`.
  - Canais: `GET services.leadconnectorhq.com/communities/{CID}/groups/{GID}/channels/{channelId}/posts?limit=20` (paginado) → posts `postType: GO_LIVE` com `metadata.licenseId`.
  - Resolver licença (público, **sem token**): `GET backend.leadconnectorhq.com/assets-drm/assets-license/{licenseId}` → `url` (MP4) + `meta.durationInSeconds`.
- **Fonte de vídeo:** **MP4 público** no Google Storage — `https://storage.googleapis.com/revex-{membership|communities}-production/{memberships|communities}/{CID}/videos/cts-{id}_{360p|720p|1080p}.mp4`. Sem token.
- **Download:** áudio → `ffmpeg -hide_banner -loglevel error -y -i <mp4> -vn -c:a copy out.m4a` (fallback `-c:a aac -b:a 128k`). Vídeo → `curl -o` ou `ffmpeg -i <mp4> -c copy out.mp4`.
- **Armadilhas:**
  1. `Authorization: Bearer` → **401**. O certo é `token-id` + `source: PORTAL_USER` (visto nos request headers reais na camada de rede).
  2. Hook de `fetch` na página **não pega** o token (o app cacheia a ref de `fetch` no load e não usa XHR) → capturar auth dos headers de uma request real, não injetando JS.
  3. claude-in-chrome **trava** na montagem do player Plyr/hls.js → usar playwright (lê a camada de rede sem depender do player montar).
  4. Dedup por **`cts`**. O mesmo vídeo em curso + canal pode ter `cts` diferente; e duração igual entre office hours de ~1h é **coincidência**, não dupe.
  5. Conteúdo é **tier-gated**: a API só devolve o que o plano do usuário libera (cursos vazios = sem acesso, não é bug).

## Curseduca / nocodestartup "flix" (visto em: Trilha Supabase Completo)

Front "flix" (Next.js) sobre a plataforma Curseduca; vídeos no Panda Video.

- **Auth:** `authorization: Bearer <JWT>` + `api_key: <chave>` + `x-tenant-id: <n>` + `x-platform: web`. Origin/referer do front flix. JWT dura ~30 dias.
- **Enumeração:**
  - `GET clas.curseduca.pro/tracks/{trackId}` → `contents[]` = módulos (cada um com `id`).
  - `GET clas.curseduca.pro/contents/{moduleId}/modules` → `modules[]` (seções) → `lessons[]` **já com `videoId`/`filePath` = URL m3u8**, `ord`, `title`, `lessonComplementary[]` (.pptx).
  - `type: 11` = vídeo Panda; `type: 8` = formulário Tally (ignorar). Alt: `GET /lessons/{classId}` devolve 1 aula com m3u8 + `nextLesson`/`prevLesson`.
- **Fonte de vídeo:** **Panda Video HLS aberto** — `https://b-vz-{lib}.tv.pandavideo.com.br/{uuid}/playlist.m3u8`. Materiais complementares públicos em `files.curseduca.com/...`.
- **Download:** `yt-dlp --add-header "Referer:https://player-vz-{lib}.tv.pandavideo.com.br/" -f "b[height<=1080]/bv*+ba/b" --merge-output-format mp4 -P "temp:C:\...\sbt" -o "<dir>/<fn>.%(ext)s" <m3u8>`. `.pptx` via `urllib`/`curl` na URL direta.
- **Armadilhas:**
  1. **MAX_PATH 260**: os fragmentos `.mp4.part-FragN.part` estouram em caminho fundo. Em curso raso (`Módulo/Seção/aula`) basta `-P temp:<dir curto>` + encurtar nome de módulo. Mas em **4 níveis** (trilha/módulo/seção/aula — trilhas "Geral" tipo Bubble/Cursor/N8N) o `-P temp:` **NÃO protege os fragmentos** → **baixar cada vídeo num path curto e mover o `.mp4` final** pro destino. Também truncar o nome da aula pra caber. *(Aprendido baixando as 14 trilhas da NoCodeStartup: 8/626 falharam só por isso.)*
  2. `.temp.mp4` órfão fica se o processo é morto no meio do merge → limpar na verificação (contar mp4 vs manifesto).
  3. Só precisa do header `Referer` do player; os segmentos `.ts` vêm da CDN **sem token**.
