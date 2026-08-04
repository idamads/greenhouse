# Greenhouse Climate Dashboard

A lightweight Flask application for monitoring greenhouse climate conditions.

The dashboard simulates environmental sensors and provides a convenient web interface for observing greenhouse health in real time.

---

## Features

- Real-time climate dashboard
- Temperature monitoring
- Humidity tracking
- Light intensity monitoring
- CO₂ concentration display
- Automatic sensor simulation
- Climate status indicators
- Historical data storage
- REST API endpoints
- Responsive interface

---

## Technologies

- Python 3
- Flask
- HTML5
- CSS3
- Vanilla JavaScript

---

## Project Structure

```
greenhouse-climate-dashboard/
│
├── src/
├── templates/
├── static/
├── data/
├── tests/
└── docs/
```

---

## Installation

```bash
git clone https://github.com/yourname/greenhouse-climate-dashboard.git

cd greenhouse-climate-dashboard

python -m venv venv
```

Activate the environment.

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

Open your browser.

```
http://127.0.0.1:5000
```

---

## Dashboard Metrics

| Metric | Unit |
|---------|------|
| Temperature | °C |
| Humidity | % |
| Light | lux |
| CO₂ | ppm |

---

## Example JSON

```json
{
    "temperature": 23.7,
    "humidity": 58,
    "light": 640,
    "co2": 520
}
```

---

## Future Improvements

- MQTT integration
- Real sensor support
- CSV export
- User authentication
- Mobile dashboard
- Charts with historical trends
- Email notifications

---

## License

MIT
