from PyQt5 import uic, QtWidgets
from BD import Banco_Dados
from datetime import datetime
data = datetime.now()
banco = Banco_Dados()

class Compra():
    def __init__(self):
        self.Tela_Compra = uic.loadUi("tela_compra.ui")
        self.Tela_Cadastro_compra = uic.loadUi("tela_cadatro_compra.ui")
        self.Tela_Compra.remover.clicked.connect(self.Excluir_Compra)
        self.Tela_Compra.add.clicked.connect(self.Menu_Cadastro)
        self.Tela_Cadastro_compra.calcula.clicked.connect(self.Calcular)
        self.Tela_Cadastro_compra.cadastro.pressed.connect(self.Cadastro_Estoque)
        self.Tela_Cadastro_compra.Pesquisar.clicked.connect(self.Pesquisa)
        self.Tela_Cadastro_compra.save.pressed.connect(self.Salva)

    def Tabela_Compra(self):
            sql = "SELECT * FROM trabalho_gestor_fornecedores.compra"
            resultado = banco.pesquisa(sql)
            self.Tela_Compra.tabela.setRowCount(len(resultado))
            for i in range(0, len(resultado)):
                for j in range(0, 8):
                    self.Tela_Compra.tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def Excluir_Compra(self):
        # Exclui o produto da tabela
        linha = self.Tela_Compra.tabela.currentRow()  # id da linha selsecionada
        self.Tela_Compra.tabela.removeRow(linha)

        # Exclui o produto do estoque
        sql = "SELECT codigo FROM trabalho_gestor_fornecedores.compra"
        resultado = banco.pesquisa(sql)
        id_excluir = resultado[linha][0]  # Pega o codigo do produto da linha selecionada
        sql = "DELETE FROM trabalho_gestor_fornecedores.compra WHERE codigo =" + str(id_excluir)
        banco.deletar(sql)

    def Calcular(self):
        quantidade = self.Tela_Cadastro_compra.lineEdit_4.text()
        valor_unit = self.Tela_Cadastro_compra.lineEdit_6.text()
        valor_total = float(quantidade) * float(valor_unit)
        self.Tela_Cadastro_compra.lineEdit_7.setText('{}'.format(str(valor_total)))

    def Cadastro_Estoque(self):
        cnpj = self.Tela_Cadastro_compra.lineEdit_2.text()
        pagamento = self.Tela_Cadastro_compra.lineEdit_3.text()
        quantidade = self.Tela_Cadastro_compra.lineEdit_4.text()
        valor_unit = self.Tela_Cadastro_compra.lineEdit_6.text()
        valor_total = self.Tela_Cadastro_compra.lineEdit_7.text()
        descricao = self.Tela_Cadastro_compra.lineEdit_8.text()
        data_compra = self.Tela_Cadastro_compra.lineEdit_9.text()

        sql = "INSERT INTO trabalho_gestor_fornecedores.compra (codigo_fornecedor, tipo_pagamento, quantidade, valor_unitario, valor, descricao, data_compra) VALUES (%s,%s,%s, %s, %s, %s,%s)"
        values = (cnpj, pagamento, quantidade, valor_unit, valor_total, descricao, data_compra)
        banco.inserir(sql, values)
        self.Tabela_Compra()

    def Pesquisa(self):
        # Pega o codigo digitado e joga nos campos brancos os dados para alteração
        id_busca = self.Tela_Cadastro_compra.lineEdit_5.text()
        sql = "SELECT * FROM trabalho_gestor_fornecedores.compra WHERE codigo =" + str(id_busca)

        result = banco.pesquisa(sql)

        self.Tela_Cadastro_compra.lineEdit_2.setText(str(result[0][1]))
        self.Tela_Cadastro_compra.lineEdit_3.setText(str(result[0][2]))
        self.Tela_Cadastro_compra.lineEdit_4.setText(str(result[0][3]))
        self.Tela_Cadastro_compra.lineEdit_6.setText(str(result[0][4]))
        self.Tela_Cadastro_compra.lineEdit_7.setText(str(result[0][5]))
        self.Tela_Cadastro_compra.lineEdit_8.setText(str(result[0][6]))
        self.Tela_Cadastro_compra.lineEdit_9.setText(str(result[0][7]))

    def Salva(self):
        id_busca = self.Tela_Cadastro_compra.lineEdit_5.text()
        pagamento = self.Tela_Cadastro_compra.lineEdit_3.text()
        quantidade = self.Tela_Cadastro_compra.lineEdit_4.text()
        valor_unit = self.Tela_Cadastro_compra.lineEdit_6.text()
        valor_total = self.Tela_Cadastro_compra.lineEdit_7.text()
        descricao = self.Tela_Cadastro_compra.lineEdit_8.text()
        data_compra = self.Tela_Cadastro_compra.lineEdit_9.text()

        sql = """UPDATE trabalho_gestor_fornecedores.compra SET tipo_pagamento = '"""+pagamento+"""',quantidade = '"""+quantidade+"""',valor_unitario = '"""+valor_unit+"""',valor = '"""+valor_total+"""',descricao ='"""+descricao+"""',data_compra ='"""+data_compra+"""'WHERE codigo = '"""+id_busca +"""'"""
        banco.alterar(sql)
        self.Tabela_Compra()

    def Menu_Cadastro(self):
        # Chama a tela de cadastro/alterar
        self.Tela_Cadastro_compra.show()
        # Seta a linha com o texto
        self.Tela_Cadastro_compra.lineEdit_5.setText('Para alterar uma compra, digite o código da compra.')
        self.Tela_Cadastro_compra.lineEdit_9.setText('{}'.format(data.strftime('%y/%m/%d')))

    def Menu_Compra(self):
            self.Tela_Compra.show()
            self.Tabela_Compra()
