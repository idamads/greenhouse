import json
from pathlib import Path
from datetime import datetime

from config import DATA_FILE


class Storage:

    def __init__(self):
        self.path = Path(DATA_FILE)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def save(self, data):

        history = self.history()

        history.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            **data
        })

        history = history[-100:]

        with self.path.open("w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def history(self):

        with self.path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def latest(self):

        history = self.history()

        if history:
            return history[-1]

        return None

    def clear(self):

        with self.path.open("w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
