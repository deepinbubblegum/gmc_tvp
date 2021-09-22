import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
class UiSetting(QWidget):
    def __init__(self):
        super(UiSetting, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_setting.ui', self)
        self.load_component()
        
    def load_component(self):
        self.btn_new = self.findChild(QtWidgets.QPushButton, "btnNew")
        self.btn_new.clicked.connect(self.invoke_new)
        
    def invoke_new(self):
        self.hide()