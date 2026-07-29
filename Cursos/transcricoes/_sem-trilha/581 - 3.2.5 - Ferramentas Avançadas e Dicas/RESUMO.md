# 3.2.5 - Ferramentas Avançadas e Dicas

(sem trilha) | 4 aulas | ~31 min (00:31:26) | nível intermediário

> Módulo de fechamento da trilha avançada de OpenClaw: revisa os comandos de barra do dia a dia, ensina a ligar entrada e saída de voz (áudio no Telegram) e consolida o 80/20 de operação — custo, roteamento de modelo, segurança e os 10 erros mais comuns.

## O que você sai sabendo fazer

- Usar os comandos de barra do OpenClaw no Telegram para gerenciar sessão, modelo, contexto, custo, skills e plugins sem abrir o dashboard.
- Mandar arquivos (planilha, PDF, imagem) para o agente analisar e pedir o caminho inverso: ele gera um `.md` na VPS e devolve o arquivo pelo Telegram.
- Configurar entrada de voz (transcrição via Groq Whisper large-v3-turbo) e saída de voz (Microsoft Edge TTS) no `openclaw.json`, usando um prompt que faz a configuração e reinicia o gateway.
- Escolher modelo por tarefa (barato para conversa/monitoramento, caro só para código e raciocínio pesado) e enxugar custo de crons e heartbeats.
- Auditar riscos de segurança do setup: chave de API no chat, agente aberto a qualquer pessoa, dashboard exposto sem Tailscale, agente rodando no computador pessoal.
- Evoluir a personalidade do agente editando `soul.md`, `user.md`, `agents.md` e `lessons.md` de tempos em tempos.

## Stack e ferramentas

- **OpenClaw** (agente rodando em VPS) + **Telegram** como canal principal.
- **Groq** (groq.com) — chave de API para transcrição com **Whisper large-v3-turbo** (gratuito/barato).
- Alternativas de transcrição citadas: **OpenAI gpt-4o-mini-transcribe**, **Deepgram**, **Mistral**, **Whisper local** rodando na própria VPS.
- **Microsoft Edge TTS** para saída de voz (gratuito e nativo no OpenClaw), vozes pt-BR **AntonioNeural** e **FranciscaNeural**. Alternativas de TTS: **OpenAI**, **ElevenLabs**, **MiniMax**.
- **Talk mode / voz ao vivo** (nível avançado, não configurado na aula): modelos realtime da **OpenAI** e **Google Gemini Live** conectados a sala de voz do **Discord** (ou Slack).
- Modelos citados no roteamento: **GPT 5.4 mini** (padrão do dia a dia, via assinatura Codex), **GPT 5.5** (código e planejamento), **DeepSeek** (crédito pré-pago, janela de contexto grande) e outros modelos chineses baratos.
- **Tailscale** para acesso protegido ao dashboard. **Notion** usado pelo instrutor só como repositório dos prompts prontos.
- Arquivos de memória/personalidade: `soul.md`, `user.md`, `agents.md`, `lessons.md`.

## Pré-requisitos

Sim — este é o módulo final da trilha avançada e assume o setup já feito nas aulas anteriores: OpenClaw instalado numa VPS, bot conectado ao Telegram com restrição por ID de usuário, Tailscale configurado, skills/plugins e arquivos Markdown de memória já em uso.

## Aula a aula

