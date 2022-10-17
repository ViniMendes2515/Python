altura = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo F ou M: "))
genM = 'M'
genF = 'F'
ideal = 0


if sexo == 'F':
    ideal = (72.7*altura) - 44.7
elif sexo == 'M':
    ideal = (62.1*altura) - 58
else:
    exit()

peso = float(input("Digite seu peso: "))

if peso > ideal:
    print("Voce esta acima do peso")
elif peso < ideal:
    print("Voce esta abaixo do peso")
elif peso == ideal:
    print("Voce esta dentro do peso")


