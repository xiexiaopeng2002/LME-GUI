from PySide6 import QtCore, QtWidgets
from MainWindow_ui import Ui_MainWindow
from WorkflowConfigCreater_ui import Ui_wfcCreater
# from browser import Browser
from SelectPoint import SelectPoint
from fileserver import start_fileserver
import time
from multiprocessing import Process

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
    def __init__(self):
        super(wfcCreater,self).__init__()
        self.setupUi(self)
        self.fileBrowserbutton_1.clicked.connect(self.gofilebrowser1)
        self.fileBrowserbutton_2.clicked.connect(self.gofilebrowser2)
        self.fileBrowserbutton_3.clicked.connect(self.gofilebrowser3)
        # self.selectpointButton.clicked.connect(self.gowebview3dmol)
    def gofilebrowser1(self):
        rootdir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择产物输出路径")
        self.lineEdit_1.setText(rootdir)
    def gofilebrowser2(self):
        moldir = QtWidgets.QFileDialog.getOpenFileName(self, "选择模板文件路径")
        self.lineEdit_2.setText(moldir[0])
    def gofilebrowser3(self):
        rootdir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择取代基路径")
        self.lineEdit_3.setText(rootdir)

class webview3dmol(SelectPoint):
    def __init__(self):
        super(SelectPoint,self).__init__()

class fliebrowser(QtWidgets.QFileDialog):
    def __init__(self):
        super(fliebrowser,self).__init__()
        self.setupUi(self)

class Controller:
    def __init__(self) -> None:
        self.wfcCreater = None
    # 跳转到主界面
    def show_mainwindow(self):
        self.mainwindow = MainWindow()
        self.mainwindow.switch_wfcCreater.connect(self.show_wfcCreater)
        self.mainwindow.switch_actionOpen.connect(self.show_selectpoint)
        self.mainwindow.show()
    # 跳转到workflow配置文件生成器
    def show_wfcCreater(self):
        self.wfcCreater = wfcCreater()
        self.wfcCreater.selectpointButton.clicked.connect(self.show_selectpoint)
        self.wfcCreater.show()
    # def showstructure(self):
    def show_selectpoint(self):
        molpath = self.wfcCreater.lineEdit_2.text()
        # 创建一个新的进程来运行start_fileserver函数
        server_process = Process(target=start_fileserver, args=(molpath,))
        server_process.start() # 启动新进程
        time.sleep(2)
        # 在主进程中继续执行其他代码
        self.selectpoint = SelectPoint()
        self.selectpoint.show()
        
