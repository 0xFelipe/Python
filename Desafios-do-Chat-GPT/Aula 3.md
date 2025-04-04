### Aula 3: Funções

Funções são blocos de código que realizam uma tarefa específica e podem ser reutilizadas sempre que necessário. Elas ajudam a organizar o código, evitando repetições.

#### 1. **Como Criar uma Função**

Para definir uma função em Python, usamos a palavra-chave `def`, seguida pelo nome da função e parênteses. O código da função fica indentado.

Exemplo de uma função simples:

python

Copiar código

`def saudacao():     print("Olá! Seja bem-vindo!")`

Para chamar essa função, você só precisa usar o nome dela:

python

Copiar código

`saudacao()  # Isso vai imprimir "Olá! Seja bem-vindo!"`

#### 2. **Funções com Parâmetros**

Podemos passar dados para uma função por meio de **parâmetros**. Isso torna a função mais flexível.

Exemplo com parâmetros:

python

Copiar código

`def saudacao(nome):     print(f"Olá, {nome}! Seja bem-vindo!")`

Aqui, `nome` é o parâmetro, e quando chamamos a função, podemos passar um valor:

python

Copiar código

`saudacao("Carlos")  # Resultado: Olá, Carlos! Seja bem-vindo!`

#### 3. **Funções com Retorno**

Uma função também pode retornar um valor usando a palavra-chave `return`. Isso permite usar o resultado da função em outras partes do código.

Exemplo de uma função que soma dois números e retorna o resultado:

python

Copiar código

`def soma(a, b):     return a + b`

Podemos então armazenar o resultado em uma variável ou usá-lo diretamente:

python

Copiar código

`resultado = soma(5, 3) print(resultado)  # Resultado: 8`

---

### Exercício Prático:

1. Crie uma função que receba dois números como parâmetros e retorne a soma deles.
2. Crie uma função que receba um nome e a idade, e exiba uma saudação personalizada que inclua a informação se a pessoa é maior ou menor de idade.