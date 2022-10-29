# https://rszalski.github.io/magicmethods/

class A:
    def __new__(cls, *args, **kwargs):
        print('__new__')

        ## SINGLETON - as classes terao a msm instância
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return super().__new__(cls)

    # posso usar minha classe como uma função
    def __call__(self, *args, **kwargs):
        return f'__call__: {args} {kwargs}'

    def __len__(self):
        return 999

    def __init__(self, nome=None):
        print('__init__')

    def __str__(self):
        return f'O que quero exibir quando essa classe se transformar em uma str'

    def __del__(self):
        print('Objeto coletado.')

    # é chamando toda vez que atribuir um valor novo a uma variável
    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


a = A('luiz otávio')
print("str__", str(a))
print(a(1, 2, 3, 4, nome='Andrew'))
