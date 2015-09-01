# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_form2 import Ui_Form
import model


class FormCitas(QtGui.QDialog):

    def __init__(self, parent=None, paciente_rut=None, medico_rut = None,
        fecha = None, sintomas = None, diagnostico = None, recomendaciones = None,
        receta = None):
        super(FormCitas, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if paciente_rut is None:# Cuando no recibe rut crea, cuando recibe edita
            self.ui.save.clicked.connect(self.crear_ct)
        else:
            self.colocar_datos(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
            self.ui.save.clicked.connect(self.editar_cita)

    def colocar_datos(self, paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta):
        #ingresa los datos de los medicos en las grillas

        self.ui.p_rut.setText(str(paciente_rut))
        self.ui.m_rut.setText(str(medico_rut))
        self.ui.fecha.setText(fecha)
        self.ui.sintoma.setText(sintomas)
        self.ui.diagnostico.setText(diagnostico)
        self.ui.recomendaciones.setText(recomendaciones)
        self.ui.receta.setText(receta)

    def obtener_datos(self):
        #obtiene los datos del medico del formulario
        paciente_rut = self.ui.p_rut.text()
        medico_rut = self.ui.m_rut.text()
        fecha = self.ui.fecha.text()
        sintomas = self.ui.sintoma.text()
        diagnostico = self.ui.diagnostico.text()
        recomendaciones = self.ui.recomendaciones.text()
        receta = self.ui.receta.text()
        return (paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)

    def crear_ct(self):
        paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta = self.obtener_datos()
        print(paciente_rut)
        print(medico_rut)
        print(fecha)
        print(sintomas)
        print(diagnostico)
        print(recomendaciones)
        print(receta)

        try:
            model.agregar_cita(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"La cita ha sido creada.")
            msgBox.exec_()
            self.close()
        except(ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass

    def editar_cita(self):

        paciente_rut, medico_rut, fecha, sintomas, diagnostico, recomendaciones, receta = self.obtener_datos()
        try:
            model.editar_cita(paciente_rut,medico_rut,fecha,sintomas,diagnostico,recomendaciones,receta)
            print "Editar"
        except (ValueError, IOError):
            errorMessageDialog = QtGui.QMessageBox(self)
            self.errorMessageDialog.setText("Debe Completar los campos correctamente")
            self.errorMessageDialog.exec_()
            pass
