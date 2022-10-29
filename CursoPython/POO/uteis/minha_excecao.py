class MeuError(Exception):
    pass


def testar():
    raise MeuError('Errado')


try:
    testar()
except MeuError as e:
    print(f'Error: {e}')
