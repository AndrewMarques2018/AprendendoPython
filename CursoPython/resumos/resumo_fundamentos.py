"""Documentação desse modulo

Resumo de todos os assuntos aprendidos
"""

# Strings
''''
:s - texto
:d - inteiros
:f - float
:.(numero)f - quantidade de casass dicimais
:(caracter)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
'''

variavel1 = "v11234"
variavel2 = 37.3333
texto = "variável 1: " + variavel1 + " variavel 2: " + str(variavel2)
texto = f'variável 1: {variavel1:.2s} variavel 2: {variavel2:0<2.2f}'
texto = 'variável 1: {:.2s} variavel 2: {:.2f}'.format(variavel1, variavel2)
textos = texto.split(" ")

# Condicionais
condicao1 = True
condicao2 = False
if condicao1 and condicao2:
    pass
elif condicao2 or condicao1:
    pass
else:
    pass

# while
x = -10
while x < 10:
    x += 2
else:
    pass

# for
for x in range(-10, 11, 2):
    ...
else:
    pass

# Listas
lista = [1, 2, 3, 'a', 'b', 'c', 12.4, True, []]
lista.append(6)
lista.insert(1, 'f')
lista.pop()
lista.clear()
lista2 = [2, 0, 3, 6, 3, 5, 9]
lista.extend(lista2)
lista.sort()

# Desempacotamento
elemento1, elemento2, *lista3 = lista

# Enumeradores
for indice, valor in enumerate(lista):
    pass

# Operador Ternario
condicao = False
x = 10.0 if condicao else 00.0







