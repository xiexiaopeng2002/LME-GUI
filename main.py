import sys
from PySide6 import QtWidgets
from pagecontroller import Controller
import subprocess
import rc_lmegui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_mainwindow()
    php_path = "D:\\php8\\php.exe"
    subprocess.Popen([php_path, "-S", "localhost:8000", "-t", "D:\\Documents\\Qt\\resources\\3rdparty\\php"])
    sys.exit(app.exec())
