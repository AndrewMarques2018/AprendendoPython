# Count - Itercools
from itertools import count
from types import GeneratorType

variavel = zip('Alo', 'Alo')  # isso é um iterador
print(isinstance(variavel, GeneratorType))

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))  # isso é um contador
print(isinstance(variavel, GeneratorType))

contador = count(start=5, step=-0.1)  # isso é um contador infinito
print(round(next(contador), 2))
print(round(next(contador), 2))
print(round(next(contador), 2))
print(round(next(contador), 2))
print(round(next(contador), 2))
print()

# indexando lista de elementos
contador = count()
list = ["andrew", "joaquin", "Jurema", "Astoufo"]
list = zip(contador, list)

for v in list:
    print(v)



