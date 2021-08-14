import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
from PyQt5 import uic, QtWidgets

banco = connect('SysFinanCtrl.db')
cursor = banco.cursor()

cursor.execute('SELECT * FROM tbgrcategorias')

def Bloqueia():
    formulario.txtNome.setStyleSheet('QLineEdit {font:bold; font-size:20px; background-color:rgb(182, 182, 182)}')
    formulario.btnConfirmar.setStyleSheet('QPushButton {background-color: rgb(177, 180, 197); color: rgb(134, 134, 134)}')
    formulario.btnSair.setStyleSheet('QPushButton {background-color: rgb(177, 180, 197); color: rgb(134, 134, 134)}')


def CarregarGrCategorias():
    
    for i in cursor.fetchall():
        print(i[0],i[1])


app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmGrCategorias.ui')

Bloqueia()

#print(formulario.lstGrCategorias.setItem(0, 0, QtWidgets.QTableWidgetItem('teste')))
print(dir(formulario.lstGrCategorias.rowCount()))
#CarregarGrCategorias() 

#formulario.show()

app.exec()