pessoa = int(input("Digite o número de pessoas: "))

cont = 0

while cont < pessoa:
    
    dia = int(input("Digite o dia de nascimento da pessoa %i: " %(cont+1)))
    mes= int(input("Digite o mês de nascimento da pessoa %i: " %(cont+1)))
    ano = int(input("Digite o ano de nascimento da pessoa %i: " %(cont+1)))
    idade = int(input("Digite a idade a ser completada da pessoa %i: " %(cont+1)))
    print("A pessoa {4} fara {0} anos no dia {1}/{2}/{3}" .format(idade, dia, mes, ano + idade, cont + 1))

    cont += 1

