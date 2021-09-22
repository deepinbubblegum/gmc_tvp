from PyQt5 import QtWidgets, QtGui

from PyQt5.QtCore import QTimer, QDateTime
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import random
import time
import queue


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        
        buffer_size = 100
        self.data_index = list(range(buffer_size))
        self.data = list(range(buffer_size))

        for i in range(buffer_size):
            self.data_index[i] = i
            self.data[i] = 0


        self.timer = QTimer()
        self.timer.timeout.connect(self.plot)
        self.timer.start(10)

    def plot(self):
        n = random.randint(0,10)

        self.data = self.data[1:]
        self.data.append(n)
        self.graphWidget.plot(self.data_index, self.data)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    # main = MainWindow()
    # main.show()
    ui_app = MainWindow()
    ui_app.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()