# Vibelytics Post-Signoff Handoff

Last updated: 2026-09-22
Canonical production: `https://www.vibelytics.ai`
Vercel deployment URL: `https://vibelytics-landing.vercel.app`
Current status: `SV2-DATE-002` passed canonical and Vercel production monitoring for commit `1e34f3e`.

Local implementation status: `SV2-DATE-004` passed local QA on 2026-09-22 but is not yet represented by the production checkpoint above.

## Production Status

- `/` and `/pilot` are live static routes.
- Static V2 adds stronger promoter/venue positioning on `/` and a richer static launch-brief generator on `/pilot`.
- The current growth iteration adds a launch brief checklist on `/`, a clearer `/pilot` email-brief path, and a more intake-ready generated brief artifact.
- The current qualification iteration adds good-fit/not-fit guidance on `/` and email-readiness guidance in generated `/pilot` briefs.
- The current trust iteration adds how-to-read guidance on `/`, bounds scenario confidence and recommendation copy on `/pilot`, and carries the same interpretation into copied, downloaded, and emailed briefs.
- The current validation-handoff iteration adds one concise recommendation-specific `What would change this decision` block on `/pilot` and carries the same evidence or re-scope threshold into copied, downloaded, and emailed briefs.
- Fresh `/pilot` visits compute a target date six weeks ahead. Valid explicit query dates remain authoritative, and the selected date is carried into generated, share, and email artifacts.
- `https://www.vibelytics.ai` currently resolves through Vercel and matches the Vercel deployment URL.
- No Hostinger website ID, Horizons edit URL, or Hostinger deployment config is present in this repo. If Hostinger is intended to be a separate live surface, obtain the Hostinger website ID/edit URL before updating it.
- Production brand signoff passed for the current static public scope.
- Current production monitoring passed on 2026-09-21 for commit `1e34f3e`; this is the only entry meant by “current monitoring.”
- Growth/conversion production monitoring passed after commit `93dd793`.
- Qualification production monitoring passed after commit `4c15836`.
- Trust/decision-clarity production monitoring passed on 2026-07-13 for commit `368b265`; canonical and Vercel `/` and `/pilot` matched the committed route files byte-for-byte.
- Validation-handoff production monitoring passed on 2026-07-27 for commit `91142e0`; canonical and Vercel `/` and `/pilot` matched the committed route files byte-for-byte.
- Calendar-date guard production monitoring passed on 2026-09-21 for commit `1e34f3e`; canonical and Vercel `/` and `/pilot` matched the committed route files byte-for-byte, fresh visits selected `2026-11-02`, valid dates restored unchanged, and impossible dates preserved the computed default at desktop and mobile sizes.
- Live route HTML matched local `index.html` and `pilot/index.html` during monitoring.
- Favicon, app icon, OG image, and Twitter image URLs resolved on production.
- No backend, API route, external service, runtime credential, or tracking behavior is approved.
- The 2026-07-05 `9532f2c` and `b8bcd50` monitoring records are historical only. Their former SR007 pilot-context allowance is `SUPERSEDED` by the pure Vibelytics policy established after `27b202e`.

## Brand Boundaries

- Product identity backbone: Signal Desk.
- Campaign layers: Culture Graph and First Yes may support future campaigns, but must not replace the core Vibelytics identity.
- Preserve the rounded-square V mark direction and canonical source at `brand/vibelytics-mark.svg`.
- Do not redesign, regenerate, or replace brand assets without an explicit scoped task and provenance update.

## Route Rules

- `/` must remain pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- `/pilot` must also remain pure Vibelytics with no SR007, Speedrun, a16z, or Andreessen references.
- Use Vibelytics-native preview language on `/pilot`, such as `Vibelytics preview`, `Preview context only`, and static/no-backend disclosures.
- Preserve the Static V2 conversion motion: generate a launch brief, then copy, download, share, or email it to Vibelytics for pressure-testing.
- Preserve the growth conversion motion: review what to send, generate the static launch brief, then email the intake artifact to Vibelytics.
- Preserve qualification guidance: Vibelytics is best for launch decisions that are still movable, not live campaign reporting, attendee identification, hidden tracking, heatmaps, or emotion detection.
- Preserve the trust boundary: recommendations are scenario directions, preview confidence is not a sell-through probability, and synthetic assumptions must be replaced with real venue, economics, audience, partner, and deadline evidence before committing.
- Preserve the validation-handoff boundary: Go names the evidence required before commitment; Adjust names the variables to change or verify; Do Not Launch names the re-scope and evidence required before reconsideration.
- Preserve the date boundary: fresh visits use local calendar date plus 42 days; valid explicit query dates restore unchanged; visible, copied/downloaded, share, and email artifacts keep one selected date.
- Keep both routes static-only.

## Source Of Truth

- Brand kit: `docs/brand/brand-kit.md`
- Final review: `docs/design/final-review.md`
- Production readiness: `docs/design/production-readiness.json`
- UX QA: `docs/design/ux-qa.md`
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

For Static V2 pilot QA, also check:

- changing artist, city, capacity, budget, date, timeline, sponsor, ticketing, goal, and risk updates the generated decision
- `Copy brief`, `Download brief`, `Copy share link`, and `Email brief` all use the same generated launch brief
- a copied share URL restores the selected scenario via query parameters
- a fresh visit defaults exactly 42 calendar days ahead
- a valid explicit query date restores unchanged
- the visible date, copied share URL, and encoded email body agree
- an impossible but shape-valid query date preserves the computed six-week default

For production monitoring, also re-run:

```bash
npm run verify:production -- --token=COMMIT_OR_RUN_ID
```

The repo-owned helper checks route status, byte parity, route-purity/static-only boundaries, and production/provenance JSON. Browser behavior remains a separate manual check: desktop/mobile `/` and `/pilot`, no broken images, no console warnings/errors, no unexpected third-party requests, no horizontal overflow, and the focused pilot scenario/date/artifact smoke tests recorded in `docs/design/roadmap.md`.

## Queue Handoff

Status boundaries are defined in `docs/design/roadmap.md`. Historical or locally completed `VERIFIED` work is not pending; `CANDIDATE` work is not authorized or ordered; a bounded implementation run may start only when exactly one task is `SELECTED`.

No next implementation task is selected. `SV2-DATE-004` is locally verified with exact helper copy, `aria-describedby`, aligned desktop/tablet/mobile layouts, and unchanged date artifacts. Commit, push, deploy, and repeat production parity/browser checks before promoting it to current production monitoring.
