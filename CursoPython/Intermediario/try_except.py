# https://docs.python.org/3/library/exceptions.html

try:
    print(a)
except NameError as error:
    print("error", error)
except Exception as error:
    print("error inesperado", error)

try:
    print(22 / 0)
except IndentationError as error:
    print(error)
except Exception as error:
    print(error)
else:
    print('nao ocorreu nenhum erro')
finally:
    print('seu try foi executado')
print()


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1 / n2


print(divide(2, 1))
print(divide(2, 0))
