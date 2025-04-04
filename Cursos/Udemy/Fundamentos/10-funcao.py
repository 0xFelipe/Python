# 1 - Função para imprimir uma mensagem
def welcome():
    print("Bem-vindo ao programa de filmes!")


welcome()

#2 - Função para calcular a media de notas

def calculate_average():
    num_ratings = int(input("Digite o número de avaliaçoes que deseja atribuir:\n"))
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Digite a nota {i + 1}:\n"))
        total += note
    
    if num_ratings > 0:
        average = total / num_ratings
        print(f"A média das notas é: {average:.2f}")
    else:
        print("Nenhuma nota foi informada.")
    return average
calculate_average()

# 3 - Função para cadastrar um filme
def register_movie():
    movie_name = input("Digite o nome do filme:\n")
    release_year = int(input("Digite o ano de lançamento:\n"))
    rating = float(input("Digite a nota do filme:\n"))
    is_watched = input("Você já assistiu ao filme? (s/n):\n").lower() == "s"
    
    movie_data = {
        "name": movie_name,
        "year": release_year,
        "rating": rating,
        "watched": is_watched
    }
    
    return movie_data
filme = register_movie()
print(f"Filme cadastrado: {filme['name']} ({filme['year']}) - Nota: {filme['rating']} - Assistido: {'Sim' if filme['watched'] else 'Não'}")