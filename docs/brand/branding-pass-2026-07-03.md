# Vibelytics Branding Pass

Date: 2026-07-03
Pass: `design-to-code-workflow:branding-pass`
Mode: Evolve existing identity, not replace
Status: Awaiting direction approval before implementation

Supersession note, 2026-07-05: This file is historical evidence from the initial branding pass. Direction 1, Signal Desk, was later approved as the product identity backbone; source/provenance blockers were resolved for the current public scope; final visual QA, production brand signoff, and production monitoring passed. Use `docs/HANDOFF.md`, `docs/brand/brand-kit.md`, `docs/design/production-readiness.json`, and `docs/design/roadmap.md` for current status before acting on this pass.

## Scope

This pass audits the current Vibelytics landing site and pilot identity, records three brand territories for approval, and updates the design operating system. No UI, logo, copy, or asset implementation changes were made.

## Evidence Inspected

- Routes: `/`, `/pilot`, `/privacy`, `/terms`
- Core files: `index.html`, `pilot/index.html`, `README.md`, `package.json`
- Docs: `docs/SR007_SUMMARY.md`, `docs/VERCEL_DEPLOYMENT_SUMMARY.md`
- Brand assets: `brand/vibelytics-mark.png`, `brand/vibelytics-og-image.png`, `brand/vibelytics-x-avatar.png`, `brand/vibelytics-x-header.png`
- Product imagery: `assets/festival-network.png`, `assets/taste-map.png`, `assets/backstage.png`, `assets/control-room.png`, `assets/app_screen_mock.png`
- Screenshots: `docs/assets/vibelytics-landing-screenshot.png`, `docs/assets/vibelytics-pilot-screenshot.png`
- CSS tokens and repeated UI primitives in `index.html` and `pilot/index.html`

## Current Brand Read

Vibelytics is positioned as the AI launch copilot for live culture. The most consistent and defensible brand idea is pre-commitment judgment: helping promoters and venues decide what to launch before room holds, guarantees, paid media, and sponsor packages harden.

The current visual identity is already recognizable:

- Dark premium live-culture backdrop.
- Cyan, violet, mint, coral, and warm highlight gradients.
- Rounded-square gradient V mark with a dark inset and angled white V.
- Large direct type, dense product surfaces, and event imagery with network overlays.
- Tone: confident, operator-facing, direct, and anti-generic-dashboard.

The current system should be evolved rather than replaced. The strongest opportunity is to make the identity more ownable and disciplined: source-controlled mark construction, clearer token hierarchy, less decorative gradient dependence, and sharper distinction between identity, campaign imagery, and product UI.

## Approved / Unknown / Risky

Approved by current repo evidence:

- Category: AI launch copilot for live culture.
- Core audience: promoters, midsize venues, creators, and brand partners involved in launch decisions.
- Product promise: choose city, room, price, sponsor story, and launch angle before capital is committed.
- Constraint: static-only site and pilot, no backend, no API routes, no external runtime services.
- Route distinction: `/` stays pure Vibelytics; `/pilot` may carry SR007/static pilot context.

Unknown:

- Canonical logo source file does not exist as SVG/vector source.
- Provenance and usage rights for generated or assembled PNG assets are not documented.
- Preferred brand territory has not been approved.
- Whether future SceneQuest activation should become a campaign layer, product module, or separate brand surface.

Risky:

- Current mark is PNG and CSS-derived, so production use can drift without a canonical construction file.
- The palette can become one-note neon dark if every surface leans on cyan/violet gradients.
- Product UI and marketing imagery currently share similar glow/network language, which may blur identity versus campaign layer.
- No durable brand kit exists yet, so future edits could create duplicate visual systems.

## Direction 1: Signal Desk

Positioning snapshot: Vibelytics is the operator's launch desk for deciding what deserves capital before the public announcement.

Audience and category: Promoters, midsize venue operators, and small launch teams comparing gut instinct, spreadsheets, agency decks, and generic analytics dashboards.

