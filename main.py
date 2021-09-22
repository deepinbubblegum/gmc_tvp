import sys
from PyQt5 import QtWidgets, uic
from ui.gmc_tvp_main import UiMain

app = QtWidgets.QApplication(sys.argv)
windows = UiMain()
app.exec_()