# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkflowConfigCreater.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QToolButton, QWidget)

class Ui_wfcCreater(object):
    def setupUi(self, wfcCreater):
        if not wfcCreater.objectName():
            wfcCreater.setObjectName(u"wfcCreater")
        wfcCreater.resize(567, 507)
        wfcCreater.setMinimumSize(QSize(256, 29))
        self.horizontalLayoutWidget = QWidget(wfcCreater)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 491, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(128, 0))
        self.textBrowser.setMaximumSize(QSize(128, 29))

        self.horizontalLayout.addWidget(self.textBrowser)

        self.lineEdit_1 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.horizontalLayout.addWidget(self.lineEdit_1)

        self.fileBrowserbutton_1 = QToolButton(self.horizontalLayoutWidget)
        self.fileBrowserbutton_1.setObjectName(u"fileBrowserbutton_1")

        self.horizontalLayout.addWidget(self.fileBrowserbutton_1)

        self.horizontalLayoutWidget_2 = QWidget(wfcCreater)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 50, 491, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_2 = QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMinimumSize(QSize(128, 0))
        self.textBrowser_2.setMaximumSize(QSize(128, 29))

        self.horizontalLayout_2.addWidget(self.textBrowser_2)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.fileBrowserbutton_2 = QToolButton(self.horizontalLayoutWidget_2)
        self.fileBrowserbutton_2.setObjectName(u"fileBrowserbutton_2")

        self.horizontalLayout_2.addWidget(self.fileBrowserbutton_2)

        self.horizontalLayoutWidget_3 = QWidget(wfcCreater)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 90, 491, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_3 = QTextBrowser(self.horizontalLayoutWidget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMinimumSize(QSize(128, 0))
        self.textBrowser_3.setMaximumSize(QSize(128, 29))

        self.horizontalLayout_3.addWidget(self.textBrowser_3)

        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.fileBrowserbutton_3 = QToolButton(self.horizontalLayoutWidget_3)
        self.fileBrowserbutton_3.setObjectName(u"fileBrowserbutton_3")

        self.horizontalLayout_3.addWidget(self.fileBrowserbutton_3)

        self.selectpointButton = QPushButton(wfcCreater)
        self.selectpointButton.setObjectName(u"selectpointButton")
        self.selectpointButton.setGeometry(QRect(50, 170, 111, 31))
        self.pushButton_2 = QPushButton(wfcCreater)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 450, 111, 31))
        self.pushButton_3 = QPushButton(wfcCreater)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 450, 111, 31))
        self.tableWidget = QTableWidget(wfcCreater)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 7):
            self.tableWidget.setRowCount(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(230, 130, 256, 111))
        self.pushButton_4 = QPushButton(wfcCreater)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 300, 111, 31))

        self.retranslateUi(wfcCreater)

        QMetaObject.connectSlotsByName(wfcCreater)
    # setupUi

    def retranslateUi(self, wfcCreater):
        wfcCreater.setWindowTitle(QCoreApplication.translate("wfcCreater", u"Workflow\u7f16\u8f91\u5668", None))
        self.textBrowser.setHtml(QCoreApplication.translate("wfcCreater", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u4ea7\u7269\u8f93\u51fa\u8def\u5f84</span></p></body></html>", None))
        self.fileBrowserbutton_1.setText(QCoreApplication.translate("wfcCreater", u"...", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("wfcCreater", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u6a21\u677f\u6587\u4ef6\u8def\u5f84</span></p></body></html>", None))
        self.fileBrowserbutton_2.setText(QCoreApplication.translate("wfcCreater", u"...", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("wfcCreater", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u53d6\u4ee3\u57fa\u8def\u5f84</span></p></body></html>", None))
        self.fileBrowserbutton_3.setText(QCoreApplication.translate("wfcCreater", u"...", None))
        self.selectpointButton.setText(QCoreApplication.translate("wfcCreater", u"\u6807\u8bb0\u4f4d\u70b9\u9009\u62e9\u5668", None))
        self.pushButton_2.setText(QCoreApplication.translate("wfcCreater", u"\u4fdd\u5b58Workflow", None))
        self.pushButton_3.setText(QCoreApplication.translate("wfcCreater", u"\u9884\u89c8Workflow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("wfcCreater", u"\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("wfcCreater", u"\u5750\u6807", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("wfcCreater", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("wfcCreater", u"2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("wfcCreater", u"3", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("wfcCreater", u"4", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("wfcCreater", u"5", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("wfcCreater", u"6", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("wfcCreater", u"7", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("wfcCreater", u"\u539f\u5b50", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("wfcCreater", u"[0,0,0]", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("wfcCreater", u"\u952e", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_4.setText(QCoreApplication.translate("wfcCreater", u"\u65b0\u589ejob", None))
    # retranslateUi

