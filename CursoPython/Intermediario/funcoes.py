# funcoes
def funcao(msg="olá", nome='usuario'):
    print(msg, nome)


def saudacao(msg='olá', nome='nome'):
    return f'{msg} {nome}'


funcao()
funcao('hellow')
funcao('bem vindo', "josé")
funcao(nome='astoufo', msg='olá')
print(saudacao("oi"))
print()


# variaveis recebem uma funcao
def f(var):
    print(var)


def d():
    return f


def dumb():
    return ('Luiz', 'Otávio')


var = d()
print(var)
var("Ola var")

var = dumb()
print(var)
print()


# argumentos
def func(a1, a2, a3, a4, a5, nome=None):
    print(a1, a2, a3, a4, a5, nome)


# nao posso alterar valores de args
def func2(*args):
    print(args)

# posso alterar args
def func3(*args, **kwargs):
    args = list(args)
    args[0] = 20
    print(args)
    nome = kwargs.get('nome')
    if nome is not None:
        print(nome)
    '''
    if kwargs.__len__()>0:
        print(kwargs['nome'], kwargs['id'])
    '''

func3(1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]
func3(lista)  # a lista vai como argumento
func3(*lista, nome='Luiz', id=12)  # cada elemento da lista vai como argumento
print()

# Escopo de variaveis
vg = 'variavel global'

def f1():
     print(vg)

def f2():
    vg = "variavel local"
    print(vg)

# não é uma boa prática
def f3():
    global vg
    vg = "variavel local"
    print(vg)

def f4(var):
    var = "teste"

f1()
f2()
print(vg)
f3()
print(vg)
f4(vg)
print(vg)

