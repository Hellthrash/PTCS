# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid.ui'
#
# Created: Sun Aug 30 19:06:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Grid(object):
    def setupUi(self, Grid):
        Grid.setObjectName("Grid")
        Grid.resize(775, 545)
        self.verticalLayout = QtGui.QVBoxLayout(Grid)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Grid)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(463, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_edit = QtGui.QPushButton(self.widget)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_delete = QtGui.QPushButton(self.widget)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.verticalLayout.addWidget(self.widget)
        self.table = QtGui.QTableView(Grid)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)

        self.retranslateUi(Grid)
        QtCore.QMetaObject.connectSlotsByName(Grid)

    def retranslateUi(self, Grid):
        Grid.setWindowTitle(QtGui.QApplication.translate("Grid", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("Grid", "Administrar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("Grid", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))

