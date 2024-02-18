import sys
from PySide6 import QtWidgets
from pagecontroller import Controller

import rc_lmegui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_mainwindow()
    sys.exit(app.exec())
