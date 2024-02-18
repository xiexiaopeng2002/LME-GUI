# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectPoint.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_SelectPoint(object):
    def setupUi(self, SelectPoint):
        if not SelectPoint.objectName():
            SelectPoint.setObjectName(u"SelectPoint")
        SelectPoint.resize(400, 300)
        self.preview = QWebEngineView(SelectPoint)
        self.preview.setObjectName(u"preview")
        self.preview.setEnabled(True)
        self.preview.setGeometry(QRect(0, 0, 401, 291))
        self.preview.setUrl(QUrl(u"about:blank"))

        self.retranslateUi(SelectPoint)

        QMetaObject.connectSlotsByName(SelectPoint)
    # setupUi

    def retranslateUi(self, SelectPoint):
        SelectPoint.setWindowTitle(QCoreApplication.translate("SelectPoint", u"\u9009\u62e9\u4f4d\u70b9", None))
    # retranslateUi

