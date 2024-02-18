from PySide6 import QtCore, QtWidgets
from MainWindow_ui import Ui_MainWindow
from WorkflowConfigCreater_ui import Ui_wfcCreater
# from browser import Browser

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    switch_wfcCreater = QtCore.Signal()
    switch_wfcEditer = QtCore.Signal()
    switch_actionOpen = QtCore.Signal()
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.NewWorkFlow.triggered.connect(self.gowfcCreater)
        self.actionOpen.triggered.connect(self.showstructure)
    def gowfcCreater(self):
        self.switch_wfcCreater.emit()
    def showstructure(self):
        self.switch_actionOpen.emit()

class wfcCreater(QtWidgets.QMainWindow,Ui_wfcCreater):
    switch_fliebrowser1 = QtCore.Signal()
    switch_fliebrowser2 = QtCore.Signal()
    switch_fliebrowser3 = QtCore.Signal()
    switch_selectpoint = QtCore.Signal()
    def __init__(self):
        super(wfcCreater,self).__init__()
        self.setupUi(self)
        self.fileBrowserbutton_1.clicked.connect(self.gofilebrowser1)
        self.fileBrowserbutton_2.clicked.connect(self.gofilebrowser2)
        self.fileBrowserbutton_3.clicked.connect(self.gofilebrowser3)
        self.selectpointButton.clicked.connect(self.gowebview3dmol)
    def gofilebrowser1(self):
        rootdir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择产物输出路径")
        self.lineEdit_1.setText(rootdir)
    def gofilebrowser2(self):
        rootdir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择模板文件路径")
        self.lineEdit_2.setText(rootdir)
    def gofilebrowser3(self):
        rootdir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择取代基路径")
        self.lineEdit_3.setText(rootdir)
    def gowebview3dmol(self):
        self.switch_selectpoint.emit()



class fliebrowser(QtWidgets.QFileDialog):
    def __init__(self):
        super(fliebrowser,self).__init__()
        self.setupUi(self)

class Controller:
    def __init__(self) -> None:
        pass
    # 跳转到主界面
    def show_mainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.switch_wfcCreater.connect(self.show_wfcCreater)
        self.mainwindow.show()
    # 跳转到workflow配置文件生成器
    def show_wfcCreater(self):
        self.wfcCreater = wfcCreater()
        self.wfcCreater.show()
    # def showstructure(self):
    def show_browser(self):
        self.browser = Browser()
        self.browser.__init__
        