# Dicionario - par chave valor - chaves unicas
import copy

d1 = {'chave1': "valor1"}
d1["chave2"] = "valor2"

print(d1)
print(d1["chave2"])

d2 = dict(chave1="valor1", chave2="valor2")
print(d2)

# menos utilizado
d2.update({'chave3': 'valor3'})

if 'chave3' in d2:
    print(d2["chave3"])

if d2.get('chave3') is not None:
    print(d2["chave3"])

# Encontrar valores no dicionario
print('chave1' in d2)
print('chave1' in d2.keys())
print('valor3' in d2.values())

print("quantidade de pares", len(d2))

for key in d2:
    print('key', key)

for v in d2.values():
    print('values', v)

for itens in d2.items():
    print('key', itens[0], "values", itens[1])

for k, v in d2.items():
    print('key', k, "values", v)
print()

# Exemplos praticos
clients = {
    'client1': {
        'name': "Luiz",
        'sobrenome': 'Otavio'
    },
    'client2': {
        'name': "Jose",
        'sobrenome': 'Moreira'
    },
    'client3': {
        'name': "Anderson",
        'sobrenome': 'Andrade'
    }
}

for clients_key, clients_values in clients.items():
    print(f'Exibindo {clients_key}:')
    for dados_k, dados_v in clients_values.items():
        print(f'\t{dados_k} = {dados_v}')
print()

# copiando um dicionario - copia rasa
d1 = {1: ['v1', 'v2', 'v3'], 2: 'b', 3: 'c'}
v = d1.copy()

v[1][0] = 'v5'
print(d1)
print(v)
print()

# copiando um dicionario - copia real
d1 = {1: ['v1', 'v2', 'v3'], 2: 'b', 3: 'c'}
v = copy.deepcopy(d1)

v[1][0] = 'v5'
print(d1)
print(v)
print()

# convertendo lista ou tuplas em dicionario
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
    ['c4', 4]
]

d3 = dict(lista)
print(d3)

# Pop, Updade
d3.pop('c2')
print(d3)
d3.popitem()
print(d3)

d4 = [
    ['d1', 1],
    ['d2', 2],
    ['d3', 3],
    ['d4', 4]
]

d3.update(d4)
print(d3)
