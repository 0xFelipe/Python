import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# Exclusão de dados da tabela
id = (1,2)  # IDs dos filmes a serem excluídos
cursor.execute(
    """ 
        DELETE FROM filmes
        WHERE id IN (?, ?)
    """,
    id
)
conexao.commit()
conexao.close()
print('Dados excluídos com sucesso!')