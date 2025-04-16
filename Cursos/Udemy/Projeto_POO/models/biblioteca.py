from models.avaliacao import Avaliacao
class Biblioteca:
    bibliotecas = []
    def __init__(self,nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(31)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"Nome: {biblioteca.nome.ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
      return "ativada" if self._ativo else "desativado"

    def receber_avaliacao (self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        