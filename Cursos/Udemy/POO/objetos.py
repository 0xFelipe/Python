class Game:
    name = ""
    yearLaunch = 0
    multplayer = False
    note = 0

# Primeiro jogo
game1 = Game()
game1.name = "The Last of Us"
game1.yearLaunch = 2013
game1.multplayer = False
game1.note = 10

print('\n###Dados do Jogo###\n')
print(f'Nome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}\nMultiplayer: {game1.multplayer}\nNota: {game1.note}')

# Segundo jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multplayer = True
game2.note = 8

print('\n###Dados do Jogo###\n')
print(f'Nome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}\nMultiplayer: {game2.multplayer}\nNota: {game2.note}')

# Terceiro jogo
game3 = Game()
game3.name = "God of War"
game3.yearLaunch = 2018
game3.multplayer = False
game3.note = 9

print('\n###Dados do Jogo###\n')
print(f'Nome do jogo: {game3.name}\nAno de Lançamento: {game3.yearLaunch}\nMultiplayer: {game3.multplayer}\nNota: {game3.note}')

# Quarto jogo
game4 = Game()
game4.name = "Minecraft"
game4.yearLaunch = 2011
game4.multplayer = True
game4.note = 9

print('\n###Dados do Jogo###\n')
print(f'Nome do jogo: {game4.name}\nAno de Lançamento: {game4.yearLaunch}\nMultiplayer: {game4.multplayer}\nNota: {game4.note}')