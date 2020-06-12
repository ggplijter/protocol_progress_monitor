
from PySide2 import QtWidgets, QtCore, QtGui, QtCharts
import ui_mymainwindow

from widgets import SecondScreenWidget

__all__ = ["MyMainWindow"]


class MyMainWindow(QtWidgets.QMainWindow, ui_mymainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnStart.clicked.connect(self.onBtnStart)
        self.btnStop.clicked.connect(self.onBtnStop)

        self.secondscreen = SecondScreenWidget()
        self.secondscreen.info.setText("")





    def onBtnStart(self):
        self.secondscreen.showMaximized()

        self.secondscreen.mychart.startProtocol()

    def onBtnStop(self):
        # self.secondscreen.close()
        self.secondscreen.mychart.stopProtocol()
        self.secondscreen.info.setText("")







