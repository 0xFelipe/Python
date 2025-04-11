class Game:
    def __init__(self, name="", yearLaunch=0, multplayer=False, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multplayer = multplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f'Nome do jogo: {self.name}\nAno de Lançamento: {self.yearLaunch}\nMultiplayer: {self.multplayer}\nNota: {self.note}'
    
    def technical_sheet(self):
        print('\n###Dados do Jogo###\n')
        print(f'Nome do jogo: {self.name}\nAno de Lançamento: {self.yearLaunch}\nMultiplayer: {self.multplayer}\nNota: {self.note}\n')

    class GameStudio:
        def __init__(self, name=""):
            self.name = name
            self.games = []
        
        def add_game(self, game):
            self.games.append(game)

        def evaluate_studio_quality(self):
            total_notes = sum(game.note for game in self.games)
            num_games = len(self.games)
            if num_games == 0:
                print(f"Estúdio {self.name} não tem jogos lançados")
            else:
                average_note = total_notes / num_games
                print(f"A média de notas dos jogos do estúdio {self.name} é: {average_note:.2f}")

game1 = Game("The Last of Us", 2013, False, 10)
game2 = Game("Fortnite", 2017, True, 8)
game3 = Game("God of War", 2018, False, 9)
game4 = Game("Minecraft", 2011, True, 9)


studio = Game.GameStudio("Naughty Dog")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()