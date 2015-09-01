# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_form import Ui_Form
import model


class FormPaciente(QtGui.QDialog):

    def __init__(self, parent=None, rut=None):
        super(FormPaciente, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if rut is None:# Cuando no recibe rut crea, cuando recibe edita
            self.ui.save.clicked.connect(self.crear_paciente)
        else:
            self.colocar_datos(rut)
            self.ui.save.clicked.connect(self.editar_alumno)

    def colocar_datos(self, rut):
        #ingresa los datos de los pacientes en las grillas
        alumno = model.alumno(rut)
        self.ui.rut.setText(alumno["rut"])
        self.ui.names.setText(alumno["nombres"])
        self.ui.lastnames.setText(alumno["apellidos"])
        self.ui.email.setText(alumno["ficha"])

    def obtener_datos(self):
        #obtiene los datos del paciente del formulario
        rut = self.ui.rut.text()
        nombres = self.ui.names.text()
        apellidos = self.ui.lastnames.text()
        ficha = self.ui.email.text()
        return (rut, nombres, apellidos, ficha)

    def crear_paciente(self):
        rut, nombres, apellidos, ficha = self.obtener_datos()
        print (rut)
        print (nombres)
        print (apellidos)

        try:
            model.agregar_paciente(rut, nombres, apellidos, ficha)
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"El alumno ha sido creado.")
            msgBox.exec_()
            self.close()
        except(ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass

    def editar_alumno(self):
        rut, nombres, apellidos, ficha = self.obtener_datos()
        try:
            model.editar_paciente(rut, nombre, apellidos, ficha)
            print "Editar"
        except (ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass
