from PyQt5 import QtWidgets, uic
import sys

class UiSetting(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiSetting, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_setting.ui', self)
        self.show()