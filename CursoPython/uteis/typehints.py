"""Documentação desse modulo

Ele nã faz nada! È apenas um exemplo
Typing - https://docs.python.org/3/library/typing.html
"""
from typing import Union

# typing
variavel: str = "variavel"


# retorna um float
def funcao(p1: float, p2: str, p3: dict) -> float:
    return p1 * 2


# retorna ou uma lista ou um dicionario
def funcao2(boleana: bool) -> Union[list, dict]:
    if boleana:
        return [1, 2, 3, 4]
    else:
        return {1: "a", 2: "b"}


def funcao3() -> tuple[float, str]:
    return 2.4, "str"
