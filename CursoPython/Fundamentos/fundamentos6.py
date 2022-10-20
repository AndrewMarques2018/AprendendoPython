# Split, Join, Enumerate em python
# enumerate( arg-lista, arg-inicio da contagem)
string = "O Brasil é o pais do futebol, o Brasil é penta"
lista1 = string.split(" ")
lista2 = string.split(",")

print(lista1)
print(lista2)

for valor in lista1:
    print(f'a palavra "{valor}" apareceu {lista1.count(valor)} na lista')

for indice, valor in enumerate(lista1):
    print(indice, valor)

lista = [1, 2, 3, 4, 5]
n1, n2, n3, n4, n5 = lista

print('n1',n1,'n5',n5)