"""
def solution(sequence):
    abre = []

    for i in range(len(sequence)):
        c = sequence[i]

        if c == '(' or c == '[' or c == '{':
            abre.append(c)

        elif c == ')' or c == ']' or c == '}':

            if len(abre) == 0:
                return False

            peek = abre[len(abre)-1]
            if peek == '(' and c == ')':
                abre.pop()
            elif peek == '[' and c == ']':
                abre.pop()
            elif peek == '{' and c == '}':
                abre.pop()
            else:
                return False

    return len(abre) == 0
"""
from itertools import count

"""
def solution(a, b):
    a = list(a)
    b = list(b)

    repeticoes = dict()
    for c in a:
        count = 0
        i = 0
        while i < len(b):
            cc = b[i]
            if c == cc:
                del b[i]
                count += 1
            else:
                i += 1
        if not repeticoes.keys().__contains__(c):
            repeticoes[c] = count

    print(repeticoes)
    i = 0
    while i < len(a):
        c = a[i]
        n = a.count(c)
        if n > 1:
            a = [x for x in a if x != c]
            print(repeticoes[c], n)
            repeticoes[c] = int(repeticoes[c] / n)
        else:
            i += 1

    return min(repeticoes.values())

a = 'ccc'
b = 'cccccc'
print(solution(a, b))  # resposta de ser 3
"""

a = "a;b;c;".split(';')
print(len(a))
