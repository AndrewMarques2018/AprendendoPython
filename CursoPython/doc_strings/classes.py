class A:
    """Descriçao rapida e simples

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua. Eget arcu dictum varius duis at consectetur. Odio ut sem nulla pharetra diam. Non
    tellus orci ac auctor augue mauris. Integer vitae justo eget magna fermentum iaculis eu non. Tempor
    id eu nisl nunc mi ipsum faucibus. Netus et malesuada fames ac turpis. Et malesuada fames ac turpis
    egestas integer eget aliquet. Vitae elementum curabitur vitae nunc sed velit dignissim sodales ut.
    """

    atributo1 = 1
    atributo2 = 'valor'

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """

        self.texto = texto
        self.imprimir(texto)

    @staticmethod
    def imprimir(texto):
        """Exibe um texto de até 100 caraters

        :param texto: o texto
        :type texto: str

        :return: O texto de 100 caracters
        :rtype: str

        :raises Value Error: Se o texto tiver mais de 100 caracters
        :raises TypeError: Se o texto não for uma string
        """
        if not isinstance(texto, str):
            raise TypeError('Texto precisa ser uma string')

        if len(texto) > 100:
            raise ValueError('texto precisa ter 100 caracters ou menos')
