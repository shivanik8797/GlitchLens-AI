# Architecture

```text
React + Vite
  | Supabase Auth (browser publishable key)
  | HTTPS API requests with user access token
  v
FastAPI
  | verify JWT + authorize organization membership/role
  | validate and normalize CSVs
  | detection + scoring + recommendations
  v
Supabase PostgreSQL + private Storage
```

## Main modules

- Payments: failure spikes, pending anomalies, method/route patterns.
- Settlements: missing/mismatched/delayed settlement records.
- Workflows: delayed approvals, long-running tasks and handoff delays.
- Investigation: evidence, possible causes, recommended action and human decision.

## Important boundaries

The frontend is not trusted for authorization or data validation. The backend must verify the user token and membership for every organization-scoped operation. Supabase RLS is an additional boundary, not a replacement for backend authorization.
