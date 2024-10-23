#Exercicio 1
print ("Qual o seu nome?")
nome = input()
print ("Certo",nome,"agora me diga qual a sua idade?")
idade = int(input())

if (idade) >= 18:
    status = "Maior"
else:
    status = "Menor"
print ("Certo,", nome , "vi aqui que você tem", idade ,"e já é considerado", status , "de idade." )