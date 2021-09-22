import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget

class UiEditApp(QWidget):
    def __init__(self):
        super(UiEditApp, self).__init__()
        uic.loadUi('./ui/resource/gmc_tvp_editapp.ui', self)