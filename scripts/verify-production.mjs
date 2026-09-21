import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";

const tokenArgument = process.argv.find((argument) => argument.startsWith("--token="));
const verificationToken = tokenArgument?.slice("--token=".length) || `run-${Date.now()}`;

const routes = [
  { label: "canonical /", url: "https://www.vibelytics.ai/", file: "index.html" },
  { label: "canonical /pilot", url: "https://www.vibelytics.ai/pilot/", file: "pilot/index.html" },
  { label: "Vercel /", url: "https://vibelytics-landing.vercel.app/", file: "index.html" },
  { label: "Vercel /pilot", url: "https://vibelytics-landing.vercel.app/pilot", file: "pilot/index.html" }
];

const jsonFiles = [
  "docs/design/asset-provenance.json",
  "docs/design/production-readiness.json"
];

const forbiddenTerms = /\b(?:SR007|Speedrun|a16z|Andreessen)\b/i;
const staticOnlyViolations = /fetch\s*\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|\/api\/|supabase|firebase|posthog|segment|mixpanel|analytics/i;

function hash(content) {
  return createHash("sha256").update(content).digest("hex");
}

function withVerificationToken(url) {
  const checkedUrl = new URL(url);
  checkedUrl.searchParams.set("verify", verificationToken);
  return checkedUrl;
}

async function verifyJson() {
  for (const file of jsonFiles) {
    JSON.parse(await readFile(file, "utf8"));
    console.log(`PASS json ${file}`);
  }
}

async function verifyRoutes() {
  const localFiles = new Map();

  for (const route of routes) {
    if (!localFiles.has(route.file)) {
      localFiles.set(route.file, await readFile(route.file));
    }

    let response;
    try {
      response = await fetch(withVerificationToken(route.url), { redirect: "follow" });
    } catch (error) {
      const detail = error instanceof Error ? error.message : String(error);
      throw new Error(`${route.label} request failed: ${detail}`);
    }
    if (!response.ok) {
      throw new Error(`${route.label} returned HTTP ${response.status}`);
    }

    const remoteContent = Buffer.from(await response.arrayBuffer());
    const localContent = localFiles.get(route.file);
    if (!remoteContent.equals(localContent)) {
      throw new Error(
        `${route.label} does not match ${route.file} ` +
        `(local ${hash(localContent)}, remote ${hash(remoteContent)})`
      );
    }

    const html = remoteContent.toString("utf8");
    if (forbiddenTerms.test(html)) {
      throw new Error(`${route.label} contains a forbidden public-route term`);
    }
    if (staticOnlyViolations.test(html)) {
      throw new Error(`${route.label} contains a static-only violation`);
    }

    console.log(`PASS route ${route.label} -> ${route.file} ${hash(remoteContent)}`);
  }
}

try {
  await verifyJson();
  await verifyRoutes();
  console.log(`PASS production verification token=${verificationToken}`);
} catch (error) {
  console.error(`FAIL ${error instanceof Error ? error.message : String(error)}`);
  process.exitCode = 1;
}
