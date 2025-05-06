import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Atualizar dados na tabela
id = 2 # ID do filme a ser atualizado
cursor.execute(
    '''
        UPDATE filmes SET titulo = ?, ano = ?, nota = ?
        WHERE id = ?
        
    ''',
    ('Homem Aranha', 2018, 7.4, id)
               )

conexao.commit()

print('Dados atualizados com sucesso!')