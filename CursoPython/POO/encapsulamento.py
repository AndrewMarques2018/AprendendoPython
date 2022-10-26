"""
Outras linguagens -> public, protect, private
Python -> _ ("protect") ou __ ("privado")
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

    @property
    def dados(self):
        return self.__dados


bd = BaseDeDados()
bd.inserir_cliente(1, 'Jose')
bd.inserir_cliente(2, 'Joao')
bd.inserir_cliente(3, 'Andre')
bd.inserir_cliente(4, 'Gustavo')
bd.inserir_cliente(5, 'Abreu')

bd.apaga_cliente(2)
bd.lista_clientes()

# assim consseguimos acessar um elemento privado
print(bd._BaseDeDados__dados)  # raiz - não recomendado
print(bd.dados)  # getter