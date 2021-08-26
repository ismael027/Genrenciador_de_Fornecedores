# Gerenciador_Fornecedores, Projeto realizado para Diciplina de Engenharia de Software II

# Requisitos
É necessário ter o PyQT5 tools intalado e o Python MySQL.\
Para instalar o PyQT5 digite no teminal o seguinte comando:\
pip install pyqt5

Depois digite o seguinte código para baixar a extensão tools:\
pip install pyqt5-tools

Para instalar o MySQL é so baixar o MySQL Workbench:\
https://dev.mysql.com/downloads/workbench/ 

Para se conectar ao banco de dados edite a  classe Banco_Dados do arquivo BD.py\
que conecta com o banco de dados, de acordo com a criação da sua máquina:
ex.:\
host = "localhost"\
user = "root"\
password = "123456"\
database = "trabalho_gestor_fornecedores"
# Descrição
O Sistema desenvolvido tem como objetivo gerenciar informações sobre fornecedores. Seus produtos, endereço, informações sobre a compra e quantidade de produtos armazenados em estoque para uma empresa, podendo realizar operações de inserção, remoção, alteração e visualização dos dados armazenados.
Inicialmente pensamos em uma empresa de distribuição alimentícia (uma loja de doces).
Para realização do projeto utilizamos o SGBD MySQL para o armazenamento dos dados requisitados.
