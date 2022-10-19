# nome = input("Qual seu nome? ")
# print(f"vc digitou {nome}")

number1 = 1
number2 = 2
number3 = '1'
texto = ''

if number2 > number1 != number3:
    print("verdade 0")

if not number1 > number2:
    print("Nao")

if number1 == number2:
    print("Verdade 1")
elif type(number1) == int:
    print("Verdade 1")
elif number1 >= number2:
    print("Verdade 1")
else:
    print("verdade 3")

if not texto:
    print("texto vazio")

texto = "abcdefghijklmnopqrstu"
if 'u' in texto:
    print("texto contem 'u'")

print("O texto tem o tamanho de", len(texto), "caracters")
print("O texto tem o tamanho de", texto.__len__(), "caracters")