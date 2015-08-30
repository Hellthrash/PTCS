# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sportal.ui'
#
# Created: Sun Aug 30 01:11:43 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_welcome2(object):
    def setupUi(self, welcome2):
        welcome2.setObjectName("welcome2")
        welcome2.resize(386, 310)
        welcome2.setMinimumSize(QtCore.QSize(386, 310))
        welcome2.setMaximumSize(QtCore.QSize(386, 310))
        self.label = QtGui.QLabel(welcome2)
        self.label.setGeometry(QtCore.QRect(80, 0, 291, 101))
        self.label.setAccessibleName("")
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(welcome2)
        self.pushButton.setGeometry(QtCore.QRect(150, 240, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtGui.QWidget(welcome2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(79, 100, 231, 95))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(welcome2)
        QtCore.QMetaObject.connectSlotsByName(welcome2)

    def retranslateUi(self, welcome2):
        welcome2.setWindowTitle(QtGui.QApplication.translate("welcome2", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("welcome2", "Seleccione el portal que desea administrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("welcome2", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("welcome2", "Portal Citas", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("welcome2", "Portal Pacientes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("welcome2", "Portal Medicos", None, QtGui.QApplication.UnicodeUTF8))

