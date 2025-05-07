import sqlite3

# Conexão com o banco de dados
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# inserir dados no banco de dados

def inserir_dados(titulo, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO filmes(titulo, ano, nota)
    VALUES (?, ?, ?)
''', (titulo, ano, nota)
)
    conexao.commit()
    conexao.close()

# Listar dados do banco de dados

def obtendo_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    conexao.close()
    return dados

    
