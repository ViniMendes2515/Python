nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = nota1 + nota2 + nota3
media /= 3

if media >= 7 and media < 10:
    print("\nAprovado com %.2f de média" %media)
elif media < 7:
    print("\nReprovado com %.2f de média" %media)
elif media == 10:
    print("\nAprovado com Distinção")
