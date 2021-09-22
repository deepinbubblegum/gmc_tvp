from PyQt5 import QtWidgets, uic
import sys

class UiAppedit(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiAppedit, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_appedit.ui', self)
        self.show()