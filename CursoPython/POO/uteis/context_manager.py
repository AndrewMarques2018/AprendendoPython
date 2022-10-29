arquivo = open('arquivo.txt', 'w')
arquivo.write('Alguma coisa')
arquivo.close()

with open('arquivo.txt', 'w') as arq:
    arq.write('Alguma coisa 2')


# gerenciador de contexto onde tenha que abrir e fechar algo
class Arquivo:

    def __init__(self, arquivo, modo):
        print('INIT')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('ENTER')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
        self.arquivo.close()
        # return True # use essa linha quando vc tratar uma possivel solução aq


with Arquivo('arquivo.txt', 'w') as arquivo:
    arquivo.write('alguma coisa 3')



# gerenciador de contexto
from contextlib import contextmanager


@contextmanager
def arqui(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo # serve para retornar uma instancia do arquivo
    finally:
        arquivo.close()


with arqui('arquivo.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
