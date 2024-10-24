x = input("Insira o Primeiro número: ")
y = input("Insira o Segundo número: ")
z = input("Insira o Terceiro número: ")
tupla = (x, y, z)

n = input(f"sua tupla tem os seguintes valores: {tupla}, vamos tentar alterar o valor {tupla[0]}, insira o valor para colocar no lugar: ")
tupla[0] = n
print(f"Se a alteração der certo sua tupla deve ter o novo seguinte resultado {tupla}") #Essa parte não foi execultada devivo o erro 'tuple' object does not support item assignment