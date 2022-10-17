n = int(input("Digite um número: "))
i, j, k = 1, 2 ,3

while i + j + k < n:
    i += 1
    j += 1
    k += 1
if i + j + k == n:
    print("O numero é perfeito")
else:
    print("O numero não é perfeito")