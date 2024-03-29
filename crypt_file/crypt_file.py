from cryptography.fernet import Fernet

def encrypt(f_name, key):
    fernet = Fernet(key)
    
    with open(f_name, 'rb') as file:
        original = file.read()
        
    encrypted = fernet.encrypt(original)
    
    with open(f_name, 'wb') as enc_file:
        enc_file.write(encrypted)

def decrypt(f_name, key):
    fernet = Fernet(key)
    
    with open(f_name, 'rb') as enc_file:
        encrypted = enc_file.read()

decrypted = Fernet.decrypt(encrypt)
with open(f_name, 'wb') as dec_file:
        dec_file.write(decrypted)


key = Fernet.generate_key()
f_name = input("Enter Your filename: ")
encrypt(f_name, key)
decrypt(f_name, key)