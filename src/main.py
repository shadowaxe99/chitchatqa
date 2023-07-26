```python
import sys
from PyQt5.QtWidgets import QApplication

from chat2code_integration import integrate_chat2code
from gpt_model import GPTModel
from real_time_responses import RealTimeResponses
from task_generation import TaskGenerator
from task_adjustment import TaskAdjuster
from input_logging import InputLogger
from user_preferences import UserPreferences
from task_reminders import TaskReminder
from interface import Interface
from data_security import DataSecurity
from database import Database

class AIChatbotAssistant:
    def __init__(self):
        self.chat2code = integrate_chat2code()
        self.gpt_model = GPTModel()
        self.real_time_responses = RealTimeResponses(self.chat2code, self.gpt_model)
        self.task_generator = TaskGenerator()
        self.task_adjuster = TaskAdjuster()
        self.input_logger = InputLogger()
        self.user_preferences = UserPreferences()
        self.task_reminder = TaskReminder()
        self.data_security = DataSecurity()
        self.database = Database()
        self.interface = Interface(self.real_time_responses, self.task_generator, self.task_adjuster, self.input_logger, self.user_preferences, self.task_reminder)

    def run(self):
        self.interface.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ai_chatbot_assistant = AIChatbotAssistant()
    ai_chatbot_assistant.run()
    sys.exit(app.exec_())
```