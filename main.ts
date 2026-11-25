// main.ts — copies POST.json from the repository root into the output
// directory the grader provides (first CLI argument, default "./output").
// Before copying it validates the file: it must parse as JSON, be an object
// with exactly one field, and that field must be a `url` string shaped like
// an X post address. After copying it re-reads both files and fails loudly
// unless the output is byte-for-byte identical to the source, so a silent
// partial write can never pass as a successful run.
// Node 22, standard library only.
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outDir = process.argv[2] ?? join(repoRoot, "output");
const sourcePath = join(repoRoot, "POST.json");
const destPath = join(outDir, "POST.json");

const sourceBytes = readFileSync(sourcePath);
let parsed: unknown;
try {
  parsed = JSON.parse(sourceBytes.toString("utf8"));
} catch (error) {
  throw new Error(`POST.json is not valid JSON: ${(error as Error).message}`);
}
if (
  typeof parsed !== "object" ||
  parsed === null ||
  Array.isArray(parsed) ||
  Object.keys(parsed).length !== 1 ||
  typeof (parsed as Record<string, unknown>).url !== "string" ||
  !/^https:\/\/(www\.|mobile\.)?(x|twitter)\.com\/[^/]+\/status\/\d+$/.test(
    (parsed as Record<string, string>).url,
  )
) {
  throw new Error(
    'POST.json must be {"url": "https://x.com/<handle>/status/<id>"}',
  );
}

mkdirSync(outDir, { recursive: true });
copyFileSync(sourcePath, destPath);

const copiedBytes = readFileSync(destPath);
if (!sourceBytes.equals(copiedBytes)) {
  throw new Error("POST.json copy differs from the source; refusing to pass");
}
console.log(`POST.json copied to ${outDir} (${sourceBytes.length} bytes, verified identical)`);
