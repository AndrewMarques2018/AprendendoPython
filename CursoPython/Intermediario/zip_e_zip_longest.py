"""
    zip - unindo iteráveis em uma lista de tamanho da menor lista
    zip_longest - intertools - unindo iteráveis em uma lista de tamanho da maior lista
"""
from itertools import zip_longest, count

indice = count()
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Qualquer']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))

cidades_estados = zip(
    indice,
    cidades,
    estados,
)
for v in cidades_estados:
    print(v)