**Aula 1: Fundamentos da Lógica de Programação com Python**

Vamos começar pelos pilares da lógica de programação:

### 1. **Variáveis e Tipos de Dados**

Variáveis são usadas para armazenar dados que podem ser reutilizados no código. Em Python, não é necessário declarar o tipo da variável explicitamente, o próprio Python detecta.

Exemplo:

python

Copiar código

`nome = "João"  # String idade = 25     # Inteiro altura = 1.75  # Float`

Tipos de dados comuns:

- **int**: números inteiros (`25`, `-10`)
- **float**: números com ponto flutuante (`1.75`, `-2.5`)
- **str**: strings, texto (`"Olá"`, `"Python"`)
- **bool**: valores booleanos (`True`, `False`)

### 2. **Operadores Aritméticos**

São usados para realizar operações matemáticas.

- Soma: `+`
- Subtração: `-`
- Multiplicação: `*`
- Divisão: `/`

Exemplo:

python

Copiar código

`a = 10 b = 5 soma = a + b  # Resultado: 15 divisao = a / b  # Resultado: 2.0`

### 3. **Estruturas Condicionais**

As estruturas condicionais permitem que o programa execute determinadas instruções dependendo de uma condição.

Exemplo:

python

Copiar código

`idade = 18 if idade >= 18:     print("Você é maior de idade.") else:     print("Você é menor de idade.")`

### 4. **Laços de Repetição (Loops)**

Repetem um bloco de código enquanto uma condição é verdadeira.

Exemplo com `for`:

python

Copiar código

`for i in range(5):  # Repetirá de 0 a 4     print(i)`

Exemplo com `while`:

python

Copiar código

`contador = 0 while contador < 5:     print(contador)     contador += 1`

---

**Exercício Prático:** Vamos criar um pequeno programa para praticar esses conceitos. Escreva um código que:

- Pergunta o nome e a idade do usuário.
- Verifica se o usuário é maior ou menor de idade.
- Exibe uma mensagem personalizada com o nome e a idade.