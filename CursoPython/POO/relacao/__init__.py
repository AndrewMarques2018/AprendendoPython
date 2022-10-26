# Associação - usa | Agregação - tem | Composição - é dono | Herança - é

from classes import Escritor, Caneta, MaquinaDeEscrever
from heranca import Cliente, Aluno, Pessoa

escritor = Escritor("Alfred")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

aluno = Aluno('Jurimias', 16)
cliente = Cliente('jerebadias', 11)
pessoa = Pessoa("Jeripadias", 9)
aluno.falar()
cliente.falar()
pessoa.falar()
