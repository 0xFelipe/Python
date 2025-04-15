class Aluno:
    def __init__ (self,nome):
        self.nome = nome
        self.nota = []

    def adicionar_nota(self, nota):
        self.nota.append(nota)
    
    def media_nota(self):
        self.media_nota = sum(self.nota) / len(self.nota)
        return self.media_nota
    
    def status(self):
        media = self.media_nota()
        if media >= 7:
            print(f"Nome: {self.nome} | Notas:{self.nota} | Média: {media} | Aprovado")
        elif media < 7 and media >= 5:
            print(f"Nome: {self.nome} | Notas:{self.nota} | Média: {media} | Recuperação")
        else:
            print(f"Nome: {self.nome} | Notas:{self.nota} | Média: {media} | Reprovado") 

aluno1 = Aluno("Maria")
aluno1.adicionar_nota(1)
aluno1.adicionar_nota(5)
aluno1.status()