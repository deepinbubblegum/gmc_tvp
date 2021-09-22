from PyQt5 import QtWidgets, uic
import sys

class UiMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiMain, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_main.ui', self)
        self.show()