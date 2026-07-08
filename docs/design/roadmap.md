# Vibelytics Design Roadmap

Last updated: 2026-07-08

## Current State

Vibelytics has a static public landing page and clickable pilot for an AI launch copilot for live culture. The current identity now has repo-owned source assets: route imagery, canonical SVG mark, raster derivatives, social images, refreshed screenshots, final visual QA, and shared route tokens.

The repo now includes a durable design roadmap, an approved strategy brand kit, a focused asset-source pass, first-party route imagery, and canonical identity exports. This roadmap is the coordination point for future design-to-code passes.

Production deployment verification passed on 2026-07-04 for commit `bccf62c` at `https://vibelytics-landing.vercel.app`. Live `/` and `/pilot` matched local `main`, production assets resolved, desktop/mobile browser QA passed, and the pilot interaction smoke test passed. This is deployment verification evidence, not production brand signoff by itself.

Production brand signoff passed on 2026-07-05 for the current static public scope. The decision covers `/`, `/pilot`, the canonical mark, deployed favicon/app/social images, current first-party route imagery, and shared tokens. It excludes future use of archived unknown-provenance imagery unless provenance is resolved.

Production monitoring passed on 2026-07-05 for commit `9532f2c`. Live `/` and `/pilot` matched local route files, production assets resolved, desktop/mobile browser QA passed, the pilot interaction smoke test passed, and no static-only, route-boundary, or brand-preservation blockers were found.

`docs/HANDOFF.md` now provides the concise post-signoff operating handoff for future Vibelytics threads.

Post-signoff documentation consistency audit passed on 2026-07-05. Historical pass docs now include supersession notes where old blocker language could mislead future work.

Docs-only production monitoring recheck passed on 2026-07-05 for commit `b8bcd50`. Production `/` and `/pilot` returned 200, live route HTML matched local route files, deployed favicon/app/OG/Twitter images resolved, `/` remained pure Vibelytics, `/pilot` retained only approved subtle SR007 static-pilot context, no backend/API/external-service behavior was found, the production pilot interaction smoke test passed, and build/JSON validation passed.

Public pilot copy cleanup was requested on 2026-07-05 after SR007 wording was identified as a Speedrun leftover. Current route policy is now pure Vibelytics on both `/` and `/pilot`; public SR007, Speedrun, a16z, and Andreessen references are not approved on either route.

Live-site discovery and verification passed on 2026-07-05 for commit `27b202e`. Canonical `https://www.vibelytics.ai` and `https://vibelytics-landing.vercel.app` both returned 200 for `/` and `/pilot`; fetched HTML matched local route files byte-for-byte; `/pilot` contained the new Vibelytics preview copy with no SR007, Speedrun, a16z, or Andreessen references; and no backend/API/external-service behavior was found. DNS/header checks showed `www.vibelytics.ai` serving through Vercel and the apex redirecting to `www`; no Hostinger website ID, Horizons edit URL, or Hostinger deployment config was discoverable from the repo.

Static V2 product/marketing implementation passed local and production QA on 2026-07-05 for commit `79e745b`. The scope keeps the site static-only while sharpening `/` around promoter/venue conversion and upgrading `/pilot` into a richer launch-brief generator with budget, timeline, ticketing, risk, copy/download/share/email actions, and URL-restorable scenarios. Canonical `https://www.vibelytics.ai/` and `/pilot/` returned 200 and matched local route files byte-for-byte.

Static V2 growth/conversion iteration passed local and production QA on 2026-07-05 for commit `93dd793`. The scope keeps the static-only constraint and sharpens qualified inbound conversion by adding a launch brief checklist on `/`, strengthening the CTA path into `/pilot`, adding a direct email-brief path inside `/pilot`, and upgrading the generated brief into an intake artifact with scenario, decision, rationale, launch sequence, next inputs, requested follow-up, preview boundary, and share link. Canonical `https://www.vibelytics.ai/` and `/pilot/` returned 200 and matched local route files byte-for-byte.

