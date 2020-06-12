from PySide2 import QtWidgets

import ui_protocolprogresswidget

__all__ = ["SecondScreenWidget"]

class SecondScreenWidget(QtWidgets.QWidget, ui_protocolprogresswidget.Ui_Form ):
    def __init__(self, parent = None):
        super(SecondScreenWidget, self).__init__(parent)
        self.setupUi(self)

        self.mychart.updateInfo.connect(self.info.setText)











