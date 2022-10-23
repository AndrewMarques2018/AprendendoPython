from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Otavio', 'Judson']

# Gera todas as combinacoes possiveis onde a ordem nao importa, sem repeticoes
print('Combinations')
for grupo in combinations(pessoas, 2):
    print(grupo)

print()
# Gera todas as combinacoes possiveis onde a ordem importa, sem repeticoes
print('Permutation')
for grupo in permutations(pessoas, 2):
    print(grupo)

print()
# Gera todas as combinacoes possiveis onde a ordem importa, com repeticoes
print('Product')
for grupo in product(pessoas, repeat=2):
    print(grupo)
