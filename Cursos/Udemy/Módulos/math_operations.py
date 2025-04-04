# Módulo de Operações Matemáticas
def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):   
    if y != 0:
        return x / y
    else:
        raise ValueError("Divisão por zero não é permitida.")