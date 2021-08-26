from PyQt5 import uic, QtWidgets
from BD import Banco_Dados
from datetime import datetime

banco = Banco_Dados()
data = datetime.now()


class Estoque():
    def __init__(self):
        self.Tela_Estoque = uic.loadUi("tela_estoque.ui")
        self.Tela_CadastroEst = uic.loadUi("tela_cadastro_estoque.ui")
        self.Tela_Estoque.remover.clicked.connect(self.Excluir_Estoque)
        self.Tela_CadastroEst.Pesquisar.clicked.connect(self.Pesquisa)

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
        # Pega o codigo digitado e joga nos campos brancos os dados para alteração
        id_busca = self.Tela_CadastroEst.lineEdit_5.text()
        sql = "SELECT * FROM trabalho_gestor_fornecedores.estoque WHERE codigo =" + str(id_busca)

        result = banco.pesquisa(sql)

        self.Tela_CadastroEst.lineEdit.setText(str(result[0][0]))
        self.Tela_CadastroEst.lineEdit_2.setText(str(result[0][1]))
        self.Tela_CadastroEst.lineEdit_3.setText(str(result[0][2]))
        self.Tela_CadastroEst.lineEdit_4.setText(str(result[0][3]))

    def Menu_Cadastro(self):
        #Chama a tela de cadastro/alterar
        self.Tela_CadastroEst.show()
        #Seta a linha com o texto
        self.Tela_CadastroEst.lineEdit_5.setText('Para alterar o estoque, digite o código do produto.')
        self.Tela_CadastroEst.lineEdit_3.setText('{}'.format(data.strftime('%y/%m/%d')))
        self.Tela_CadastroEst.lineEdit_4.setText('AA/MM/DD')

    def Menu_Estoque(self):
        self.Tela_Estoque.show()
        self.Tabela_Estoque()
