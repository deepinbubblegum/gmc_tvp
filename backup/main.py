import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QDateTime
from gmc_tvp_main import Ui_MainWindow
from gmc_tvp_setting import formSetting
from gmc_tvp_editapp import formEditApp

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from subprocess import call
from configparser import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets


import numpy as np

import datetime
import queue
import smbus
import time
import board
import busio
import Adafruit_ADS1x15

i2c = busio.I2C(board.SCL, board.SDA)
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
adc.start_adc(3, gain=GAIN)

q_raw_data = queue.Queue(5)
m = 0
y2 = 0
y1 = 0
x1 = 0
x2 = 0

thd_start = 900
thd_avg = 0
detect_start = False
detect_cutoff = False
start_time = datetime.datetime.now()
end_time = datetime.datetime.now()
delta_time = datetime.datetime.now()
# include file class new From Page
# from new_FormPage import newPage

config = ConfigParser()
config_setting = ConfigParser()

status_torqe = 0 #0=idle 1=NG 2=OK 3=Cycle
status_torqe_prev = 99
status_timeout = 30
status_timeout_count = 0
count_cyclecomplete = 0
torqe_value = 50

application_name = "Default"
actual = 0
target = 3

class App(QMainWindow):
    
    def showStatus(self):
        global status_torqe,status_torqe_prev
        global actual,target,application_name

        if status_torqe != status_torqe_prev:
            status_torqe_prev = status_torqe
            if status_torqe == 0: #Idle
                self.ui.frameActual.setStyleSheet("")
                self.ui.frameTarget.setStyleSheet("")
                self.ui.frameOK.setStyleSheet("")
                self.ui.frameNG.setStyleSheet("")
                self.ui.frameCycleComplete.setStyleSheet("")
                self.ui.txtTq.setText("-")

            if status_torqe == 1: #NG
                self.ui.frameActual.setStyleSheet("background-color: rgb(255, 25, 0);")
                self.ui.frameTarget.setStyleSheet("background-color: rgb(255, 25, 0);")
                self.ui.frameOK.setStyleSheet("")
                self.ui.frameNG.setStyleSheet("background-color: rgb(255, 25, 0);")
                self.ui.frameCycleComplete.setStyleSheet("")
                self.ui.txtTq.setText("-")

            if status_torqe >= 2: #OK
                self.ui.frameActual.setStyleSheet("background-color: rgb(25, 255, 0);")
                self.ui.frameTarget.setStyleSheet("background-color: rgb(25, 255, 0);")
                self.ui.frameOK.setStyleSheet("background-color: rgb(25, 255, 0);")
                self.ui.frameNG.setStyleSheet("")
                self.ui.frameCycleComplete.setStyleSheet("")
                torqe_display = torqe_value + (random.randint(0,9)/10)
                self.ui.txtTq.setText(str(torqe_display))

            if status_torqe == 3: # Cycle Complete
                self.ui.frameCycleComplete.setStyleSheet("background-color: rgb(245, 121, 0);")
            else:
                self.ui.frameCycleComplete.setStyleSheet("")
            
        
        #self.statusIdle()
        self.ui.txtActual.setText(str(actual + 1))
        self.ui.txtTarget.setText(str(target))
        self.ui.btnApplication.setText(str(application_name))
        self.ui.txtCycleCounter.setText(str(count_cyclecomplete))


    def statusIdle(self):
        global status_torqe,status_timeout_count,status_timeout

        if status_torqe > 0:
            if status_timeout_count == 0:
                status_timeout_count = status_timeout
            else:
                status_timeout_count -= 1
                self.ui.txtTarget.setText(str(status_timeout_count))
                if status_timeout_count == 0:
                    status_torqe = 0

    def Torqe_Ready(self):
        global status_torqe,status_torqe_prev,actual,target,count_cyclecomplete
        if status_torqe_prev >= 2:
            actual += 1
            if actual >= target:
                actual = 0
        status_torqe = 0
        self.showStatus()


    def Torqe_OK(self):
        global status_torqe,status_timeout_count,status_timeout,actual,target,count_cyclecomplete
        if actual == target - 1:
            status_torqe = 3
            count_cyclecomplete += 1
        else:
            status_torqe = 2
                
    def Torqe_NG(self):

        global status_torqe,status_timeout_count,status_timeout
        status_torqe = 1

    def showHw(self):
        self.ui_hw = formHw()
        self.ui_hw.btnSelectApp.clicked.connect(self.showHw_OK)
        self.ui_hw.showFullScreen()
        self.hide()

    def showHw_OK(self):
        self.showFullScreen()
        self.ui_hw.hide()
        self.showStatus()

    # def readADC(self):
    #     if hw_connect:
    #         value = adc.get_last_result()
    #         print(value)

    def detectPulse(self):
        global thd_start,x1,x2,y1,y2,detect_start,detect_cutoff,q_raw_data,delta_time,end_time,start_time  
        ct = datetime.datetime.now()
        value = adc.get_last_result()
        if value > int(self.ui.progressBar.maximum()):
            self.ui.progressBar.setMaximum(value + 100)
        #self.ui.progressBar.setMaximum(8000)
        self.ui.progressBar.setValue(value)
        thd_avg = value
        if thd_avg > thd_start:
            
            q_raw_data.put(value)
            

            if q_raw_data.full():
                x2 = q_raw_data.qsize()
                x1 = 0
                y1 = q_raw_data.get(1)
                y2 = q_raw_data.get(x2)    
                m = (y2-y1)/(x2-x1)

                print("{},{}".format(value,m), end="\r")

                if detect_start == False:
                    if detect_cutoff == False:
                        if m > 100:
                            detect_start = True
                            print('START  = {0}:{1}:{2}:{3}'.format(ct,y1,y2,m))
                            start_time = datetime.datetime.now()
                            q_raw_data.empty()
                            self.toolStart()
                            #time.sleep(0.5)
                else:
                    if detect_cutoff == False:
                        print('RUN    = {0}:{1}:{2}:{3}'.format(ct,y1,y2,m))
                        self.toolStart()
                        if (m >= 10) & (m <= 100):
                            detect_cutoff = True
                            end_time = datetime.datetime.now()
                            delta_time = (end_time - start_time)
                            print('CUTOFF = {0}:{1}:{2}:{3}:{4}'.format(ct,y1,y2,m,delta_time.total_seconds()))
                            print('=========================================')
                            q_raw_data.empty()
                            self.checkTigthTime()
            else:
                m = 0
        else:
            if detect_start == True:
                detect_start = False
                detect_cutoff = False
                q_raw_data.empty()
                print('STOP {0}'.format(thd_avg))
                self.toolStop()
                
    def toolStart(self):
        self.ui.frameRun.setStyleSheet("background-color: rgb(25, 255, 0);")
        self.ui.lbRun.setText("RUN")
        self.Torqe_Ready()

    def toolStop(self):
        self.ui.frameRun.setStyleSheet("")
        self.ui.frameCutOff.setStyleSheet("")

        self.ui.lbRun.setText("STOP")

    def checkTigthTime(self):
        self.ui.frameCutOff.setStyleSheet("background-color: rgb(245, 121, 0);")

        global actual,target,application_name,delta_time,status_torqe
        config.read("app.ini")
        print(application_name)
        print("p{}".format(str(actual+1)))
        print("e{}".format(str(actual+1)))
        point_value = config[str(application_name)]["p{}".format(str(actual+1))]
        point_error = config[str(application_name)]["e{}".format(str(actual+1))]
        print(point_value)
        print(point_error)
        error_time = (float(point_value) * float(point_error)) / 100
    
        point_min = int(point_value) - int(error_time)
        point_max = int(point_value) + int(error_time)
        point_time = int(delta_time.total_seconds()*1000)
        print(point_min)
        print(point_max)
        print(point_time)
        if (point_time >= point_min) & (point_time <= point_max):
            self.Torqe_OK()
        else:
            self.Torqe_NG()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global x
        #x = Ui_SettingWindow()
       #S x.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showStatus)
        self.timer.start(100)

        self.adc_timer = QTimer()
        self.adc_timer.timeout.connect(self.detectPulse)
        self.adc_timer.start(100)

        self.ui.btnLogo.clicked.connect(self.on_click_exit)
        self.ui.btnSetting.clicked.connect(self.showSetting)

        #self.ui.btnInput.clicked.connect(self.showHw)

        self.showStatus()
        self.toolStop()

        
    def showMainWindow(self):
        self.showFullScreen()
        self.ui_setting.hide()
        self.showStatus()

    def showSetting(self):
        self.ui_setting = formSetting()
        self.ui_setting.btnSelectApp.clicked.connect(self.selectApp)
        self.ui_setting.btnNew.clicked.connect(self.createApp)
        self.ui_setting.btnEdit.clicked.connect(self.editApp)
        self.ui_setting.btnDelete.clicked.connect(self.removeApp)
        self.selectApp_Update()
        self.ui_setting.showFullScreen()
        self.hide()

    def selectApp_Update(self):
        self.ui_setting.lbApplication_name.setText("")
        config.read('app.ini')
        list_app = config.sections()
        list_count = len(list_app)
        self.ui_setting.listAppllication.clear()

        if list_count == 0:
            self.addDefautApp()
            config.read('app.ini')
            list_app = config.sections()
            list_count = len(list_app)

        if list_count > 0:
            i = 0
            for list in list_app:
                self.ui_setting.listAppllication.insertItem(i, list)
                i += 1
        

    def addDefautApp(self):
        config.read('app.ini')
        config.add_section("Default")
        config.set("Default","Target","3")
        config.set("Default","p1","1000")
        config.set("Default","e1","1.0")
        config.set("Default","p2","1000")
        config.set("Default","e2","1.0")
        config.set("Default","p3","1000")
        config.set("Default","e3","1.0")
        with open('app.ini', 'w') as configfile:
            config.write(configfile)
        # self.editApp_Update()

    def selectApp(self):
        global application_name , target
        select_item = self.ui_setting.listAppllication.currentItem()
        if select_item != None:
            try:
                app_target = int(config[select_item.text() ]['Target'])
            except:
                app_target=0
            if app_target > 0:
                application_name = select_item.text()  
                target = app_target
                self.showMainWindow()
                self.ui_setting.close()
            else:
                QMessageBox.about(self, " ", "No Target in Application.")
        else :
            QMessageBox.about(self, " ", "Please Select App.")
        
    def createApp(self):
        newAppName, done1 = QtWidgets.QInputDialog.getText(self, '', 'App. Name:') 
        if done1 & (newAppName != ''):
            if (newAppName in config) == False:
                config.add_section(newAppName)
                with open('app.ini', 'w') as configfile:
                    config.write(configfile)
                self.editApp_Update()

                self.ui_editApp = formEditApp()
                self.ui_editApp.lbApplication_name.setText(newAppName)
                self.ui_editApp.btnOK.clicked.connect(self.editApp_OK)
                self.ui_editApp.btnNew.clicked.connect(self.addPoint)
                self.ui_editApp.btnEdit.clicked.connect(self.editPoint)
                self.ui_editApp.btnDelete.clicked.connect(self.remotePoint)
                self.editApp_Update()
                self.ui_editApp.showFullScreen()
                self.ui_setting.hide()                
            else:
                QMessageBox.about(self, " ", "Already App. Name")

    def editApp(self):
        select_item = self.ui_setting.listAppllication.currentItem()
        if select_item != None:
            self.ui_editApp = formEditApp()
            self.ui_editApp.lbApplication_name.setText(select_item.text())
            self.ui_editApp.btnOK.clicked.connect(self.editApp_OK)
            self.ui_editApp.btnNew.clicked.connect(self.addPoint)
            self.ui_editApp.btnEdit.clicked.connect(self.editPoint)
            self.ui_editApp.btnDelete.clicked.connect(self.remotePoint)
            self.editApp_Update()
            self.ui_editApp.showFullScreen()
            self.ui_setting.hide()
        else :
            QMessageBox.about(self, " ", "Please Select App.")

    def editApp_Update(self):
        config.read('app.ini')
        try:
            app_target = int(config[self.ui_editApp.lbApplication_name.text()]['Target'])
        except:
            app_target=0
        #print(app_target)
        if app_target > 0:
            self.ui_editApp.listAppllication.clear()
            for i in range(app_target):
                point_value = config[self.ui_editApp.lbApplication_name.text()]["p{}".format(str(i+1))]
                point_error = config[self.ui_editApp.lbApplication_name.text()]["e{}".format(str(i+1))]
                #print(point_value)
                point_data = "Point {} = {} ms   Range = {}%".format(i+1,point_value,float(point_error))
                self.ui_editApp.listAppllication.insertItem(i, point_data)

    def editApp_OK(self):
        self.selectApp_Update()
        self.ui_setting.showFullScreen()
        self.ui_editApp.close()

    def removeApp(self):
        index = self.ui_setting.listAppllication.currentRow()
        if index >= 0:
            app_name = self.ui_setting.listAppllication.currentItem().text()
            items = ("No" , "Yes")
            res, done1 = QtWidgets.QInputDialog.getItem(self, 'Remove App', 'Remove App {} ?:'.format(app_name),items,0,False) 
            if done1 & (res == 'Yes'):     
                config.remove_section(str(app_name))
                with open('app.ini', 'w') as configfile:
                    config.write(configfile)
                self.selectApp_Update()
        else:
            QMessageBox.about(self, " ", "Please select App to remove.")     

    def addPoint(self):
        point_value, done1 = QtWidgets.QInputDialog.getInt(self, 'Add Point', 'Enter Tigth Time (ms):',1000,0,20000,1) 
        if done1 :
            point_error , done2 = QtWidgets.QInputDialog.getDouble(self, 'Add Point', 'Enter Range Time (%) :',1.0,0,50,1.0) 
            if done1 & done2:
                point_count = self.ui_editApp.listAppllication.count()
                section = self.ui_editApp.lbApplication_name.text()
                key_value = "p{}".format(point_count + 1)
                key_error = "e{}".format(point_count + 1)
                config[self.ui_editApp.lbApplication_name.text()]["Target"] = str(point_count + 1)
                config.set(str(section),str(key_value),str(point_value))
                config.set(str(section),str(key_error),str(point_error))
                with open('app.ini', 'w') as configfile:
                    config.write(configfile)
                self.editApp_Update()


    def editPoint(self):
        config.read('app.ini')
        index = self.ui_editApp.listAppllication.currentRow()
        if index >= 0:
            point_value = config[self.ui_editApp.lbApplication_name.text()]["p{}".format(index+1)]
            point_error = config[self.ui_editApp.lbApplication_name.text()]["e{}".format(index+1)]

            new_point_value, done1 = QtWidgets.QInputDialog.getInt(self, 'Edit Point', 'Enter Tigth Time (ms):',int(point_value),0,20000,1)    
            if done1 :
                new_point_error , done2 = QtWidgets.QInputDialog.getDouble(self, 'Edit Point', 'Enter Range Time (%) :',float(point_error),0,50,1.0) 
                
                if done1 & done2:
                    section = self.ui_editApp.lbApplication_name.text()
                    key_value = "p{}".format(index + 1)
                    key_error = "e{}".format(index + 1)
                    config.set(str(section),str(key_value),str(new_point_value))
                    config.set(str(section),str(key_error),str(new_point_error))
                    with open('app.ini', 'w') as configfile:
                        config.write(configfile)
                    self.editApp_Update()
        else:
            QMessageBox.about(self, " ", "Please Select Point.")

    def remotePoint(self):
        point_count = self.ui_editApp.listAppllication.count()
        items = ("No" , "Yes")
        res, done1 = QtWidgets.QInputDialog.getItem(self, 'Remove Point', 'Remove Point {} ?:'.format(point_count),items,0,False) 
        if done1 & (res == 'Yes'):     
            section = self.ui_editApp.lbApplication_name.text()
            key_value = "p{}".format(point_count + 1)
            key_error = "e{}".format(point_count + 1)
            config.remove_option(str(section),str(key_value))
            config.remove_option(str(section),str(key_error))
            config[self.ui_editApp.lbApplication_name.text()]["Target"] = str(point_count - 1)
            with open('app.ini', 'w') as configfile:
                config.write(configfile)
            self.editApp_Update()

    def test(self):
        self.showFullScreen()
        self.ui_setting.hide()
        

    

    def on_click_exit(self):
        QCoreApplication.instance().quit()


    def btnLogo_clicked(self):
        global status_torqe,status_timeout_count,status_timeout,x
        #status_torqe = 2
        #status_timeout_count = status_timeout
        #self.showStatus()
        #x = Ui_formSetting()
        #x.setupUi(self)
        

    def showTime(self):
        global status_torqe
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('hh:mm:ss')
        #self.ui.txtActual.setText(timeDisplay)
        
        
        #if status_torqe > 3: 
         #   status_torqe = 0
        
        #self.ui.txtTarget.setText(str(status_torqe))
        #self.showStatus()
        #status_torqe += 1


def main():
    app = QApplication(sys.argv)
    ui_app = App()
    ui_app.showFullScreen()
    #ui_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
