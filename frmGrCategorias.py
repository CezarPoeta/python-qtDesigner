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

def addTableRow(self, table, row_data):
    row = table.rowCount()
    table.setRowCount(row+1)

    col = 0
    for item in row_data:
        cell = QtWidgets.QTableWidgetItem(str(item))
        table.setItem(row, col, cell)
        col += 1

def CarregarGrCategorias(self):
    table = QtWidgets.QTableWidget(self)
        
    table.rowCount()
    row_1 = ['001', 'John']
    row_2 = ['002', 'Lily']
    row_3 = ['003', 'Kate']
    row_4 = ['004', 'Tom']

    addTableRow(table, row_1)
    addTableRow(table, row_2)
    addTableRow(table, row_3)
    addTableRow(table, row_4)


app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmGrCategorias.ui')

Bloqueia()

CarregarGrCategorias(formulario) 

#formulario.show()

app.exec()