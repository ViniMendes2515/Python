numero_maior = numero_menor = int(input("Digite o seu número: "))
altura_maior = altura_menor = float(input("Digite sua altura: "))

for i in range(9):
    numero = int(input("Digite o seu número: "))
    altura = float(input("Digite sua altura: "))

    if altura < altura_menor:
        altura_menor = altura
        numero_menor = numero
    if altura > altura_maior:
        altura_maior = altura
        numero_maior = numero

print("O Aluno de numero %i tem a maior altura %.2f"%(numero_maior, altura_maior))
print("O Aluno de numero %i tem a menor altura %f"%(numero_menor, altura_menor))

