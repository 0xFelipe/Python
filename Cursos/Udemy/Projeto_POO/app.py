from models.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")
biblioteca_barreiro = Biblioteca("Biblioteca do Barreiro")

biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()
# biblioteca_barreiro.alterna_estado()

biblioteca_cidade.receber_avaliacao("Cliente 1", 5)
biblioteca_cidade.receber_avaliacao("Cliente 2", 4)
biblioteca_shopping.receber_avaliacao("Cliente 3", 3)



def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()