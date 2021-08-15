from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from boConexaoBD import ConnectDBSQLite

banco = ConnectDBSQLite()

class GrCategorias():

    def __init__(self):
        print('Acessou Classe GrCategorias')       

    def Bloqueia(self, form):
        form.txtNome.setStyleSheet('QLineEdit {font:bold; font-size:20px; background-color:rgb(182, 182, 182)}')
        form.btnConfirmar.setStyleSheet('QPushButton {background-color: rgb(177, 180, 197); color: rgb(134, 134, 134)}')
        form.btnSair.setStyleSheet('QPushButton {background-color: rgb(177, 180, 197); color: rgb(134, 134, 134)}')


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
        cursor.execute('SELECT id, nome FROM tbgrcategorias')
        dados = cursor.fetchall()
        table = form.lstGrCategorias 

        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['Id','Name'])
        table.setColumnWidth(0, 100)
        table.setColumnWidth(1, 300)
        
        table.rowCount()
        for row in dados:
            self.addTableRow(table, row)


    def MostraForm(self, form ):
        form.show()
