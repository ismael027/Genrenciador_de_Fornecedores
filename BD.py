import mysql.connector
from mysql.connector import errorcode
from PyQt5 import uic

class Banco_Dados():
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "123456"
        self.database = "trabalho_gestor_fornecedores"

    def Aviso(self,frase):
        self.Tela_Aviso = uic.loadUi("Aviso_Confirmação.ui")
        self.Tela_Aviso.lineEdit.setText("")
        self.Tela_Aviso.lineEdit.setText(str(frase))
        self.Tela_Aviso.show()

    def conecta(self):
        try:
            self.conexao_bd = mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.Aviso('Nome de usuário ou senha incorretos!')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.Aviso('Banco de dados não existe!')
            else:
                self.Aviso('Erro: {}'.format(str(err)))

        self.cur = self.conexao_bd.cursor()

    def desconecta(self):
        self.cur.close()
        self.conexao_bd.close()

    def pesquisa(self, sql):
        try:
            self.conecta()
            self.cur.execute(sql)
            resultado = self.cur.fetchall()
            self.desconecta()
            return resultado
        except mysql.connector.Error as erro:
            self.Aviso("Falha ao pesquisar: {}".format(erro))

    def deletar(self, sql):
        try:
            self.conecta()
            self.cur.execute(sql)
            self.conexao_bd.commit()
            self.desconecta()
            self.Aviso('Remoção realizada com sucesso!!')
        except mysql.connector.Error as erro:
            self.Aviso("Falha ao remover: {}".format(erro))

    def alterar(self, sql):
        try:
            self.conecta()
            self.cur.execute(sql)
            self.conexao_bd.commit()
            self.desconecta()
            self.Aviso("Alteração realizada com sucesso!!")
        except mysql.connector.Error as erro:
            self.Aviso("Falha ao alterar: {}".format(erro))

    def inserir(self,sql, value):
        try:
            self.conecta()
            self.cur.execute(sql,value)
            self.conexao_bd.commit()
            self.desconecta()
            self.Aviso('Inserido com sucesso!!')
        except mysql.connector.Error as erro:
            self.Aviso("Falha ao inserir: {}".format(erro))
