# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 238)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 3, 2, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout.addWidget(self.pushButton_dot, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_pl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pl.setObjectName("pushButton_pl")
        self.verticalLayout.addWidget(self.pushButton_pl)
        self.pushButton_mi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mi.setObjectName("pushButton_mi")
        self.verticalLayout.addWidget(self.pushButton_mi)
        self.pushButton_um = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_um.setObjectName("pushButton_um")
        self.verticalLayout.addWidget(self.pushButton_um)
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.verticalLayout.addWidget(self.pushButton_del)
        self.pushButton_ravn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ravn.setObjectName("pushButton_ravn")
        self.verticalLayout.addWidget(self.pushButton_ravn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_delete.setText(_translate("MainWindow", "del"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_pl.setText(_translate("MainWindow", "+"))
        self.pushButton_mi.setText(_translate("MainWindow", "-"))
        self.pushButton_um.setText(_translate("MainWindow", "*"))
        self.pushButton_del.setText(_translate("MainWindow", "/"))
        self.pushButton_ravn.setText(_translate("MainWindow", "="))