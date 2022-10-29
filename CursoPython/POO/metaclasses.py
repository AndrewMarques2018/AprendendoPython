class Meta(type):

    def __new__(mcs, name, bases, namespace):
        # nao quero que a classe A tenha alterecoes
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        # nao deixar atributos serem sobreescritos
        if 'atributo' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['atributo']

        # avisa as classes filhas terem um metodo b_fala
        if 'b_fala' not in namespace:
            print('oi vc precisa criar o metodo b_fala')
        else:
            if not callable(namespace['b_fala']):
                print('b_fala precisa ser um metodo')
        print(namespace)

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    atributo = "valor atributo"

    def fala(self):
        self.b_fala()


class B(A):
    def b_fala(self):
        print('falei')

    atributo = "valor B"
    pass


class C(B):
    atributo = "valor C"
    pass


c = C()
print(c.atributo)
