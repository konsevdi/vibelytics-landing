# Vibelytics Post-Signoff Handoff

Last updated: 2026-07-05
Canonical production: `https://www.vibelytics.ai`
Vercel deployment URL: `https://vibelytics-landing.vercel.app`
Current status: production brand signoff passed; latest lightweight production monitoring passed; legacy SR007 public pilot wording has been removed from current route policy.

## Production Status

- `/` and `/pilot` are live static routes.
- `https://www.vibelytics.ai` currently resolves through Vercel and matches the Vercel deployment URL.
- No Hostinger website ID, Horizons edit URL, or Hostinger deployment config is present in this repo. If Hostinger is intended to be a separate live surface, obtain the Hostinger website ID/edit URL before updating it.
- Production brand signoff passed for the current static public scope.
- Latest production monitoring passed after commit `27b202e`.
- Live route HTML matched local `index.html` and `pilot/index.html` during monitoring.
- Favicon, app icon, OG image, and Twitter image URLs resolved on production.
- No backend, API route, external service, runtime credential, or tracking behavior is approved.

## Brand Boundaries

- Product identity backbone: Signal Desk.
- Campaign layers: Culture Graph and First Yes may support future campaigns, but must not replace the core Vibelytics identity.
- Preserve the rounded-square V mark direction and canonical source at `brand/vibelytics-mark.svg`.
- Do not redesign, regenerate, or replace brand assets without an explicit scoped task and provenance update.

## Route Rules

- `/` must remain pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- `/pilot` must also remain pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- Use Vibelytics-native preview language on `/pilot`, such as `Vibelytics preview`, `Preview context only`, and static/no-backend disclosures.
- Keep both routes static-only.

## Source Of Truth

- Brand kit: `docs/brand/brand-kit.md`
- Final review: `docs/design/final-review.md`
- Production readiness: `docs/design/production-readiness.json`
- Roadmap: `docs/design/roadmap.md`
- Asset provenance: `docs/design/asset-provenance.json`
- Shared tokens: `styles/tokens.css`
- Canonical mark: `brand/vibelytics-mark.svg`
- Brand exports: `scripts/generate-brand-assets.py`
- Route imagery exports: `scripts/generate-route-assets.py`

## Accepted Risks

- `assets/control-room.png` has unknown provenance and is internal evidence only.
- `assets/app_screen_mock.png` has unknown provenance and is internal evidence only.
- Do not use either asset in public surfaces unless provenance is resolved and recorded.

## Checks To Re-Run After Future Changes

```bash
git status --short --branch
npm run build
node -e 'for (const f of ["docs/design/asset-provenance.json","docs/design/production-readiness.json"]) { JSON.parse(require("fs").readFileSync(f,"utf8")); console.log(f+" ok") }'
rg -n "SR007|Speedrun|a16z|Andreessen" index.html pilot/index.html
rg -n "fetch\(|XMLHttpRequest|navigator\.sendBeacon|serviceWorker|/api/|supabase|firebase|posthog|segment" index.html pilot/index.html
```

For production monitoring, also re-run:

```bash
curl -sS -D /tmp/vibelytics-canonical-home.headers https://www.vibelytics.ai/ -o /tmp/vibelytics-canonical-home.html
curl -sS -D /tmp/vibelytics-canonical-pilot.headers https://www.vibelytics.ai/pilot/ -o /tmp/vibelytics-canonical-pilot.html
curl -sS -D /tmp/vibelytics-vercel-home.headers https://vibelytics-landing.vercel.app/ -o /tmp/vibelytics-vercel-home.html
curl -sS -D /tmp/vibelytics-vercel-pilot.headers https://vibelytics-landing.vercel.app/pilot -o /tmp/vibelytics-vercel-pilot.html
shasum -a 256 index.html pilot/index.html /tmp/vibelytics-canonical-home.html /tmp/vibelytics-canonical-pilot.html /tmp/vibelytics-vercel-home.html /tmp/vibelytics-vercel-pilot.html
cmp -s index.html /tmp/vibelytics-canonical-home.html
cmp -s pilot/index.html /tmp/vibelytics-canonical-pilot.html
curl -sS -I https://vibelytics-landing.vercel.app/favicon.png
curl -sS -I https://vibelytics-landing.vercel.app/apple-touch-icon.png
curl -sS -I https://vibelytics-landing.vercel.app/og-image.png
curl -sS -I https://vibelytics-landing.vercel.app/twitter-image.png
curl -sS -I https://www.vibelytics.ai/og-image.png
curl -sS -I https://www.vibelytics.ai/twitter-image.png
node /private/tmp/vibelytics-brand-signoff-qa.mjs
```

If the temp Playwright script is unavailable, recreate the same checks from `docs/design/roadmap.md`: desktop/mobile `/` and `/pilot`, no broken images, no console warnings/errors, no unexpected third-party requests, no horizontal overflow, and the Mira K / London / 2,000-3,000 cap hall / Fashion pilot smoke test.

## Next Work

Default next mode is preservation and monitoring. Implement route, token, copy, or asset changes only when there is a concrete approved task, and update provenance/readiness docs before claiming a new production-ready state.
