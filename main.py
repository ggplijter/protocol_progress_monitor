from PySide2 import QtWidgets, QtGui, QtCore
import sys
sys.path.append(".\\ui\\")

from widgets import MyMainWindow

def main():
    global app

    app = QtWidgets.QApplication(sys.argv)
    mw = MyMainWindow()
    mw.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()