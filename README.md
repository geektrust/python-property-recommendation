This is the starter kit for the problem statement defined for interface.ai's Data Engineer role

## Problem Statement

### Multi-tenant Windowed Aggregation

Your team runs a multi-tenant data platform that receives a stream of
transaction events from different customers (tenants).
Each event has the following fields:
```
{
    "tenant_id": str,
    "user_id": str,
    "event_time": str, # ISO-8601 in UTC, e.g. "2025-01-01T10:03:21Z"
    "amount": float,
}
```
You are given an iterable of events. You need to group events into tumbling
time windows and compute per-tenant aggregates.

#### Requirements:
1. Use tumbling time windows of fixed length `window_minutes` in UTC.
2. For each event:
- Parse event_time as a UTC timestamp.
- Assign the event to a window based on its timestamp.
3. Windows are half-open intervals: window_start <= event_time < window_end
Example with 15-minute windows:
- 10:00:00Z – 10:15:00Z
- 10:15:00Z – 10:30:00Z
- 10:30:00Z – 10:45:00Z
4. Window calculation:
- window_start is truncated down to the nearest multiple of window_minutes
since the Unix epoch.
- window_end = window_start + window_minutes
5. Aggregate per (tenant_id, window). For each combination, compute:
- tenant_id: str
- window_start: ISO-8601 UTC string, e.g. "2025-01-01T10:00:00Z"
- window_end: ISO-8601 UTC string
- event_count: number of events
- unique_users: number of distinct user_id values
- total_amount: sum of amount
- avg_amount_per_event: total_amount / event_count (or 0.0 if no events)
6. Return a list of dictionaries with exactly these keys:
    ```
    {
        "tenant_id": str,
        "window_start": str,
        "window_end": str,
        "event_count": int,
        "unique_users": int,
        "total_amount": float,
        "avg_amount_per_event": float,
    }
    ```
7. Sort output by: tenant_id ascending, then window_start ascending.
Assumptions:
- event_time is always valid in format "%Y-%m-%dT%H:%M:%SZ"
- amount can be safely cast to float