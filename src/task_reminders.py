```python
import time
from threading import Timer
from src.user_preferences import get_user_preferences
from src.database import get_pending_tasks

def remind_task():
    user_preferences = get_user_preferences()
    reminder_interval = user_preferences.get('reminder_interval', 60)  # Default to 60 minutes if not set

    while True:
        pending_tasks = get_pending_tasks()
        for task in pending_tasks:
            print(f"Reminder: You have a pending task: {task['name']}")
        time.sleep(reminder_interval * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    remind_task()
```