vetor = []
soma = 0

for i in range(1, 5):
    nota = float(input("Digite a nota %i: " % i))
    soma += nota
    vetor.append(nota)
print("")
print("Notas:", vetor)
print("\nA media das notas foram: %.3g" % (soma/4))

