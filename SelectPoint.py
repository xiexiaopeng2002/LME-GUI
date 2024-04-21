# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause


from PySide6.QtCore import QFile, QIODevice, QUrl, Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QWidget
from PySide6.QtWebEngineCore import QWebEngineSettings
from SelectPoint_ui import Ui_SelectPoint
from previewpage import PreviewPage


class SelectPoint(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_file_path = ''
        self._ui = Ui_SelectPoint()
        self._ui.setupUi(self)
        self._ui.preview.setContextMenuPolicy(Qt.NoContextMenu)
        self._page = PreviewPage(self)
        self._ui.preview.setPage(self._page)
        page = self._ui.preview.page()
        page.profile().settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        page.profile().settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)

        self._channel = QWebChannel(self)
        self._page.setWebChannel(self._channel)

        self._ui.preview.setUrl(QUrl("qrc:3rdparty/test2.htm"))
        self._ui.preview.loadFinished.connect(lambda: page.runJavaScript('Jmol.loadFile(jmolApplet0,"C:/Users/97521/Desktop/Clwithoutbug.mol2")'))
        




