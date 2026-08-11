import unittest
from unittest.mock import patch

import tracker


class TestCalculateProgression(unittest.TestCase):
    def test_increase(self):
        self.assertAlmostEqual(tracker.calculate_progression(100, 110), 10.0)

    def test_decrease(self):
        self.assertAlmostEqual(tracker.calculate_progression(100, 90), -10.0)

    def test_no_change(self):
        self.assertAlmostEqual(tracker.calculate_progression(100, 100), 0.0)

    def test_zero_initial_returns_none(self):
        self.assertIsNone(tracker.calculate_progression(0, 50))


class TestAddExcersize(unittest.TestCase):
    def setUp(self):
        tracker.excersizes = {"monday": {}, "tuesday": {}, "wednesday": {},
                               "thursday": {}, "friday": {}, "saturday": {},
                               "sunday": {}}

    @patch("tracker.save_data")
    @patch("builtins.input", side_effect=["bench", "100", "8", "3", "n"])
    def test_adds_new_excersize(self, mock_input, mock_save):
        tracker.add_excersize("monday")
        logs = tracker.excersizes["monday"]["bench"]["logs"]
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0], {"date": logs[0]["date"], "weight": 100.0, "reps": 8, "sets": 3})

    @patch("tracker.save_data")
    @patch("builtins.input", side_effect=["bench", "abc", "100", "8", "3", "n"])
    def test_rejects_invalid_weight_then_accepts(self, mock_input, mock_save):
        tracker.add_excersize("monday")
        logs = tracker.excersizes["monday"]["bench"]["logs"]
        self.assertEqual(logs[0]["weight"], 100.0)

    @patch("tracker.save_data")
    @patch("builtins.input", side_effect=[
        "bench", "100", "8", "3", "y",
        "bench", "y", "110", "same", "4", "n",
    ])
    def test_duplicate_confirm_appends_new_log_entry(self, mock_input, mock_save):
        tracker.add_excersize("monday")
        logs = tracker.excersizes["monday"]["bench"]["logs"]
        self.assertEqual(len(logs), 2)
        self.assertEqual(logs[1]["weight"], 110.0)
        self.assertEqual(logs[1]["reps"], 8)
        self.assertEqual(logs[1]["sets"], 4)


if __name__ == "__main__":
    unittest.main()