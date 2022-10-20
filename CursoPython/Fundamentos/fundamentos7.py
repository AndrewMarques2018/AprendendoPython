# desempacotamento
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n1, n2, n3, n4, n5, *outraLista, nf = lista
n1, n2, n3, n4, n5, *_, nf = lista
print(n1, nf)
print()

# inverter variaveis
x = 'a'
y = 1
z = True
print(x, y, z)
x, y, z = y, x, False
print(x, y, z)

# operador ternário
logged_user = False
msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar'
print(msg)

# expressão condicional OR
nome = ""
print(nome or None or 0 or "vc nao digitou nada!")

a = 0
b = None
c = False
d = []
e = {}
f = ""
g = 22

variavel = a or b or c or d or e or f or g
print(variavel)
print()

# random
from random import randint

for x in range(20):
    print(randint(0, 10))  # 0 ao 10
