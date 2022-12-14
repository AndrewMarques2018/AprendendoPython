def fala_oi():
    print('oi')


variavel = fala_oi
variavel()
print("----------------- separador ----------------------")


def master(funcao):
    def slave(*args, **kwargs):
        print("Agora estou decorada!")
        funcao(*args, **kwargs)

    return slave


@master
def saudacao():
    print('oi')


# saudacao = master(saudacao)
saudacao()
print("----------------- separador ----------------------")

# exemplo - tempo de execução de uma função
from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A funcao {funcao.__name__} levou {tempo}ms para executar  ')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        sleep(1)

demora()
