from dados import lista, produtos, pessoas
from functools import reduce

# soma 1
acumula = 0
for item in lista:
    acumula += item
print(acumula)

# soma 2
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)


soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
