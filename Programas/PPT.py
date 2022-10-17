def jogo():
    import random
    
    seu_movimento = input("Pedra, papel ou tesoura:")
    seu_movimento.lower() # coloca a string em minúsculo

    # chama a função random e escolhe o movimento da máquina de forma aleatória
    máquina = random.random()

    if máquina >= 0 and máquina <= 0.33:
        máquina = "pedra"
    elif máquina >= 0.34 and máquina <= 0.66:
        máquina = "papel"
    else:
        máquina = "tesoura"

    if seu_movimento == "pedra":
        if máquina == "pedra":
            print ("Empatou!")
        elif máquina == "papel":
            print ("A máquina escolheu: 'PAPEL'\nVocê perdeu!")
        elif máquina == "tesoura":
            print ("A máquina escolheu: 'TESOURA'\nVocê venceu!")

    if seu_movimento == "papel":
        if máquina == "pedra":
            print ("A máquina escolheu: 'PEDRA'\nVocê venceu!")
        elif máquina == "papel":
            print ("Empatou!")
        elif máquina == "tesoura":
            print ("A máquina escolheu: 'TESOURA'\nVocê perdeu!")

    if seu_movimento == "tesoura":
        if máquina == "pedra":
            print ("A máquina esscolheu: 'PEDRA'\nVocê perdeu!")
        elif máquina == "papel":
            print ("A máquina escolheu: 'PAPEL'\nVocê venceu!")
        elif máquina == "tesoura":
            print ("Empatou!")
        
print (jogo())