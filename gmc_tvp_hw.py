# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmc_tvp_hw.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class formHw(QWidget):
    def __init__(self):
        super(formHw, self).__init__()
        self.setupUi(self)
    def setupUi(self, formHw):
        formHw.setObjectName("formHw")
        formHw.resize(800, 480)
        formHw.setMinimumSize(QtCore.QSize(800, 480))
        formHw.setMaximumSize(QtCore.QSize(800, 480))
        self.btnSelectApp = QtWidgets.QPushButton(formHw)
        self.btnSelectApp.setGeometry(QtCore.QRect(570, 390, 211, 81))
        self.btnSelectApp.setObjectName("btnSelectApp")
        self.qwtPlot = QwtPlot(formHw)
        self.qwtPlot.setGeometry(QtCore.QRect(-10, 50, 541, 261))
        self.qwtPlot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qwtPlot.setAutoReplot(True)
        self.qwtPlot.setObjectName("qwtPlot")
        self.verticalSlider = QtWidgets.QSlider(formHw)
        self.verticalSlider.setGeometry(QtCore.QRect(590, 49, 20, 271))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.retranslateUi(formHw)
        self.verticalSlider.valueChanged['int'].connect(self.qwtPlot.replot)
        QtCore.QMetaObject.connectSlotsByName(formHw)

    def retranslateUi(self, formHw):
        _translate = QtCore.QCoreApplication.translate
        formHw.setWindowTitle(_translate("formHw", "Form"))
        self.btnSelectApp.setText(_translate("formHw", "DONE"))
from PyQt5.Qwt import *
import resource_rc
