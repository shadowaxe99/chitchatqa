```python
from task_management_library import TaskManager
from database import Database

class TaskAdjustment:
    def __init__(self):
        self.task_manager = TaskManager()
        self.db = Database()

    def adjust_task(self, task_id, new_priority=None, new_status=None):
        task = self.task_manager.get_task(task_id)
        if not task:
            return "Task not found"

        if new_priority:
            task.priority = new_priority
        if new_status:
            task.status = new_status

        self.task_manager.update_task(task)
        self.db.update_task(task)

        return "Task updated successfully"

    def adjust_task_based_on_chatbot_interaction(self, chatbot_response):
        tasks_to_adjust = self.db.get_tasks_based_on_chatbot_response(chatbot_response)
        for task in tasks_to_adjust:
            self.adjust_task(task.id, new_priority=task.priority, new_status=task.status)

    def adjust_task_based_on_user_feedback(self, user_feedback):
        tasks_to_adjust = self.db.get_tasks_based_on_user_feedback(user_feedback)
        for task in tasks_to_adjust:
            self.adjust_task(task.id, new_priority=task.priority, new_status=task.status)
```