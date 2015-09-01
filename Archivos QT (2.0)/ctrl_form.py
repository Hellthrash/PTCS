# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_form import Ui_Form
import model


class FormAlumno(QtGui.QDialog):

    def __init__(self, parent=None, rut=None):
        """
        Formulario para crear y editar alumnos.
        Si se recibe la var rut
        entonces se está en modo de edición.
        """
        super(FormAlumno, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if rut is None:
            self.ui.save.clicked.connect(self.crear_alumno)
        else:
            self.colocar_datos(rut)
            self.ui.save.clicked.connect(self.editar_alumno)

    def colocar_datos(self, rut):
        """
        Coloca los datos del alumno en los widgets
        para su edición
        """
        alumno = model.alumno(rut)
        self.ui.rut.setText(alumno["rut"])
        self.ui.names.setText(alumno["nombres"])
        self.ui.lastnames.setText(alumno["apellidos"])
        self.ui.email.setText(alumno["correo"])

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        rut = self.ui.rut.text()
        nombres = self.ui.names.text()
        apellidos = self.ui.lastnames.text()
        correo = self.ui.email.text()
        return (rut, nombres, apellidos, correo)

    def crear_alumno(self):
        rut, nombres, apellidos, correo = self.obtener_datos()
        try:
            model.crear_alumno(rut, nombres, apellidos, correo)
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"El alumno ha sido creado.")
            msgBox.exec_()
            self.close()
        except:
            #Tratar errores!!!!!!
            pass

    def editar_alumno(self):
        rut, nombres, apellidos, correo = self.obtener_datos()
        try:
            # Invocar la función del modelo que permite editar
            print "Editar"
        except:
            #Tratar errores!!!!!!
            pass
