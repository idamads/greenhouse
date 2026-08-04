from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "greenhouse.json"

SECRET_KEY = "greenhouse-dashboard-demo"

REFRESH_INTERVAL = 5

CLIMATE_LIMITS = {
    "temperature": {
        "min": 18,
        "max": 28
    },
    "humidity": {
        "min": 45,
        "max": 70
    },
    "light": {
        "min": 250,
        "max": 900
    },
    "co2": {
        "min": 400,
        "max": 1000
    }
}
