# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmc_tvp_setting.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

class formSetting(QWidget):
    def __init__(self):
        super(formSetting, self).__init__()
        self.setupUi(self)
    
    def setupUi(self, formSetting):
        formSetting.setObjectName("formSetting")
        formSetting.resize(800, 480)
        self.btnSetting = QtWidgets.QPushButton(formSetting)
        self.btnSetting.setGeometry(QtCore.QRect(700, 390, 71, 71))
        self.btnSetting.setAutoFillBackground(False)
        self.btnSetting.setStyleSheet("border-image: url(:/img/setting.png);")
        self.btnSetting.setText("")
        self.btnSetting.setObjectName("btnSetting")
        self.listApplication = QtWidgets.QListView(formSetting)
        self.listApplication.setGeometry(QtCore.QRect(0, 60, 491, 411))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listApplication.setFont(font)
        self.listApplication.setObjectName("listApplication")
        self.btnLogo = QtWidgets.QPushButton(formSetting)
        self.btnLogo.setGeometry(QtCore.QRect(550, 390, 71, 71))
        self.btnLogo.setAutoFillBackground(False)
        self.btnLogo.setStyleSheet("border-image: url(:/img/joinmaxlogo2.png);")
        self.btnLogo.setText("")
        self.btnLogo.setObjectName("btnLogo")
        self.lbApplication_2 = QtWidgets.QLabel(formSetting)
        self.lbApplication_2.setGeometry(QtCore.QRect(0, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbApplication_2.setFont(font)
        self.lbApplication_2.setObjectName("lbApplication_2")

        self.retranslateUi(formSetting)
        QtCore.QMetaObject.connectSlotsByName(formSetting)

    def retranslateUi(self, formSetting):
        _translate = QtCore.QCoreApplication.translate
        formSetting.setWindowTitle(_translate("formSetting", "Form"))
        self.lbApplication_2.setText(_translate("formSetting", "Setting :"))
