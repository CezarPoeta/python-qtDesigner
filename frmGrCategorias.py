from PyQt5 import uic, QtWidgets
import boGrCategorias

app = QtWidgets.QApplication([])

formulario=uic.loadUi('frmGrCategorias.ui')

frm = boGrCategorias.GrCategorias()
frm.Bloqueia(formulario)
frm.CarregaDados(formulario)
frm.MostraForm(formulario)

app.exec()