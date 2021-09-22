import sys
import time
import threading
from PyQt5 import QtWidgets, uic

from ui.gmc_tvp_setting import UiSetting

class UiMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiMain, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_main.ui', self)
        # ui child init 
        self.ui_Setting = UiSetting()
        self.load_component()
        self.show()
        
        # start thr check windows
        self.thr_windows = threading.Thread(target=self.thread_windows_manager, args=())
        self.thr_windows.daemon = True
        self.thr_windows.start()
        
    def thread_windows_manager(self):
        while True:
            try:
                if self.ui_Setting.isVisible():
                    self.hide()
                else:
                    self.show()
            except AttributeError:
                pass
            time.sleep(0.1)
        
    def load_component(self):
        # btn component
        self.btn_setting = self.findChild(QtWidgets.QPushButton, "btnSetting")
        self.btn_setting.clicked.connect(self.invoke_form_settings)
        
    def invoke_form_settings(self):
        self.ui_Setting.show()
        
    def closeEvent(self, event):
        event.accept()