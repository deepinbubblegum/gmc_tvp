from PyQt5 import QtWidgets, uic
import sys

class UiHw(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiHw, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_hw.ui', self)
        self.show()