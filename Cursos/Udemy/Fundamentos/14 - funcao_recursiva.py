# 1 - Fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * fatorial(n - 1))
n = int(input("Digite um número para calcular o fatorial:\n"))
print(f"O fatorial de {n} é: {fatorial(n)}")

# 2 - Soma  total de um número
def total_sum(num):
    if num <= 1:
        return num
    else:
        return num + total_sum(num - 1)
num = int(input("Digite um número para calcular a soma total:\n"))
print(f"A soma total de {num} é: {total_sum(num)}")