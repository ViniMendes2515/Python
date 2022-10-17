notas = []

nota = float(input("Digite uma nota: "))

while nota != -1:
    notas.append(nota)
    nota = float(input("Digite uma nota: "))

print("Foram lidos %i valores."%len(notas))

print("\nValores informados: ")
for nota in notas:
    print(nota)

print("\nValores informados(ordem inversa): ")
notas.reverse()
for nota in notas:
    print(nota)

soma = 0
for nota in notas:
    soma += nota
print("\nA soma de valores é", soma)

soma /= len(notas)
print("\nA média dos valores é", soma)

acima = 0
for nota in notas:
    if nota > soma:
        acima += 1
print("\nNúmero de notas acima da média é", acima)

abaixo = 0
for nota in notas:
    if nota < 7:
        abaixo += 1
print("\nNúmero de notas abaixo de 7 é", abaixo)

print("\nÉ isso ai pessoal!")







