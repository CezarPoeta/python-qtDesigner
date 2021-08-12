#Controle do frm com o Python

from PyQt5 import uic, QtWidgets

def funcao_principal():
    print('Modelo')

app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmTres.ui')

#formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()

app.exec()