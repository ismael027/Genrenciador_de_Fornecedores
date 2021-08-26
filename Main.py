from PyQt5 import uic, QtWidgets
from Produto import Produto
from Fornecedor import Fornecedores
from Estoque import Estoque
from Compra import Compra

app=QtWidgets.QApplication([])

#telas Produto
Tela_Principal = uic.loadUi("tela_principal.ui")

Tela_Principal.show()
prod = Produto()
forn = Fornecedores()
estoque = Estoque()
compra = Compra()

#Botões Produto
Tela_Principal.Botao_Produto.clicked.connect(prod.Menu_Produto)
Tela_Principal.Botao_Fornecedor.clicked.connect(forn.Menu_Produto)
Tela_Principal.Botao_Estoque.clicked.connect(estoque.Menu_Estoque)
Tela_Principal.Botao_Compra.clicked.connect(compra.Menu_Compra)
app.exec()