class Biblioteca:
    nome = ""
    ativo = False;

biblioteca_cidade = Biblioteca()
biblioteca_cidade.nome = "Biblioteca da Cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = Biblioteca()

bibliotecas = [biblioteca_cidade, biblioteca_shopping]
print(vars(biblioteca_shopping))
print(vars(biblioteca_cidade))

for biblioteca in bibliotecas:
    print(vars(biblioteca))