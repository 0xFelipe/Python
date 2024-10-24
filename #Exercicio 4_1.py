nome = input("insira seu nome completo: ")

print ("Já pensou que se apelidos fossem somente as 5 primeiras letras do seu nome, o seu seria {}".format(nome[0:5]))
print ("Seu nome completo em maiusculo é {}".format(nome.upper()))

substituicao = input("Supondo que você fosse trocar um sobre nome qual você trocaria: ")
substituto = input(f"Por qual você trocaria o sobrenome {substituicao}?: ")
print ("Certo nesse caso seu novo nome ficaria {}".format(nome.replace(substituicao, substituto)))
