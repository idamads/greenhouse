import unittest

from src.storage import Storage


class StorageTest(unittest.TestCase):

    def setUp(self):
        self.storage = Storage()
        self.storage.clear()

    def test_empty_history(self):

        self.assertEqual(
            self.storage.history(),
            []
        )

    def test_save(self):

        sample = {
            "temperature": 22,
            "humidity": 60,
            "light": 550,
            "co2": 620,
            "signal": 99
        }

        self.storage.save(sample)

        history = self.storage.history()

        self.assertEqual(len(history), 1)
        self.assertEqual(
            history[0]["temperature"],
            22
        )

    def test_latest(self):

        sample = {
            "temperature": 24,
            "humidity": 57,
            "light": 640,
            "co2": 580,
            "signal": 98
        }

        self.storage.save(sample)

        latest = self.storage.latest()

        self.assertIsNotNone(latest)
        self.assertEqual(latest["co2"], 580)


if __name__ == "__main__":
    unittest.main()
