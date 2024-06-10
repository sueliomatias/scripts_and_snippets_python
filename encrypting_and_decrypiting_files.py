from cryptography.fernet import Fernet

# arquivo a ser criptografado
file_to_encrypt = 'sensitive_data.txt'

# gerar uma chave de criptografia
key = Fernet.generate_key()

# criar uma instância do objeto Fernet com a chave gerada
cipher = Fernet(key)

# ler o arquivo a ser criptografado
with open(file_to_encrypt, 'rb') as file:
    data = file.read()

# criptografar o arquivo
encrypted_data = cipher.encrypt(data)

# escrever os dados criptografados em um novo arquivo
with open('encrypted_file.txt', 'wb') as file:
    file.write(encrypted_data)

print("arquivo criptografado com sucesso.")

# descriptografar o arquivo criptografado
with open('encrypted_file.txt', 'rb') as file:
    encrypted_data = file.read()

decrypted_data = cipher.decrypt(encrypted_data)

# escrever os dados descriptografados em um novo arquivo
with open('decrypted_file.txt', 'wb') as file:
    file.write(decrypted_data)

print("arquivo descriptografado com sucesso.")