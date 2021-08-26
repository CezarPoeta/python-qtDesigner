#Controle do frm com o Python

from PyQt5 import uic, QtWidgets

def funcao_principal():
    if formulario.radioButton.isChecked():
        opcao = 'Azul'
    elif formulario.radioButton_2.isChecked():    
        opcao = 'Amarelo' 
    elif formulario.radioButton_3.isChecked():    
        opcao = 'Verde' 
    elif formulario.radioButton_4.isChecked():    
        opcao = 'Vermelho' 
    else:
        opcao = 'Nenhuma Cor Foi Escolhida' 

    formulario.label_2.setText(opcao)


app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmTres.ui')
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()

app.exec()