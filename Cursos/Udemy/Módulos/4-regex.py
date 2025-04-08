import re

text = "Udemy - uma plataforma com muitos cursos"
# 1 - Indice inicial e final de palavras
# O r significa uma raw string (string bruta), que é uma string que não processa caracteres especiais como \n, \t, etc.
match = re.search(r"Udemy", text)
print(match.start()) # 21
print(match.end()) # 36

# 2 - Buscando o índice que possui o ponto
site = "https://udemy.com"
match = re.search(r"\.", site)
print(match)

# 3 - Buscando uma lista de catacteres dentro de uma frase
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

#4 - Verificando o início de uma string
rule = r'^A'
phrases = [''
'A casa está suja', 'O dia está lindo', 'Vamos para a praia']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

# 5 - Verificando o final de uma string
rule_end = r'!$'
phrase2 = ['A casa está suja!', 'O dia está lindo', 'Vamos para a praia!']
for f in phrase2:
    if re.search(rule_end, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")