def funçãoRecursiva(x, y):
    if x <= y:
        print(x)
        funçãoRecursiva(x + 1, y)

funçãoRecursiva(0, 10)