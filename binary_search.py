import math

def pesquisa_binaria(lista_ordenada: list[int], item: int) -> list[int]:
    baixo = 0
    cont = 0
    alto = len(lista_ordenada) - 1

    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista_ordenada[int(meio)]

        if chute == item:
            return [item, cont]
        if chute > item: # too high
            alto = meio - 1
            cont += 1
        else: # too low
            baixo = meio + 1
            cont += 1
    return None


lista = [0, 1, 2, 5, 80, 100, 140]
inteiro = 140
print(pesquisa_binaria(lista, inteiro))
