### Aula 2: Loops e Listas

#### 1. **Listas**

Uma lista é uma estrutura de dados que armazena múltiplos valores em uma única variável. Em Python, listas são declaradas com colchetes `[]` e podem conter diferentes tipos de dados.

Exemplo:

python

Copiar código

`numeros = [1, 2, 3, 4, 5] nomes = ["Ana", "Carlos", "Bianca"]`

Você pode acessar elementos da lista usando índices (lembrando que o índice começa em 0):

python

Copiar código

`print(numeros[0])  # Resultado: 1 print(nomes[1])    # Resultado: Carlos`

#### 2. **Loops com Listas**

Um loop é usado para iterar sobre elementos de uma lista ou repetir um bloco de código várias vezes. O `for` é o mais usado para percorrer listas.

Exemplo de loop `for`:

python

Copiar código

`for numero in numeros:     print(numero)`

#### 3. **Loop `while`**

O loop `while` repete um bloco de código enquanto a condição for verdadeira.

Exemplo:

python

Copiar código

`contador = 0 while contador < 5:     print(f"Contador: {contador}")     contador += 1  # Incremento`

---

### Exercício Prático:

1. Crie uma lista de nomes e use um loop `for` para imprimir cada nome.
2. Crie um loop `while` que conta de 1 a 10 e imprime os números.