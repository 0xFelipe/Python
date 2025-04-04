# Função de potenciação de numeros
power = lambda num: num ** 2
print(power(5)) # 25

#Teste Com if para verificar se o número é par ou impar

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é impar.")

#Função lambda para verificar se o número é par ou impar
is_even = lambda num: num % 2 == 0
print(is_even(10)) # True

#função que inverte uma string
reverse_string = lambda string: string[::-1]
print(reverse_string("Python")) # nohtyP