print("Vamos falar sobre conjuntos")
conjunto1 = input("Insira 3 valores separados por virgura para o primeiro conjunto: ")
conjunto1 = {valor.strip() for valor in conjunto1.split(",")}
conjunto2 = input("Insira 3 valores separados por virgura para o segundo conjunto: ")
conjunto2 = {valor.strip() for valor in conjunto2.split(",")}
print(f"A junção do primeiro conjunto com o segundo fica assim {conjunto1 | conjunto2}")
print(f"Em comun seu conjunto tem o seguinte argumento{conjunto1 & conjunto2}")