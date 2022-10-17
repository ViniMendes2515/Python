nomes = []
agenda = {}

while True:
    ordem = input('Deseja adicionar um novo contato(add) ou parar a execução(stop)').lower()

    if not ordem.isalpha():
        print("Digite apenas letras!")
        
    elif ordem.startswith('add'):
        contato = {}


        nome = input('Digite o nome do contato: ')
        if not nome[0].isupper():
            nome = nome[0].upper() + nome[1:]

        nomes.append(nome)

        tel = input('Digite o telefone do contato: ')
        contato['Telefone'] = tel

        end = input('Digite o endereço do contato: ')
        contato['Endereço'] = end

        email = input('Digite o Email do contato: ')
        contato['Email'] = email

        agenda[nome] = contato
        
    elif ordem.startswith('stop'):
        break

print('A G E N D A\n')
nomes.sort()
for nome in nomes:
    print('Nome: ', nome)
    print('Telefone: ', agenda[nome]['Telefone'])
    print('Endereço: ', agenda[nome]['Endereço'])
    print('Email: ', agenda[nome]['Email'])
    print("")