import hashlib

# 1 - Vericar os algoritimos de hash disponíveis
#+print(hashlib.algorithms_available)

# 2 - Verificar algoritmos de acordo com o SO
#print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "Esse é um segredo super secreto".encode()
algorithm.update(message)
print(algorithm.hexdigest()) #Pesquisar sobre rainbow tables

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
