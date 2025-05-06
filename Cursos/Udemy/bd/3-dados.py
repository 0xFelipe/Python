import sqlite3

# 1 - Conectar ao banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Inserir dados na tabela
cursor.execute('''
    INSERT INTO filmes(titulo, ano, nota)
    VALUES ('Os Vingadores', 2012, 8.0),
           ('Os Vingadores: A Era de Ultron', 2015, 7.3)
''')
conexao.commit()
conexao.close()
print('Dados inseridos com sucesso!')