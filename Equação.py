a = int(input("Digite o valor de a: "))
if a > 0:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    x1 = 0
    x2 = 0
    if delta < 0:
        print("\n***Delta Negativo***\n")
        exit()
    elif delta == 0:
        x1 = -b/(2 * a)
        print("Raíz x1: %i" % x1)
    elif delta > 0:
        x1 = -b + delta**(1/2) / (2 * a)
        x2 = -b - delta**(1/2) / (2 * a)
        print("Raízes x1: %i\nx2: %i" % (x1, x2))
else:
    print("\n***Valor de 'a' Invalido***\n")
    exit()
