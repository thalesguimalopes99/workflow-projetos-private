# Converse com um PDF, Planilhas e Arquivos | RAG

Trilha Assistants Open AI | 4 aulas | ~24 min (00:23:56) | nível intermediário

> Ensina a dar conhecimento próprio (PDF/TXT) a um Assistant da OpenAI usando File Search + Vector Store, e a plugar esse agente num fluxo de WhatsApp já existente via n8n.

## O que você sai sabendo fazer

- Explicar o ciclo de RAG (busca → embedding → comparação por similaridade em base vetorial → pergunta + contexto → resposta da LLM) e onde ele entra na arquitetura de um agente.
- Criar um Assistant na plataforma da OpenAI com prompt de persona, instruções e restrições de formato de saída.
- Ativar o File Search, subir um arquivo e entender a relação arquivo → Vector Store → Assistant (e gerenciar tudo pelo Storage do dashboard).
- Contornar a limitação de CSV/XLSX convertendo a planilha em PDF antes do upload.
- Ajustar o prompt para eliminar markdown, hiperlinks e citações de fonte, deixando a resposta legível no WhatsApp.
- Reaproveitar o fluxo n8n do módulo anterior trocando o assistant ID no node que cria a run, e religar credenciais e webhook.

## Stack e ferramentas

- OpenAI Assistants (dashboard, Playground, File Search, Vector Stores, seção Storage)
- Modelo GPT "mini" (escolhido na configuração do Assistant)
- n8n (fluxo de automação importado do módulo anterior)
- Z-API (API de WhatsApp; webhook "ao receber")
- Supabase (tabela de usuários com nome, WhatsApp e ID da thread)
- PDF como formato de ingestão (planilha Excel convertida)
- Menções teóricas de bases vetoriais: Pinecone, Redis, Qdrant, Milvus, Supabase

## Pré-requisitos

- Módulo de Fundamentos de Assistants da OpenAI (o instrutor recomenda fortemente assistir antes).
- Módulo do agente de IA no WhatsApp — o fluxo n8n, a tabela do Supabase e a integração Z-API vêm de lá e são só incrementados aqui.
- Desejável: curso de engenharia de prompt da formação (citado como complemento).

## Aula a aula

### 1 - O que vamos construir (parte 1 e 2)  (00:05:22)
- **Resumo:** Abertura do módulo, apresentando a proposta de alimentar o assistente com documentos próprios (PDF, TXT) para que ele responda com conhecimento especializado. O instrutor demonstra no WhatsApp um agente de suporte que responde perguntas sobre as aulas da NoCode Startup e devolve os links certos. Fecha mostrando a arquitetura que será usada e os pré-requisitos.
- **Pontos-chave:**
  - Casos de uso citados: agente de suporte treinado com material próprio, agente de vendas com dados da empresa e "clones de IA".
  - Arquitetura: WhatsApp como front-end, Supabase como fonte de verdade, n8n orquestrando, Assistants da OpenAI com GPT, API de WhatsApp na ponta.
  - Pré-requisitos explícitos: fundamentos de Assistants e o agente de IA no WhatsApp.
  - Materiais ficam na descrição da aula, na comunidade e na página inicial da formação.
- **Link:** https://flix.nocodestartup.io/m/lessons/3920

### 2 - RAG e Embeddings Teoria (parte 1 e 2)  (00:03:59)
- **Resumo:** Revisão conceitual do que acontece "por debaixo dos panos" no RAG. Situa a base de conhecimento dentro dos componentes de um agente (modelo, prompt de sistema, memória, base de conhecimento, ferramentas) e explica embeddings como representações vetoriais posicionadas por similaridade. Descreve o fluxo completo da consulta até a resposta enriquecida.
- **Pontos-chave:**
  - Componentes de um agente: modelo (GPT, Llama), prompt de sistema, memória de contexto, base de conhecimento (RAG) e ferramentas/APIs — estas ficam para o próximo módulo.
  - Embeddings = vetores; a busca compara vetor com vetor por similaridade para achar contexto extra.
  - Pipeline: pergunta → embedding da busca → avaliação na base vetorial → pergunta + contexto → LLM → resposta mais confiável.
  - Exemplos de bancos vetoriais de mercado: Pinecone, Redis, Qdrant, Milvus, Supabase.
  - Aviso: no dia a dia, com as ferramentas certas, quase nada disso precisa ser manipulado à mão.