Personality tension: Calm authority versus cultural electricity. It should feel decisive and sober without becoming corporate software.

Visual territory rationale: Product-first, dark, precise, and high-contrast. The brand borrows from dispatch desks, trading terminals, and production control rooms, but keeps live-culture warmth through event imagery and human launch copy.

Logo concept: Keep the rounded-square V, but rebuild it as a deterministic vector mark. The V becomes a decisive check-shaped signal, slightly angled but optically corrected.

Logo construction logic and source strategy: Create a source-controlled `brand/vibelytics-mark.svg` with a rounded-square container, inset dark panel, and geometric V from two polygons. Export PNGs from the SVG. Preserve current PNGs until SVG approval.

Wordmark concept: Heavy grotesk wordmark with tight spacing and a slight optical notch in the V only if legibility survives small sizes.

Lockups and usage notes: Horizontal lockup for nav/social headers, standalone mark for favicon/avatar, monochrome mark for legal and low-color contexts. Avoid placing the mark over busy event imagery without a dark plate.

Color palette:

- Primary: signal cyan `#1EE7FF`, decision mint `#3CF2B5`, deep stage `#04060D`
- Secondary: violet `#A36AFF`, ember `#FF8B5C`, production blue `#5796FF`
- Neutral: ink `#F8FBFF`, muted `#C4CEDC`, steel `#8996AA`, line `rgba(219,231,255,.16)`
- Semantic: go `#3CF2B5`, adjust `#F6C65B`, no-go `#FF6D5F`, info `#5796FF`

Accessibility and contrast: Keep bright semantic fills on near-black panels. Avoid small muted text below 14px on dark gradients. Buttons with cyan/violet gradients need dark text only where contrast remains above AA.

Typography: Continue system sans for static simplicity, but define a hierarchy: display 76-156, section 38-76, app headings 16-24, control labels 11-12 uppercase. If a webfont is later approved, choose a sturdy grotesk such as Space Grotesk or Söhne-like equivalent, loaded locally only.

Icon/illustration/photo style: Product diagrams should be sharp, annotated, and signal-based. Photos should show real stages, backstage, city maps, and operator context, never generic audience heatmaps or emotion overlays.

UI token direction: Consolidate route-specific variables into shared brand tokens for background, panel, line, text, semantic decisions, radius, and elevation. Pilot should be denser than marketing pages.

Motion/interaction tone: Fast confidence, not spectacle. 150-250ms state changes, subtle rise, no decorative looping motion.

Voice and microcopy: Short operator language: "Make the call", "Hold the room", "Re-scope capacity", "Open founder presale". Avoid "unlock insights" and generic AI phrasing.

Social/avatar/favicon notes: Use the vector mark as canonical. Avatar can keep the light grid background, but favicon should simplify to dark inset plus white V for small-size clarity.

Marketing material concepts:

- Channel: Founder/investor deck cover. CTA: "Open the pilot." Measurement: deck-to-pilot clickthrough. Rationale: proof through product.
- Channel: LinkedIn/X launch graphic. CTA: "Go / adjust / no-go before spend." Measurement: profile visits and pilot opens. Rationale: maps brand to decision moment.
- Channel: Sales one-pager for venues. CTA: "Pressure-test a launch." Measurement: email replies to `yes@vibelytics.ai`. Rationale: simple B2B conversion path.

Style-guide artifacts beyond swatches: SVG logo construction sheet, token table, component state examples, social crop map, launch-copy tone examples.

Merch/real-world extension: Staff pass lanyards using the V mark and a "Launch Desk" label; venue sticker with "Go / Adjust / Hold" semantic stripes.

Best fit if: Vibelytics wants to feel most like a serious operator tool and avoid looking like a campaign microsite.

## Direction 2: Culture Graph

Positioning snapshot: Vibelytics maps cultural pull into launch decisions: artist, city, room, sponsor, and story.

