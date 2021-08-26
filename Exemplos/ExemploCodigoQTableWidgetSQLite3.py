import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5 import QtCore

import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect

banco = connect('SysFinanCtrl.db')
cursor = banco.cursor()

cursor.execute('SELECT * FROM tbgrcategorias')
dados = cursor.fetchall()

class YuTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)

        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    def initUI(self): 
        self.setWindowTitle('PyQT Table Add Row Data Dynamically')  
        vbox = QVBoxLayout()
        
        # add table 
        table = QTableWidget(self)
        table.setColumnCount(4)
        
        table.rowCount()
        #set table header
        table.setHorizontalHeaderLabels(['id','Name','DtInsert','DtUpdate'])
      
        #add data
        for row in dados:
            self.addTableRow(table, row)

        vbox.addWidget(table)
        self.setLayout(vbox)
        self.setGeometry(300,400,500,400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = YuTextFrame()
    sys.exit(app.exec_())