Static V2 qualification iteration passed local and production QA on 2026-07-08 for commit `4c15836`. The scope keeps the static-only constraint and improves conversion quality by adding good-fit/not-fit launch guidance on `/` and adding email-readiness guidance to `/pilot` generated output and exported briefs. Canonical `https://www.vibelytics.ai/` and `/pilot/` returned 200 and matched local route files byte-for-byte after cache-busted deployment verification refreshed the Vercel edge.

## Decisions Recorded

- Brand mode is `evolve`, not `create` or `replace`.
- `/` should remain pure Vibelytics branding with no SR007 references.
- `/pilot` should also remain pure Vibelytics branding with no SR007, Speedrun, a16z, or Andreessen references.
- Canonical public production is `https://www.vibelytics.ai`; the Vercel deployment URL is `https://vibelytics-landing.vercel.app`.
- If a separate Hostinger surface exists, it requires a Hostinger website ID or edit URL before it can be verified or updated.
- Static-only constraints remain in force: no backend, no API routes, no external runtime services, no new dependencies unless separately approved.
- The current PNG/CSS mark can be preserved as evidence, but it is not sufficient as canonical editable identity source.
- Signal Desk is approved as the product identity backbone.
- Culture Graph is preserved as a campaign imagery layer, not the product identity backbone.
- First Yes is preserved as a launch campaign layer, not the product identity backbone.
- Production brand signoff passed on 2026-07-05 for the current static public route and brand/social asset scope.
- The 2026-07-03 asset-source pass found no current PNG approved as canonical production brand source.
- Route-used campaign/product imagery was replaced with deterministic first-party PNGs generated from repo source.
- The canonical SVG mark now exists at `brand/vibelytics-mark.svg`.
- Favicon, app icon, brand, avatar, social, and screenshot derivatives were refreshed from repo-owned source/export paths.
- Final visual QA passed across `/`, `/pilot`, favicon/app icon/social crops, desktop/mobile viewports, and the pilot interaction smoke test.
- Shared color, semantic, typography, radius, elevation, and motion primitives now live in `styles/tokens.css` and are consumed by `index.html` and `pilot/index.html`.
- Production verification passed for the current static deployment.
- Docs-only production monitoring recheck passed after the historical signoff clarification commit.
- Public pilot copy cleanup removes SR007 wording from `/pilot`; use Vibelytics-native preview language instead.
- Canonical live-site verification confirms `www.vibelytics.ai` currently serves the same Vercel-backed static HTML as the deployment URL.
- Static V2 conversion motion is generate a launch brief, then copy, download, share, or email it to Vibelytics for pressure-testing.
- Static V2 production monitoring passed for commit `79e745b`.
- Static V2 growth conversion motion is review what to send, generate the launch brief, and email the intake artifact to Vibelytics without forms, backend, analytics, tracking, API calls, external services, auth, or credentials.
- Static V2 qualification motion is to help promoters and venues self-select before emailing: best fit is a launch decision that is still movable; not-fit contexts include live campaign reporting, incomplete briefs, attendee identification, hidden tracking, heatmaps, or emotion detection.

## Artifacts

- `docs/brand/branding-pass-2026-07-03.md`: three strategic brand territories, recommendation, blockers, and implementation checklist.
- `docs/brand/brand-kit.md`: approved Signal Desk brand kit, rejected options, rationale, implementation checklist, and assets to preserve.
- `docs/design/asset-provenance.json`: public asset provenance register with per-asset source decisions, approval states, and replacement recommendations.
- `docs/design/asset-source-pass-2026-07-03.md`: focused source pass summary, replacement list, blockers, verification commands, and next action.
- `docs/design/identity-source-pass-2026-07-03.md`: canonical mark source, raster export, route logo, screenshot refresh, verification, and next action.
- `docs/design/final-review.md`: final production brand review, evidence, accepted risks, and PASS decision for the current static scope.
- `docs/design/production-readiness.json`: structured production readiness decision for the current static brand scope.
- `docs/HANDOFF.md`: concise post-signoff handoff with production status, brand boundaries, route rules, source-of-truth files, accepted risks, and re-run checks.
- Historical pass docs with supersession notes: `docs/brand/branding-pass-2026-07-03.md`, `docs/design/asset-source-pass-2026-07-03.md`, and `docs/design/identity-source-pass-2026-07-03.md`.
- `scripts/generate-route-assets.py`: deterministic source generator for `assets/festival-network.png`, `assets/taste-map.png`, and `assets/backstage.png`.
- `brand/vibelytics-mark.svg`: canonical editable Vibelytics mark source.
- `scripts/generate-brand-assets.py`: deterministic export generator for mark, favicon, app icon, avatar, and social PNG derivatives.
- `docs/assets/vibelytics-landing-screenshot.png`: current landing screenshot evidence.
- `docs/assets/vibelytics-pilot-screenshot.png`: current pilot screenshot evidence.

