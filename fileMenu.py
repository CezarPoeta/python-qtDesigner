import sys
import Formularios

#Controle do frm com o Python
from PyQt5 import uic, QtWidgets

def funcao_principal():
    print('Modelo')

def chama_form():
    form2.show()

if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    formulario=uic.loadUi('Formularios\\frmListW.ui')
    form2 = uic.loadUi('Formularios\\frmSimples.ui')

    formulario.pushButton.clicked.connect(funcao_principal)
    formulario.pushButton_3.clicked.connect(chama_form)

    formulario.show()


    sys.exit(app.exec_())
