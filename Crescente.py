n = int(input("Digite n: "))
i = int(input("Digite i: "))
j = int(input("Digite j: "))
nat, cont = 0, 0
while cont < n:
    if nat % i == 0 or nat % j == 0:
        print (nat)
        cont += 1
    nat += 1