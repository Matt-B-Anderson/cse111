import datetime
from unittest.mock import patch
import emotional_state_tracker

emotions = ["happy", "anxious", "happy", "sad", "excited", "happy", "tired"]
base_date = datetime.date(2025, 4, 10)

for i, emotion in enumerate(emotions):
    fake_date = base_date + datetime.timedelta(days=i)
    with patch("builtins.input", return_value=emotion), \
        patch("emotional_state_tracker.get_today_date", return_value=fake_date):
        emotional_state_tracker.log_emotions()
