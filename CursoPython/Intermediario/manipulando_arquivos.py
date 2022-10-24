# https://docs.python.org/3/library/functions.html#open

""" Macete para recuperar raiz do progama
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise
"""

import json

file = open('file.txt', 'w+')
file.write("linha 1\n")
file.write("linha 2\n")
file.write("linha 3\n")

file.seek(0, 0)  # posiciona o cursor
print(file.read())

file.seek(0, 0)  # posiciona o cursor
for l in file.readlines():
    print(l)

file.close()

try:
    file = open('file.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()

# gerenciadores de contexto
with open('file.txt', 'w+') as file:
    file.write('Linha 1/n')
    file.write('Linha 2/n')
    file.write('Linha 3/n')

    file.seek(0, 0)
    print(file.read())

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 30
    },
    'Pessoa 2': {
        'nome': 'Lucas',
        'idade': 25
    },
    'Pessoa 3': {
        'nome': 'Lorenzo',
        'idade': 95
    }
}

d1_json = json.dumps(d1, indent=True)
with open('file.txt', 'w+') as file:
    file.write(d1_json)

with open('file.txt', 'r')as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

print(d1_json)


