### Aula 4: Manipulação de Strings

#### 1. **Fatiamento de Strings**

Em Python, as strings podem ser tratadas como sequências de caracteres, o que permite que você acesse uma parte específica da string usando "fatiamento".

Exemplo:

python

Copiar código

`texto = "Python é incrível!" print(texto[0:6])  # Resultado: Python`

- **`texto[0:6]`**: Acessa os caracteres da posição 0 até a 5. O índice 6 é exclusivo, ou seja, ele não é incluído.
- **`texto[:6]`**: Quando omitimos o valor inicial, o Python assume que queremos começar do início.
- **`texto[7:]`**: Quando omitimos o valor final, ele vai até o final da string.
- **`texto[-1]`**: Acessa o último caractere da string.

#### 2. **Métodos de Strings**

Python oferece diversos métodos para manipular strings. Aqui estão alguns dos mais úteis:

- **`upper()`**: Converte todos os caracteres para maiúsculas.
    
    python
    
    Copiar código
    
    `print(texto.upper())  # Resultado: PYTHON É INCRÍVEL!`
    
- **`lower()`**: Converte todos os caracteres para minúsculas.
    
    python
    
    Copiar código
    
    `print(texto.lower())  # Resultado: python é incrível!`
    
- **`replace(antigo, novo)`**: Substitui uma parte da string por outra.
    
    python
    
    Copiar código
    
    `print(texto.replace("incrível", "fantástico"))  # Resultado: Python é fantástico!`
    
- **`strip()`**: Remove espaços em branco extras no início e no fim da string.
    
    python
    
    Copiar código
    
    `texto_com_espacos = "  Python   " print(texto_com_espacos.strip())  # Resultado: Python`
    

#### 3. **Formatando Strings**

Você já usou `f-strings`, mas Python também oferece outras formas de formatar strings.

- **Usando `.format()`**:
    
    python
    
    Copiar código
    
    `nome = "Carlos" idade = 30 print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))`
    
- **Usando `f-strings` (a forma mais moderna)**:
    
    python
    
    Copiar código
    
    `print(f"Meu nome é {nome} e eu tenho {idade} anos.")`
    

---

### Exercício Prático:

1. Peça ao usuário para inserir uma frase e, em seguida, exiba:
    
    - Apenas os 5 primeiros caracteres.
    - A frase toda em maiúsculas.
    - A frase substituindo uma palavra à sua escolha.
2. Crie uma string com espaços extras no início e no final, e mostre o resultado após remover esses espaços com `strip()`. 