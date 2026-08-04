import random

from .simulator import ClimateSimulator


class SensorManager:

    def __init__(self):
        self.simulator = ClimateSimulator()

    def read(self):

        simulated = self.simulator.generate()

        return {
            "temperature": round(simulated["temperature"], 1),
            "humidity": round(simulated["humidity"], 1),
            "light": int(simulated["light"]),
            "co2": int(simulated["co2"]),
            "signal": random.randint(95, 100)
        }