### 1.1 - Comandos de Barra e Análise de Arquivos  (00:07:46)
- **Resumo:** Revisão dos comandos de barra que o instrutor usa no dia a dia direto no Telegram, com foco em controlar a janela de contexto e o custo. Também mostra dois usos de arquivo: enviar planilha/PDF/imagem para o agente analisar e pedir que ele escreva um Markdown na VPS e devolva o arquivo pelo chat. Termina com um exercício prático: digitar `/` no Telegram e percorrer a lista inteira de comandos disponíveis.
- **Pontos-chave:**
  - `/new` e `/reset` reiniciam a sessão — use ao trocar de assunto, porque o contexto vai inchando e o agente começa a esquecer; `/compact` compacta a conversa sem perder o fio.
  - `/model` troca o modelo, `/context` mostra o que a IA está lendo/lembrando, `/user` mostra o custo da sessão.
  - `/skill` roda uma skill; skills instaladas podem trazer seus próprios comandos de barra (ex.: um `/meta-ads` de uma skill de marketing) — verifique isso antes de instalar.
  - `/plugins` lista, ativa, desativa e desinstala plugins. Desligue plugin fora de contexto (ex.: plugin de marketing durante tarefa de programação) para não sujar o contexto.
  - Prompt de melhoria contínua sugerido: "leia minhas últimas 30 mensagens e proponha melhorias no meu agent.md".
  - Na lista do Telegram aparecem também comandos nativos como listar comandos/ferramentas/skills, status, goal, diagnóstico, `/start`, `/stop`, `/fast`, `/voice`, `/codex`.
- **Link:** https://flix.nocodestartup.io/m/lessons/5788

### 1.2 - Voz: Configurando Interação por Áudio  (00:08:33)
- **Resumo:** Configura o ciclo completo de voz: o agente transcreve áudios que você manda e responde em áudio. A entrada usa Groq com Whisper large-v3-turbo (chave de API criada em groq.com, com data de expiração); a saída usa Microsoft Edge TTS, gratuito e nativo. A configuração é feita colando um prompt pronto no Telegram junto com a chave, e o agente edita o `openclaw.json`, salva a chave no cofre e reinicia o gateway sozinho. No teste final, a transcrição sai praticamente instantânea.
- **Pontos-chave:**
  - Caminho no `openclaw.json`: `tools` > `media` > `audio` → habilitar `audio`, definir provider `groq` e model `whisper-large-v3-turbo`.
  - Trocar de provider é só mudar o par: `openai` + `gpt-4o-mini-transcribe`; há ainda Deepgram, Mistral e Whisper local (roda de graça na VPS, dependendo do poder dela).
  - Regras embutidas no prompt de configuração: não expor a chave em logs/respostas/prints, salvar no storage/cofre do OpenClaw, nada de hardcode, e definir `pt-BR-AntonioNeural` como voz padrão com `pt-BR-FranciscaNeural` como alternativa.
  - Não é preciso pegar a chave do Groq: crie em groq.com (o Groq com Q, não o Grok do Elon Musk) em "API Keys", com expiração curta.
  - Saída de voz do Edge TTS soa robótica (chega a ler "JSON" como "John"); para qualidade melhor, usar OpenAI, ElevenLabs, MiniMax ou o próprio Groq — todos pagos.
  - Nível seguinte (só apontado, não executado): talk mode ao vivo com OpenAI realtime ou Gemini Live dentro de sala de voz do Discord/Slack, pela baixa latência.
- **Link:** https://flix.nocodestartup.io/m/lessons/5789

### 2.1 - O 80/20 do OpenClaw  (00:07:03)
- **Resumo:** Consolida os 20% de decisões que dão 80% do resultado na operação do agente. O eixo é custo e higiene: quantidade de crons e heartbeats, escolha de modelo por tipo de tarefa, manutenção periódica dos arquivos de personalidade e cautela com plugins e skills de terceiros. Também diz explicitamente o que ignorar por enquanto: multi-agente e canais exóticos.
- **Pontos-chave:**
  - Cada cron job e heartbeat custa tokens só de disparar a mensagem; filtre o que realmente precisa rodar e considere um plano coding se for rodar muitos.
  - Roteamento de modelo: modelo barato como padrão do dia a dia (o instrutor usa GPT 5.4 mini e às vezes DeepSeek, que rende meses com US$ 10); GPT 5.5 só para planejar código e caçar bug.
  - Heartbeat deve sempre rodar em modelo barato — ele só dispara, monitora e morre ("é uma batida de coração").
  - Revise `soul.md`, `user.md`, `agents.md` e o `lessons.md` de tempos em tempos, inclusive pedindo ao próprio agente que releia a memória e proponha melhorias.
  - Skill é só um prompt grande — leia o conteúdo antes de instalar: pode ter código malicioso e pode subir processo em background que trava a VPS.
  - Multi-agente (duas instâncias do OpenClaw conversando entre si) é diferente de sub-agentes, dá muito trabalho de configuração e não vale no começo.
  - Fique nos canais principais (Telegram, WhatsApp, Discord, Slack) e evite os exóticos (Nostr, Twitch, Zalo, WeChat).
