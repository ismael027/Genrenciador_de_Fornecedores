from PyQt5 import uic, QtWidgets
from Produto import Produto
from Fornecedor import Fornecedores
from Estoque import Estoque
from Compra import Compra
from BD import Banco_Dados

banco = Banco_Dados()


app=QtWidgets.QApplication([])


def Entrar():
    nome = Tela_Login.lineEdit.text()
    senha = Tela_Login.lineEdit_2.text()

    if len(nome) == 0 or len(senha) == 0:
        Tela_Login.label_4.setText("Complete todos os campos!")
        
    else:
        sql = """SELECT senha FROM trabalho_gestor_fornecedores.login WHERE usuario ='"""+ nome +"""'"""
        dados = banco.pesquisa(sql)
        resultado = dados[0][0]

        if resultado == senha:
            Tela_Login.label_4.setText("Sucesso!")
            Tela_Login.close()
            Tela_Principal.show()
 
        else:
            Tela_Login.label_4.setText("Nome ou senha incorretos!")
    
def Cadastro():
    nome = Tela_Cadastro.lineEdit.text()
    senha = Tela_Cadastro.lineEdit_2.text()
    confirm_senha = Tela_Cadastro.lineEdit_3.text()

    if len(nome) == 0 or len(senha) == 0 or len(confirm_senha) ==0:
        Tela_Cadastro.label_5.setText("Complete todos os campos!")
    elif nome == senha:
        Tela_Cadastro.label_5.setText("Insira nome e senha diferentes!")
    elif senha != confirm_senha:
        Tela_Cadastro.label_5.setText("Senhas diferentes!")
    else:
        sql = "INSERT INTO trabalho_gestor_fornecedores.login (usuario, senha) VALUES (%s, %s);"
        values = (nome, senha)
        banco.inserir(sql,values)
        Tela_Cadastro.label_5.setText("Cadastro realizado com sucesso!")

def Tela():
    Tela_Cadastro.show()

#Tela Login
Tela_Login = uic.loadUi("tela_login.ui")
Tela_Cadastro = uic.loadUi("tela_cadastro.ui")
Tela_Login.Entrar.clicked.connect(Entrar)
Tela_Login.add.clicked.connect(Tela)
Tela_Login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
Tela_Cadastro.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
Tela_Cadastro.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
Tela_Login.show()

#Tela Cadastro
Tela_Cadastro.Cadastro.clicked.connect(Cadastro)
prod = Produto()
forn = Fornecedores()
estoque = Estoque()
compra = Compra()

#Telas Principal
Tela_Principal = uic.loadUi("tela_principal.ui")
Tela_Principal.Botao_Produto.clicked.connect(prod.Menu_Produto)
Tela_Principal.Botao_Fornecedor.clicked.connect(forn.Menu_Produto)
Tela_Principal.Botao_Estoque.clicked.connect(estoque.Menu_Estoque)
Tela_Principal.Botao_Compra.clicked.connect(compra.Menu_Compra)

app.exec()