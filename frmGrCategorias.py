import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela (QMainWindow):

    def __init__(self):
    
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Hello World"

        self.caixatexto = QLineEdit(self)
        self.caixatexto.move(25, 20)
        self.caixatexto.resize(250, 50)

        botao1 = QPushButton('Botão 1', self)
        botao1.move(150, 200)
        botao1.resize(150, 80)
        botao1.setStyleSheet('QPushButton {background-color:"blue"; font:bold; font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botaocaixa = QPushButton('Enviar Texto', self)
        botaocaixa.move(550, 200)
        botaocaixa.resize(150, 80)
        botaocaixa.setStyleSheet('QPushButton {background-color:"blue"; font:bold; font-size:20px}')
        botaocaixa.clicked.connect(self.mostra_texto)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(350, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color:"red"; font:bold; font-size:20px}')
        botao2.clicked.connect(self.botao2_click)
        
        self.label1 = QLabel(self)
        self.label1.setText('Aperte um dos Botões Abaixo!')
        self.label1.move(50, 100)
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px; color:"black"}')
        self.label1.resize(400, 30)

        self.labelcaixa = QLabel(self)
        self.labelcaixa.setText('Aperte um dos Botões Abaixo!')
        self.labelcaixa.move(450, 100)
        self.labelcaixa.setStyleSheet('QLabel {font:bold; font-size:20px; color:"black"}')
        self.labelcaixa.resize(400, 30)
        self.labelcaixa.setText("Digitou: ")

        #Para ser acessado fora da classe precisa colocar o self na frente do label
        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.carro.resize(400, 200)
        self.CarregarJanela()


    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        #print('o Botão 1 foi clicado')
        self.label1.setText("O Botão 1 foi Clicado")
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px; color:"green"}')
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))

    def botao2_click(self):
        #print('o Botão 2 foi clicado')
        self.label1.setText("O Botão 2 foi Clicado")
        self.label1.setStyleSheet('QLabel {font:bold; font-size:20px; color:"red"}')
        self.carro.setPixmap(QtGui.QPixmap('carro2.png'))

    def mostra_texto(self):
        conteudo = self.caixatexto.text()
        self.labelcaixa.setText("Digitou: " + conteudo)
        

aplicacao = QApplication(sys.argv)

j = Janela()

sys.exit(aplicacao.exec_())