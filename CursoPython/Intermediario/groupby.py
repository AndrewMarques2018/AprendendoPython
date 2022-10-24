from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Edu', 'nota': 'D'},
    {'nome': 'Lara', 'nota': 'E'},
    {'nome': 'Larissa', 'nota': 'B'},
    {'nome': 'Joao', 'nota': 'C'},
    {'nome': 'Josias', 'nota': 'C'},
    {'nome': 'Luana', 'nota': 'E'},
    {'nome': 'Luciana', 'nota': 'E'}
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_group = groupby(alunos, ordena)

for agrupamento, valores_group in alunos_group:
    """
    list_back criada por conta dos valores retornados ser iteravel, 
    e usuaremos os valores mais de uma vez no code
    """
    list_back = list(valores_group)
    quantidade = len(list_back)
    print(f'agrupamento: {agrupamento} tem {quantidade} alunos')

    for aluno in list_back:
        print(f'\t{aluno}')
