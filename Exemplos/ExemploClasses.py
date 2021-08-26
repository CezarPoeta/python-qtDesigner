import sys

from PyQt5.QtWidgets import QApplication

class Hello():

    def __init__(self):
        self.message = 'Hello World'
        print('A classe foi instanciada')

    def imprime_nome(self, nome, sobrenome):
        print(nome, sobrenome)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ola = Hello()
    print(ola.message)
    ola.imprime_nome('Cezar', 'Poeta')
    sys.exit(app.exec_())