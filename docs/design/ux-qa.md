# Vibelytics Static V2 Future-Relative Target-Date UX QA

Last updated: 2026-08-31
Status: `SV2-DATE-002` passed local UX QA; production monitoring remains tied to shipped commit `a3c0a36`.

## Routes And Journey Reviewed

- `/`: hero to example decisions, decision-reading guidance, good-fit/not-fit qualification, launch brief checklist, and `/pilot` CTA.
- `/pilot`: scenario inputs, generated recommendation, scenario-confidence framing, decision interpretation, recommendation-specific validation guidance, email readiness, rationale, assumptions, intake next step, copy/download/share/email actions, and query-state restoration.
- Production surfaces: canonical `https://www.vibelytics.ai/pilot/` and `https://vibelytics-landing.vercel.app/pilot`.
- Primary journey: self-qualify, open a fresh six-weeks-ahead brief or restore an explicit dated scenario, understand the preview boundary, generate a launch decision, and create a date-consistent share/email artifact.

## Viewport Matrix

| Viewport | `/` | `/pilot` | Result |
| --- | --- | --- | --- |
| 1440 × 960 | Preserved by byte-identical route parity | Fresh/default and explicit-date browser/artifact QA on canonical and Vercel | Pass |
| 390 × 844 | Preserved by byte-identical route parity | Fresh/default and explicit-date browser/artifact QA on canonical and Vercel | Pass |

No screenshots or approved repo assets were regenerated for this logic-only reconciliation. Browser state, DOM values, encoded email artifacts, action status, console output, image completion, and overflow were inspected directly.

## Interaction And State Matrix

| State or action | Evidence | Result |
| --- | --- | --- |
| Default Go scenario | Requires venue terms, full room economics, ticket evidence, sponsor commitments, and deadline confirmation before committing | Pass |
| Mira K / London / 2,000-3,000 cap / Fashion | Adjust names room, release, economics, ticket gate, sponsor, and timing variables to change or verify | Pass |
| Mira K / London / 5,000-7,000 cap / Fashion | Do Not Launch requires a lower-risk room, reduced exposure, staged inventory, buyer evidence, and confirmed partner terms before reconsideration | Pass |
| Copy/download/email artifact | The shared `currentBriefText` path includes the matching validation section, scenario confidence, how-to-read guidance, email readiness, assumptions, and share link; copy and download actions returned their success states and the email body contained the same generated brief | Pass |
| Query-state restore | Selected 6,000-cap scenario restores after URL navigation | Pass |
| Fresh target date | On 2026-07-29, both production surfaces selected `2026-09-09`, exactly 42 calendar days ahead | Pass |
| Explicit target date | `date=2026-08-15` restored unchanged on canonical and Vercel | Pass |
| Share/email date consistency | Encoded email bodies contained the selected `Target date` and a share URL with the same date; `Copy share link` reported success | Pass |
| Invalid calendar date | `date=2026-99-99` preserves the computed `2026-10-12` default and keeps email/share artifacts aligned | Pass locally |
| Leap-year boundary | `2028-02-29` restores exactly; invalid `2027-02-29` preserves the computed default | Pass locally |
| All scenario inputs | Artist, city, capacity, budget, date, timeline, sponsor, ticketing, goal, and risk updated generated state and URL parameters | Pass |
| Console | No browser warnings or errors on the production checks | Pass |

## Accessibility And Responsive Notes

- The new homepage guidance uses a semantic section, heading, articles, and an explicit accessible label.
- The generated pilot interpretation and validation threshold remain text, not color-only meaning, and update with the existing generated state.
- Existing keyboard-native controls and visible focus behavior are preserved.
- No horizontal overflow or broken route images were found at either viewport.
- The runtime date default and valid query restoration use the existing native date control and do not alter focus order, labels, keyboard behavior, or semantic structure.
- The existing mobile pilot navigation exceeded the browser-visible content width by 14 pixels during QA; tighter mobile-only link spacing resolved the overflow without changing labels or hierarchy.
- Long bounded recommendation and validation copy wraps within the existing output panel on desktop and narrow mobile.

## Visual Fidelity And Asset Notes

- The new pilot block reuses the existing highlighted result treatment, Signal Desk tokens, borders, spacing, and typography without introducing a new component family.
- No images were added, regenerated, recropped, or replaced. Asset provenance is unchanged.
- The homepage is unchanged; how-to-read guidance, qualification, and launch checklist remain in their existing order.
- The pilot block sits directly after `How to read this decision` and before email readiness, preserving the decision-to-email path.
- No visual drift affecting comprehension, trust, readability, or the primary CTA was found.

## Prioritized Punch List And Fixes

- P1 resolved: recommendation interpretation did not name the concrete evidence or re-scope that should change the preview direction. The new three-state validation guidance supplies that handoff threshold.
- P1 resolved: copied, downloaded, and emailed artifacts now carry the same recommendation-specific validation guidance as the visible output.
- P1 resolved during responsive QA: the four pilot navigation links caused narrow-browser horizontal overflow; mobile spacing was tightened and rechecked at 390 × 844.
- P2 accepted: synthetic numeric scores remain intentionally prominent because the preview demonstrates the decision surface; their meaning is now clearly bounded in adjacent copy.
- P2 resolved locally: query restoration validates Gregorian month lengths and leap years before replacing the computed default.

## Taste Delta

- Closest to target: the new guidance turns the recommendation into a short validation handoff without making the output read like a report.
- Changed since the prior pass: fresh target dates now stay future-relative while valid explicit shared dates remain stable.
- Do not disturb: good-fit/not-fit qualification, launch brief checklist, email-ready intake flow, pure Vibelytics route policy, and current assets.
- Next: after deployment, repeat canonical/Vercel parity plus valid, invalid, share, and email date checks before claiming production success.

## Gate Decision

- P0 blockers: none.
- P1 blockers: none for local implementation.
- Production status: current monitoring pass for commit `a3c0a36`; canonical and Vercel route HTML matched the committed files byte-for-byte.
- Local build and evidence validation: pass; product change is limited to the calendar-date guard in `pilot/index.html`.
- Production UX QA: pass at 1440 × 960 and 390 × 844 for the future-relative default, valid explicit query restoration, share/email date consistency, asset resolution, clean console output, and zero horizontal overflow.
- Gate distinction: this is a production-monitoring pass for the shipped date change, not a new global aesthetic or brand signoff.
- `SV2-DATE-002` local UX QA: pass for fresh, valid, impossible, valid-leap, and invalid-leap dates; production status is pending deployment and re-verification.
