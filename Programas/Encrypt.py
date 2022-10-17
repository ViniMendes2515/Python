import pyAesCrypt
import glob
import os
# Encrypt/decrypt Buffer de 64K
bufferSize = 64 * 1024
# Diretório atual
curDir = os.getcwd()
# Solicitar senha ao usuário para criptografar arquivos
password1 = input('\n> Digite a senha para o Encripty: ')
 
print('\n> Começando a criptografar...\n\n')
# Loop principal para criptografar
for x in glob.glob('diretorio\\**\*', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.aes')
    # Encrypt
    if os.path.isfile(fullpath):
        print('>>> Original: \t' + fullpath + '')
        print('>>> Criptografado: \t' + fullnewf + '\n')
        pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
        os.remove(fullpath)           # Remove o arquivo depois de criptografado