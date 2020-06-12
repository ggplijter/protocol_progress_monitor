# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mymainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(185, 128)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnStart = QToolButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/play.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.btnStart, 0, 0, 1, 1)

        self.btnStop = QToolButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnStop.setIcon(icon1)
        self.btnStop.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.btnStop, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 185, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

