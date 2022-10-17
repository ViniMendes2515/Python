print("\n***Quem foi o melhor jogador?***\n")

votos = []
voto = int(input("Digite o número do jogador (0 = fim): "))

while voto != 0:
    votos.append(voto)
    if 1 <= voto <= 23:
        voto = int(input("Digite o número do jogador (0 = fim): "))
    else:
        voto = int(input("\nNúmero inválido\n\nDigite o número do jogador (0 = fim): "))

print("\nResultado da Votação: \n")

print("Foram computados %i votos\n" % len(votos))

print("Jogador           Votos           %")

maior_votos = 0
melhor = 1
porcentagem = 0

for i in range(1, 24):
    total_i = votos.count(i)
    porcentagem_i = 100*votos.count(i)/len(votos)
    if total_i > 0:
        print("%4.i             %4.i          %.1f%%" %(i, total_i, porcentagem_i))
        if total_i > maior_votos:
            maior_votos = total_i
            melhor = i
            porcentagem = porcentagem_i

print("O melhor jogador foi o número %i, com %i votos, correspondendo a %.1f%% do total de votos."%(melhor, maior_votos, porcentagem))