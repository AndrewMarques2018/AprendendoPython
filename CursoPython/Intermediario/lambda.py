# Expressões Lambda
# lambda simples, multiplicacao
a = lambda x, y: x * y
print(a(2, 4))
print()

# ordenar uma lista
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8]
]
# metodo funcao
"""""
def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
"""

# metodo lambda
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
