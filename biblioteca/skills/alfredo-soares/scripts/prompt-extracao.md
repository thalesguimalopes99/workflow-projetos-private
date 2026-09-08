# Prompt de extração por vídeo — Alfredo Soares

Você recebe transcrições (`raw/long/<id>.txt`) com marcadores `[mm:ss]` a cada ~30s e `¶` onde o ASR do YouTube detectou troca de falante. Sua tarefa: extrair, por vídeo, uma ficha estruturada em `references/videos/<id>.md`, fiel ao que ALFREDO SOARES disse — não ao convidado.

## Regras que não podem quebrar

1. **Rastreabilidade.** Toda tese, framework, história, número e frase literal carrega o marcador `[mm:ss]` do bloco onde aparece. Sem marcador = não entra. Isso é o que permite à skill dizer "ele fala disso no vídeo X aos 12:40" em vez de inventar.
2. **Alfredo ≠ convidado.** Muitos vídeos são entrevistas (Thiago Nigro, empresários do G4, clientes). Use `¶`, contexto e estilo pra atribuir falas. Se não der pra atribuir com confiança, marque `(provável convidado)` e NÃO use na seção Voz. Voz contaminada pelo convidado destrói o teste cego.
3. **Literal é literal.** Na seção Voz, copie a frase como está (corrija só erro óbvio de ASR: "primo rico" ok, "Thiago Negro" → "Thiago Nigro", "g4"/"G quatro" → "G4"). Não parafraseie, não embeleze, não censure gíria/palavrão (`[ __ ]` = palavrão censurado pelo YouTube — mantenha o marcador).
4. **Zero invenção.** Se o vídeo não tem framework nomeado, a seção fica "—". Ficha curta e verdadeira > ficha longa e inflada.
5. **Nomes/termos ASR.** Normalize: G4, Xtech, VTEX, Loja Integrada, Bora Vender, Bora Varejo, Todos Somos uma Marca, Tallis Gomes, Bruno Nardon, Thiago Nigro.

## Formato exato da ficha (`references/videos/<id>.md`)

```markdown
# <título do vídeo>
video_id: <id> · url: https://youtu.be/<id> · data: <AAAA-MM-DD> · duração: <h:mm:ss> · views: <n>
formato: <solo | entrevista com <nome/papel> | consultoria ao vivo | evento/palestra>
tema: <1 linha — sobre o que é, na visão dele>

## Resumo
<5-8 linhas. O argumento central do vídeo como Alfredo o constrói. Sem lista.>

## Teses
- **<tese em 1 frase, na voz dele>** — <explicação 1-2 linhas>. [mm:ss] "<citação literal curta>"
- ...

## Frameworks / métodos
- **<nome que ele dá, ou nome descritivo entre aspas se ele não nomeia>** — passos: 1) ... 2) ... 3) ... [mm:ss]
- ...  (ou "—")

## Histórias / casos
- **<quem/onde>** — <o que aconteceu em 2 linhas> → lição: <1 linha>. [mm:ss]
- ...

## Números / claims
- <claim com número> [mm:ss]  (faturamento, %, prazos, tamanhos — como ELE diz, mesmo que redondo)

## Posições
- **Defende:** <o que ele afirma com convicção> [mm:ss]
- **Ataca / discorda:** <o que ele critica, de quem, por quê> [mm:ss]
- **Nuance:** <onde ele diz "depende" e do quê> [mm:ss]

## Voz (só falas do Alfredo, literais)
- [mm:ss] "<frase>"
- ... (10-20 frases: bordões, aberturas, provocações, gírias, jeito de dar ordem, jeito de elogiar, jeito de discordar)

## Cacoetes observados
<3-6 linhas: tics verbais ("ó", "cara", "mano", "tá bom?"), ritmo (frase curta vs longa), como abre e fecha, uso de pergunta retórica, imperativo, humor, palavrão, autorreferência (Xtech/G4/livros).>

## Perguntas que ele faria
<3-5 perguntas que Alfredo faria a um empresário que trouxesse o problema deste vídeo — inferidas do jeito que ele diagnostica no vídeo. Marque como (inferido).>

## Conexões
<temas/vídeos relacionados se você tiver processado outros do lote; senão "—">
```

## Depois de todas as fichas do lote

Devolva ao orquestrador (na sua resposta final, NÃO em arquivo) um resumo de 10-15 linhas: quais ids processou, 5 teses mais fortes do lote com ids, bordões que se repetiram entre vídeos, e qualquer vídeo onde a atribuição Alfredo/convidado ficou difícil.
