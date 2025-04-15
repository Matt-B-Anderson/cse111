from datetime import date
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import emotional_state_tracker as tracker

class TestEmotionalStateTracker(unittest.TestCase):

    def test_log_emotions(self):
        """Test that logging an emotion writes the correct date and emotion to the log file."""
        fixed_date = date(2025, 1, 1)
        test_emotion = "happy"
        expected_date_str = fixed_date.isoformat()
        m = mock_open()

        with patch.object(tracker, 'get_today_date', return_value=fixed_date), \
            patch('builtins.open', m), \
            patch('builtins.input', return_value=test_emotion):
            result = tracker.log_emotions()

        m.assert_called_once_with("emotion_log.txt", "a")
        handle = m()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn(expected_date_str, written_content)
        self.assertIn(test_emotion, written_content)
        self.assertIsNone(result)

    def test_calculate_emotion_stats(self):
        """Test that emotion statistics are calculated correctly from the log data."""
        sample_content = "2025-01-01,happy\n2025-01-01,sad\n2025-01-02,happy\n"
        m = mock_open(read_data=sample_content)

        with patch('builtins.open', m):
            stats = tracker.calculate_emotion_stats()

        m.assert_called_once_with("emotion_log.txt", "r")
        self.assertIsInstance(stats, dict)
        self.assertEqual(len(stats), 2)
        self.assertEqual(stats.get("happy"), 2)
        self.assertEqual(stats.get("sad"), 1)

    def test_load_emotion_data(self):
        """Test that loading emotion data returns the correct list of date/emotion entries."""
        sample_content = "2025-01-01,happy\n2025-01-02,sad\n"
        m = mock_open(read_data=sample_content)

        with patch('builtins.open', m):
            data = tracker.load_emotion_data()

        m.assert_called_once_with("emotion_log.txt", "r")
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], (date(2025, 1, 1), "happy"))
        self.assertEqual(data[1], (date(2025, 1, 2), "sad"))

    def test_get_user_input(self):
        """Test that get_user_input() returns the user input string and uses the correct prompt."""
        user_input_value = "Calm"
        prompt_text = "How are you feeling today? "

        with patch('builtins.input', return_value=user_input_value) as mock_input:
            result = tracker.get_user_input(prompt_text)
            mock_input.assert_called_once_with(prompt_text)

        self.assertEqual(result, user_input_value)

    def test_log_emotions_rejects_numeric(self):
        """Test that log_emotions() rejects emotion inputs containing numbers."""
        invalid_inputs = ["sad2", "123"]
        for bad_emotion in invalid_inputs:
            with patch('builtins.input', return_value=bad_emotion), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = tracker.log_emotions()
                output = mock_stdout.getvalue()
                self.assertIn("Invalid input. Emotion must not contain numbers.", output)
                self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()