## P0 / P1 Blockers

P0: Resolved for route-used campaign/product imagery. `assets/festival-network.png`, `assets/taste-map.png`, and `assets/backstage.png` are now first-party deterministic assets generated from `scripts/generate-route-assets.py`.

P1: Resolved for canonical identity source. `brand/vibelytics-mark.svg` exists and current raster derivatives are generated by `scripts/generate-brand-assets.py`.

P1: Resolved for current favicon/social PNG source lineage. Continue to regenerate with `scripts/generate-brand-assets.py` after future mark or social crop changes.

P1: Resolved for current screenshot source lineage. Screenshots were refreshed with Playwright after source assets and route logo updates.

P1: Resolved for current static routes. Shared color, typography, radius, elevation, semantic, and motion token decisions are consolidated in `styles/tokens.css`, with route-specific layout CSS kept in `index.html` and `pilot/index.html`.

P1: Resolved for current static routes. Final visual QA found no blocking crop, layout, copy, asset-load, or pilot interaction issues.

P1: Resolved for current production deployment. Production QA found no deployment, asset-resolution, copy purity, static-only, viewport, or pilot interaction blockers.

P1: Resolved for current production brand scope. Final production brand review found no P0/P1 blockers. `assets/control-room.png` and `assets/app_screen_mock.png` remain accepted P2 archive risks: internal evidence only, not approved for future public implementation unless provenance is resolved.

P1: Resolved for current production monitoring. The 2026-07-05 monitoring pass found no production route, asset-resolution, copy-boundary, static-only, viewport, or pilot interaction regressions.

P1: Resolved for docs-only production monitoring after commit `b8bcd50`. The 2026-07-05 recheck found no production route, asset-resolution, copy-boundary, static-only, pilot interaction, build, or JSON validation regressions.

P1: Resolved for live-site discovery after commit `27b202e`. The 2026-07-05 check found canonical `www.vibelytics.ai` serving the Vercel-backed route HTML with no Hostinger project identifier available in the repo.

P1: Resolved for Static V2 production monitoring after commit `79e745b`. The 2026-07-05 check found canonical `/` and `/pilot/` live, static-only, pure Vibelytics, matching local route files, and passing the upgraded pilot interaction smoke test.

P1: Resolved for the Static V2 growth/conversion iteration after commit `93dd793`. The 2026-07-05 check found the new launch brief checklist and email-brief journey live, static-only, pure Vibelytics, matching local route files, and passing build, JSON validation, route-boundary scans, static-only scans, asset checks, and the upgraded pilot interaction smoke test.

P1: Resolved for the Static V2 qualification iteration after commit `4c15836`. The 2026-07-08 check found good-fit/not-fit guidance and email-readiness generated brief copy live, static-only, pure Vibelytics, matching local route files, and passing build, JSON validation, route-boundary scans, static-only scans, asset checks, and the upgraded pilot interaction smoke test.

## Recommended Path

1. Preserve the current static route strategy: `/` and `/pilot` stay pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
2. Keep shared tokens in `styles/tokens.css`; add new route-specific CSS only when it is layout or component behavior, not a duplicate brand primitive.
3. Keep asset export scripts and provenance register current if future visual QA changes any source assets.
4. Monitor canonical `https://www.vibelytics.ai` first, with `https://vibelytics-landing.vercel.app` as the deployment URL.
5. If Hostinger is intended to host a separate live surface, get its website ID/edit URL before making claims about that deployment.
6. Re-run production QA after any route, token, or asset change, and keep asset provenance current before expanding public brand surfaces.
7. After future route, token, or asset changes, re-run canonical production monitoring and update `docs/design/production-readiness.json` only if live `/` and `/pilot` match the committed route files.
8. Next conversion work should preserve the static email-brief path unless a backend, form, analytics, or CRM integration is explicitly approved.
9. Keep future qualification copy specific to launch planning and avoid claims about live reporting, surveillance, attendee identity, or emotion detection.

