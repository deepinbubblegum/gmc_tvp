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
        formSetting.setMinimumSize(QtCore.QSize(800, 480))
        formSetting.setMaximumSize(QtCore.QSize(800, 480))
        self.lbApplication_name = QtWidgets.QLabel(formSetting)
        self.lbApplication_name.setGeometry(QtCore.QRect(260, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbApplication_name.setFont(font)
        self.lbApplication_name.setObjectName("lbApplication_name")
        self.btnNew = QtWidgets.QPushButton(formSetting)
        self.btnNew.setGeometry(QtCore.QRect(570, 60, 211, 51))
        self.btnNew.setObjectName("btnNew")
        self.listAppllication = QtWidgets.QListWidget(formSetting)
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
        self.btnEdit = QtWidgets.QPushButton(formSetting)
        self.btnEdit.setGeometry(QtCore.QRect(570, 120, 211, 51))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(formSetting)
        self.btnDelete.setGeometry(QtCore.QRect(570, 180, 211, 51))
        self.btnDelete.setObjectName("btnDelete")
        self.btnSelectApp = QtWidgets.QPushButton(formSetting)
        self.btnSelectApp.setGeometry(QtCore.QRect(570, 390, 211, 81))
        self.btnSelectApp.setObjectName("btnSelectApp")
        self.lbApplication_2 = QtWidgets.QLabel(formSetting)
        self.lbApplication_2.setGeometry(QtCore.QRect(10, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbApplication_2.setFont(font)
        self.lbApplication_2.setObjectName("lbApplication_2")

        self.retranslateUi(formSetting)
        QtCore.QMetaObject.connectSlotsByName(formSetting)

    def retranslateUi(self, formSetting):
        _translate = QtCore.QCoreApplication.translate
        formSetting.setWindowTitle(_translate("formSetting", "Form"))
        self.lbApplication_name.setText(_translate("formSetting", "NAME"))
        self.btnNew.setText(_translate("formSetting", "NEW"))
        self.btnEdit.setText(_translate("formSetting", "EDIT"))
        self.btnDelete.setText(_translate("formSetting", "DEL"))
        self.btnSelectApp.setText(_translate("formSetting", "OK"))
        self.lbApplication_2.setText(_translate("formSetting", "Select Application :"))
import resource_rc
