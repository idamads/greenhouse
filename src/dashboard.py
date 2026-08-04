from flask import Blueprint, jsonify, render_template

from .sensors import SensorManager
from .alerts import AlertManager
from .storage import Storage

dashboard = Blueprint("dashboard", __name__)

sensors = SensorManager()
storage = Storage()
alerts = AlertManager()


@dashboard.get("/")
def index():
    return render_template("index.html")


@dashboard.get("/api/climate")
def climate():

    data = sensors.read()

    storage.save(data)

    return jsonify({
        "status": "success",
        "data": data,
        "alerts": alerts.evaluate(data)
    })


@dashboard.get("/api/history")
def history():

    return jsonify({
        "history": storage.history()
    })
