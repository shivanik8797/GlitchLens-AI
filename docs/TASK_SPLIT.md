# Two-person task split

Use two separate work areas and integrate through the shared API contract. Do not have both people edit the same files unless agreed first.

## Person 1 — Frontend owner

**Owns:** everything inside `frontend/`.

Deliverables:
1. React + Vite + Tailwind app shell and routing.
2. Login/signup screens and organization selection/creation UI.
3. Dashboard layout, KPI cards, charts and glitch list.
4. CSV upload screens with category selection (payments, settlements, workflows).
5. Glitch investigation detail page with evidence and possible causes.
6. Recommendation approve/reject UI and action history.
7. Loading, empty, validation and API-error states.
8. Supabase browser client using only the publishable/anon key.
9. Responsive styling and final demo flow.

**Do not:** implement detection logic in the browser, put service-role credentials in frontend, or invent API response fields. Follow `shared/contracts/API_CONTRACT.md`.

## Person 2 — Backend + data owner

**Owns:** everything inside `backend/` and the Supabase SQL/migrations documented under `docs/`.

Deliverables:
1. FastAPI app, configuration and health endpoint.
2. Supabase JWT verification and organization/role authorization.
3. CSV upload validation, parsing and normalization.
4. Payment failure-rate spike detection.
5. Pending transaction monitoring (separate from failures).
6. Settlement mismatch detection.
7. Workflow delay/bottleneck detection (if time allows).
8. Glitch Score, evidence payload and recommendation generation.
9. API endpoints matching the shared contract.
10. Backend tests, retention/deletion workflow and audit events.

**Do not:** trust organization IDs supplied by the browser without authorization, expose privileged keys, or treat a pending payment as failed.

## Shared work — both people

| Task | Person 1 | Person 2 |
|---|---|---|
| Agree API request/response shapes | Review | Define |
| Supabase project + schema | Auth UI/client | Schema, policies, verification |
| CSV template examples | Upload UI | Parser/validation |
| Integration testing | Test UI/API | Test API/UI |
| Tenant isolation test with two users | Participate | Lead |
| Demo preparation | UI walkthrough | Prepare labelled sample data |
| Bug fixing | Frontend bugs | Backend/data bugs |

## Suggested 12-hour schedule

- Hour 0–1: both agree contract, create branches, run both apps.
- Hours 1–3: Person 1 builds app shell/auth screens; Person 2 builds FastAPI, Supabase verification and health route.
- Hours 3–5: Person 1 builds upload/dashboard UI; Person 2 builds CSV ingestion and database writes.
- Hours 5–7: Person 1 builds glitch detail/recommendation UI; Person 2 builds detection and scoring.
- Hours 7–9: integrate APIs and fix contract mismatches.
- Hours 9–10: test tenant boundaries, malformed CSVs and empty states.
- Hours 10–12: polish one end-to-end demo, prepare labelled sample data and rehearse.

## Git collaboration

Recommended branches:
- `main` — stable demo branch.
- `frontend` — Person 1's work.
- `backend` — Person 2's work.

Each person commits only their owned folders plus agreed shared files. Open pull requests into `main`; integrate early rather than waiting until the end.

Suggested commit prefixes:
- `feat(frontend): ...`
- `feat(backend): ...`
- `fix: ...`
- `docs: ...`

## Definition of done for the demo

A judge can sign in, create/select an organization, upload a payment CSV, see a detected issue with evidence and score, inspect a recommendation, and approve/reject it. Workflow analysis is a secondary demonstration if time remains.
