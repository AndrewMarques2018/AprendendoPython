"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict


# Possibilita a não implementação de métodos padroes
# frozen -> não possibilita edição da class
# order ->
@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)  # Omitir sobrenome de __repr__

    # È executado após o init
    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', 'D')  # __init__
p2 = Pessoa('B', 'A')
p3 = Pessoa('D', 'B')
p4 = Pessoa('C', 'C')

lista = [p1, p2, p3, p4]
lista.sort()  # __order__
print("Order by __order__", lista)
print("Order by lambda   ", sorted(lista, key=lambda p: p.nome, reverse=False))

print(p1.nome_completo)
print(p1)  # __repr__
print(p1 == p2)  # __eq__

print(asdict(p1))
