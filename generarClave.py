from cryptography.fernet import Fernet

# Generar una clave Fernet segura
clave = Fernet.generate_key()

# Imprimir la clave en formato de bytes (b'...')
print("Clave en formato bytes:")
print(clave)

# Opcional: Imprimir la clave como un string normal de texto
print("\nClave en formato texto (string):")
print(clave.decode())