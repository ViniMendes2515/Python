import random

def TrocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10 -1][pos1%10 -1]
    elemento2 = matriz[pos2//10 -1][pos2%10-1]
    matriz[pos1//10-1][pos1%10-1] = elemento2
    matriz[pos2//10-1][pos2%10-1] = elemento1


def geraMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

#############################################################
#   Funções Propostas                                       #
#############################################################

def VerificaSeVenceu(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if ((4*i + j + 1) != matriz[i][j] and i != 3 and j != 3) or (i == 3 and j == 3 and matriz[i][j] != 0):
                return False

    return True

def VerificaJogada(pos, zero_pos):
    linha = pos//10
    coluna = pos%10

    linha_zero = zero_pos//10
    coluna_zero = zero_pos%10

    if linha < 1 or linha > 4 or coluna < 1 or coluna > 4:
        return False
    else:
        if (linha == linha_zero -1 and coluna == coluna_zero) or (linha == linha_zero and (coluna == coluna_zero-1 or coluna == coluna_zero+1)) or (linha == linha_zero+1 and coluna == coluna_zero):
            return True
        else:
            return False


def imprimeJogo(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

#############################################################
#   Funções Pessoais                                        #
#############################################################

def AchaPosZero(matriz):
    #Função que procura e devolve a posição do zero da matriz(espaço vazio)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                return (i+1)*10 + j+1

def fazJogada(jogo):
    #Imprime o jogo na tela e pergunta se o usuário quer continuar
    imprimeJogo(jogo)
    dec = bool(int(input("Deseja continuar(1) ou desistir(0): ")))
    return dec

#############################################################
#   Função Main                                             #
#############################################################

def main():
    jogo = []
    geraMatriz(jogo)

    venceu =False

    zero_pos = AchaPosZero(jogo)

    jogando = fazJogada(jogo)


    while jogando:
        pos = int(input("Digite a posição do elemento que você deseja trocar: "))

        while not VerificaJogada(pos, zero_pos):
            print("Entrada inválida. Digite novamente")
            pos = int(input("Digite a posição do elemento que você deseja trocar: "))

        TrocaElemento(pos, zero_pos, jogo)

        zero_pos = pos

        venceu = VerificaSeVenceu(jogo)
        jogando = not venceu

        if jogando:
            jogando = fazJogada(jogo)

    if venceu:
        print("Parabens, você venceu!!!")
    else:
        print("Obrigado por jogar.")

main()
