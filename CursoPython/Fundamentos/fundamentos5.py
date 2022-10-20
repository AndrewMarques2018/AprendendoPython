# listas fatiamento, append, insert, pop, del, clear, extend, +, min, max
lista = ['a', 'bacalhau', -1, 2.5, True]
lista[3] = 23.5
print(lista[0:4:2])

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c']

l1.append(6)
l2.insert(1, 'f')
l2.pop()
l1.clear()
print(l1)
print(l2)

l1 = list(range(0, 20, 2))
l2 = ['a', 'b', 'c']
l2.extend(l1[0:3])
del (l1[0:2])

print(l1)
print(f'max:{max(l1)} min {min(l1)}')
print(l2)