## Verification Commands

Commands run for the 2026-07-03 branding pass:

```bash
git status --short --branch
rg --files -g '!node_modules' -g '!dist' -g '!archive'
find docs -maxdepth 3 -type f -print
find brand assets -maxdepth 2 -type f -print
sips -g pixelWidth -g pixelHeight brand/*.png assets/*.png docs/assets/*.png
```

Commands run for the 2026-07-03 brand-kit approval step:

```bash
git status --short --branch
sed -n '1,280p' docs/brand/branding-pass-2026-07-03.md
sed -n '1,260p' docs/design/roadmap.md
sed -n '1,260p' docs/design/asset-provenance.json
rg -n "SR007|Signal Desk|brand-kit|asset provenance|vibelytics-mark.svg|static-only|no backend|AI launch copilot" README.md index.html pilot/index.html docs/brand/branding-pass-2026-07-03.md docs/design/roadmap.md docs/design/asset-provenance.json
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
```

Commands run for the 2026-07-03 asset-source pass:

```bash
git status --short --branch
rg --files brand assets docs/assets
sips -g pixelWidth -g pixelHeight brand/*.png assets/*.png docs/assets/*.png
sips -g pixelWidth -g pixelHeight favicon.png apple-touch-icon.png og-image.png twitter-image.png
rg -n "vibelytics-mark|vibelytics-og-image|vibelytics-x-avatar|vibelytics-x-header|festival-network|taste-map|backstage|control-room|app_screen_mock|vibelytics-landing-screenshot|vibelytics-pilot-screenshot|favicon|apple-touch-icon|og-image|twitter-image" . -g '!node_modules' -g '!dist' -g '!archive'
file brand/*.png assets/*.png docs/assets/*.png
file favicon.png apple-touch-icon.png og-image.png twitter-image.png
git log --oneline --name-status -- brand assets docs/assets favicon.png apple-touch-icon.png og-image.png twitter-image.png docs/design/asset-provenance.json docs/design/roadmap.md docs/brand/brand-kit.md
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
```

Commands run for the 2026-07-03 route-asset replacement pass:

```bash
python3 scripts/generate-route-assets.py
sips -g pixelWidth -g pixelHeight assets/festival-network.png assets/taste-map.png assets/backstage.png
file assets/festival-network.png assets/taste-map.png assets/backstage.png
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
rg -n "SR007|Speedrun" index.html
npm run build
```

Commands run for the 2026-07-03 canonical identity source pass:

```bash
python3 scripts/generate-brand-assets.py
sips -g pixelWidth -g pixelHeight brand/*.png favicon.png apple-touch-icon.png og-image.png twitter-image.png docs/assets/*.png
file brand/*.png favicon.png apple-touch-icon.png og-image.png twitter-image.png brand/vibelytics-mark.svg
npm run start
Playwright: 1440x960 capture of `/` and `/pilot/`
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
rg -n "SR007|Speedrun" index.html
npm run build
```

Commands run for the 2026-07-03 final visual QA and token consolidation pass:

```bash
npm run build
rg -n "a16z|Andreessen|Speedrun|SR007" . -g '!node_modules' -g '!dist' -g '!archive'
rg -n "SR007|Speedrun|a16z|Andreessen" index.html
rg -n "SR007 static pilot|Synthetic scenarios|No backend|SR007 static demo context|no external services|no attendee tracking|Speedrun|a16z|Andreessen" pilot/index.html
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
python -m http.server 4173
node /private/tmp/vibelytics-qa.mjs
```

Final QA notes:

