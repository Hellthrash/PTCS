# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from sportal import Ui_inicio
#from crtl_main import Main

class Vtn2(QtGui.QMainWindow):
    def __init__(self):
        super(Vtn2, self).__init__()
        self.ui2 = Ui_inicio()
        self.ui2.setupUi(self)
        self.botones()
        self.show()

    def botones(self):
        self.ui2.exit_i.clicked.connect(self.volver)

    def volver(self):
        inicio = Main()
        inicio.__init__().show()



#def run():
#    app = QtGui.QApplication(sys.argv)
#    main = Vtn2()
#    sys.exit(app.exec_())
