# Vibelytics Asset Source Pass

Date: 2026-07-03
Scope: Public PNG brand, social, campaign, product, favicon, and screenshot assets
Status: Source gate still open; production brand signoff blocked

## What Was Inspected

Required docs:

- `docs/brand/brand-kit.md`
- `docs/brand/branding-pass-2026-07-03.md`
- `docs/design/roadmap.md`
- `docs/design/asset-provenance.json`

Asset folders:

- `brand/`
- `assets/`
- `docs/assets/`

Additional deployed PNG derivatives inspected because they are public favicon/social endpoints:

- `favicon.png`
- `apple-touch-icon.png`
- `og-image.png`
- `twitter-image.png`

Reference checks:

- Current route and package references for each PNG.
- Git history for when asset groups entered or changed in the repo.
- Pixel dimensions and PNG file type checks.

No production UI, route files, screenshots, favicons, social images, or asset binaries were changed.

## Decisions Made

No current PNG is approved as canonical production brand source.

The Signal Desk brand direction remains approved as strategy, but the asset source gate remains open. Current PNGs may remain in place temporarily, but they should not be treated as production-ready source assets, expanded into new campaigns, or used as proof of final brand signoff.

## Assets To Preserve

Preserve as temporary implementation assets or internal evidence until replacements are approved:

- `brand/vibelytics-mark.png`
- `favicon.png`
- `apple-touch-icon.png`
- `docs/assets/vibelytics-landing-screenshot.png`
- `docs/assets/vibelytics-pilot-screenshot.png`

Preserve the rounded-square V mark concept, not the current raster file as canonical source. The future canonical source should still be `brand/vibelytics-mark.svg`, but it should not be created until the replacement/source direction is accepted.

## Assets To Replace

P0 route-used campaign/product imagery:

- `assets/festival-network.png`
- `assets/taste-map.png`
- `assets/backstage.png`

These are currently used on `/` or `/pilot`, but their source and rights remain unknown. Replace them with documented first-party, licensed, or generated assets before production brand signoff.

P1 logo/social/favicon derivatives:

- `brand/vibelytics-og-image.png`
- `brand/vibelytics-x-avatar.png`
- `brand/vibelytics-x-header.png`
- `favicon.png`
- `apple-touch-icon.png`
- `og-image.png`
- `twitter-image.png`

These should be rebuilt from approved source assets after the SVG mark and campaign imagery are resolved.

## Assets Removed From Future Brand Implementation

Do not use these in future brand implementation unless provenance is later resolved:

- `assets/control-room.png`
- `assets/app_screen_mock.png`

They are not referenced by current routes, and keeping them out of the implementation path reduces ambiguity while the new Vibelytics site moves away from the old submission context.

## Remaining P0 / P1 Blockers

P0: Route-used campaign/product images still have unknown source and rights.

P1: No source-controlled vector mark exists. `brand/vibelytics-mark.svg` remains the right next identity source, but it should wait until the source/replacement direction is accepted.

P1: Deployed favicon and social preview PNGs are temporary derivatives with unknown source lineage.

P1: Current screenshots are safe only as internal evidence because they inherit unresolved embedded asset provenance. Regenerate them after asset replacement.

## Verification Commands

Commands run during this pass:

```bash
git status --short --branch
sed -n '1,240p' docs/brand/brand-kit.md
sed -n '241,520p' docs/brand/brand-kit.md
sed -n '1,260p' docs/brand/branding-pass-2026-07-03.md
sed -n '1,280p' docs/design/roadmap.md
sed -n '1,320p' docs/design/asset-provenance.json
rg --files brand assets docs/assets
sips -g pixelWidth -g pixelHeight brand/*.png assets/*.png docs/assets/*.png
rg -n "vibelytics-mark|vibelytics-og-image|vibelytics-x-avatar|vibelytics-x-header|festival-network|taste-map|backstage|control-room|app_screen_mock|vibelytics-landing-screenshot|vibelytics-pilot-screenshot|favicon|apple-touch-icon|og-image|twitter-image" . -g '!node_modules' -g '!dist' -g '!archive'
file brand/*.png assets/*.png docs/assets/*.png
sips -g pixelWidth -g pixelHeight favicon.png apple-touch-icon.png og-image.png twitter-image.png
file favicon.png apple-touch-icon.png og-image.png twitter-image.png
git log --oneline --name-status -- brand assets docs/assets favicon.png apple-touch-icon.png og-image.png twitter-image.png docs/design/asset-provenance.json docs/design/roadmap.md docs/brand/brand-kit.md
git ls-files brand assets docs/assets favicon.png apple-touch-icon.png og-image.png twitter-image.png
```

`exiftool` was attempted but is not installed in this environment.

JSON/docs sanity commands to run after edits:

```bash
node -e 'JSON.parse(require("fs").readFileSync("docs/design/asset-provenance.json","utf8")); console.log("asset-provenance.json ok")'
rg -n "SR007|Speedrun" index.html
```

## Next Action For Future Codex Thread

Run the replacement-source implementation pass:

1. Replace or document rights for `assets/festival-network.png`, `assets/taste-map.png`, and `assets/backstage.png`.
2. After the P0 image direction is accepted, create `brand/vibelytics-mark.svg` as the deterministic source mark.
3. Export new favicon, app icon, brand, and social PNG derivatives from approved source assets.
4. Refresh screenshots after route-used assets are replaced.
5. Keep `/` pure Vibelytics with no legacy submission references; keep any subtle static-pilot context limited to `/pilot` or docs.
