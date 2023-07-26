```python
import os
import sys
from PyQt5.QtWidgets import QApplication
from interface import MainWindow

def deploy_app():
    # Check the platform and print a message accordingly
    if sys.platform.startswith('win32'):
        print("Deploying on Windows OS")
    elif sys.platform.startswith('darwin'):
        print("Deploying on MacOS")
    elif sys.platform.startswith('linux'):
        print("Deploying on Linux OS")
    else:
        print("Unsupported OS")
        return

    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of the application's main window
    main_window = MainWindow()

    # Show the application's main window
    main_window.show()

    # Execute the application's main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    deploy_app()
```