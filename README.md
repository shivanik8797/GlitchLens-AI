# GlitchLens AI

GlitchLens AI is an operations-investigation MVP for authorized business data. It detects payment and workflow anomalies, explains the evidence, recommends actions, and records human decisions.

## Repository layout

- `frontend/` — React + Vite user interface.
- `backend/` — FastAPI API, CSV ingestion, detection and scoring.
- `shared/` — API contracts, CSV templates and sample datasets used by both contributors.
- `docs/` — setup, architecture, task ownership and integration notes.

## MVP user journey

1. A business user signs in and selects an organization.
2. The user uploads an authorized payment, settlement or workflow CSV.
3. The backend validates and normalizes the records.
4. Detection rules identify suspicious patterns.
5. The dashboard shows evidence, severity and a Glitch Score.
6. The user reviews and approves/rejects a recommendation.

## Quick start

See:
- [Frontend setup](frontend/README.md)
- [Backend setup](backend/README.md)
- [Task split](docs/TASK_SPLIT.md)
- [API contract](shared/contracts/API_CONTRACT.md)
- [CSV formats](shared/contracts/CSV_FORMATS.md)

## Security rules

- Never collect UPI PINs, OTPs, CVVs, full card numbers, bank passwords or payment-app credentials.
- Only upload data the organization is authorized to share.
- Do not expose Supabase service-role keys in the browser or commit secrets.
- Validate CSV content on the backend; browser MIME checks are not sufficient.
- Treat pending transactions separately from failed transactions.
- Label all generated/demo records clearly as simulated.
- Do not claim PCI DSS, RBI or DPDP compliance without an actual assessment.

## Current status

This is a project scaffold, not a finished application. Add implementation incrementally and keep the API contract in `shared/contracts/API_CONTRACT.md` synchronized between frontend and backend.
