salário = float(input("Digite o seu salário: "))
if salário <= 280:
    percentual = 20
elif 280 < salário <= 700:
    percentual = 15
elif 700 < salário <= 1500:
    percentual = 10
else:
    percentual = 5

print("Salário inicial: R$%.2f"%salário)
print("Percentual aplicado: %%%i"%percentual)
print("Valor do aumento: R$%.2f"%(salário*percentual/100))
print("Novo salário: R$%g"%(salário*(1+percentual/100)))