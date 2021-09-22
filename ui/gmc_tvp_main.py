from PyQt5 import QtWidgets, uic
import sys

class UiMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiMain, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_main.ui', self)
        self.load_component()
        self.show()
        
    def load_component(self):
        # btn component
        self.btn_setting = self.findChild(QtWidgets.QPushButton, "btnSetting")
        self.btn_setting.clicked.connect(self.invoke_form_settings)
        
    def invoke_form_settings(self):
        print("hello")