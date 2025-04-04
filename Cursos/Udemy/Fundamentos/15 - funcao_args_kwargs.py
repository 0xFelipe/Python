"""
    *args - Utilizamos ele quando não sabemos quantos argumentos serão passados para a função.
    - Os argumentos são passados como uma tupla.

    **kwargs - Além dos valores, podemos passar também os nomes dos argumentos.
    - Os argumentos são passados como um dicionário.
    """
# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"A soma total é: {sum_total}")
sum(-7, 7)

# 2 - Apresetação de Cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
print("Apresentação de Cursos")
presentation(nome="Python", carga_horaria=80, professor="Gustavo Guanabara")
presentation(nome="Java", carga_horaria=100, professor="Gustavo Guanabara")