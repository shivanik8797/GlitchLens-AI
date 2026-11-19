# API contract (initial proposal)

Base URL: `/api/v1`

All organization-scoped endpoints require:
`Authorization: Bearer <Supabase access token>`

The backend must derive/verify the user from the token and verify membership in the requested organization. Never trust an `organization_id` by itself.

## Endpoints

### `GET /health`
Response:
```json
{ "status": "ok", "service": "glitchlens-api" }
```

### `POST /organizations`
Request:
```json
{ "name": "Example Business" }
```
Response:
```json
{ "id": "uuid", "name": "Example Business", "role": "owner" }
```

### `POST /datasets/upload`
Multipart fields:
- `file`: CSV file
- `organization_id`: UUID
- `category`: `payments` | `settlements` | `workflows`

Response:
```json
{
  "dataset_id": "uuid",
  "category": "payments",
  "status": "processed",
  "row_count": 120
}
```

### `GET /organizations/{organization_id}/dashboard`
Response:
```json
{
  "payment_health": {
    "total": 120,
    "successful": 105,
    "failed": 10,
    "pending": 5,
    "failure_rate": 8.33
  },
  "open_glitches": 2,
  "critical_glitches": 1
}
```

### `GET /organizations/{organization_id}/glitches`
Response:
```json
{
  "items": [
    {
      "id": "uuid",
      "module": "payments",
      "title": "Payment failure spike",
      "description": "Failure rate is above the historical baseline.",
      "severity": "high",
      "glitch_score": 82,
      "status": "open",
      "evidence": {
        "current_failure_rate": 15.0,
        "baseline_failure_rate": 2.0,
        "sample_size": 100
      },
      "possible_causes": ["A payment route may be experiencing elevated errors."],
      "recommended_action": "Review the affected payment method and route."
    }
  ]
}
```

### `POST /glitches/{glitch_id}/decision`
Request:
```json
{ "decision": "approved", "notes": "Escalated to payment operations." }
```
Response:
```json
{ "status": "recorded", "decision": "approved" }
```

## Contract rules

- Dates/times use ISO 8601 with timezone.
- Monetary values use decimal strings or numeric values with explicit currency; never silently mix currencies.
- `pending` is not `failed`.
- Include evidence and sample size for every detection.
- Possible causes must be framed as hypotheses, not confirmed root causes.
- Errors should use a consistent shape:
```json
{ "detail": "Human-readable explanation", "code": "VALIDATION_ERROR" }
```
This is an initial contract. If changed, both contributors must update this file and coordinate before implementation.
