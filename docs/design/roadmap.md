# Vibelytics Design Roadmap

Last updated: 2026-07-03

## Current State

Vibelytics has a static public landing page and clickable pilot for an AI launch copilot for live culture. The current identity is coherent enough to preserve and evolve: dark live-culture visuals, a rounded-square gradient V mark, bold system typography, and product surfaces centered on go / adjust / no-go launch decisions.

The repo now includes a durable design roadmap, an approved strategy brand kit, a focused asset-source pass, and first-party replacements for the three route-used P0 images. This roadmap is the coordination point for future design-to-code passes.

## Decisions Recorded

- Brand mode is `evolve`, not `create` or `replace`.
- `/` should remain pure Vibelytics branding with no SR007 references.
- `/pilot` may include subtle SR007/static pilot context.
- Static-only constraints remain in force: no backend, no API routes, no external runtime services, no new dependencies unless separately approved.
- The current PNG/CSS mark can be preserved as evidence, but it is not sufficient as canonical editable identity source.
- Signal Desk is approved as the product identity backbone.
- Culture Graph is preserved as a campaign imagery layer, not the product identity backbone.
- First Yes is preserved as a launch campaign layer, not the product identity backbone.
- No production brand implementation should proceed until asset provenance and canonical SVG source gates are resolved.
- The 2026-07-03 asset-source pass found no current PNG approved as canonical production brand source.
- Route-used campaign/product imagery was replaced with deterministic first-party PNGs generated from repo source.
- The remaining blocker before production brand signoff is the canonical SVG mark plus exported favicon, social, and screenshot derivatives.

## Artifacts

- `docs/brand/branding-pass-2026-07-03.md`: three strategic brand territories, recommendation, blockers, and implementation checklist.
- `docs/brand/brand-kit.md`: approved Signal Desk brand kit, rejected options, rationale, implementation checklist, and assets to preserve.
- `docs/design/asset-provenance.json`: public asset provenance register with per-asset source decisions, approval states, and replacement recommendations.
- `docs/design/asset-source-pass-2026-07-03.md`: focused source pass summary, replacement list, blockers, verification commands, and next action.
- `scripts/generate-route-assets.py`: deterministic source generator for `assets/festival-network.png`, `assets/taste-map.png`, and `assets/backstage.png`.
- `docs/assets/vibelytics-landing-screenshot.png`: current landing screenshot evidence.
- `docs/assets/vibelytics-pilot-screenshot.png`: current pilot screenshot evidence.

## P0 / P1 Blockers

P0: Resolved for route-used campaign/product imagery. `assets/festival-network.png`, `assets/taste-map.png`, and `assets/backstage.png` are now first-party deterministic assets generated from `scripts/generate-route-assets.py`.

P1: No source-controlled vector logo exists. Create `brand/vibelytics-mark.svg` before replacing brand mark, favicon, app icon, avatar, social, or screenshot derivatives.

P1: Current favicon/social PNGs are temporary derivatives with unknown source lineage. Re-export them only after approved source assets exist.

P1: Current screenshots are internal evidence only. Refresh them after approved source assets and route visuals are accepted.

P1: Shared design tokens are duplicated across `index.html` and `pilot/index.html`. Consolidate token decisions after asset provenance and canonical SVG gates are resolved.

## Recommended Path

1. Create canonical SVG/vector identity source for the Vibelytics mark.
2. Export raster logo, favicon, app icon, avatar, social, and screenshot derivatives from approved source assets.
3. Normalize shared color, typography, spacing, semantic, radius, and elevation tokens from `docs/brand/brand-kit.md`.
4. Apply approved tokens to `/` and `/pilot` without changing route strategy.
5. Refresh screenshots and run build, route, copy, viewport, and interaction checks.

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
rg -n "SR007|Speedrun|a16z" index.html
npm run build
```

## Next Action For Future Codex Thread

Run the canonical identity source pass:

1. Create `brand/vibelytics-mark.svg` as the deterministic source logo.
2. Keep `docs/design/asset-provenance.json` current.
3. Export favicon, app icon, brand mark, avatar, social images, and screenshots only after source assets are approved.
4. Do not claim production-ready brand signoff until identity exports, social images, and screenshots are refreshed from approved sources.