Audience and category: Promoters, creators, brand marketers, and venue teams who need a sharper alternative to social listening, static surveys, and agency taste decks.

Personality tension: Intuitive taste versus quantified signal. It should feel alive and cultural, but still decision-grade.

Visual territory rationale: Builds on the current network-map imagery but makes it more ownable through graph motifs, city nodes, path lines, and score states. This direction leans more editorial and atmospheric than Signal Desk.

Logo concept: The V becomes a forked path or venue beam inside the rounded-square container, suggesting launch routes converging into a decision.

Logo construction logic and source strategy: Deterministic SVG with three path strokes that resolve into a V. Use current PNG mark only as temporary raster reference.

Wordmark concept: Same bold wordmark, but supported by a "culture graph" motif in headers and social rather than changing letterforms.

Lockups and usage notes: Mark plus wordmark for product; mark plus city-node pattern for campaign imagery. Avoid using node overlays to imply live audience tracking.

Color palette:

- Primary: midnight `#050711`, graph cyan `#1EE7FF`, signal violet `#B26CFF`
- Secondary: warm stage `#FF8B5C`, creator pink `#F472B6`, destination blue `#5796FF`
- Neutral: ice `#F8FAFC`, cloud `#D6DEE9`, haze `#75839A`
- Semantic: go mint, adjust gold, no-go coral, uncertainty blue-gray

Accessibility and contrast: Network lines should be decorative only and never carry required information without labels. Keep text on calm dark surfaces, not directly on high-noise image zones.

Typography: Large editorial display moments on `/`; compact product typography on `/pilot`. Do not let campaign type scale invade controls.

Icon/illustration/photo style: City maps, taste graphs, stage images, sponsor category symbols. No live crowd monitoring metaphors, no facial/emotion diagrams, no surveillance-like UI.

UI token direction: Add graph-line and node tokens for marketing visuals, while product UI keeps restrained decision tokens.

Motion/interaction tone: Network nodes can reveal or connect on marketing surfaces; product interactions should remain quick and functional.

Voice and microcopy: More cultural language than Signal Desk: "city pull", "genre fit", "launch story", "first signal". Still concrete and decision-oriented.

Social/avatar/favicon notes: Social headers can use city graph imagery; favicon must remain simplified and not depend on tiny node detail.

Marketing material concepts:

- Channel: X/LinkedIn carousel showing artist to city to room to launch story. CTA: "Try the static pilot." Measurement: carousel completion and pilot clicks.
- Channel: Venue operator email graphic with one city graph and three recommendation states. CTA: "Send us a launch brief." Measurement: replies.
- Channel: SR007 deck visual language. CTA: "See the decision surface." Measurement: demo opens after deck.

Style-guide artifacts beyond swatches: Graph motif rules, approved node density, image overlay recipes, city-map crop examples, forbidden surveillance examples.

Merch/real-world extension: Poster series for fictional first-city launches with route lines and semantic decision stamps.

Best fit if: Vibelytics wants to own the live-culture strategy space and feel more culturally native than pure B2B software.

## Direction 3: First Yes

Positioning snapshot: Vibelytics gives launch teams the first confident yes, or the useful no, before spend hardens.

Audience and category: Founders, promoters, venue owners, brand partners, and creators who need alignment before committing budget and reputation.

Personality tension: Human conviction versus disciplined restraint. It should feel premium, emotional, and decisive, but never hype-driven.

Visual territory rationale: The most campaign-ready direction. It centers on the decision moment and makes "Go / Adjust / Hold" the memorable brand device.

Logo concept: Keep the V mark, but pair it with a three-state decision stripe that can appear in campaigns, decks, and merchandise.

Logo construction logic and source strategy: SVG mark plus a separate decision-stripe asset. The stripe is not part of the core logo and must not replace the mark.

Wordmark concept: Stable wordmark with optional campaign lockup: "Vibelytics / First Yes".

