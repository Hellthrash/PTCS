# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paciente.ui'
#
# Created: Sat Aug 29 23:41:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtGui.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 50, 271, 118))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nombreLabel = QtGui.QLabel(self.formLayoutWidget)
        self.nombreLabel.setObjectName("nombreLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombreLabel)
        self.nombreLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.nombreLineEdit.setObjectName("nombreLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreLineEdit)
        self.apellidosLabel = QtGui.QLabel(self.formLayoutWidget)
        self.apellidosLabel.setObjectName("apellidosLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.apellidosLabel)
        self.apellidosLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.apellidosLineEdit.setObjectName("apellidosLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.apellidosLineEdit)
        self.rutLabel = QtGui.QLabel(self.formLayoutWidget)
        self.rutLabel.setObjectName("rutLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.rutLabel)
        self.rutLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.rutLineEdit.setObjectName("rutLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.rutLineEdit)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(114, 190, 171, 27))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.buscarRutLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.buscarRutLabel.setObjectName("buscarRutLabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.buscarRutLabel)
        self.buscarRutLineEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.buscarRutLineEdit.setObjectName("buscarRutLineEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.buscarRutLineEdit)
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(130, 70, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 20, 85, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(70, 80, 231, 95))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.nombresLabel = QtGui.QLabel(self.formLayoutWidget_3)
        self.nombresLabel.setObjectName("nombresLabel")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombresLabel)
        self.nombresLineEdit = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.nombresLineEdit.setObjectName("nombresLineEdit")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombresLineEdit)
        self.apellidosLabel_2 = QtGui.QLabel(self.formLayoutWidget_3)
        self.apellidosLabel_2.setObjectName("apellidosLabel_2")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.apellidosLabel_2)
        self.apellidosLineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.apellidosLineEdit_2.setObjectName("apellidosLineEdit_2")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.apellidosLineEdit_2)
        self.correoLineEdit = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.correoLineEdit.setObjectName("correoLineEdit")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.correoLineEdit)
        self.correoLabel = QtGui.QLabel(self.formLayoutWidget_3)
        self.correoLabel.setObjectName("correoLabel")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.correoLabel)
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 190, 171, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayoutWidget_4 = QtGui.QWidget(self.tab_3)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.buscarRutLabel_2 = QtGui.QLabel(self.formLayoutWidget_4)
        self.buscarRutLabel_2.setObjectName("buscarRutLabel_2")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.buscarRutLabel_2)
        self.buscarRutLineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.buscarRutLineEdit_2.setObjectName("buscarRutLineEdit_2")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.buscarRutLineEdit_2)
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 20, 85, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_2 = QtGui.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(130, 70, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(55, 106, 281, 71))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 270, 85, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Datos necesarios:", None, QtGui.QApplication.UnicodeUTF8))
        self.nombreLabel.setText(QtGui.QApplication.translate("Form", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.apellidosLabel.setText(QtGui.QApplication.translate("Form", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.rutLabel.setText(QtGui.QApplication.translate("Form", "Ficha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.buscarRutLabel.setText(QtGui.QApplication.translate("Form", "Buscar Rut", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.nombresLabel.setText(QtGui.QApplication.translate("Form", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.apellidosLabel_2.setText(QtGui.QApplication.translate("Form", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.correoLabel.setText(QtGui.QApplication.translate("Form", "Ficha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.buscarRutLabel_2.setText(QtGui.QApplication.translate("Form", "Buscar Rut", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Despliegue de informacion a eliminar</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))
