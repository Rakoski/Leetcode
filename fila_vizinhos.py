from collections import deque
from graphs import grafo

def vendedor_manga() -> bool:
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa_e_vendedor(pessoa):
            print(pessoa + " é um vendedor de manga!")
            return True
        else:
            fila_de_pesquisa += grafo[pessoa]
            verificadas.append(pessoa)
    return False

def pessoa_e_vendedor(nome):
    return nome[-1] == 'y'

print(vendedor_manga())