- Browser plugin QA first exposed stale local service-worker interference on `127.0.0.1:3000` and `localhost:4173`; clean Playwright QA was run with service workers blocked.
- Clean Playwright checks passed for `/` and `/pilot/` at 1440x960 and 390x844: status 200, meaningful Vibelytics content, no console warnings/errors, no framework overlay, no horizontal overflow, and no broken route images.
- Pilot interaction smoke test passed after selecting Mira K / London / 2,000-3,000 cap hall / Fashion and generating a decision: output changed to Adjust, Run 08, 68% confidence, demand score 69, GBP34-99 pricing, and an updated mailto launch brief.
- Favicon, app icon, OG image, and X header were visually reviewed for obvious crop issues; no asset source/export changes were made, so `docs/design/asset-provenance.json` was not changed.

Commands run for the 2026-07-04 production deployment verification:

```bash
git status --short --branch
git log -1 --oneline
curl -sS -D - https://vibelytics-landing.vercel.app/ -o /tmp/vibelytics-prod-home.html
curl -sS -D - https://vibelytics-landing.vercel.app/pilot -o /tmp/vibelytics-prod-pilot.html
shasum -a 256 index.html pilot/index.html /tmp/vibelytics-prod-home.html /tmp/vibelytics-prod-pilot.html
cmp -s index.html /tmp/vibelytics-prod-home.html
cmp -s pilot/index.html /tmp/vibelytics-prod-pilot.html
curl -sS -I https://vibelytics-landing.vercel.app/favicon.png
curl -sS -I https://vibelytics-landing.vercel.app/apple-touch-icon.png
curl -sS -I https://vibelytics-landing.vercel.app/og-image.png
curl -sS -I https://vibelytics-landing.vercel.app/twitter-image.png
curl -sS -I https://www.vibelytics.ai/favicon.png
curl -sS -I https://www.vibelytics.ai/apple-touch-icon.png
curl -sS -I https://www.vibelytics.ai/og-image.png
curl -sS -I https://www.vibelytics.ai/twitter-image.png
node /private/tmp/vibelytics-prod-qa.mjs
rg -n "SR007|Speedrun|a16z|Andreessen" /tmp/vibelytics-prod-home.html /tmp/vibelytics-prod-pilot.html
rg -n "fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" /tmp/vibelytics-prod-home.html /tmp/vibelytics-prod-pilot.html index.html pilot/index.html
```

Production verification notes:

- `git log -1 --oneline` returned `bccf62c Consolidate Vibelytics tokens and final QA`.
- Live `/` and `/pilot` returned HTTP 200 from Vercel, and their SHA-256 hashes matched `index.html` and `pilot/index.html` from local `main`.
- Production favicon, app icon, OG image, and Twitter image URLs resolved with HTTP 200 and `image/png` content types on both `vibelytics-landing.vercel.app` and canonical `www.vibelytics.ai` asset URLs.
- Playwright production QA passed for `/` and `/pilot` at 1440x960 and 390x844: status 200, Vibelytics content present, no console warnings/errors, no horizontal overflow, no broken images, and no unexpected third-party requests.
- `/` remained pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- `/pilot` retained only the approved subtle SR007/static pilot context: `SR007 static pilot`, `SR007 static demo context`, and the footer static pilot note. No Speedrun, a16z, or Andreessen references were found.
- No backend/API/external-service behavior was found in the local source or fetched production HTML.
- Production pilot interaction smoke test passed after selecting Mira K / London / 2,000-3,000 cap hall / Fashion and generating a decision: output changed to Adjust, demand score 69, confidence 68%, London GBP pricing, and an updated mailto launch brief.

Commands run for the 2026-07-05 docs-only production monitoring recheck:

