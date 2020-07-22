from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
from PyQt5.QtCore import Qt, QSize, QPoint
from TimerClass import Timer
from threading import Thread
# CSS has been placed into a seperate folder to help clean up code
from styles import Style
import time

import sys

class Ui_Form(QtWidgets.QMainWindow):
    active = False
    timerApp = Timer()
        
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")

        # Creates a framless window
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        # Makes the background translucent which completes the frameless config
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground,on=True)
        
        self.setGeometry(500,300,300,110)
        
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet(Style.widget)
        self.widget.setObjectName("widget")
        self.widget.resize(300,110)
        
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.lineEdit_minutes = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_minutes.setEnabled(False)
        self.lineEdit_minutes.setStyleSheet(Style.lineEdit_minutes)
        self.lineEdit_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_minutes.setObjectName("lineEdit_minutes")
        
        self.gridLayout_2.addWidget(self.lineEdit_minutes, 0, 2, 1, 1)
        self.pushButton_set = QtWidgets.QPushButton(self.widget)
        self.pushButton_set.setStyleSheet(Style.pushButton_set)
        self.pushButton_set.setObjectName("pushButton_set")
        self.gridLayout_2.addWidget(self.pushButton_set, 1, 2, 1, 1)
        self.pushButton_set.clicked.connect(self.set_timer)
        
        self.pushButton_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_start.setStyleSheet(Style.pushButton_start)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 1, 0, 1, 1)
        self.pushButton_start.clicked.connect(self.start)
        
        self.lineEdit_seconds = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_seconds.setEnabled(False)
        self.lineEdit_seconds.setStyleSheet(Style.lineEdit_seconds)
        self.lineEdit_seconds.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_seconds.setObjectName("lineEdit_seconds")
        self.gridLayout_2.addWidget(self.lineEdit_seconds, 0, 4, 1, 1)
        
        self.lineEdit_hours = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_hours.setEnabled(False)
        self.lineEdit_hours.setAutoFillBackground(False)
        self.lineEdit_hours.setStyleSheet(Style.lineEdit_hours)
        self.lineEdit_hours.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_hours.setObjectName("lineEdit_hours")
        self.gridLayout_2.addWidget(self.lineEdit_hours, 0, 0, 1, 1)
        
        self.pushButton_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_close.setStyleSheet(Style.pushButton_close)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_2.addWidget(self.pushButton_close, 1, 4, 1, 1)
        self.pushButton_close.clicked.connect(self.exit_program)
        
        self.label_one = QtWidgets.QLabel(self.widget)
        self.label_one.setStyleSheet(Style.label_one)
        self.label_one.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_one.setObjectName("label_one")
        self.gridLayout_2.addWidget(self.label_one, 0, 1, 1, 1)
        
        self.label_two = QtWidgets.QLabel(self.widget)
        self.label_two.setStyleSheet(Style.label_two)
        self.label_two.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_two.setWordWrap(False)
        self.label_two.setObjectName("label_two")
        self.gridLayout_2.addWidget(self.label_two, 0, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Countdown"))
        self.lineEdit_minutes.setText(_translate("Form", "0"))
        self.pushButton_set.setText(_translate("Form", "SET"))
        self.pushButton_start.setText(_translate("Form", "START"))
        self.lineEdit_seconds.setText(_translate("Form", "0"))
        self.lineEdit_hours.setText(_translate("Form", "0"))
        self.pushButton_close.setText(_translate("Form", "CLOSE"))
        self.label_one.setText(_translate("Form", ":"))
        self.label_two.setText(_translate("Form", ":"))
        
    def exit_program(self):
            self.active = False
            sys.exit()

    def set_timer(self):
        text, okPressed = QtWidgets.QInputDialog.getText(None, 
                                                "",
                                                "Enter Countdown Minutes:", 
                                                QtWidgets.QLineEdit.Normal, 
                                                "")   
        if okPressed and text != '':
            self.timerApp.set_minutes(int(text))
            self._update()
    
    def _update(self):
        
        self.lineEdit_hours.setText(str(self.timerApp.hours))
        self.lineEdit_minutes.setText(str(self.timerApp.minutes))
        self.lineEdit_seconds.setText(str(self.timerApp.seconds))
    
    def start(self):
        t = Thread(target=self._run)
        t.start()
        
    def _run(self):
        if self.active == False:
            self.active = True
            self.pushButton_start.setText('STOP')

        else:
            self.active = False
            self.pushButton_start.setText('START')
            sys.exit()
            
        while self.active:
            if self.timerApp.total_seconds != 0:
                time.sleep(1)
                self.timerApp.total_seconds -= 1
                self.timerApp._convert_seconds_to_all()
                self._update()
            
            else:
                self.active = False
            






# Code below lets user move frameless window
    def mousePressEvent(self, event):
            self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
