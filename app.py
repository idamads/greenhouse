from flask import Flask

from src.dashboard import dashboard

app = Flask(__name__)
app.config.from_pyfile("config.py")

app.register_blueprint(dashboard)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Greenhouse Climate Dashboard"
    }


if __name__ == "__main__":
    app.run(debug=True)
