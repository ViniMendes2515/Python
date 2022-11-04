turma = int(input("Digite o número de turmas: "))
soma = 0


for i in range(1, turma+1):
    alunos = int(input(f"Digite o número de alunos da turma {i}:"))
    
    while alunos > 40 or alunos < 0:
        print("Número de alunos inválido")
        alunos = int(input("Digite o número de alunos da turma %i: "%i))

    soma += alunos

print(f"A media de alunos por turma são: {soma/turma}")

