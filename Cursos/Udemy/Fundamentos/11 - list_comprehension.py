movieList = ["Star Wars", "Harry Potter", "O Senhor dos Anéis", "Avatar", "Titanic", "Jurassic Park"]
# 1 - Listando valores de 0 a 10 que sejam menores do que 4
for i in range(10):
    if i < 4:
        print(i)
# 2 - Listando valores de 0 a 10 que sejam menores do que 4
# Compreensão de lista
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)
# 3 - Encontrando um filme pelo nome
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print("Encerrando o programa...")
        break
    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filmes encontrados: {searchName}")
        for foundMovie in foundMovies:
            print(f"- {foundMovie}")
    else:
        print(f"Nenhum filme encontrado com esse nome. {searchName}" )
# Um aprendizado nessa aula, no python caso a indentação não esteja correta, o código não é executado corretamente, diferente do Java que o código é executado mesmo com a indentação errada.
   