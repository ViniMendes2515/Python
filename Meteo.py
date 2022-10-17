cont = int(input("Digite quantas temperaturas você pretende registrar: "))
soma = maior = menor = float(input("Digite a temperatura 1: "))

for i in range(2, cont+1):
    temp = float(input("Digite a temperatura %i: "%i))

    if temp > maior:
        maior = temp
    elif temp < menor:
        menor = temp
    soma += temp
print("\nA maior temperatura foi: %.2f" %maior)
print("A menor temperatura foi: %.2f" %menor)
print("a média entre as temperaturas foi: %f" %soma/cont)