Lockups and usage notes: Core product lockup stays Vibelytics. Campaign lockups may add "First Yes" only in marketing or deck contexts.

Color palette:

- Primary: black stage `#03040A`, white ink `#F8FBFF`, first-yes mint `#3CF2B5`
- Secondary: adjust gold `#F6C65B`, no-go coral `#FF6D5F`, violet accent `#A36AFF`
- Neutral: slate `#101827`, fog `#AAB6C8`, dim line `rgba(255,255,255,.1)`
- Semantic: go, adjust, no-go become hero-level campaign colors

Accessibility and contrast: Semantic colors must always be paired with text labels. Do not rely on color-only states in pilot cards, screenshots, or social graphics.

Typography: Punchier, shorter headlines. Campaign type can be huge and sparse; app type remains compact.

Icon/illustration/photo style: Real pre-show, backstage, empty-room, and first-drop moments. Less graph-heavy, more decision-stamp and launch-card language.

UI token direction: More emphasis on semantic state chips, decision cards, and output blocks. Keep gradients as accents, not global backgrounds.

Motion/interaction tone: State transitions feel like a call being made: quick flash, confident lock-in, no celebratory confetti.

Voice and microcopy: "Open the pilot. Make the call." "Do not launch this version." "Win the sponsor story." "Hold until the first allocation clears."

Social/avatar/favicon notes: Avatar stays core mark. Social headers can use the decision stripe and "First Yes" campaign lockup.

Marketing material concepts:

- Channel: Event industry social ad. CTA: "Make the call before spend." Measurement: pilot opens and email starts.
- Channel: Venue one-sheet. CTA: "Send a launch brief." Measurement: qualified inbound.
- Channel: Deck close slide. CTA: "Open the pilot." Measurement: live demo click.

Style-guide artifacts beyond swatches: Decision-state usage matrix, campaign lockup rules, semantic accessibility examples, launch-copy before/after examples.

Merch/real-world extension: Wristband or pass design with "GO / ADJUST / HOLD" stripes; notebook for launch planning with first-page decision grid.

Best fit if: Vibelytics wants a memorable campaign platform for the SR007 submission and early sales motion while preserving product seriousness.

## Recommendation

Choose Direction 1, Signal Desk, as the product identity backbone. It best protects Vibelytics from being mistaken for audience monitoring, emotion detection, or a generic cultural dashboard. Direction 2 can supply campaign imagery rules. Direction 3 can become the launch campaign layer after the source identity is stabilized.

## P0 / P1 Blockers

P0: Asset provenance is not complete for current public PNG imagery. Do not mark the brand system production-ready until source, usage rights, allowed uses, attribution, and open rights questions are resolved in `docs/design/asset-provenance.json`.

P1: No canonical editable logo source exists. Before future brand implementation, create and approve a deterministic SVG mark, then export favicons/social images from that source.

P1: No approved brand kit exists. After a territory is approved, create `docs/brand/brand-kit.md` with the chosen kit, rejected options, rationale, implementation checklist, and assets to preserve.

## Implementation Checklist After Approval

1. Confirm chosen territory.
2. Resolve or replace assets with unknown provenance.
3. Create `brand/vibelytics-mark.svg` and export raster derivatives.
4. Create `docs/brand/brand-kit.md`.
5. Consolidate shared tokens across `/` and `/pilot`.
6. Update social assets and screenshots only after identity source is approved.
7. Run `npm run build`, route checks, screenshot checks, and copy scans.

## Verification Commands Run

```bash
git status --short --branch
rg --files -g '!node_modules' -g '!dist' -g '!archive'
find docs -maxdepth 3 -type f -print
find brand assets -maxdepth 2 -type f -print
sips -g pixelWidth -g pixelHeight brand/*.png assets/*.png docs/assets/*.png
```

## Next Thread Note

Future Codex thread should ask the user to approve one territory. If no explicit approval is given, continue with strategy artifacts only and do not change logo, tokens, screenshots, or production UI.