```bash
curl -sS -L -w '%{http_code} %{url_effective}\n' https://vibelytics-landing.vercel.app/ -o /tmp/vibelytics-prod-home.html
curl -sS -L -w '%{http_code} %{url_effective}\n' https://vibelytics-landing.vercel.app/pilot -o /tmp/vibelytics-prod-pilot.html
curl -sS -I https://vibelytics-landing.vercel.app/favicon.png
curl -sS -I https://vibelytics-landing.vercel.app/apple-touch-icon.png
curl -sS -I https://vibelytics-landing.vercel.app/og-image.png
curl -sS -I https://vibelytics-landing.vercel.app/twitter-image.png
shasum -a 256 index.html pilot/index.html /tmp/vibelytics-prod-home.html /tmp/vibelytics-prod-pilot.html
cmp -s index.html /tmp/vibelytics-prod-home.html
cmp -s pilot/index.html /tmp/vibelytics-prod-pilot.html
rg -n "SR007|Speedrun|a16z|Andreessen|fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" /tmp/vibelytics-prod-home.html /tmp/vibelytics-prod-pilot.html index.html pilot/index.html
node -e "const { chromium } = require('playwright'); /* production pilot interaction smoke */"
npm run build
node -e "for (const f of ['docs/design/production-readiness.json','docs/design/asset-provenance.json']) { JSON.parse(require('fs').readFileSync(f,'utf8')); console.log(f+' ok'); }"
```

Docs-only production monitoring notes:

- `git log -1 --oneline` before the recheck was `b8bcd50 Clarify historical signoff docs`.
- Live `/` and `/pilot` returned HTTP 200 from Vercel, and their SHA-256 hashes matched `index.html` and `pilot/index.html`.
- Production favicon, app icon, OG image, and Twitter image URLs resolved with HTTP 200 and `image/png` content types.
- `/` remained pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- `/pilot` retained only the approved subtle SR007/static pilot context: `SR007 static pilot`, `SR007 static demo context`, and the footer static pilot note.
- No backend/API/external-service behavior was found in the local route files or fetched production HTML.
- Production pilot interaction smoke test passed after selecting Mira K / London / 2,000-3,000 cap hall / Fashion and generating a decision: output changed to Adjust, Run 08, demand score 69, confidence 68%, GBP34-99 pricing, and an updated mailto launch brief.
- `npm run build` passed, and `docs/design/production-readiness.json` plus `docs/design/asset-provenance.json` parsed as valid JSON.

Commands run for the 2026-07-05 production brand signoff review:

```bash
git status --short --branch
sed -n '1,260p' docs/design/roadmap.md
sed -n '1,320p' docs/brand/brand-kit.md
sed -n '1,260p' docs/design/asset-provenance.json
rg -n "SR007|Speedrun|a16z|Andreessen|fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" index.html pilot/index.html
node /private/tmp/vibelytics-brand-signoff-qa.mjs
sips -g pixelWidth -g pixelHeight brand/*.png favicon.png apple-touch-icon.png og-image.png twitter-image.png docs/assets/*.png assets/*.png
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
npm run build
curl -sS -I https://vibelytics-landing.vercel.app/og-image.png
```

Production brand signoff notes:

- Final decision: PASS for the current static public brand scope.
- Fresh production Playwright QA passed for `/` and `/pilot` at desktop and mobile viewports, with the pilot interaction smoke test returning Adjust, demand 69, confidence 68%.
- No site, product copy, route, token, or asset implementation changes were made during signoff.
- Updated signoff artifacts: `docs/design/final-review.md`, `docs/design/production-readiness.json`, `docs/design/asset-provenance.json`, `docs/brand/brand-kit.md`, and this roadmap.
- Accepted P2 archive risk: `assets/control-room.png` and `assets/app_screen_mock.png` remain internal evidence only and are not approved for future public brand implementation unless provenance is resolved.

Commands run for the 2026-07-05 lightweight production monitoring pass:

```bash
git status --short --branch
git log -1 --oneline
curl -sS -D /tmp/vibelytics-monitor-home.headers https://vibelytics-landing.vercel.app/ -o /tmp/vibelytics-monitor-home.html
curl -sS -D /tmp/vibelytics-monitor-pilot.headers https://vibelytics-landing.vercel.app/pilot -o /tmp/vibelytics-monitor-pilot.html
curl -sS -I https://vibelytics-landing.vercel.app/favicon.png
curl -sS -I https://vibelytics-landing.vercel.app/apple-touch-icon.png
curl -sS -I https://vibelytics-landing.vercel.app/og-image.png
curl -sS -I https://vibelytics-landing.vercel.app/twitter-image.png
curl -sS -I https://www.vibelytics.ai/og-image.png
curl -sS -I https://www.vibelytics.ai/twitter-image.png
shasum -a 256 index.html pilot/index.html /tmp/vibelytics-monitor-home.html /tmp/vibelytics-monitor-pilot.html
cmp -s index.html /tmp/vibelytics-monitor-home.html
cmp -s pilot/index.html /tmp/vibelytics-monitor-pilot.html
rg -n "SR007|Speedrun|a16z|Andreessen" /tmp/vibelytics-monitor-home.html /tmp/vibelytics-monitor-pilot.html
rg -n "fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" /tmp/vibelytics-monitor-home.html /tmp/vibelytics-monitor-pilot.html index.html pilot/index.html
node /private/tmp/vibelytics-brand-signoff-qa.mjs
node -e 'for (const f of ["docs/design/asset-provenance.json","docs/design/production-readiness.json"]) { JSON.parse(require("fs").readFileSync(f,"utf8")); console.log(f+" ok") }'
npm run build
```

