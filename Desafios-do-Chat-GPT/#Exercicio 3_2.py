nome = input("Qual o seu nome?")
idade = int(input(f"Certo, {nome}, agora me diga qual a sua idade?"))
status = 0
def id (idade):
    if idade >= 18:
        return "Maior"
    else:
        return "Menor"
    
status = id(idade)
 
print(f"Olá, {nome}! vi aqui que você tem {idade} anos de idade e é considerado {status} de idade.")