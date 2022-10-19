
# Pass e Ellipsis - reservar linhas
valor = False
if valor:
    ...
else:
    pass

# formatar valores
''''
:s - texto
:d - inteiros
:f - float
:.(numero)f - quantidade de casass dicimais
:(caracter)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
'''
n1 = 10
n2 = 3
div = n1 / n2
print(div)
print(f"{div:.2f}")
print(f"{n1:0>10}")
print(f"{n1:0<10.2f}")
print(f"{n1:0^10}")

nome = "andrew"
print(f"{nome:*^10.3s}")
print("{n:!>10.5s}".format(n=nome))

print(nome.upper())
print(nome.title())
nome = nome.ljust(10, "!")
print(nome)

# subStrings
nome = 'Andrew Marques'
print("indice 2 ->", nome[2])
print(nome[7:-3])
print(nome[:-3])
print(nome[7:])
# steps
print(nome[0::1])
print(nome[0::2])
print(nome[0:9:2])
