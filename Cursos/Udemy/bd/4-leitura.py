import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# Leitura dos dados da tabela
dados = cursor.execute('SELECT * FROM filmes').fetchall()
print(dados)