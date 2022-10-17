alunos = 10
notas = 0
mediaV = []
media = 0

for i in range(1, alunos+1):
    for j in range(4):
        nota = float(input("Digite as notas do aluno %i: "%i))
    soma =+ nota
    media = soma / 4
    mediaV.append(media)

num = 0
for mediaC in mediaV:
    if media >= 7:
        num += 1

print("O número de alunos com a média maior que 7.0 é: %i" %num)





        