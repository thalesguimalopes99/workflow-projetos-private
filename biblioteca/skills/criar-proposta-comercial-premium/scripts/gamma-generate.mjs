#!/usr/bin/env node
// gamma-generate.mjs — gera um deck no Gamma e baixa o export.
// Uso:
//   node gamma-generate.mjs --input ./outline.md --export pptx --out ./proposta.pptx \
//        [--theme "Nome do Tema"] [--numCards 11] [--textMode preserve]
// Requer env GAMMA_API_KEY.

import fs from "node:fs";
import path from "node:path";

// auto-load .env da raiz (cwd) se a key não estiver no ambiente
if (!process.env.GAMMA_API_KEY) {
  try {
    const _envPath = path.resolve(process.cwd(), ".env");
    for (const _line of fs.readFileSync(_envPath, "utf8").split(/\r?\n/)) {
      const _m = _line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
      if (_m && !process.env[_m[1]]) process.env[_m[1]] = _m[2];
    }
  } catch {}
}

const API = "https://public-api.gamma.app/v1.0/generations";
const KEY = process.env.GAMMA_API_KEY;

function arg(name, def = undefined) {
  const i = process.argv.indexOf(`--${name}`);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}

async function main() {
  if (!KEY) throw new Error("GAMMA_API_KEY ausente no ambiente.");

  const inputPath = arg("input");
  if (!inputPath) throw new Error("--input <arquivo> é obrigatório.");
  const inputText = fs.readFileSync(inputPath, "utf8");

  const exportAs = arg("export", "pptx"); // pptx | pdf | png
  const out = arg("out", `./out.${exportAs}`);
  const textMode = arg("textMode", "preserve"); // preserve não reescreve a copy
  const numCards = Number(arg("numCards", "11"));
  const theme = arg("theme"); // opcional

  const body = {
    inputText,
    format: "presentation",
    textMode,
    numCards,
    exportAs,
  };
  if (theme) body.themeName = theme;

  // 1) cria a geração
  const createRes = await fetch(API, {
    method: "POST",
    headers: { "X-API-KEY": KEY, "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!createRes.ok) {
    throw new Error(`POST falhou ${createRes.status}: ${await createRes.text()}`);
  }
  const { generationId } = await createRes.json();
  if (!generationId) throw new Error("Resposta sem generationId.");
  console.log(`generationId=${generationId} (poll a cada 5s)`);

  // 2) poll até completed/failed (timeout 5 min)
  const deadline = Date.now() + 5 * 60 * 1000;
  let result;
  while (Date.now() < deadline) {
    await new Promise((r) => setTimeout(r, 5000));
    const res = await fetch(`${API}/${generationId}`, {
      headers: { "X-API-KEY": KEY },
    });
    if (!res.ok) throw new Error(`GET falhou ${res.status}: ${await res.text()}`);
    result = await res.json();
    if (result.status === "completed") break;
    if (result.status === "failed") throw new Error(`Geração falhou: ${JSON.stringify(result)}`);
    console.log(`status=${result.status}...`);
  }
  if (!result || result.status !== "completed") throw new Error("Timeout no poll.");

  // 3) baixa o export
  const url = result.exportUrl;
  if (!url) throw new Error("Sem exportUrl na resposta completed.");
  const fileRes = await fetch(url);
  if (!fileRes.ok) throw new Error(`Download falhou ${fileRes.status}`);
  const buf = Buffer.from(await fileRes.arrayBuffer());
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  fs.writeFileSync(out, buf);

  console.log(JSON.stringify({ ok: true, out, gammaUrl: result.gammaUrl, gammaId: result.gammaId }));
}

main().catch((e) => {
  console.error(`ERRO: ${e.message}`);
  process.exit(1);
});
