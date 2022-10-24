from dados import lista, produtos, pessoas

nova_lista = filter(lambda x: x >= 10, lista)
# nova_lista = [x for x in lista if x >= 10]

print(lista)
print(list(nova_lista))
print()


def filtrar(p):
    return p['preco'] >= 50


# novos_produtos = filter(lambda p: p['preco'] >= 50, produtos)
novos_produtos = filter(filtrar, produtos)
print(produtos)
print(list(novos_produtos))
