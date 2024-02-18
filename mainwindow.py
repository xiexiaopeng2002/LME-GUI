from PySide6.QtCore import QDir, QFile, QIODevice, QUrl, Qt, Slot
from PySide6.QtGui import QFontDatabase
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox
from MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_file_path = ''
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self._ui.editor.setFont(font)
        self._ui.preview.setContextMenuPolicy(Qt.NoContextMenu)
        self._page = PreviewPage(self)
        self._ui.preview.setPage(self._page)

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.NewWorkFlow.triggered.connect(self.gowfcCreater)
        self.actionOpen.triggered.connect(self.showstructure)
    def gowfcCreater(self):
        self.switch_wfcCreater.emit()
    def showstructure(self):
        self.switch_actionOpen.emit()