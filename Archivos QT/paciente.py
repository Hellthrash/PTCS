# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paciente.ui'
#
# Created: Sun Aug 30 21:30:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_paciente(object):
    def setupUi(self, paciente):
        paciente.setObjectName("paciente")
        paciente.resize(400, 300)
        self.tabWidget = QtGui.QTabWidget(paciente)
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
        self.nm_ap = QtGui.QLineEdit(self.formLayoutWidget)
        self.nm_ap.setObjectName("nm_ap")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nm_ap)
        self.apellidosLabel = QtGui.QLabel(self.formLayoutWidget)
        self.apellidosLabel.setObjectName("apellidosLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.apellidosLabel)
        self.ap_ap = QtGui.QLineEdit(self.formLayoutWidget)
        self.ap_ap.setObjectName("ap_ap")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.ap_ap)
        self.rutLabel = QtGui.QLabel(self.formLayoutWidget)
        self.rutLabel.setObjectName("rutLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.rutLabel)
        self.fch_ap = QtGui.QLineEdit(self.formLayoutWidget)
        self.fch_ap.setObjectName("fch_ap")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fch_ap)
        self.agr_ap = QtGui.QPushButton(self.tab)
        self.agr_ap.setGeometry(QtCore.QRect(114, 190, 171, 27))
        self.agr_ap.setObjectName("agr_ap")
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
        self.bcr_mp = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.bcr_mp.setObjectName("bcr_mp")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.bcr_mp)
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(130, 70, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bcr1_mp = QtGui.QPushButton(self.tab_2)
        self.bcr1_mp.setGeometry(QtCore.QRect(300, 20, 85, 27))
        self.bcr1_mp.setObjectName("bcr1_mp")
        self.formLayoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(70, 80, 231, 95))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.nombresLabel = QtGui.QLabel(self.formLayoutWidget_3)
        self.nombresLabel.setObjectName("nombresLabel")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombresLabel)
        self.nm_mp = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.nm_mp.setObjectName("nm_mp")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.nm_mp)
        self.apellidosLabel_2 = QtGui.QLabel(self.formLayoutWidget_3)
        self.apellidosLabel_2.setObjectName("apellidosLabel_2")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.apellidosLabel_2)
        self.ap_mp = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.ap_mp.setObjectName("ap_mp")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.ap_mp)
        self.fch_mp = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.fch_mp.setObjectName("fch_mp")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.fch_mp)
        self.correoLabel = QtGui.QLabel(self.formLayoutWidget_3)
        self.correoLabel.setObjectName("correoLabel")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.correoLabel)
        self.mdf_mp = QtGui.QPushButton(self.tab_2)
        self.mdf_mp.setGeometry(QtCore.QRect(110, 190, 171, 27))
        self.mdf_mp.setObjectName("mdf_mp")
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
        self.bcr_ep = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.bcr_ep.setObjectName("bcr_ep")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.bcr_ep)
        self.elm_ep = QtGui.QPushButton(self.tab_3)
        self.elm_ep.setGeometry(QtCore.QRect(300, 20, 85, 27))
        self.elm_ep.setObjectName("elm_ep")
        self.line_2 = QtGui.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(130, 70, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.imp_ep = QtGui.QLabel(self.tab_3)
        self.imp_ep.setGeometry(QtCore.QRect(55, 106, 281, 71))
        self.imp_ep.setObjectName("imp_ep")
        self.tabWidget.addTab(self.tab_3, "")
        self.exit_p = QtGui.QPushButton(paciente)
        self.exit_p.setGeometry(QtCore.QRect(160, 270, 85, 27))
        self.exit_p.setObjectName("exit_p")

        self.retranslateUi(paciente)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(paciente)

    def retranslateUi(self, paciente):
        paciente.setWindowTitle(QtGui.QApplication.translate("paciente", "Formulario Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("paciente", "Datos necesarios:", None, QtGui.QApplication.UnicodeUTF8))
        self.nombreLabel.setText(QtGui.QApplication.translate("paciente", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.apellidosLabel.setText(QtGui.QApplication.translate("paciente", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.rutLabel.setText(QtGui.QApplication.translate("paciente", "Ficha", None, QtGui.QApplication.UnicodeUTF8))
        self.agr_ap.setText(QtGui.QApplication.translate("paciente", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("paciente", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.buscarRutLabel.setText(QtGui.QApplication.translate("paciente", "Buscar Rut", None, QtGui.QApplication.UnicodeUTF8))
        self.bcr1_mp.setText(QtGui.QApplication.translate("paciente", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.nombresLabel.setText(QtGui.QApplication.translate("paciente", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.apellidosLabel_2.setText(QtGui.QApplication.translate("paciente", "Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.correoLabel.setText(QtGui.QApplication.translate("paciente", "Ficha", None, QtGui.QApplication.UnicodeUTF8))
        self.mdf_mp.setText(QtGui.QApplication.translate("paciente", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("paciente", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.buscarRutLabel_2.setText(QtGui.QApplication.translate("paciente", "Buscar Rut", None, QtGui.QApplication.UnicodeUTF8))
        self.elm_ep.setText(QtGui.QApplication.translate("paciente", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.imp_ep.setText(QtGui.QApplication.translate("paciente", "<html><head/><body><p align=\"center\">Despliegue de informacion a eliminar</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("paciente", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_p.setText(QtGui.QApplication.translate("paciente", "Volver", None, QtGui.QApplication.UnicodeUTF8))

