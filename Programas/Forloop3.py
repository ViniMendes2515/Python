cont = 1
element = []

while cont > -1:
    num = int(input("Digite um elemento da sequência: "))
    element.append(num)
    if num == -1:
        cont = -1

par = []
for i in element:
    if i % 2 == 0:
        par.append(i)

print("Os números pares são: {0}".format(par))
