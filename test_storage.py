import os
import unittest

import storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.original_data_file = storage.DATA_FILE
        storage.DATA_FILE = "test_workouts_temp.json"

    def tearDown(self):
        if os.path.exists(storage.DATA_FILE):
            os.remove(storage.DATA_FILE)
        storage.DATA_FILE = self.original_data_file

    def test_save_and_load_round_trip(self):
        data = {"monday": {"bench": {"logs": [{"date": "2026-01-01", "weight": 100, "reps": 8, "sets": 3}]}}}
        storage.save_data(data)
        self.assertEqual(storage.load_data(), data)

    def test_load_missing_file_returns_none(self):
        self.assertIsNone(storage.load_data())

    def test_load_empty_file_returns_none(self):
        with open(storage.DATA_FILE, "w") as f:
            f.write("")
        self.assertIsNone(storage.load_data())

    def test_load_corrupted_file_returns_none(self):
        with open(storage.DATA_FILE, "w") as f:
            f.write("{not valid json")
        self.assertIsNone(storage.load_data())


if __name__ == "__main__":
    unittest.main()