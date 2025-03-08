def regressiva(i: int):
    print("i: ", i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

regressiva(10)