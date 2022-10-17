import pyAesCrypt
import glob
import os
# Encrypt/decrypt Buffer de 64K
bufferSize = 64 * 1024
# Diretório atual
curDir = os.getcwd()
# Solicitar senha ao usuário para descriptografar arquivos
password1 = input('\n> Digite a senha para o Decripty: ')
 
print('\n> Começando a descriptografar...\n\n')
# Loop principal para descriptografar 
for x in glob.glob('directory\\**\*', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, os.path.splitext(x)[0])
    # Decrypt
    if os.path.isfile(fullpath):
        print('>>> Criptografado: \t' + fullpath + '')
        try:
            pyAesCrypt.decryptFile(fullpath, fullnewf, password1, bufferSize)
            print('>>> Descriptografado: \t' + fullnewf + '\n')
            os.remove(fullpath)      # Remove o arquivo depois de descriptografado
        except ValueError:
            print('>>> Error - Senha Incorreta!\n')