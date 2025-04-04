num1 = int(input("Digite o primeiro numero:\n "))
num2 = int(input("Digite o segundo numero:\n "))

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"A soma de {num1} e {num2} é: {sum}")
print(f"A subtração de {num1} e {num2} é: {sub}")
print(f"A divisão de {num1} e {num2} é: {div}")
print(f"A multiplicação de {num1} e {num2} é: {mult}")
print(f"O resto da divisão de {num1} e {num2} é: {mod}")
print(f"{num1} elevado a {num2} é: {exp}")

#Comparação

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"{num1} é maior que {num2}? {bigger}")
print(f"{num1} é menor que {num2}? {smaller}")
print(f"{num1} é igual a {num2}? {equal}")
print(f"{num1} é maior ou igual a {num2}? {bigger_equal}")
print(f"{num1} é menor ou igual a {num2}? {smaller_equal}")

# Atribuição

num1 += 1 #num1 = num1 + 1
num2 -= 1 #num2 = num2 - 1
num1 *= 2 #num1 = num1 * 2
num2 /= 2 #num2 = num2 / 2