# Backend

FastAPI + Pandas + Pydantic + Supabase/PostgreSQL.

## Suggested setup (PowerShell)

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Create `.env` from `.env.example` before running.

## Security

Verify Supabase access tokens and organization membership for every protected request. Do not trust client-supplied organization IDs. Never put service-role credentials in frontend code.
