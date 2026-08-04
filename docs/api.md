# REST API

## GET /

Returns the dashboard page.

---

## GET /health

Response

```json
{
    "status": "ok",
    "service": "Greenhouse Climate Dashboard"
}
```

---

## GET /api/climate

Returns current greenhouse conditions.

Example

```json
{
    "status": "success",
    "data": {
        "temperature": 23.4,
        "humidity": 58,
        "light": 610,
        "co2": 640,
        "signal": 99
    },
    "alerts": []
}
```

---

## GET /api/history

Returns previously recorded measurements.

Example

```json
{
    "history": [
        {
            "timestamp": "2026-08-04T14:30:11",
            "temperature": 23.1,
            "humidity": 57,
            "light": 598,
            "co2": 621,
            "signal": 98
        }
    ]
}
```

## Status Codes

| Code | Description |
|------|-------------|
| 200 | Successful request |
| 404 | Endpoint not found |
| 500 | Internal server error |
