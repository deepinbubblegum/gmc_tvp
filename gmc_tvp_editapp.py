# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmc_tvp_editapp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class formEditApp(QWidget):
    def __init__(self):
        super(formEditApp, self).__init__()
        self.setupUi(self)
    def setupUi(self, formEditApp):
        formEditApp.setObjectName("formEditApp")
        formEditApp.resize(800, 480)
        formEditApp.setMinimumSize(QtCore.QSize(800, 480))
        formEditApp.setMaximumSize(QtCore.QSize(800, 480))
        self.btnNew = QtWidgets.QPushButton(formEditApp)
        self.btnNew.setGeometry(QtCore.QRect(570, 60, 211, 51))
        self.btnNew.setObjectName("btnNew")
        self.listAppllication = QtWidgets.QListWidget(formEditApp)
        self.listAppllication.setGeometry(QtCore.QRect(10, 60, 541, 411))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.listAppllication.setFont(font)
        self.listAppllication.setFrameShape(QtWidgets.QFrame.Box)
        self.listAppllication.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listAppllication.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listAppllication.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listAppllication.setAutoScrollMargin(16)
        self.listAppllication.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listAppllication.setObjectName("listAppllication")
        self.btnEdit = QtWidgets.QPushButton(formEditApp)
        self.btnEdit.setGeometry(QtCore.QRect(570, 120, 211, 51))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(formEditApp)
        self.btnDelete.setGeometry(QtCore.QRect(570, 180, 211, 51))
        self.btnDelete.setObjectName("btnDelete")
        self.btnCalc = QtWidgets.QPushButton(formEditApp)
        self.btnCalc.setGeometry(QtCore.QRect(570, 240, 211, 51))
        self.btnCalc.setObjectName("btnCalc")
        self.btnOK = QtWidgets.QPushButton(formEditApp)
        self.btnOK.setGeometry(QtCore.QRect(570, 390, 211, 81))
        self.btnOK.setObjectName("btnOK")
        self.lbApplication_name = QtWidgets.QLabel(formEditApp)
        self.lbApplication_name.setGeometry(QtCore.QRect(170, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbApplication_name.setFont(font)
        self.lbApplication_name.setObjectName("lbApplication_name")
        self.lbApplication = QtWidgets.QLabel(formEditApp)
        self.lbApplication.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbApplication.setFont(font)
        self.lbApplication.setObjectName("lbApplication")

        self.retranslateUi(formEditApp)
        QtCore.QMetaObject.connectSlotsByName(formEditApp)

    def retranslateUi(self, formEditApp):
        _translate = QtCore.QCoreApplication.translate
        formEditApp.setWindowTitle(_translate("formEditApp", "Form"))
        self.btnNew.setText(_translate("formEditApp", "ADD"))
        self.btnEdit.setText(_translate("formEditApp", "EDIT"))
        self.btnDelete.setText(_translate("formEditApp", "DEL"))
        self.btnCalc.setText(_translate("formEditApp", "CALC"))
        self.btnOK.setText(_translate("formEditApp", "DONE"))
        self.lbApplication_name.setText(_translate("formEditApp", "NAME"))
        self.lbApplication.setText(_translate("formEditApp", "Application :"))
import resource_rc
