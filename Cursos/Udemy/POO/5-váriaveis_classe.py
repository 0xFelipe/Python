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

# Primeiro jogo
game1 = Game("The Last of Us", 2013, False, 10)
game2 = Game("Fortnite", 2017, True, 8)
game3 = Game("God of War", 2018, False, 9)
game4 = Game("Minecraft", 2011, True, 9)
game1.technical_sheet()
game1.evaluate(9)
game1.evaluate(10)
game1.average()

# Exibindo o numero total de jogos criados
print(f'Total de jogos criados: {Game.total_games}')