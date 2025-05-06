from models.biblioteca import Biblioteca
from models.itens.livro import Livro
from models.itens.revista import Revista


biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")
biblioteca_barreiro = Biblioteca("Biblioteca do Barreiro")

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 39.90, "978-3-16-148410-0")
revista1 = Revista("Revista de Ciência", "Revista Científica", 19.90, "Edição 1")
# biblioteca_cidade.alterna_estado()
# biblioteca_shopping.alterna_estado()
# biblioteca_barreiro.alterna_estado()

# biblioteca_cidade.receber_avaliacao("Cliente 1", 5)
# biblioteca_cidade.receber_avaliacao("Cliente 2", 4)
# biblioteca_shopping.receber_avaliacao("Cliente 3", 3)



def main():
    # Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
if __name__ == "__main__":
    main()