movieName = "The Godfather"
gameName = "The Sims"

# string [inicio:fim] - índice começa na posição 0 / ídice final -1
print(movieName[0:1]) # T
print(movieName[1:2]) # h
print(movieName[2:3]) # e
print(movieName[0:3]) # The
print(f"{movieName[0:3]} {gameName[4:]}  ") # Formando um nome de jogo com as strings

# Incremento
print(movieName[::2]) # Pega de 2 em 2 caracteres

# Inversão
print(gameName[::-1]) # Inverte a string