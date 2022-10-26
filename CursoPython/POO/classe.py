import random

class Pessoa:
    # variável de classe
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return random.randint(10000, 19999)

    # getter
    @property
    def idade(self):
        return self._idade

    @property
    def nome(self):
        return self._nome

    # setter
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self._idade = idade

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self._nome = nome

p1 = Pessoa("Jozias", 12)
p2 = Pessoa.por_ano_nasc("Jurema", 1990)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(Pessoa.gera_id())
print(p1.gera_id())
print()
