nome = input("Digite seu nome: ").capitalize()

if len(nome) <= 3:
 while (len(nome) <= 3):
   print("\n**Nome inválido**\n")
   print("--Deve conter mais de 3 caracteres--\n")
   nome = input("Digite seu nome: ").capitalize()
   if len(nome) > 3:
    n = 4


idade = int(input("Digite sua idade: "))

while (idade > 150 or idade <= 0):
  print("\n**Idade inválida**\n")
  idade_nova = int(input("Digite sua idade: "))
   


salario = int(input("Digite seu salário: "))

while(salario <= 0 ):
  print("\n**Salário inválido**\n")
  salario = int(input("Digite seu salário: "))
   
    

sexo = input("Digite seu sexo (f) (m): ").upper()

while sexo != 'F' and sexo != 'M':
	print("\n**Genêro inválido**\n")
	sexo = (input("Digite seu sexo novamente (f) (m): ")).upper()
if sexo == "M":
	sexo = 'Masculino'
if sexo == "F":
	sexo = 'Feminino'


estado_civil = input("Digite seu estado civil (s) (c) (v) (d): ").upper()

while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
	print("\n**Estado Civil inválido**\n")
	estado_civil = input("Digite seu estado civil (s) (c) (v) (d): ").upper()

if estado_civil == 'S':
 if sexo == 'Feminino':
    estado_civil = 'Solteira'
 if sexo == 'Masculino':
    estado_civil = 'Solteiro'

if estado_civil == 'C':
 if sexo == 'Feminino':
  estado_civil = 'Casada'
 if sexo == 'Masculino':
  estado_civil = 'Casado'

if estado_civil == 'V':
 if sexo == 'Feminino':
  estado_civil = 'Viúva'
 if sexo == 'Masculino':
  estado_civil = 'Viúvo'

if estado_civil == 'D':
 if sexo == 'Feminino':
  estado_civil = 'Divorciada'
 if sexo == 'Masculino':
  estado_civil = 'Divorciado'

dados = input("Deseja ver os seus dados cadastrados no site? (S) (N): ").upper()

if dados == 'S':
	print("Nome: {} \nIdade: {} \nSalário: {} \nSexo: {} \nEstado Civil: {}".format(nome, idade, salario, sexo, estado_civil))
else:
	print("\nObrigado por se cadastrar :)\n)")





