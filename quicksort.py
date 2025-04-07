def quicksort(array: list[int]) -> list[int]:
    if (len(array)) <= 1: return array;
    pivo = array[0]
    maiores = [i for i in array[1:] if i <= pivo]
    menores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)


array = [1, 2, 7, 10, 5, 44, 23, 0]
print(quicksort(array))
