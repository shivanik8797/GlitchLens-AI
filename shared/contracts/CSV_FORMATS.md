# CSV formats

Use UTF-8 CSV with a header row. Backend validation is authoritative. Avoid personal identifiers unless necessary and authorized.

## Payments

Required columns:
- `transaction_ref`
- `amount`
- `currency`
- `payment_method`
- `status` (`SUCCESS`, `FAILED`, `PENDING`)
- `timestamp`

Optional:
- `merchant_ref` (pseudonymous preferred)
- `error_code`
- `route`

## Settlements

Required:
- `transaction_ref`
- `settlement_amount`
- `settlement_status` (`SETTLED`, `PENDING`, `FAILED`)
- `settlement_time`

## Workflows

Required:
- `task_ref`
- `team_name`
- `event_type`
- `status`
- `created_time`

Optional:
- `completed_time`
- `approval_time`
- `meeting_hours`

Never include UPI PIN, OTP, CVV, full card number, bank passwords or payment-app credentials.
