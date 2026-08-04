import unittest

from src.alerts import AlertManager


class AlertManagerTest(unittest.TestCase):

    def setUp(self):
        self.manager = AlertManager()

    def test_no_alerts(self):

        values = {
            "temperature": 22,
            "humidity": 55,
            "light": 500,
            "co2": 700
        }

        self.assertEqual(
            self.manager.evaluate(values),
            []
        )

    def test_temperature_alert(self):

        values = {
            "temperature": 34,
            "humidity": 55,
            "light": 500,
            "co2": 700
        }

        alerts = self.manager.evaluate(values)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["metric"], "temperature")

    def test_multiple_alerts(self):

        values = {
            "temperature": 35,
            "humidity": 20,
            "light": 100,
            "co2": 1500
        }

        alerts = self.manager.evaluate(values)

        self.assertEqual(len(alerts), 4)


if __name__ == "__main__":
    unittest.main()
