```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListView, QInputDialog
from PyQt5.QtCore import Qt
from chat2code_integration import integrate_chat2code
from real_time_responses import generate_response
from task_generation import create_task
from task_adjustment import adjust_task
from user_preferences import set_preferences
from task_reminders import remind_task

class Chat2CodeAssistant(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.chatDisplay = QTextEdit()
        self.chatDisplay.setReadOnly(True)
        layout.addWidget(self.chatDisplay)

        self.taskListView = QListView()
        layout.addWidget(self.taskListView)

        self.settingsButton = QPushButton('Settings')
        self.settingsButton.clicked.connect(self.openSettings)
        layout.addWidget(self.settingsButton)

        self.setLayout(layout)

    def openSettings(self):
        preferences, ok = QInputDialog.getText(self, 'Preferences', 'Enter your preferences:')
        if ok:
            set_preferences(preferences)

    def updateChat(self, userInput, botResponse):
        self.chatDisplay.append("User: " + userInput)
        self.chatDisplay.append("Bot: " + botResponse)

    def updateTasks(self, tasks):
        self.taskListView.setModel(tasks)

    def remindTasks(self):
        reminders = remind_task()
        for reminder in reminders:
            self.chatDisplay.append("Reminder: " + reminder)

def main():
    app = QApplication(sys.argv)

    assistant = Chat2CodeAssistant()

    while True:
        userInput = input("Enter your command: ")
        botResponse = generate_response(userInput)
        assistant.updateChat(userInput, botResponse)

        tasks = create_task(userInput, botResponse)
        assistant.updateTasks(tasks)

        assistant.remindTasks()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```