Production monitoring notes:

- `git log -1 --oneline` returned `9532f2c Record production brand signoff`.
- Live `/` and `/pilot` returned HTTP 200 and matched local `index.html` and `pilot/index.html` by SHA-256 and `cmp`.
- Vercel-hosted favicon, app icon, OG image, and Twitter image URLs resolved with HTTP 200 and `image/png` content types; canonical `www.vibelytics.ai` OG and Twitter image URLs also resolved.
- `/` remained pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- `/pilot` retained only the approved SR007 static-pilot references and no Speedrun, a16z, or Andreessen references.
- No backend/API/external-service behavior was found in local or production route HTML.
- Production Playwright QA passed for `/` and `/pilot` at desktop and mobile viewports, and the pilot interaction smoke test returned Adjust, demand 69, confidence 68%.
- No site, product copy, route, token, or asset implementation changes were made during monitoring.

Commands run for the 2026-07-05 post-signoff handoff package:

```bash
git status --short --branch
rg --files docs README.md package.json index.html pilot/index.html styles/tokens.css brand assets
sed -n '1,260p' docs/design/production-readiness.json
sed -n '1,260p' docs/design/final-review.md
sed -n '1,260p' docs/design/roadmap.md
sed -n '1,220p' README.md
npm run build
node -e 'for (const f of ["docs/design/asset-provenance.json","docs/design/production-readiness.json"]) { JSON.parse(require("fs").readFileSync(f,"utf8")); console.log(f+" ok") }'
rg -n "SR007|Speedrun|a16z|Andreessen" index.html pilot/index.html
rg -n "fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" index.html pilot/index.html
```

Post-signoff handoff notes:

- Added `docs/HANDOFF.md` as the concise operational handoff package.
- No production route, product copy, implementation, or asset changes were made.
- The handoff preserves the approved route boundaries, static-only constraints, source-of-truth files, accepted P2 archive risks, and checks to re-run after future changes.

Commands run for the 2026-07-05 post-signoff documentation consistency audit:

```bash
git status --short --branch
rg -n "production brand signoff pending|signoff pending|final visual QA.*open|visual QA.*open|token consolidation.*open|source gate still open|Source gate still open|production brand signoff blocked|brand signoff blocked|source/provenance|provenance.*pending|pending provenance|still not final production brand signoff|not final production brand signoff|Do not claim production-ready|does not by itself claim|remainingBeforeProductionBrandSignoff|visual signoff pending|source_assets_established_visual_signoff_pending|implementation QA gated" docs README.md
rg -n "open|blocked|pending|not final|Do not claim|remain|remaining|signoff" docs/brand docs/design docs/HANDOFF.md README.md
npm run build
node -e 'for (const f of ["docs/design/asset-provenance.json","docs/design/production-readiness.json"]) { JSON.parse(require("fs").readFileSync(f,"utf8")); console.log(f+" ok") }'
rg -n "SR007|Speedrun|a16z|Andreessen" index.html pilot/index.html
rg -n "fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" index.html pilot/index.html
```

Post-signoff documentation consistency notes:

- Added supersession notes to historical pass docs that still carry old blocker/open-gate language.
- Current source-of-truth docs remain `docs/HANDOFF.md`, `docs/design/production-readiness.json`, `docs/design/final-review.md`, `docs/design/roadmap.md`, `docs/design/asset-provenance.json`, and `docs/brand/brand-kit.md`.
- No production route, product copy, implementation, token, or asset files were changed.

