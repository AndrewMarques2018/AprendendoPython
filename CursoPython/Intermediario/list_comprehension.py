# duplicar elementos de uma lista
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel * 2 for variavel in l1]

print(l1)
print(l2)

# criar chave valor
ex2 = [(v1, v2) for v1 in l1 for v2 in range(2)]
print(ex2)

# inverter chave valor
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3')
)

print(tupla)
ex3 = [(y, x) for x, y in tupla]
print(ex3)
print()

# add elementos para uma lista com condicoes
l3 = list(range(100))
ex4 = [x for x in l3 if x % 8 == 0 and x % 3 == 0]
print(ex4)

ex5 = [x if x % 8 == 0 and x % 3 == 0 else '' for x in l3]

print(ex5)