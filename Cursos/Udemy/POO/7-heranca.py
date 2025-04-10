class Game:
    total_games = 0 #Variavel de classe para contar o total de jogos
    def __init__(self, name="", yearLaunch=0, multplayer=False, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multplayer = multplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f'Nome do jogo: {self.name}\nAno de Lançamento: {self.yearLaunch}\nMultiplayer: {self.multplayer}\nNota: {self.note}'
    
    def technical_sheet(self):
        print('\n###Dados do Jogo###\n')
        print(f'Nome do jogo: {self.name}\nAno de Lançamento: {self.yearLaunch}\nMultiplayer: {self.multplayer}\nNota: {self.note}\n')

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f'A média de avaliações do jogo {self.name} é: {self.totalEvaluation / self.evaluators}')

# Classe derivada (Subclasse)
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, note=0, storyline=""):
        super().__init__(name, yearLaunch, multplayer=False, note=note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f'Enredo: {self.storyline}\n')

mult_game = Game("Fortnite", 2017, True, 8)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("The Last of Us", 2013, 10, "Sobrevivência em um mundo pós-apocalíptico")
sing_game.technical_sheet()