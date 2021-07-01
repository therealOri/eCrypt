from cryptography.fernet import Fernet
import time
import os
ver = 'v1.0'

fkey = input('Please input/load your file key: ')
os.system('clear||cls')

with open('keyfile.key', 'w') as keyf:
    keyf.write(fkey)
    keyf.close()
print(f'Key has been loaded!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\n')

with open('keyfile.key', 'rb') as keyfile:
    key = keyfile.read()
    keyfile.close()

fernet = Fernet(key)

nfile = input('What file would you like decrypted?: ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('\n')


with open(nfile, 'rb') as enc_file:
    encrypted = enc_file.read()
    enc_file.close()
  

decrypted = fernet.decrypt(encrypted)


with open(nfile, 'wb') as dec_file:
    dec_file.write(decrypted)
    dec_file.close()
    
time.sleep(1.5)
print(f'{nfile} has been decrypted successfully!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Made by: therealOri on GitHub | {ver}')
