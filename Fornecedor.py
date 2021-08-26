from PyQt5 import uic, QtWidgets
from BD import Banco_Dados
banco = Banco_Dados()

class Fornecedores():
    def __init__(self):
        self.Tela_Fornecedor = uic.loadUi("tela_fornecedores.ui")
        self.Tela_CadastroForn = uic.loadUi("tela_cadastro_forne.ui")
        self.Tela_Fornecedor.remover.clicked.connect(self.Excluir_Fornecedor)
        self.Tela_Fornecedor.Cadastrar.clicked.connect(self.Menu_Cadastro)
        self.Tela_CadastroForn.add.pressed.connect(self.Cadastro_Fornecedor)
        self.Tela_CadastroForn.Pesquisar.clicked.connect(self.Pesquisa)
        self.Tela_CadastroForn.Salvar.pressed.connect(self.Salva)

    def Tabela_Fornecedor(self):
        sql = "SELECT F.cnpj,F.nome, F.email, F.telefone, F.codigo_produto, E.rua, E.numero,E.bairro,E.cidade, E.estado,E.cep FROM fornecedor F, endereco E WHERE F.cnpj = E.cnpj;"
        resultado = banco.pesquisa(sql)
        self.Tela_Fornecedor.tabela.setRowCount(len(resultado))
        for i in range(0, len(resultado)):
            for j in range(0, 11):
                self.Tela_Fornecedor.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def Cadastro_Fornecedor(self):
        cnpj = self.Tela_CadastroForn.lineEdit.text()
        nome = self.Tela_CadastroForn.lineEdit_2.text()
        email = self.Tela_CadastroForn.lineEdit_3.text()
        telefone = self.Tela_CadastroForn.lineEdit_4.text()
        codigo_prod = self.Tela_CadastroForn.lineEdit_6.text()
        rua = self.Tela_CadastroForn.lineEdit_7.text()
        numero = self.Tela_CadastroForn.lineEdit_8.text()
        bairro = self.Tela_CadastroForn.lineEdit_9.text()
        cidade = self.Tela_CadastroForn.lineEdit_10.text()
        estado = self.Tela_CadastroForn.lineEdit_11.text()
        cep = self.Tela_CadastroForn.lineEdit_12.text()

        #Cadastra o Fornecedor
        sql = "INSERT INTO trabalho_gestor_fornecedores.fornecedor (cnpj, nome, email, telefone, codigo_produto) VALUES (%s,%s,%s,%s,%s)"
        values = (cnpj, nome, email, telefone, codigo_prod)
        banco.inserir(sql,values)
        #Cadastra o Endereço
        sql = "INSERT INTO trabalho_gestor_fornecedores.endereco (cnpj, rua, numero, bairro, cidade, estado, cep) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (cnpj, rua, numero, bairro, cidade, estado, cep)
        banco.inserir(sql, values)
        self.Tabela_Fornecedor()

    def Excluir_Fornecedor(self):
        # Exclui o fornecedor da tabela
        linha = self.Tela_Fornecedor.tabela.currentRow()  # id da linha selsecionada
        self.Tela_Fornecedor.tabela.removeRow(linha)

        # Exclui o produto do banco de dados
        sql = "SELECT cnpj FROM trabalho_gestor_fornecedores.fornecedor"
        resultado = banco.pesquisa(sql)
        id_excluir = resultado[linha][0]  # Pega o codigo do produto da linha selecionada
        #sql= "DELETE FROM trabalho_gestor_fornecedores.endereco WHERE cnpj ="+str(id_excluir)
        #banco.deletar(sql)
        sql = "DELETE FROM trabalho_gestor_fornecedores.fornecedor WHERE cnpj =" + str(id_excluir)
        banco.deletar(sql)

    def Pesquisa(self):
        # Pega o codigo digitado e joga nos campos brancos os dados para alteração
        id_busca = self.Tela_CadastroForn.lineEdit_5.text()
        sql = "SELECT F.cnpj,F.nome, F.email, F.telefone, F.codigo_produto, E.rua, E.numero,E.bairro,E.cidade, E.estado,E.cep FROM fornecedor F, endereco E WHERE F.cnpj = E.cnpj and F.cnpj = " + str(id_busca)

        result = banco.pesquisa(sql)

        self.Tela_CadastroForn.lineEdit.setText(str(result[0][0]))
        self.Tela_CadastroForn.lineEdit_2.setText(str(result[0][1]))
        self.Tela_CadastroForn.lineEdit_3.setText(str(result[0][2]))
        self.Tela_CadastroForn.lineEdit_4.setText(str(result[0][3]))
        self.Tela_CadastroForn.lineEdit_6.setText(str(result[0][4]))
        self.Tela_CadastroForn.lineEdit_7.setText(str(result[0][5]))
        self.Tela_CadastroForn.lineEdit_8.setText(str(result[0][6]))
        self.Tela_CadastroForn.lineEdit_9.setText(str(result[0][7]))
        self.Tela_CadastroForn.lineEdit_10.setText(str(result[0][8]))
        self.Tela_CadastroForn.lineEdit_11.setText(str(result[0][9]))
        self.Tela_CadastroForn.lineEdit_12.setText(str(result[0][10]))

    def Salva(self):
        id_busca = self.Tela_CadastroForn.lineEdit_5.text()
        nome = self.Tela_CadastroForn.lineEdit_2.text()
        email = self.Tela_CadastroForn.lineEdit_3.text()
        telefone = self.Tela_CadastroForn.lineEdit_4.text()
        codigo_prod = self.Tela_CadastroForn.lineEdit_6.text()
        rua = self.Tela_CadastroForn.lineEdit_7.text()
        numero = self.Tela_CadastroForn.lineEdit_8.text()
        bairro = self.Tela_CadastroForn.lineEdit_9.text()
        cidade = self.Tela_CadastroForn.lineEdit_10.text()
        estado = self.Tela_CadastroForn.lineEdit_11.text()
        cep = self.Tela_CadastroForn.lineEdit_12.text()

        sql = """UPDATE trabalho_gestor_fornecedores.fornecedor SET nome = '""" +nome + """',email = '""" + email + """', telefone = '""" + telefone + """', codigo_produto = '""" + codigo_prod + """' WHERE cnpj = '""" + id_busca + """'"""
        banco.alterar(sql)
        sql = """UPDATE trabalho_gestor_fornecedores.endereco SET rua ='"""+rua+"""', numero = '"""+numero+"""', bairro ='"""+bairro+"""', cidade = '"""+cidade+"""',estado = '"""+estado+"""',cep ='"""+cep+"""'WHERE cnpj ='"""+id_busca+"""'"""
        banco.alterar(sql)
        self.Tabela_Fornecedor()

    def Menu_Cadastro(self):
        #Chama a tela de cadastro/alterar
        self.Tela_CadastroForn.show()
        #Seta a linha com o texto
        self.Tela_CadastroForn.lineEdit_5.setText('Para alterar um fornecedor, digite seu CNPJ.')
        self.Tela_CadastroForn.lineEdit_4.setText('(DDD)XXXX-XXXX')

    def Menu_Produto(self):
        self.Tela_Fornecedor.show()
        self.Tabela_Fornecedor()
