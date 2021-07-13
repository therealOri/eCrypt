from cryptography.fernet import Fernet
import time
import os
ver = 'v1.0'

key = Fernet.generate_key()

fkey = input('File name for generated file key: ')
os.system('clear||cls')
with open(fkey, 'wb') as keyf:
    keyf.write(key)
    keyf.close()
print(f'Key has been saved to {fkey}!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\n')

with open('keyfile.key', 'wb') as keyfile:
    keyfile.write(key)
    keyfile.close()
print('Your file key has also been saved to a file called keyfile.key.\nI do this so I can read the key in this file later to encrypt and decrypt your data.')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\n')


with open('keyfile.key', 'rb') as keyfile:
    key = keyfile.read()
    keyfile.close()
    
fernet = Fernet(key)

nfile = input('What file would you like encrypted?: ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
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
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Made by: therealOri on GitHub | {ver}')
