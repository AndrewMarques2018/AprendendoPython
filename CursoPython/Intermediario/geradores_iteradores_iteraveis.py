import sys
import time

lista = list(range(1000))
print(sys.getsizeof(lista))
# lista = 1,2,3,4,5
# lista = "string"
lista = iter(lista)
# print(hasattr(lista, '__iter__'))
# print(hasattr(lista, '__next__'))

'''
print(lista.__next__())
print(lista.__next__())
print(lista.__next__())
print(lista.__next__())
print(lista.__next__())
print(lista.__next__())
'''


# geradores
def gera():
    variavel = 'valor_1'
    yield variavel
    variavel = 'valor_2'
    yield variavel
    variavel = 'valor_3'
    yield variavel

g = gera()

print(next(g))
l1 = [x for x in range(1000000)]
print(type(l1))
print(sys.getsizeof(l1))

l2 = (x for x in range(1000000))
print(type(l2))
print(sys.getsizeof(l2))

# iteradores
nome = 'Luiz Otávio'
iterador = iter(nome)
