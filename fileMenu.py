import sys
import Formularios

#Controle do frm com o Python

from PyQt5 import uic, QtWidgets

def funcao_principal():
    print('Modelo')


if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    formulario=uic.loadUi('frmListW.ui')

    formulario.pushButton.clicked.connect(funcao_principal)
    formulario.pushButton_3.clicked.connect(Formularios.frmPrimeiraJanela.Janela)
    formulario.show()

    sys.exit(app.exec_())
    #app.exec()