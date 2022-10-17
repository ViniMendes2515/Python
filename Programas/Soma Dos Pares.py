n = int(input('\nDigite um número inteiro: '))
cont = 0
soma = 0
while cont <= n:
    if cont % 2 == 0:
        soma += cont
        cont += 1
print("A soma dos {0} primeiros naturais pares é igual a {1}." .format(n, soma))
