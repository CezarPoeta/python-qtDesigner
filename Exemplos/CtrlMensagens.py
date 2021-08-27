import sys

'''

sys.path.append('C:\\SysFinanCtrl')
sys.path.append('C:\\SysFinanCtrl\\Modulos')
sys.path.append('C:\\SysFinanCtrl\\Formularios')
sys.path.append('C:\\SysFinanCtrl\\ModulosClasses')


'''

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Modulos.mDataBase import connectDBSQLite
import Formularios

def cmdGrupoCategorias_Click():
    Formularios.frmGrCategorias.F_GrCategorias(frmGrC)
    frmGrC.show()


def cmdCategorias_Click():
    QtWidgets.QMessageBox.about(form, 'Alerta','Testando o botão: Categorias')
    print('Testando o botão: Categorias')
#    frmCategorias.Show

def cmdBeneficiarios_Click():
    print('Testando o botão: Beneficiarios')
#    frmBeneficiarios.Show

def cmdClientes_Click():
    QtWidgets.QMessageBox.question(form, '', 'Do you like coffee?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
    print('Testando o botão: Clientes')
#    frmClientes.Show

def cmdContaPeriodos_Click():
    msg = QMessageBox()
    msg.setWindowTitle('Meu Título!')
    msg.setText('Texto da mensagem!')
    msg.setInformativeText('Texto Informativo!')
#    msg.setIcon(QMessageBox.Critical)
#    msg.setIcon(QMessageBox.Question)
#    msg.setIcon(QMessageBox.Warning)
    msg.setIcon(QMessageBox.Information)
    msg.setStyleSheet("QLabel{min-width:500px; font-size: 24px;} QPushButton{width:250px; font-size:18px;}")
    
    msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
    resposta = msg.exec_()
    if resposta == QMessageBox.Yes:
        print('YES')
    elif resposta == QMessageBox.No:
        print('NO')
    else:
        print('CANCEL')

    print('Testando o botão: Conta x Periodos')
#    frmContaPeriodo.Show

def cmdContas_Click():
    print('Testando o botão: Contas')
#    frmContas.Show

def cmdFluxoCaixa_Click():
    print('Testando o botão: Fluxo Caixa')
#    frmFluxoCaixa.Show


def cmdLancamentos_Click():
    print('Testando o botão: Lançamentos Gerais')
#    frmFatosContabeis.Show

def cmdLancAPrazo_Click():
    print('Testando o botão: Lançamentos a Prazo')
#    frmLancAPrazo.Show

def cmdLancDiarios_Click():
    print('Testando o botão: Lançamentos Diários')
#    frmLancamento.Show

def cmdPeriodos_Click():
    print('Testando o botão: Períodos')
#    frmPeriodos.Show

def cmdPlanoContas_Click():
    print('Testando o botão: Plano Contas')
#    frmPlanoContas.Show
    

if __name__ == '__main__':

    #Inicia Aplicativo
    app = QtWidgets.QApplication(sys.argv)


    #Conecta ao Banco de Dados
#    Conn = connectDBSQLite()


    #Carrega Formulários do PyQt
    form=uic.loadUi('SysFinanCtrl.ui')
    frmGrC=uic.loadUi('frmGrCategorias.ui')




    #Mostra Menu Principal de Funções
    form.show()

    #Encerra Conexão com o Banco de Dados
#    Conn.close    
    
    #Encerra Aplicativo
    sys.exit(app.exec())