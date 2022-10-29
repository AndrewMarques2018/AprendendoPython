# Listas
lista = [1, 2, 3, 4, 5, 6]

# Tuplas - lista em que os valores não são modificados
t1 = (1, 2, 3, 4, 5, 5, 1)
t1 = 1, 2, 3, 4, 5, 5, 1

# Dicionarios - par chave valor
dicionario = {'chave1': "valor1", "chave2": "valor2"}
dicionario['chave3'] = "valor3"

dicionario = dict(chave1="valor1", chave2="valor2")

dicionario.update({'chave3': 'valor3'})
"""
print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
"""

# copiando um dicionario - copia rasa - valores mutáveis mudam
d1 = {1: ['v1', 'v2', 'v3'], 2: 'b', 3: 'c'}
v = d1.copy()

# copiando um dicionario - copia real
import copy
d1 = {1: ['v1', 'v2', 'v3'], 2: 'b', 3: 'c'}
v = copy.deepcopy(d1)

# Set - conjuntos - não há elementos duplicados - não há ordem
# Add, Update, Clear, Discart, Union, Intersection, diference, symmetric_diference
s1 = {1, 1, 2, 3, 0, 4, 5, 6, -1, 2, 5, 5}
s2 = {1, 2, 2, 3, 1, 4, 6}
s1.discard(3)
s1.add(7)
s1.update([1, 2, 3, 4], {3, 4, 5, 6})
s3 = s1 | s2
# print("union", s3)
s3 = s1 & s2
# print("intersection", s3)
s3 = s1 - s2
# print("diference", s3)
s3 = s1 ^ s2
# print("symetric_intersection", s3)
