import unittest
from unittest.mock import patch, mock_open
import emotional_state_tracker as est
import datetime


class TestEmotionalStateTracker(unittest.TestCase):

    @patch("builtins.input", return_value="happy")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_emotions(self, mock_file, mock_input):
        est.log_emotions()
        today = datetime.date.today().isoformat()
        mock_file().write.assert_called_with(f"{today},happy\n")

    def test_load_emotion_data(self):
        mock_data = "2025-04-14,happy\n2025-04-15,sad\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            with patch("os.path.exists", return_value=True):
                data = est.load_emotion_data()
                self.assertEqual(len(data), 2)
                self.assertEqual(data[0][1], "happy")
                self.assertEqual(data[1][1], "sad")

    def test_get_user_input(self):
        with patch("builtins.input", return_value="excited"):
            self.assertEqual(est.get_user_input("Test: "), "excited")

    @patch("emotional_state_tracker.load_emotion_data")
    def test_calculate_emotion_stats(self, mock_load_data):
        mock_load_data.return_value = [
            (datetime.date(2025, 4, 14), "happy"),
            (datetime.date(2025, 4, 15), "happy"),
            (datetime.date(2025, 4, 16), "sad"),
        ]
        with patch("builtins.print") as mock_print:
            est.calculate_emotion_stats()
            mock_print.assert_any_call("Most Common Emotion: happy (2 times)")


if __name__ == "__main__":
    unittest.main()