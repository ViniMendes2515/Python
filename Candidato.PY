x = 1
while x == True:
    eleitor = int(input("Digite o número de eleitores: "))
    Lula = 0
    Bolsonaro = 0
    Ciro = 0

    for i in range(1, eleitor+1):
        candidato = int(
            input("Lula: 13 \nBolsonaro: 22 \nCiro: 15\nQual o seu voto: "))
        if candidato == 13:
            Lula += 1
        elif candidato == 22:
            Bolsonaro += 1
        elif candidato == 15:
            Ciro += 1
        else:
            print("Invalido")
        print("")

    print("\nVotos Lula: %i" % Lula)
    print("Votos Bolsonaro: %i" % Bolsonaro)
    print("Votos Ciro: %i" % Ciro)

    if Lula > Bolsonaro:
        if Lula > Ciro:
            print("\nLula ganhou com %i votos" % Lula)

    elif Bolsonaro > Lula:
        if Bolsonaro > Ciro:
            print("\nBolsonaro ganhou com %i votos" % Bolsonaro)

    elif Ciro > Lula:
        if Ciro > Bolsonaro:
            print("\nCiro ganhou com %i votos" % Ciro)
    elif Lula == Bolsonaro or Ciro:
        print("A eleição empatou")