- **Link:** https://flix.nocodestartup.io/m/lessons/5787

### 2.2 - Dicas Finais: os 10 Erros Mais Comuns  (00:08:04)
- **Resumo:** Lista dos dez erros que o instrutor já cometeu operando OpenClaw, agrupados em segurança/privacidade, custo e comportamento do agente. Cada erro vem com a correção que ele adotou, incluindo o hábito de tratar o agente como funcionário com credenciais e escopo próprios. Fecha o módulo antes do case final do curso.
- **Pontos-chave:**
  - Erros 1 a 4 (segurança): não jogar senha/chave de API no chat (peça para salvar no cofre); restringir quem fala com o bot pelo ID do Telegram, senão qualquer um acha o bot na busca; não expor o dashboard à internet sem Tailscale; não rodar o agente no computador pessoal — VPS isolada, também porque fica 24h ativa.
  - Erros 5 e 6 (custo): não usar o modelo mais caro (GPT 5.5 ou Opus) como conversa padrão; não deixar o agente "se mexendo" o tempo todo com crons e heartbeats esquecidos.
  - Erro 7: não atualizar no dia em que a versão sai — espere alguns dias a uma semana, até outros testarem e os bugs serem corrigidos. Vale para OpenClaw, n8n e software em geral.
  - Erro 8: personalidade vaga ("seja útil") não serve; prompts específicos de faça/não faça/resultado esperado é o que diferencia o agente de um ChatGPT genérico.
  - Erro 9: não dar autonomia para enviar e-mail ou apagar coisas. O instrutor criou um Gmail separado para o agente e compartilha apenas a pasta ou documento específico do Drive.
  - Erro 10: não deixar a conversa crescer sem limite — `/compact`, `/new` ou `/reset` ao encerrar um assunto.
- **Link:** https://flix.nocodestartup.io/m/lessons/5786

## Pegadinhas e insights

- **Heartbeat esquecido é o vilão silencioso de custo.** O instrutor descobriu um heartbeat de uma automação antiga ainda ativo, mandando "heartbeat ok" repetidamente e queimando tokens; ele voltou a disparar sozinho depois de uma troca de modelo. Recomendação: passar um checklist periódico em todos os crons e heartbeats.
- **Cron quebrado continua custando.** Quando ele cancelou a assinatura de um modelo, o cron seguiu disparando só para retornar erro — e cada disparo custava.
- **Groq com Q, não Grok com K.** A confusão é fácil e a aula avisa: o serviço da transcrição é groq.com, não o modelo do Elon Musk.
- **A chave de API na aula foi criada com expiração de 1 dia** — prática recomendada ao seguir tutoriais, já que a chave aparece na tela.
- **Contradição prática assumida:** a aula de voz cola a chave no chat, mas o prompt manda o agente salvá-la no cofre e não expor em logs. O risco real aparece quando o OpenClaw é compartilhado (ex.: instância no Slack com o time).
- **Arquitetura de instâncias separadas:** o instrutor mantém um OpenClaw no Slack (compartilhado com o time, sem segredos) gerenciado pelo OpenClaw pessoal do Telegram, que é quem detém as chaves.
- **Modelos chineses baratos já apagaram dados dele** (uma tabela excluída numa CLI, recuperada por backup) — é a origem da regra de tratar o agente como funcionário com acesso mínimo.
- **Edge TTS é gratuito mas robótico** — inclusive lê "JSON" como "John". Vale pagar por voz melhor se o áudio for entregável.
- **Prompt reverso de entrega:** pedir ao agente que escreva a pesquisa num `.md` na VPS e depois envie o arquivo pelo Telegram é mais rápido do que entrar na VPS para baixar o arquivo.
