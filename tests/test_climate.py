import unittest

from src.climate import ClimateStatus


class ClimateStatusTest(unittest.TestCase):

    def test_temperature_optimal(self):
        self.assertEqual(
            ClimateStatus.temperature_state(22),
            "Optimal"
        )

    def test_temperature_low(self):
        self.assertEqual(
            ClimateStatus.temperature_state(10),
            "Cold"
        )

    def test_temperature_high(self):
        self.assertEqual(
            ClimateStatus.temperature_state(35),
            "Hot"
        )

    def test_humidity(self):
        self.assertEqual(
            ClimateStatus.humidity_state(55),
            "Optimal"
        )

    def test_light(self):
        self.assertEqual(
            ClimateStatus.light_state(600),
            "Optimal"
        )

    def test_co2(self):
        self.assertEqual(
            ClimateStatus.co2_state(700),
            "Optimal"
        )


if __name__ == "__main__":
    unittest.main()
