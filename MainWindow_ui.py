# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 599)
        self.NewWorkFlow = QAction(MainWindow)
        self.NewWorkFlow.setObjectName(u"NewWorkFlow")
        self.EditWorkflow = QAction(MainWindow)
        self.EditWorkflow.setObjectName(u"EditWorkflow")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 738, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuTemplate = QMenu(self.menubar)
        self.menuTemplate.setObjectName(u"menuTemplate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuTemplate.menuAction())
        self.menu.addAction(self.NewWorkFlow)
        self.menu.addAction(self.EditWorkflow)
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.actionhelp)
        self.menuTemplate.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NewWorkFlow.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5de5\u4f5c\u6d41", None))
        self.EditWorkflow.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u5de5\u4f5c\u6d41", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5de5\u4f5c\u6d41", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Workflow", None))
        self.menuTemplate.setTitle(QCoreApplication.translate("MainWindow", u"Template", None))
    # retranslateUi

