class A:
    # variavel de classe, todos os filhos tem acesso
    vc = 123

a1 = A()
a2 = A()

# quando a propria classe modifica suas variaveis, seus filhos tbm sofrem alteracoes
a1.vc = 999  # a1 não modifica A.vc, ele cria um atributo direto na instancia
A.vc = 456
print(A.vc)
print(a1.vc)
print(a2.vc)
print()

a1.vc = 333
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
