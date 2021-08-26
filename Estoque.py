from PyQt5 import uic, QtWidgets
from BD import Banco_Dados
from datetime import datetime

banco = Banco_Dados()
data = datetime.now()


class Estoque():
    def __init__(self):
        self.Tela_Estoque = uic.loadUi("tela_estoque.ui")
        self.Tela_Estoque.remover.clicked.connect(self.Excluir_Estoque)
        self.Tela_Estoque.Pesquisar.clicked.connect(self.Pesquisa)

    def Tabela_Estoque(self):
        sql = "SELECT Q.codigo, Q.nome, Q.tipo_produto, Q.quantidade, Q.data_entrada, Q.hora FROM produto P, estoque Q where P.codigo = Q.codigo"
        resultado = banco.pesquisa(sql)
        self.Tela_Estoque.tabela.setRowCount(len(resultado))
        for i in range(0, len(resultado)):
            for j in range(0, 6):
                    self.Tela_Estoque.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def Excluir_Estoque(self):
        # Exclui o produto da tabela
        linha = self.Tela_Estoque.tabela.currentRow()  # id da linha selsecionada
        self.Tela_Estoque.tabela.removeRow(linha)

        # Exclui o produto do estoque
        sql = "SELECT id FROM trabalho_gestor_fornecedores.estoque"
        resultado = banco.pesquisa(sql)
        id_excluir = resultado[linha][0]  # Pega o codigo do produto da linha selecionada
        sql = "DELETE FROM trabalho_gestor_fornecedores.estoque WHERE id =" + str(id_excluir)
        banco.deletar(sql)

    def Pesquisa(self):
        # Pega o codigo digitado e preenche a tabela
        codigo = self.Tela_Estoque.lineEdit.text()
        sql = "SELECT Q.codigo, Q.nome, Q.tipo_produto, Q.quantidade, Q.data_entrada, Q.hora FROM produto P, estoque Q where P.codigo = Q.codigo AND Q.codigo ="+str(codigo)
        resultado = banco.pesquisa(sql)

        self.Tela_Estoque.tabela.setRowCount(len(resultado))
        for i in range(0, len(resultado)):
            for j in range(0, 6):
                    self.Tela_Estoque.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def Menu_Estoque(self):
        self.Tela_Estoque.lineEdit.setText("Para filtrar um produto, digite seu código.")
        self.Tela_Estoque.show()
        self.Tabela_Estoque()
