from cryptography.fernet import Fernet
import time


with open('keyfile.key', 'rb') as keyfile:
    key = keyfile.read()
    keyfile.close()

fernet = Fernet(key)

nfile = input('What file would you like decrypted?: ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Made by: therealOri on GitHub')
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