- **Link:** https://flix.nocodestartup.io/m/lessons/3919

### 3 - Criando Assistants com RAG (parte 1 e 2)  (00:08:28)
- **Resumo:** Parte prática principal. Cria o assistente de suporte no dashboard da OpenAI, escreve o prompt, liga o File Search e sobe o PDF com o mapeamento das aulas da formação. Mostra que o upload gera automaticamente uma Vector Store associada ao assistente e navega pelo Storage. Testa no Playground e depois refina o prompt para limpar a formatação da resposta.
- **Pontos-chave:**
  - Prompt usado: persona ("melhor agente de suporte do mundo") + instrução de usar os arquivos da base vetorial + tom motivador + regra dura de nunca inventar resposta e mandar o usuário para a comunidade quando não souber.
  - Modelo escolhido: mini. Interpretador de código e funções ficam desligados; formato de resposta em texto; temperatura e top P no padrão.
  - File Search precisa ser habilitado manualmente; no "+" faz-se o upload, e o botão Attach cria a Vector Store e a vincula ao assistente.
  - Vector Store tem ID próprio, não expira, aceita novos arquivos, pode ser renomeada, desassociada ou deletada; visível em Storage no dashboard.
  - Segunda rodada de prompt adiciona restrições: nunca citar os arquivos-fonte (os colchetes de referência), nunca usar markdown e enviar links diretos em vez de hiperlinks.
  - O instrutor confere manualmente os links devolvidos no navegador para checar se o modelo não alucinou URLs.
- **Link:** https://flix.nocodestartup.io/m/lessons/3922

### 4 - Integrando o Assistente de Suporte ao WhatsApp  (00:06:07)
- **Resumo:** Fecha o módulo conectando o novo assistente ao WhatsApp. Importa no n8n o fluxo construído no módulo anterior, reconfigura credenciais e webhook, e mostra que a única mudança real de arquitetura é apontar o assistant ID novo. Testa a ponta a ponta enviando uma pergunta pelo WhatsApp e recebendo a resposta com link funcional.
- **Pontos-chave:**
  - Credenciais a religar após importar o fluxo: Supabase, OpenAI (em vários nodes) e Z-API.
  - Tabela do Supabase precisa dos campos nome, WhatsApp e ID da thread — padrão herdado do módulo anterior.
  - Webhook: copiar a URL do node webhook do n8n e colar em Z-API → instância → webhooks → "ao receber".
  - O assistant ID fica fixo no body do node que cria a run — é ali que se amarra thread + assistente.
  - Encerramento: a interface no-code da OpenAI evita implementar embedding e retrieval na mão; o próximo módulo cobre funções, APIs e acesso a banco de dados.
- **Link:** https://flix.nocodestartup.io/m/lessons/3921

## Pegadinhas e insights

- **Assistants da OpenAI não lidam bem com CSV nem com XLSX/planilhas Excel.** A solução do curso é converter a planilha em PDF antes de subir — foi exatamente o que ele fez com a tabela de aulas.
- **Formatação padrão do File Search quebra no WhatsApp:** o modelo devolve markdown, hiperlinks e citações em colchetes das fontes. A mitigação é por prompt (proibir markdown, proibir menção a arquivo-fonte, exigir link cru) — e o próprio instrutor avisa que isso não funciona 100% das vezes.
- **Modelo alucina link:** ele testa manualmente cada URL retornada no navegador antes de dar o resultado como bom.
- **Regra anti-alucinação no prompt:** mandar o agente admitir que não sabe e encaminhar para a comunidade em vez de inventar.
- **A qualidade da resposta depende da qualidade da base**, não do setup — dito explicitamente no fechamento.
- **Arquitetura:** o RAG mora inteiramente dentro do assistente na OpenAI; o fluxo n8n não muda de estrutura, só troca o assistant ID. Isso torna barato trocar de agente sem mexer na automação.
- **Hierarquia a memorizar:** arquivo → Vector Store → Assistant. Uma Vector Store pode ser reaproveitada por mais de um assistente.
