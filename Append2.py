vetor = []
vetor_par = []
vetor_impar = []

for i in range(1, 21):
    num = int(input("Digite um número inteiro: "))
    vetor.append(num)
    if num % 2 == 0:
        vetor_par.append(num)
    elif num % 2 == 1:
        vetor_impar.append(num)
print("")
print("Vetor:", vetor)
print("")
print("Vetor Par:", vetor_par)
print("")
print("Vetor Ímpar: ", vetor_impar)