Commands run for the 2026-07-05 live-site discovery and verification pass:

```bash
git status --short --branch
git log -1 --oneline
rg -n "Hostinger|hostinger|Horizons|horizons|vibelytics\.ai|vibelytics-landing|vercel|Vercel|domain|DNS|CNAME|A record|nameserver" . -g '!node_modules' -g '!dist' -g '!archive'
git config --get remote.origin.url
find . -maxdepth 3 -iname '*hostinger*' -o -iname '*horizons*' -o -iname '.htaccess' -o -iname 'CNAME'
curl -sS -L -w '%{http_code} %{url_effective}\n' https://vibelytics-landing.vercel.app/pilot -o /tmp/vibelytics-vercel-pilot.html
curl -sS -L -w '%{http_code} %{url_effective}\n' https://www.vibelytics.ai/pilot/ -o /tmp/vibelytics-canonical-pilot.html
curl -sS -I https://www.vibelytics.ai/
curl -sS -I https://vibelytics.ai/
dig +short www.vibelytics.ai
dig +short vibelytics.ai
curl -sS -L -w '%{http_code} %{url_effective}\n' https://www.vibelytics.ai/ -o /tmp/vibelytics-canonical-home.html
curl -sS -L -w '%{http_code} %{url_effective}\n' https://vibelytics-landing.vercel.app/ -o /tmp/vibelytics-vercel-home.html
curl -sS -I https://www.vibelytics.ai/og-image.png
curl -sS -I https://www.vibelytics.ai/twitter-image.png
curl -sS -I --resolve vibelytics.ai:443:66.33.60.130 https://vibelytics.ai/
rg -n "SR007|Speedrun|speedrun|a16z|Andreessen|fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" /tmp/vibelytics-canonical-home.html /tmp/vibelytics-canonical-pilot.html /tmp/vibelytics-vercel-home.html /tmp/vibelytics-vercel-pilot.html index.html pilot/index.html
shasum -a 256 index.html pilot/index.html /tmp/vibelytics-canonical-home.html /tmp/vibelytics-canonical-pilot.html /tmp/vibelytics-vercel-home.html /tmp/vibelytics-vercel-pilot.html
npm run build
node -e 'for (const f of ["docs/design/asset-provenance.json","docs/design/production-readiness.json"]) { JSON.parse(require("fs").readFileSync(f,"utf8")); console.log(f+" ok") }'
```

Live-site discovery and verification notes:

- `git log -1 --oneline` returned `27b202e Remove SR007 wording from pilot`.
- Canonical `https://www.vibelytics.ai/` and `https://www.vibelytics.ai/pilot/` returned HTTP 200 and matched local `index.html` and `pilot/index.html` by SHA-256.
- Vercel deployment `https://vibelytics-landing.vercel.app/` and `/pilot` also returned HTTP 200 and matched the same local route files.
- Canonical `/pilot` contains `Vibelytics preview` and `Preview context only`; no SR007, Speedrun, a16z, or Andreessen references were found in local or fetched route HTML.
- No backend/API/external-service behavior was found in local or fetched route HTML.
- `www.vibelytics.ai` resolves to `cname.vercel-dns.com`, and the apex redirects to `https://www.vibelytics.ai/` with Vercel headers.
- The repo contains no Hostinger website ID, Horizons edit URL, `.htaccess`, `CNAME`, or Hostinger deployment config. The Hostinger app cannot update a separate Hostinger surface without the website ID/edit URL.

## Next Action For Future Codex Thread

Move to lightweight production monitoring and preservation:

1. Re-run production QA after any route, token, or asset change.
2. Keep `docs/design/asset-provenance.json` current if any future asset source/export changes are made.
3. Keep `/` and `/pilot` pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
4. Monitor canonical `https://www.vibelytics.ai` first and the Vercel deployment URL second.
5. If Hostinger is intended as a separate live site, get the Hostinger website ID/edit URL before attempting updates.
6. Do not use archived unknown-provenance imagery in public brand surfaces unless provenance is resolved.
