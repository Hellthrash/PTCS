# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from grid import Ui_Grid
from crtl_main import *
import model as db_model

class Vtn3(QtGui.QMainWindow):

    def iniciarP(self):
        self.ui3 = Ui_Grid()
        self.ui3.setupUi(self)
        self.load_data()
        self.show()

    def load_data(self):
        paciente = db_model.obtener_pacientes()
        self.data = QtGui.QStandardItemModel(len(paciente), 4)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"RUT"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Nombres"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Apellidos"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"Ficha"))

        for r, row in enumerate(paciente):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['rut'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['nombres'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['apellidos'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['Ficha Medica'])

        self.ui3.table.setModel(self.data)

        self.ui3.table.horizontalHeader().setResizeMode(
            1, self.ui3.table.horizontalHeader().Stretch)
        self.ui3.table.horizontalHeader().setResizeMode(
            2, self.ui3.table.horizontalHeader().Stretch)
        self.ui3.table.setColumnWidth(0, 100)
        self.ui3.table.setColumnWidth(1, 210)
        self.ui3.table.setColumnWidth(2, 210)
        self.ui3.table.setColumnWidth(3, 220)