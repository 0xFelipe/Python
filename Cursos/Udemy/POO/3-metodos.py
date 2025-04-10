class Game:
    def __init__(self, name="", yearLaunch=0, multplayer=False, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multplayer = multplayer
        self.note = note

    def __str__(self):
        return f'Nome do jogo: {self.name}\nAno de Lançamento: {self.yearLaunch}\nMultiplayer: {self.multplayer}\nNota: {self.note}'

# Primeiro jogo
game1 = Game("The Last of Us", 2013, False, 10)
game2 = Game("Fortnite", 2017, True, 8)
game3 = Game("God of War", 2018, False, 9)
game4 = Game("Minecraft", 2011, True, 9)

print('\n###Dados do Jogo###\n')

print(f'Nome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}\nMultiplayer: {game1.multplayer}\nNota: {game1.note}')

print('\n###Dados do Jogo###\n')

print(f'Nome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}\nMultiplayer: {game2.multplayer}\nNota: {game2.note}')

print('\n###Dados do Jogo###\n')

print(f'Nome do jogo: {game3.name}\nAno de Lançamento: {game3.yearLaunch}\nMultiplayer: {game3.multplayer}\nNota: {game3.note}')

print('\n###Dados do Jogo###\n')

print(f'Nome do jogo: {game4.name}\nAno de Lançamento: {game4.yearLaunch}\nMultiplayer: {game4.multplayer}\nNota: {game4.note}')