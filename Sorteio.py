import random


def sorteio():
    print("\n\nOlá, Bem-vindo ao nosso programa!")
    print("Vamos ver se você vai ganhar um carro ou não!")

    porta = int(input("Escolha uma porta de 1 a 3: "))
    pM = porta - 1 or porta + 1
    premio = random.randint(1, 3)

    if porta <= 3:
        print("Voce escolheu a porta %i, mas eu lhe informa que na porta %i há um bode" % (
            porta, pM))
        troca = int(input("Deseja trocar de porta (1 - Sim | 0 - Não): "))
        if troca == 1:
            porta += 1
        elif troca == 0:
            porta = porta
        else:
            print("Valor Inválido | Você não trocou de porta!")

        if porta == premio:
            print("Ganhou um carro!")
        elif porta != premio:
            print("Não foi dessa vez :(")


sorteio()

proxS = int(
    input("\n\nDeseja participar de outro sorteio de carro (1 - Sim | 0 - Não): "))

while proxS <= 1:
    if proxS == 0:
        exit()
    elif proxS == 1:
        sorteio()
        proxS += 1
        proxS = int(
            input("\n\nDeseja participar de outro sorteio de carro (1 - Sim | 0 - Não): "))
        if proxS == 0:
            exit()
