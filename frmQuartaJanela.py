#Controle do frm com o Python

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

valor_max = 100
valor = 0


def funcao_listar():
    global valor
    dadolido = formulario.lineEdit.text()
    if dadolido == '': 
        QMessageBox.about(formulario, 'Minha Mensagem','Precisa informar um Dado')
    else:

        valor = valor + 10

        if valor <= valor_max:
            formulario.listWidget.addItem(dadolido)
            formulario.progressBar.setValue(valor)
            formulario.lineEdit.setText('')
        else:    
            QMessageBox.about(formulario,'Minha Mensagem', 'No máximo 10 Nomes')


def funcao_excluir():
    global valor
    valor = 0
    formulario.listWidget.clear()
    formulario.progressBar.setValue(valor)


def pegar_data():
    global valor
    data = str(formulario.calendarWidget.selectedDate())
    dataformatada = data[19:30]
    valor = valor + 10

    if valor <= valor_max:
        formulario.listWidget.addItem(dataformatada)
        formulario.progressBar.setValue(valor)
        formulario.lineEdit.setText('')
    else:    
        QMessageBox.about(formulario,'Minha Mensagem', 'No máximo 10 Nomes')


def chama_form():
    formulario2.show()


app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmListW.ui')
formulario2=uic.loadUi('frmDois.ui')
formulario.pushButton.clicked.connect(funcao_listar)
formulario.pushButton_2.clicked.connect(funcao_excluir)
formulario.pushButton_3.clicked.connect(chama_form)
formulario.calendarWidget.selectionChanged.connect(pegar_data)


formulario.show()


app.exec()