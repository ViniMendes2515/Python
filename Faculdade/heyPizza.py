import os

nomes = []
cart = []
lista_bebidas = []

pizzas = {
    'Margherita': 9.50,
    'Milho-catupiry': 9.50,
    'Muçarela': 9.50,
    '5-Queijos': 11.50,
    'Amoda': 11,
    'Calabresa': 10.50,
    'Fricasse': 11,
    'Palmito': 10,
    'Toscana': 12,
    'Portuguesa': 10.50,
    'Frango-catupiry': 11,
    'Frango-cheddar': 11,
    'Pernil-casa': 11,
    'Pernil-chefe': 11,
    'Toscana-cheddar': 12,
    'Churrasco': 11.50,
    'Bacon-catupiry': 11.50,
    'Rucula': 11,
    'Frango-catupiry-bacon': 12,
    'Carne-seca-catupiry': 11.50,
    'Peito-de-peru': 10.50,
    'Lombinho': 11,
    'Brocolis': 10.50,
    'File-gorgonzola': 11.50,
    '------------': 0
}


bebidas = {
    'Mini lata': 3.50,
    'Lata': 5.50,
    'Litro-1': 8,
    'Litro-1.5': 9.50,
    'Litro-2': 11,
    'Brahma': 6,
    'Amstel': 6,
    'Long-neck': 8.75,
    'Agua-gas': 3.50,
    'Agua-sem-gas': 2.50,
    'Agua-tonica': 5.50,
    'Guarana-600': 6.50,
    'Suco-lata': 6,
    'Suco-natural-300': 6.50,
    'Suco-natural-900': 12,
    'Suco-litro': 9,
    'Energetico': 10,
    'Aquarius': 5.50,
    '------------': 0
}


def cadastro():
    print("\nDigite 0 para parar!")
    nome = input("\nDigite o nome do cliente: ")
    nomes.append(nome)
    while True:
        nome = input("\nDigite o nome do cliente: ")
        nomes.append(nome)
        if nome == "0":
            nomes.pop()
            break


def bebida():
    print("================== BEBIDAS =====================\n")
    for key, value in bebidas.items():
        print(f'{key:16}:  R${value:.2f}')
    print("\n=============================================\n")


def cardapio():
    print("================== PIZZAS =====================\n")
    for key, value in pizzas.items():
        print(f'{key:23}:  R${value:.2f}')
    print("\n=============================================\n")


def pedido():
    global food, drink

    for i in nomes:
        while True:
            food = input(
                f"Selecione as pizzas que o {i} deseja (x para sair): ")
            if food == 'x':
                print(" ")
                cart.append('------------')
                break
            elif pizzas.get(food) is not None:
                cart.append(food)

    print("")
    bebida()
    for i in nomes:
        while True:
            drink = input(
                f"{i} deseja adicionar bebida ao pedido? (x para sair): ")
            if drink == 'x':
                print(" ")
                lista_bebidas.append('------------')
                break
            elif bebidas.get(drink) is not None:
                lista_bebidas.append(drink)

def mostrar():
    global total
    total = 0
    print("\n================== PIZZAS ===================")
    for food in cart:
        total += pizzas.get(food)
        print(food, end="\n")
    print("=============================================\n")
    print(nomes)
    print("\n================== BEBIDAS ==================")
    for drink in lista_bebidas:
        total += bebidas.get(drink)
        print(drink, end="\n")
    print("=============================================\n")
    
    print(f"\n\nFoi feito um pedido de {len(cart)} pizzas")
    print(f"\n\nO total do pedido sai por R${total:.2f}")
    prox = input("")


def main():
    ler_op = True
    os.system("clear")

    while ler_op:
        os.system("clear")
        print("\n====================== MENU ======================")
        print("\n1 - CADASTRO")
        print("\n2 - PEDIDO ")
        print("\n3 - VALORES")
        print("\n4 - SAIR")
        print("\n================================================")

        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            cadastro()
            os.system("clear")
        elif opcao == "2":
            os.system("clear")
            cardapio()
            pedido()
        elif opcao == "3":
            os.system("clear")
            mostrar()
        elif opcao == "4":
            os.system("clear")
            ler_op = False
        else:
            print("Opção Inválida")

main()
