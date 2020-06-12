# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'protocolprogresswidget.ui'
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

from widgets import QProtocolProgressChartView


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(549, 430)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mychart = QProtocolProgressChartView(Form)
        self.mychart.setObjectName(u"mychart")
        self.mychart.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.mychart, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.info = QLabel(Form)
        self.info.setObjectName(u"info")
        font = QFont()
        font.setPointSize(40)
        self.info.setFont(font)
        self.info.setWordWrap(True)

        self.gridLayout.addWidget(self.info, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

