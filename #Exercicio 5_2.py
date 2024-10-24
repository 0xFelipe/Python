nome = input(f"insira seu nome: ")
idade = int(input(f"insira sua idade: "))
cidade = input(f"insira sua cidade: ")

pessoa = {"nome": nome, "idade": idade, "cidade": cidade}

for chave, valor in pessoa.items(): #Se você quiser apenas exibir os valores e não as chaves, pode usar o método .values():
    print(f"{chave.capitalize()}: {valor}")
                                    #pessoa.items(): Este método retorna os pares chave-valor do dicionário
