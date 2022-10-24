"""
Importando listas, utilizando map
"""

from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)
# nova_lista = [x*2 for x in lista]

print(lista)
print(list(nova_lista))

def aumentar_preco(p):
    p['preco'] = round(p['preco']*1.10, 2)
    return p

#produtos_novos = map(lambda x: x, produtos)
produtos_novos = map(aumentar_preco, produtos)

print(produtos)
print(list(produtos_novos))

def aumentar_idade(p):
    p['idade'] = round(p['idade']*1.10)
    return p

pessoas_novas = map(aumentar_idade, pessoas)

print(pessoas)
print(list(pessoas_novas))