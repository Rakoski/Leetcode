def busca_menor_indice(arr: list[int]) -> int:
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
        print(arr)
    return menor_indice

def ordenacao_por_selecao(arr: list[int]) -> list[int]:
    novo_array = []
    for i in range(0, len(arr)):
        menor = busca_menor_indice(arr)
        novo_array.append(arr.pop(menor)) # it pops the menor indice (which is the menor value)
        # arr.pop(menor) pops the smallest value from the array that it just searched for
        print("reofrmulando: ", novo_array)
    return novo_array

print(ordenacao_por_selecao([5, 3, 8, 12, 1, 4]))

