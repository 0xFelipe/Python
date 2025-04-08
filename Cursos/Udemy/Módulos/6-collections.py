from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Lista de Frutas (Contagem)
fruits = ["banana", "maça", "laranja", "banana", "maça", "banana"]
counter = Counter(fruits)
print(counter) # Counter({'banana': 3, 'maça': 2, 'laranja': 1})

# 2 - Utílizando tupla nomeada
# namedtuple é uma função que cria uma classe de tupla com nomes para os campos.

game = namedtuple("Game", ["name", "price", "rating"])
g1 = game("God of War", 200, 9.8)
g2 = game("The Last of Us", 250, 9.5)
print(g1) # Game(name='God of War', price=200, rating=9.8)
print(g2) # God of War

# 3 - Ordenando dicionarios
# sorted() é uma função que ordena os elementos de um iterável (como listas, tuplas ou dicionários) e retorna uma nova lista ordenada.

students = {"Pedro": 23, "Ana": 22, "João": 25}
sorted_students = sorted(students.items(), key=itemgetter(0))
print(sorted_students) # [('Ana', 22), ('João', 25), ('Pedro', 23)]

# 4 - Utilizando uma fila e ambas extremidades
# deque é uma classe que fornece uma fila (FIFO) e uma pilha (LIFO) de forma eficiente.
# É uma estrutura de dados que permite adicionar e remover elementos de ambas as extremidades com eficiência.
deq = deque([20, 40, 60, 80])
deq.appendleft(10) # Adiciona 10 no início da fila
print(deq) # deque([10, 20, 40, 60, 80])
deq.append(100) # Adiciona 100 no final da fila
print(deq) # deque([10, 20, 40, 60, 80, 100])
deq.popleft() # Remove o primeiro elemento da fila
print(deq) # deque([20, 40, 60, 80, 100])
deq.pop() # Remove o último elemento da fila
print(deq) # deque([20, 40, 60, 80])