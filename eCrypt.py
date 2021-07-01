from cryptography.fernet import Fernet
import time


key = Fernet.generate_key()
with open('keyfile.key', 'wb') as keyfile:
    keyfile.write(key)
    keyfile.close()
    
with open('keyfile.key', 'rb') as keyfile:
    key = keyfile.read()
    keyfile.close()
    
fernet = Fernet(key)

nfile = input('What file would you like encrypted?: ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Made by: therealOri on GitHub')
print('\n')

with open(nfile, 'rb') as ofile:
    original = ofile.read()
    ofile.close()
    
encrypted = fernet.encrypt(original)

with open(nfile, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    encrypted_file.close()

time.sleep(1.5)
print(f'{nfile} has been encrypted successfully!')
print("Make sure to save the key generated in the .key file before encrypting another file. Otherwise you won't be able to decrypt your file.")
