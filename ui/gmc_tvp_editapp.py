from PyQt5 import QtWidgets, uic
import sys

class UiEditApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiEditApp, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_editapp.ui', self)
        self.show()