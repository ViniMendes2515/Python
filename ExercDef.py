def somaImposto(taxaImposto, custo):
    return custo*(1 + taxaImposto/100)

custo_normal = float(input("Digite o custo(R$): "))
taxa = float(input("Digite a taxa de imposto(%): "))

print("O custo recalculado com o imposto é de R$%.2f"%somaImposto(custo_normal, taxa))
