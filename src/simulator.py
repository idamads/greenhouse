import random


class ClimateSimulator:

    def __init__(self):

        self.temperature = random.uniform(20, 25)
        self.humidity = random.uniform(50, 65)
        self.light = random.uniform(400, 700)
        self.co2 = random.uniform(450, 700)

    def generate(self):

        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-2.0, 2.0)
        self.light += random.uniform(-40, 40)
        self.co2 += random.uniform(-20, 20)

        self.temperature = min(max(self.temperature, 12), 38)
        self.humidity = min(max(self.humidity, 20), 90)
        self.light = min(max(self.light, 0), 1200)
        self.co2 = min(max(self.co2, 250), 1800)

        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "light": self.light,
            "co2": self.co2
        }

    def reset(self):

        self.__init__()
