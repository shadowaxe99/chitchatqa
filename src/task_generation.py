```python
import datetime
from typing import List, Dict
from task_management_library import TaskManager

class TaskGenerator:
    def __init__(self):
        self.task_manager = TaskManager()

    def generate_task(self, user_input: str, bot_response: str) -> Dict:
        """
        Generate a task based on user input and bot response.
        """
        task = {
            'user_input': user_input,
            'bot_response': bot_response,
            'created_at': datetime.datetime.now(),
            'status': 'pending'
        }
        return task

    def add_task_to_list(self, task: Dict) -> None:
        """
        Add a task to the task list.
        """
        self.task_manager.add_task(task)

    def generate_and_add_task(self, user_input: str, bot_response: str) -> None:
        """
        Generate a task and add it to the task list.
        """
        task = self.generate_task(user_input, bot_response)
        self.add_task_to_list(task)

    def get_task_list(self) -> List[Dict]:
        """
        Get the current task list.
        """
        return self.task_manager.get_tasks()

    def set_task_status(self, task_id: int, status: str) -> None:
        """
        Set the status of a task.
        """
        self.task_manager.set_task_status(task_id, status)
```