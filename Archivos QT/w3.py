# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w3.ui'
#
# Created: Sun Aug 30 01:02:47 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(386, 310)
        welcome.setMinimumSize(QtCore.QSize(386, 310))
        welcome.setMaximumSize(QtCore.QSize(386, 310))
        self.formLayoutWidget = QtGui.QWidget(welcome)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 110, 181, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usuarioLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.usuarioLineEdit.setObjectName("usuarioLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.usuarioLineEdit)
        self.usuarioLabel = QtGui.QLabel(self.formLayoutWidget)
        self.usuarioLabel.setObjectName("usuarioLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.usuarioLabel)
        self.passwordLabel = QtGui.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordLineEdit)
        self.label = QtGui.QLabel(welcome)
        self.label.setGeometry(QtCore.QRect(80, 0, 291, 101))
        self.label.setAccessibleName("")
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(welcome)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(welcome)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 85, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        welcome.setWindowTitle(QtGui.QApplication.translate("welcome", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.usuarioLabel.setText(QtGui.QApplication.translate("welcome", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("welcome", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("welcome", "Bienvenido al software de horas medicas.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("welcome", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("welcome", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

