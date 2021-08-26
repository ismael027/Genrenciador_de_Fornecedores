from PyQt5 import uic, QtWidgets
from BD import Banco_Dados
from datetime import datetime

banco = Banco_Dados()
data = datetime.now()
class Produto():
    def __init__(self):
        self.Tela_Produto = uic.loadUi("tela_produto.ui")
        self.Tela_CadastroProd = uic.loadUi("tela_cadastroprod.ui")
        self.Tela_Produto.remov_produto.clicked.connect(self.Excluir_Produto)
        self.Tela_Produto.add_produto.clicked.connect(self.Menu_Cadastro)
        self.Tela_CadastroProd.Pesquisar.clicked.connect(self.Pesquisa_Produto)
        self.Tela_CadastroProd.Alterar_produto.pressed.connect(self.Salva_Produto)
        self.Tela_CadastroProd.cadastro.pressed.connect(self.Cadastro_Produto)


    def Tabela_Produto(self):
        sql = "SELECT codigo, nome, tipo_produto, quantidade FROM trabalho_gestor_fornecedores.produto"
        resultado = banco.pesquisa(sql)
        self.Tela_Produto.tabela_produtos.setRowCount(len(resultado))
        for i in range(0, len(resultado)):
            for j in range(0, 4):
                self.Tela_Produto.tabela_produtos.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def Cadastro_Produto(self):
        #Insere o novo produto no bando de dados
        codigo = self.Tela_CadastroProd.lineEdit.text()
        nome = self.Tela_CadastroProd.lineEdit_2.text()
        tipo = self.Tela_CadastroProd.lineEdit_3.text()
        quantidade = self.Tela_CadastroProd.lineEdit_4.text()
        #Cadastra no produto
        sql = "INSERT INTO trabalho_gestor_fornecedores.produto (codigo, tipo_produto, nome, quantidade) VALUES (%s,%s,%s,%s)"
        dado = (str(codigo), str(tipo), str(nome), str(quantidade))
        banco.inserir(sql,dado)

        #Cadastra no estoque
        data_entrada = data
        hora = data.strftime('%H:%M:%S')
        sql = "INSERT INTO trabalho_gestor_fornecedores.estoque (codigo, data_entrada, hora, quantidade) VALUES (%s,%s,%s,%s)"
        values = (codigo, data_entrada, hora, quantidade)
        banco.inserir(sql,values)
        self.Tabela_Produto()

    def Excluir_Produto(self):
        #Exclui o produto da tabela
        linha = self.Tela_Produto.tabela_produtos.currentRow() #id da linha selsecionada
        self.Tela_Produto.tabela_produtos.removeRow(linha)

        #Exclui o produto do banco de dados
        sql = "SELECT codigo FROM trabalho_gestor_fornecedores.produto"
        resultado = banco.pesquisa(sql)
        id_excluir = resultado[linha][0]#Pega o codigo do produto da linha selecionada
        sql = "DELETE FROM trabalho_gestor_fornecedores.produto WHERE codigo ="+str(id_excluir)
        banco.deletar(sql)

    def Salva_Produto(self):
        id_busca = self.Tela_CadastroProd.lineEdit_5.text()
        nome = self.Tela_CadastroProd.lineEdit_2.text()
        tipo = self.Tela_CadastroProd.lineEdit_3.text()
        quantidade = self.Tela_CadastroProd.lineEdit_4.text()
        sql = """UPDATE trabalho_gestor_fornecedores.produto SET tipo_produto ='""" + tipo + """', nome = '""" + nome + """', quantidade =""" + str(quantidade) + """ WHERE codigo = """ + str(id_busca)
        banco.alterar(sql)

        #Salva na tabela estoque
        data_entrada = data
        hora = data.strftime('%H:%M:%S')
        sql = "INSERT INTO trabalho_gestor_fornecedores.estoque (codigo, data_entrada, hora,quantidade) VALUES (%s,%s,%s,%s)"
        values = (id_busca, data_entrada, hora,quantidade)
        banco.inserir(sql,values)
        self.Tabela_Produto()

    def Pesquisa_Produto(self):
        #Pega o codigo digitado e joga nos campos brancos os dados para alteração
        id_busca = self.Tela_CadastroProd.lineEdit_5.text()
        sql = "SELECT * FROM trabalho_gestor_fornecedores.produto WHERE codigo ="+str(id_busca)

        result = banco.pesquisa(sql)

        self.Tela_CadastroProd.lineEdit.setText(str(result[0][0]))
        self.Tela_CadastroProd.lineEdit_2.setText(str(result[0][2]))
        self.Tela_CadastroProd.lineEdit_3.setText(str(result[0][1]))
        self.Tela_CadastroProd.lineEdit_4.setText(str(result[0][3]))

    def Menu_Cadastro(self):
        #Chama a tela de cadastro/alterar
        self.Tela_CadastroProd.show()
        #Coloca o texto
        self.Tela_CadastroProd.lineEdit_5.setText('Para alterar um produto, digite seu código.')

    def Menu_Produto(self):
        #Cria a tabela e preenche com os produtos do DB
        self.Tela_Produto.show()
        self.Tabela_Produto()
