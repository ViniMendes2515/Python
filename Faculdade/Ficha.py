import random

def Ficha():
    ficheiro = True
    while ficheiro:
        print("\n================| Gerador de Ficha/ Tormenta 20 |===================")
        print("[ 0 ] Encerrar Programa")
        print("[ 1 ] Criar Ficha")
        print("====================================================================")
    
        num = int(input("\nEscolha o Numero: "))
        if num == 0:
            exit()
    
        if num == 1:
            print("\n============================| NÍVEL |===============================")
            print("[ 0 ] Gerar nível aleatoriamente")
            print("[ 1 ] Escolher o nível")
            print("====================================================================")
    
    
        escolhaN = int(input("\nEscolha o número: "))    
        
        Força = random.randint(1, 25)
        Destre = random.randint(1, 25)
        Const = random.randint(1, 25)
        Inteli = random.randint(1, 25)
        Sabe = random.randint(1, 25)
        Cari = random.randint(1, 25)
    
        modF = ''
        modD = ''
        modC = ''
        modI = ''
        modS = ''
        modCa = ''
    
        if Força == 1:
            modF = '-5'
        elif (Força == 2) or (Força == 3):
            modF = '-4'
        elif (Força == 4) or (Força == 5):
            modF = '-3'
        elif (Força == 6) or (Força == 7):
            modF = '-2'
        elif (Força == 8) or (Força == 9):
            modF = '-1'
        elif (Força == 10) or (Força == 11):
            modF = '0'
        elif (Força == 12) or (Força == 13):
            modF = '+1'
        elif (Força == 14) or (Força == 15):
            modF = '+2'
        elif (Força == 16) or (Força == 17):
            modF = '+3'
        elif (Força == 18) or (Força == 19):
            modF = '+4'
        elif (Força == 20) or (Força == 21):
            modF = '+5'
        elif (Força == 22) or (Força == 23):
            modF = '+6'
        elif (Força == 24) or (Força == 25):
            modF = '+7'
    
        if Destre == 1:
            modD = '-5'
        elif (Destre == 2) or (Destre == 3):
            modD = '-4'
        elif (Destre == 4) or (Destre == 5):
            modD = '-3'
        elif (Destre == 6) or (Destre == 7):
            modD = '-2'
        elif (Destre == 8) or (Destre == 9):
            modD = '-1'
        elif (Destre == 10) or (Destre == 11):
            modD = '0'
        elif (Destre == 12) or (Destre == 13):
            modD = '+1'
        elif (Destre == 14) or (Destre == 15):
            modD = '+2'
        elif (Destre == 16) or (Destre == 17):
            modD = '+3'
        elif (Destre == 18) or (Destre == 19):
            modD = '+4'
        elif (Destre == 20) or (Destre == 21):
            modD = '+5'
        elif (Destre == 22) or (Destre == 23):
            modD = '+6'
        elif (Destre == 24) or (Destre == 25):
            modD = '+7'
    
        if Const == 1:
            modC = '-5'
        elif (Const == 2) or (Const == 3):
            modC = '-4'
        elif (Const == 4) or (Const == 5):
            modC = '-3'
        elif (Const == 6) or (Const == 7):
            modC = '-2'
        elif (Const == 8) or (Const == 9):
            modC = '-1'
        elif (Const == 10) or (Const == 11):
            modC = '0'
        elif (Const == 12) or (Const == 13):
            modC = '+1'
        elif (Const == 14) or (Const == 15):
            modC = '+2'
        elif (Const == 16) or (Const == 17):
            modC = '+3'
        elif (Const == 18) or (Const == 19):
            modC = '+4'
        elif (Const == 20) or (Const == 21):
            modC = '+5'
        elif (Const == 22) or (Const == 23):
            modC = '+6'
        elif (Const == 24) or (Const == 25):
            modC = '+7'
    
        if Inteli == 1:
            modI = '-5'
        elif (Inteli == 2) or (Inteli == 3):
            modI = '-4'
        elif (Inteli == 4) or (Inteli == 5):
            modI = '-3'
        elif (Inteli == 6) or (Inteli == 7):
            modI = '-2'
        elif (Inteli == 8) or (Inteli == 9):
            modI = '-1'
        elif (Inteli == 10) or (Inteli == 11):
            modI = '0'
        elif (Inteli == 12) or (Inteli == 13):
            modI = '+1'
        elif (Inteli == 14) or (Inteli == 15):
            modI = '+2'
        elif (Inteli == 16) or (Inteli == 17):
            modI = '+3'
        elif (Inteli == 18) or (Inteli == 19):
            modI = '+4'
        elif (Inteli == 20) or (Inteli == 21):
            modI = '+5'
        elif (Inteli == 22) or (Inteli == 23):
            modI = '+6'
        elif (Inteli == 24) or (Inteli == 25):
            modI = '+7'
    
        if Sabe == 1:
            modS = '-5'
        elif (Sabe == 2) or (Sabe == 3):
            modS = '-4'
        elif (Sabe == 4) or (Sabe == 5):
            modS = '-3'
        elif (Sabe == 6) or (Sabe == 7):
            modS = '-2'
        elif (Sabe == 8) or (Sabe == 9):
            modS = '-1'
        elif (Sabe == 10) or (Sabe == 11):
            modS = '0'
        elif (Sabe == 12) or (Sabe == 13):
            modS = '+1'
        elif (Sabe == 14) or (Sabe == 15):
            modS = '+2'
        elif (Sabe == 16) or (Sabe == 17):
            modS = '+3'
        elif (Sabe == 18) or (Sabe == 19):
            modS = '+4'
        elif (Sabe == 20) or (Sabe == 21):
            modS = '+5'
        elif (Sabe == 22) or (Sabe == 23):
            modS = '+6'
        elif (Sabe == 24) or (Sabe == 25):
            modS = '+7'
    
        if Cari == 1:
            modCa = '-5'
        elif (Cari == 2) or (Cari == 3):
            modCa = '-4'
        elif (Cari == 4) or (Cari == 5):
            modCa = '-3'
        elif (Cari == 6) or (Cari == 7):
            modCa = '-2'
        elif (Cari == 8) or (Cari == 9):
            modCa = '-1'
        elif (Cari == 10) or (Cari == 11):
            modCa = '0'
        elif (Cari == 12) or (Cari == 13):
            modCa = '+1'
        elif (Cari == 14) or (Cari == 15):
            modCa = '+2'
        elif (Cari == 16) or (Cari == 17):
            modCa = '+3'
        elif (Cari == 18) or (Cari == 19):
            modCa = '+4'
        elif (Cari == 20) or (Cari == 21):
            modCa = '+5'
        elif (Cari == 22) or (Cari == 23):
            modCa = '+6'
        elif (Cari == 24) or (Cari == 25):
            modCa = '+7'
    
        raças = ['Humano', 'Anão', 'Dahllan', 'Elfo', 'Goblin', 'Lefou', 'Minotauro', 'Qareen',
                 'Golem', 'Hynne', 'Medusa', 'Osteon', 'Sereia/Tritão', 'Síldide', 'Surageel', 'Trog']
        origem = ['Acólito', 'Amigo dos animais', 'Amnésico', 'Aristocrata', 'Artesão', 'Artista', 'Assistente de laboratório', 'Batedor', 'Capanga', 'Charlatão', 'Circense', 'Criminoso', 'Curandeiro',
                  'Eremita', 'Escravo', 'Estudioso', 'Fazendeiro', 'Forasteiro', 'Gladiador', 'Guarda', 'Herdeiro', 'Herói camponês', 'Marujo', 'Mateiro', 'Membro de guilda', 'Mercador', 'Minerador', 'Nômade'
                  'Pivete', 'Refugiado', 'Seguidor', 'Selvagem', 'Soldado', 'Taverneiro', 'Trabalhador']
        classe = ['Arcanista', 'Bárbaro', 'Bardo', 'Bucaneiro', 'Caçador', 'Cavaleiro',
                  'Clérigo', 'Druida', 'Guerreiro', 'Inventor', 'Ladino', ' Lutador', 'Nobre', 'Paladino']

        def Pericias():
            x3 = random.randint(1, 3)
            divplayer = nivel//2
            De = int(modD)
            Ca = int(modCa)
            Co = int(modC)
            Fo = int(modF)
            In = int(modI)
            Sa = int(modS)
    
            print("\nPerícias:\n-----------------------------")
            print(
                "Acrobacia:       {0} = {1} + {2} + {3} + {4}" .format(divplayer+De+x3, divplayer, De, x3, 0))
            print(
                "Adestramento:    {0} = {1} + {2} + {3} + {4}".format(divplayer+Ca+x3, divplayer, int(modCa), x3, 0))
            print(
                "Atletismo:       {0} = {1} + {2} + {3} + {4}".format(divplayer+Fo+x3, divplayer, int(modF), x3, 0))
            print(
                "Atuação:         {0} = {1} + {2} + {3} + {4}".format(divplayer+Ca+x3, divplayer, int(modCa), x3, 0))
            print(
                "Cavalgar:        {0} = {1} + {2} + {3} + {4}".format(divplayer+De+x3, divplayer, int(modD), x3, 0))
            print(
                "Conhecimento:    {0} = {1} + {2} + {3} + {4}".format(divplayer+In+x3, divplayer, int(modI), x3, 0))
            print(
                "Cura:            {0} = {1} + {2} + {3} + {4}".format(divplayer+Sa+x3, divplayer, int(modS), x3, 0))
            print(
                "Diplomacia:      {0} = {1} + {2} + {3} + {4}".format(divplayer+Ca+x3, divplayer, int(modCa), x3, 0))
            print(
                "Enganação:       {0} = {1} + {2} + {3} + {4}".format(divplayer+Ca+x3, divplayer, int(modCa), x3, 0))
            print(
                "Fortitude:       {0} = {1} + {2} + {3} + {4}".format(divplayer+Co+x3, divplayer, int(modC), x3, 0))
            print(
                "Furtividade:     {0} = {1} + {2} + {3} + {4}".format(divplayer+De+x3, divplayer, int(modD), x3, 0))
            print(
                "Guerra:          {0} = {1} + {2} + {3} + {4}".format(divplayer+In+x3, divplayer, int(modI), x3, 0))
            print(
                "Iniciativa:      {0} = {1} + {2} + {3} + {4}".format(divplayer+De+x3, divplayer, int(modD), x3, 0))
            print(
                "Intimidação:     {0} = {1} + {2} + {3} + {4}".format(divplayer+Ca+x3, divplayer, int(modCa), x3, 0))
            print(
                "Intuição:        {0} = {1} + {2} + {3} + {4}".format(divplayer+Sa+x3, divplayer, int(modS), x3, 0))
            print(
                "Investigação:    {0} = {1} + {2} + {3} + {4}".format(divplayer+In+x3, divplayer, int(modI), x3, 0))
            print(
                "Jogatina:        {0} = {1} + {2} + {3} + {4}".format(divplayer+Ca+x3, divplayer, int(modCa), x3, 0))
            print(
                "Ladinagem:       {0} = {1} + {2} + {3} + {4}".format(divplayer+De+x3, divplayer, int(modD), x3, 0))
            print(
                "Luta:            {0} = {1} + {2} + {3} + {4}".format(divplayer+Fo+x3, divplayer, int(modF), x3, 0))
            print(
                "Misticismo:      {0} = {1} + {2} + {3} + {4}".format(divplayer+In+x3, divplayer, int(modI), x3, 0))
            print(
                "Nobreza:         {0} = {1} + {2} + {3} + {4}".format(divplayer+In+x3, divplayer, int(modI), x3, 0))
            print(
                "Ofício:          {0} = {1} + {2} + {3} + {4}".format(divplayer+In+x3, divplayer, int(modI), x3, 0))
            print(
                "Percepção:       {0} = {1} + {2} + {3} + {4}".format(divplayer+Sa+x3, divplayer, int(modS), x3, 0))
            print(
                "Pilotagem:       {0} = {1} + {2} + {3} + {4}".format(divplayer+De+x3, divplayer, int(modD), x3, 0))
            print(
                "Pontaria:        {0} = {1} + {2} + {3} + {4}".format(divplayer+De+3, divplayer, int(modD), x3, 0))
            print(
                "Reflexos:        {0} = {1} + {2} + {3} + {4}".format(divplayer+De+x3, divplayer, int(modD), x3, 0))
            print(
                "Religião:        {0} = {1} + {2} + {3} + {4}".format(divplayer+Sa+x3, divplayer, int(modS), x3, 0))
            print(
                "Sobrevivência:   {0} = {1} + {2} + {3} + {4}".format(divplayer+Sa+x3, divplayer, int(modS), x3, 0))
            print(
                "Vontade:         {0} = {1} + {2} + {3} + {4}".format(divplayer+Sa+x3, divplayer, int(modS), x3, 0))
    
        if escolhaN == 0:
            nivel = random.randint(1, 20)
            print("")
            print("Raça: {0}           Origem: {1}           Classe: {2}           Nível: {3}" .format(random.choice(raças), random.choice(origem), random.choice(classe), nivel))      
            pv = 0
            pm = 0
            if 'Arcanista' in classe:
                pv = 8 + int(modC) + (4+int(modC)*nivel)
                pm = 6 * nivel
                Inteli += 2
                Sabe += 2
            
            elif classe == 'Bárbaro':
                pv = 24 + int(modC) +(6+int(modC)*nivel)
                pm = 3 * nivel
                Força += 2
                Destre += 2
                
            elif classe == 'Bardo':
                pv = 12 + int(modC)  +(3+int(modC)*nivel)
                pm = 4 * nivel
                Cari += 1
                Destre += 2
            elif classe == 'Bucaneiro':
                pv = 16 + int(modC)  +(4+int(modC)*nivel)
                pm = 3 * nivel
                Força += 2
                Destre += 2
            elif classe == 'Caçador':
                pv = 16 + int(modC) + (4+int(modC)*nivel)
                pm = 4 * nivel
                Força += 2
                Destre += 2
            elif classe == 'Cavaleiro':
                pv = 20 + int(modC) +(5+int(modC)*nivel)
                pm = 3 * nivel
                Força += 2
                Const += 2
            elif classe == 'Clérigo':
                pv = int(modC) + 16 +(int(modC)+4*nivel)
                pm = 5 * nivel
                Sabe += 2
                Destre += 2
            elif classe == 'Druida':
                pv = 16 + int(modC) +(4+int(modC)*nivel)
                pm = 4 * nivel
                Sabe += 4
            elif classe == 'Guerreiro':
                pv = 20 + int(modC) + (5+int(modC)*nivel)
                pm = 3 * nivel
                Força += 2 
                Destre += 2
            elif classe == 'Inventor':
                pv = 12 + int(modC) +(3+int(modC)*nivel)
                pm = 4 * nivel
                Inteli += 2 
                Sabe += 2
            elif classe == 'Ladino':
                pv = 12 + int(modC) +(3+int(modC)*nivel)
                pm = 4 * nivel
                Destre += 4
            elif classe == 'Lutador':
                pv = 20 + int(modC) +(5+int(modC)*nivel)
                pm = 3 * nivel
                Const += 2 
                Força += 2
            elif classe == 'Nobre':
                pv = 16 + int(modC) +(4+int(modC)*nivel)
                pm = 4 * nivel
                Const += 4
            elif classe == 'Paladino':
                pv = 20 + int(modC) +(4+int(modC)*nivel)
                pm = 3 * nivel
                Força += 2 
                Sabe += 2
        
            print("-------------------------------------------------------------------------------------")
            print("FOR:{0}/{1}     DES:{2}/{3}    CON:{4}/{5}     INT:{6}/{7}     SAB:{8}/{9}     CAR:{10}/{11}".format(Força, modF, Destre, modD, Const, modC, Inteli, modI, Sabe, modS, Cari, modCa))
            deslocamento = '9m'
            Tamanho = 'Médio'
            if raças == 'Goblin':
                Tamanho = 'Pequeno'
            
            print("\nPV: {0}    PM: {1}    Defesa: {2} ".format(pv, pm, 10+ int(modD)))
            print("Tamanho: {0}    Deslocamento: {1}".format(Tamanho, deslocamento))
            Pericias()
    
        elif  escolhaN != 0:
            nivel = int(input("\nEscolha o nível de 1 a 20: "))
            print("")
            if 0 < nivel < 20:
                print("Raça: {0}           Origem: {1}           Classe: {2}           Nível: {3}" .format(random.choice(raças), random.choice(origem), random.choice(classe), nivel))
                pv = 0
                pm = 0
                if 'Arcanista' in classe:
                    pv = 8 + int(modC) + 4*nivel + int(modC)*nivel
                    pm = 6 * nivel
                    Inteli += 2
                    Sabe += 2    
                elif classe == 'Bárbaro':
                    pv = 24 + int(modC) + 6*nivel + int(modC)*nivel
                    pm = 3 * nivel
                    Força += 2
                    Destre += 2
                    
                elif classe == 'Bardo':
                    pv = 12 + int(modC) + 3*nivel + int(modC)*nivel
                    pm = 4 * nivel
                    Cari += 1
                    Destre += 2
                elif classe == 'Bucaneiro':
                    pv = 16 + int(modC) + 4*nivel + int(modC)*nivel
                    pm = 3 * nivel
                    Força += 2
                    Destre += 2
                elif classe == 'Caçador':
                    pv = 16 + int(modC) + 4*nivel + int(modC)
                    pm = 4 * nivel
                    Força += 2
                    Destre += 2
                elif classe == 'Cavaleiro':
                    pv = 20 + int(modC) +(5+int(modC)*nivel)
                    pm = 3 * nivel
                    Força += 2
                    Const += 2
                elif classe == 'Clérigo':
                    pv = 16 + int(modC) + 4*nivel + int(modC)*nivel
                    pm = 5 * nivel
                    Sabe += 2
                    Destre += 2
                elif classe == 'Druida':
                    pv = 16 + int(modC) + 4*nivel + int(modC)*nivel
                    pm = 4 * nivel
                    Sabe += 4
                elif classe == 'Guerreiro':
                    pv = 20  + int(modC) + 5*nivel + int(modC)*nivel
                    pm = 3 * nivel
                    Força += 2 
                    Destre += 2
                elif classe == 'Inventor':
                    pv = 12 + int(modC) + 3*nivel + int(modC)*nivel
                    pm = 4 * nivel
                    Inteli += 2 
                    Sabe += 2
                elif classe == 'Ladino':
                    pv = 12 + int(modC) + 3*nivel + (int(modC)*nivel)
                    pm = 4 * nivel
                    Destre += 4
                elif classe == 'Lutador':
                    pv = 20  + int(modC) + 5*nivel + int(modC)*nivel
                    pm = 3 * nivel
                    Const += 2 
                    Força += 2
                elif classe == 'Nobre':
                    pv = 16  + int(modC) + 4*nivel + int(modC)*nivel
                    pm = 4 * nivel
                    Const += 4
                elif classe == 'Paladino':
                    pv = 20 + int(modC) + 4*nivel + int(modC)*nivel
                    pm = 3 * nivel
                    Força += 2 
                    Sabe += 2
                print("--------------------------------------------------------------------------")
                print("FOR:{0}/{1}     DES:{2}/{3}    CON:{4}/{5}     INT:{6}/{7}     SAB:{8}/{9}     CAR:{10}/{11}".format(Força, modF, Destre, modD, Const, modC, Inteli, modI, Sabe, modS, Cari, modCa))
                deslocamento = '9m'
                Tamanho = 'Médio'
                if raças == 'Goblin':
                  Tamanho = 'Pequeno'
                print("\nPV: %i    PM: %i    Defesa:%i"%(pv, pm, 10+ int(modD)))
                print("Tamanho: {0}    Deslocamento: {1}".format(Tamanho, deslocamento))
                Pericias()
            else:
                print("***Nível Inválido***\n")

Ficha()

    






