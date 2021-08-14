import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5 import QtCore, uic


def addTableRow(self, table, row_data):
    row = table.rowCount()
    table.setRowCount(row+1)

    col = 0
    for item in row_data:
        cell = QTableWidgetItem(str(item))
        table.setItem(row, col, cell)
        col += 1

def initUI(self): 
       
    # add table 
    table = QTableWidget(self)      
    table.rowCount()
      
    #add data
    row_1 = ['001', 'John']
    row_2 = ['002', 'Lily']
    row_3 = ['003', 'Kate']
    row_4 = ['004', 'Tom']

    self.addTableRow(table, row_1)
    self.addTableRow(table, row_2)
    self.addTableRow(table, row_3)
    self.addTableRow(table, row_4)

    self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    formulario=uic.loadUi('frmGrCategorias.ui')
    
    initUI()

    sys.exit(app.exec_())