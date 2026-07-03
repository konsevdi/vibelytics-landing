# Vibelytics Design Roadmap

Last updated: 2026-07-03

## Current State

Vibelytics has a static public landing page and clickable pilot for an AI launch copilot for live culture. The current identity is coherent enough to preserve and evolve: dark live-culture visuals, a rounded-square gradient V mark, bold system typography, and product surfaces centered on go / adjust / no-go launch decisions.

The repo did not previously include a durable design roadmap or approved brand kit. This roadmap is now the coordination point for future design-to-code passes.

## Decisions Recorded

- Brand mode is `evolve`, not `create` or `replace`.
- `/` should remain pure Vibelytics branding with no SR007 references.
- `/pilot` may include subtle SR007/static pilot context.
- Static-only constraints remain in force: no backend, no API routes, no external runtime services, no new dependencies unless separately approved.
- The current PNG/CSS mark can be preserved as evidence, but it is not sufficient as canonical editable identity source.
- No brand implementation should proceed until one territory from `docs/brand/branding-pass-2026-07-03.md` is approved.

## Artifacts

- `docs/brand/branding-pass-2026-07-03.md`: three strategic brand territories, recommendation, blockers, and implementation checklist.
- `docs/design/asset-provenance.json`: public asset provenance register with current rights/source gaps.
- `docs/assets/vibelytics-landing-screenshot.png`: current landing screenshot evidence.
- `docs/assets/vibelytics-pilot-screenshot.png`: current pilot screenshot evidence.

## P0 / P1 Blockers

P0: Asset provenance is incomplete for public PNG brand and campaign assets. Resolve source, usage rights, allowed uses, attribution, and open rights questions before production brand signoff.

P1: No source-controlled vector logo exists. Create `brand/vibelytics-mark.svg` only after territory approval.

P1: No approved brand kit exists. Create `docs/brand/brand-kit.md` only after the user approves a territory.

P1: Shared design tokens are duplicated across `index.html` and `pilot/index.html`. Consolidate token decisions after brand kit approval, not before.

## Recommended Path

1. Approve a brand territory from `docs/brand/branding-pass-2026-07-03.md`.
2. Resolve or replace assets listed as `needs_provenance` in `docs/design/asset-provenance.json`.
3. Create canonical SVG/vector identity source and export raster derivatives.
4. Write `docs/brand/brand-kit.md` with selected kit, rejected options, rationale, implementation checklist, and assets to preserve.
5. Apply approved tokens to `/` and `/pilot` without changing route strategy.
6. Refresh screenshots and run build, route, copy, viewport, and interaction checks.

## Verification Commands

Commands run for the 2026-07-03 branding pass:

```bash
git status --short --branch
rg --files -g '!node_modules' -g '!dist' -g '!archive'
find docs -maxdepth 3 -type f -print
find brand assets -maxdepth 2 -type f -print
sips -g pixelWidth -g pixelHeight brand/*.png assets/*.png docs/assets/*.png
```

## Next Action For Future Codex Thread

Ask the user to choose one of the three territories:

- Signal Desk
- Culture Graph
- First Yes

If approved, run the approval output step from the branding pass and create `docs/brand/brand-kit.md`. If not approved, keep strategy work in docs only and do not change production UI or assets.
