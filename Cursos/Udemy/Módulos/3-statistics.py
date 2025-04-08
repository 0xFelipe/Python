import statistics

# 1- Aplicando a média

print(statistics.mean([1, 2, 3, 4, 5])) # 3.0

# 2- Aplicando a mediana
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 1, 8, 9])) # Nesse caso o alggoritimo organiza os números e pega a média dos dois números do meio, que são 2 e 3.

#3- Aplicando a moda
print(statistics.mode([1, 2, 3, 4, 5, 5, 6])) # 5
print(statistics.mode([1, 2, 3, 4, 5, 5, 6, 6])) # Nesse caso o alggoritimo vai pegar o primeiro número que mais se repete, que é o 5.

#4 - Desvio padrão

"""
O desvio padrão é uma medida de dispersão que indica o quanto os valores de um conjunto de dados estão espalhados em relação à média. 
Um desvio padrão baixo indica que os valores estão próximos da média, enquanto um desvio padrão alto indica que os valores estão mais dispersos.
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])) 