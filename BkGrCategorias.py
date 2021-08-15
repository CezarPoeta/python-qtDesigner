import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

banco = connect('SysFinanCtrl.db')

class GrCategorias():

    def __init__(self):
        print('Acessou Classe GrCategorias')       

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)

        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    def CarregaDados(self, form):
        cursor = banco.cursor()
        cursor.execute('SELECT * FROM tbgrcategorias')
        dados = cursor.fetchall()
        table = form.lstGrCategorias 
        table.rowCount()
        for row in dados:
            self.addTableRow(table, row)


    def Bloqueia(self):
        formulario.txtNome.setStyleSheet('QLineEdit {font:bold; font-size:20px; background-color:rgb(182, 182, 182)}')
        formulario.btnConfirmar.setStyleSheet('QPushButton {background-color: rgb(177, 180, 197); color: rgb(134, 134, 134)}')
        formulario.btnSair.setStyleSheet('QPushButton {background-color: rgb(177, 180, 197); color: rgb(134, 134, 134)}')

    def MostraForm(self, form ):
        form.show()



app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmGrCategorias.ui')

frm = GrCategorias()
frm.Bloqueia()
frm.CarregaDados(formulario)
frm.MostraForm(formulario)

app.exec()