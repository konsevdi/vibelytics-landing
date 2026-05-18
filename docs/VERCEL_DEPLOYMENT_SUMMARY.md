# Vercel Deployment Summary

## What changed

- Replaced the root page with a clean Vibelytics SR007 landing page at `/`.
- Moved the interactive launch-copilot pilot to `/pilot`.
- Reused the existing CSS rounded-square gradient `V` logo direction.
- Kept the site static-only: local HTML, CSS, JavaScript, and image assets; no backend, API routes, package installs, or external service dependencies.
- Preserved the dark premium pilot interface and launch-copilot workflow:
  - artist / city / venue / date / sponsor input
  - demand score
  - pricing and capacity plan
  - sponsor fit
  - launch recommendation
  - launch copy
- Removed old non-goal positioning from the served pages so the site stays focused on pre-launch decisions.

## Local verification

- Started the static server with `npm run start`.
- Verified `http://127.0.0.1:3000/`.
- Verified `http://127.0.0.1:3000/pilot`.
- Checked desktop viewport at `1440 x 1100`.
- Checked mobile viewport at `390 x 900`.
- Confirmed no horizontal overflow on landing or pilot pages.
- Confirmed pilot interaction updates outputs:
  - Lisbon updates demand score to `90` and headline to `Lisbon is the asymmetric first-city bet.`
  - Berlin updates launch recommendation to `Adjust`.
- Captured screenshots:
  - `docs/assets/vibelytics-landing-screenshot.png`
  - `docs/assets/vibelytics-pilot-screenshot.png`

## Available checks

- `package.json` only defines `start`.
- No build script is present.
- No lint script is present.
- Static page copy scan passed for the served HTML pages.

## Vercel project/link status

- Local `.vercel/project.json` is not present.
- `vercel` / `vc` CLI is not installed on PATH.
- Vercel MCP deployment tools were not available in this Codex session.
- The intended GitHub repository provided by the user is `konsevdi/vibelytics-landing`.
- Because the local folder is not linked to a Vercel project, the exact existing Vercel project identity could not be confirmed from this workspace.

## Deployment URL

- Not deployed from this session.

## Remaining manual steps

1. Confirm in Vercel that the existing a16z application project is connected to `konsevdi/vibelytics-landing`.
2. If it is the correct project, deploy this static site to that project.
3. If using the Vercel CLI, link explicitly to the confirmed project before deploying:

```bash
vercel link --yes --project <confirmed-project-name-or-id> --scope <team-or-user-scope>
vercel --prod
```

Do not deploy until the Vercel project name, scope, and GitHub repository connection are confirmed.
