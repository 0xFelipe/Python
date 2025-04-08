import math

# 1 - Acessar o número PI
print(f"{math.pi:.2f}")  # 3.141592653589793

# 2 - Acessar o número Euler
# O número de Euler é uma constante matemática que é a base do logaritmo natural.
print(f"{math.e:.2f}")  # 2.718281828459045

# 3 - Arredondamento números para cima ou para baixo
num = 10.4
print(math.floor(num))  # Arredonda para baixo (10)
print(math.ceil(num))   # Arredonda para cima (11)

# 4 - Fatorial de um número
num = int(input("Digite um número: "))
print(math.factorial(num))  # Fatorial de 5 = 120

# 5 - Potência de um número
print(math.pow(2, 3))  # 2^3 = 8.0
print(2**3)  # 2^3 = 8

# 6 - Raiz quadrada de um número
num = 16
print(math.sqrt(num))  # Raiz quadrada de 16 = 4.0
print(math.sqrt(25))  # Raiz quadrada de 25 = 5.0

# 7 - MDC (Máximo Divisor Comum) de dois números
# O MDC é o maior número que divide dois números inteiros sem deixar resto.

mdc = math.gcd(10, 15)  # O MDC de 10 e 15 é 5
print(mdc)  # 5

# 8 - Logaritmo de um número
# O logaritmo é a operação inversa da exponenciação.
# O logaritmo de um número é o expoente ao qual a base deve ser elevada para obter esse número.
print(math.log(10))  # Logaritmo natural de 10 (base e)