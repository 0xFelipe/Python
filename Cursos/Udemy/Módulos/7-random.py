import random

# 1 - Seleciona valor aleatório de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(1, 10) # Gera um número inteiro aleatório entre 1 e 10 (inclusive)
print(r1)

#3 - Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name) # Gera um caractere aleatório da string
print(r2)

# 4 - Seleciona mais de um valor aleatório de uma lista
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r3 = random.sample(list2, 3) # Seleciona 3 valores aleatórios da lista
print(r3)

# 5 - Programa de Sorteio
done = False        
while not done:
    print("O que você deseja fazer?")
    print("1. Advinhar o número")
    print("2. Sair")

    choice = input(">")
    if choice == "1":
        print(f"========== Você escolheu adivinhar o número ========== \nAdivinhe o número entre 1 e 10")
        number = int(input("Digite um número de 1 a 10: \n>"))
        result = random.randint(1, 10)
        if number == result:
            print("Você acertou!")
        else:
            print(f"Você errou! O número era {result}.")
    elif choice == "2":
        print("Saindo do programa...")
        done = True
    else:
        print("Opção inválida. Tente novamente.")
