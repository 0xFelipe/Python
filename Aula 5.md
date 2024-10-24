### Aula 5: Estruturas de Dados

#### 1. **Tuplas**

Tuplas são parecidas com listas, mas têm uma diferença importante: elas são **imutáveis**, ou seja, depois de criadas, seus valores não podem ser alterados.

- **Criação de tupla**:
    
    python
    
    Copiar código
    
    `tupla = (1, 2, 3)`
    
- **Acesso a elementos** (igual às listas):
    
    python
    
    Copiar código
    
    `print(tupla[0])  # Resultado: 1`
    
- **Imutabilidade**: Você não pode alterar os valores da tupla. Por exemplo, tentar `tupla[0] = 5` resultaria em um erro.
    
- **Usos comuns de tuplas**:
    
    - Quando você quer garantir que os dados não serão modificados.
    - Como retorno de múltiplos valores de uma função:
        
        python
        
        Copiar código
        
        `def retorna_coordenadas():     return (10, 20)  x, y = retorna_coordenadas() print(f"x: {x}, y: {y}")`
        

#### 2. **Dicionários**

Dicionários são estruturas que armazenam dados em pares **chave-valor**. São muito úteis quando você quer associar dados de uma forma que tenha sentido lógico, como um nome associado a um telefone, por exemplo.

- **Criação de dicionário**:
    
    python
    
    Copiar código
    
    `dicionario = {"nome": "Carlos", "idade": 25}`
    
- **Acesso aos valores**:
    
    python
    
    Copiar código
    
    `print(dicionario["nome"])  # Resultado: Carlos`
    
- **Modificando valores**:
    
    python
    
    Copiar código
    
    `dicionario["idade"] = 26`
    
- **Adicionando novos pares chave-valor**:
    
    python
    
    Copiar código
    
    `dicionario["cidade"] = "São Paulo"`
    
- **Usos comuns de dicionários**:
    
    - Quando você quer mapear ou categorizar dados (ex: nomes de produtos e preços).

#### 3. **Sets (Conjuntos)**

Um **set** é uma coleção de itens **não ordenados** e **únicos**. Isso significa que não pode haver valores duplicados em um set.

- **Criação de set**:
    
    python
    
    Copiar código
    
    `conjunto = {1, 2, 3, 4, 4}  # O valor 4 duplicado será automaticamente removido print(conjunto)  # Resultado: {1, 2, 3, 4}`
    
- **Adicionando elementos**:
    
    python
    
    Copiar código
    
    `conjunto.add(5)`
    
- **Operações com sets**: Conjuntos são úteis para fazer operações como união, interseção e diferença.
    
    - **União**:
        
        python
        
        Copiar código
        
        `conjunto1 = {1, 2, 3} conjunto2 = {3, 4, 5} print(conjunto1 | conjunto2)  # Resultado: {1, 2, 3, 4, 5}`
        
    - **Interseção**:
        
        python
        
        Copiar código
        
        `print(conjunto1 & conjunto2)  # Resultado: {3}`
        

---

### Exercícios Práticos:

1. Crie uma tupla com 3 números e tente alterar um dos valores. O que acontece?
2. Crie um dicionário que armazene informações sobre uma pessoa (nome, idade, cidade) e imprima cada valor separadamente.
3. Crie dois conjuntos (sets) com valores distintos e mostre a união e a interseção entre eles.