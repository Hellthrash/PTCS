# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from sportal import Ui_inicio
from crtl_main import *
from ctrl_grid import *
from ui_grid import *


class Vtn2(QtGui.QMainWindow):

    def iniciar(self):
        self.ui2 = Ui_inicio()
        self.ui2.setupUi(self)
        self.botones()
        self.show()

    def botones(self):
        self.ui2.exit_i.clicked.connect(self.volver)
        self.ui2.pp_i.clicked.connect(self.pPaciente)

    def volver(self):
        self.close()
        inicio = Main()
        inicio.__init__().iniciar()

    def pPaciente(self):
        print "entro ctm"
        self.v3 = Vtn3()
        self.v3.iniciarP()



