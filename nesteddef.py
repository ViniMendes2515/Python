def tab(N):
    """
    Recebe um número N e devolve uma função mult
    """
    def mult(x):
        """
        Recebe x e devolve x*n
        """
        return x*N

    return mult

def main():
    """
    Função principal do programa
    """

    n = int(input("Digite um número: "))
    
    for i in range(1, n+1):
        f = tab(i)
        print("Para o número", i)
        for j in range(1, 11):
            print("%i * %i = %i"%(i, j, f(j)))
        print()

main()