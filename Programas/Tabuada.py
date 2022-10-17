i = int(input("Digite o inicio da tabuada: "))
f = int(input("Digite o fim da tabuada: "))

for x in range(i, f+1):
    print("\nPara o %i" % x)
    for j in range(i, f+1):
        print("%ix%i = %i" % (x, j, i * j))
