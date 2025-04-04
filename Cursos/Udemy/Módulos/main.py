# Programa Principal
import math_operations # Importando o módulo
from math_operations import multiply,divide # Importando a função de soma do módulo
import string_utils # Importando o módulo de utilidades de string

# Usando a função de soma do módulo

print(math_operations.sum(5, 3))  # Saída: 8
print(multiply(5, 3))  # Saída: 15
print(divide(5, 3))  # Saída: 1.6666666666666667
print(string_utils.capitalize("hello"))  # Saída: "olleH"
print(string_utils.reverse_string("Python"))  # Saída: "nohtyP"
print(string_utils.reverse_string("12345"))  # Saída: "54321"
print(string_utils.count("Apple"))  # Saída: "5"
