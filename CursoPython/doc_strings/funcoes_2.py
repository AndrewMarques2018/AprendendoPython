"""Descriçao rapida e simples

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua. Eget arcu dictum varius duis at consectetur. Odio ut sem nulla pharetra diam. Non
tellus orci ac auctor augue mauris. Integer vitae justo eget magna fermentum iaculis eu non. Tempor
id eu nisl nunc mi ipsum faucibus. Netus et malesuada fames ac turpis. Et malesuada fames ac turpis
egestas integer eget aliquet. Vitae elementum curabitur vitae nunc sed velit dignissim sodales ut.
"""

variavel_1 = 'valor 1'


def soma(x, y):
    """Soma x e y

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y


def multiplica(x, y, z=None):
    """Multiplica x e y

    Multiplica x, y, z. O progamador pode omitir a variavel z, caso necessário.
    """

    if z:
        return x * y
    else:
        return x * y * z


variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'
