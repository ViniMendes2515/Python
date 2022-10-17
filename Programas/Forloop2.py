cont = 1
element = []

while cont > -1:
    num = int(input("Digite um elemento da sequência: "))
    element.append(num)
    if num == -1:
        cont = -1

maior = []
for i in element:
    if i > 10:
        maior.append(i)

print("Os números maiores que 10 são: {0}".format(maior))
