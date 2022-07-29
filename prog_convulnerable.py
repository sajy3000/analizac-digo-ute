from Crypto.Cipher import AES
from Crypto import Random

state = True
iv = bytearray([
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
])

while state:
    key = input("Ingrese la clave de cifrado (máximo 16 cáracteres): ")
    if len(key) > 16:
        print("La clave ingresada debe ser máximo de 16 cáracteres, intente de nuevo")
    else:
        state = False

with open("archivo_ejemplo.txt", "r") as archivo_ejemplo:
    text = archivo_ejemplo.read()

class CifrarDescifrar:

    def __init__(self, key, text, iv):
        self.padding_key = key + '0'*(16-len(key))
        self.padding_data = text + '0'*(16-len(text))
        self.modo = AES.MODE_CBC
        self.iv = iv
        self.verify = len(text)

    def encrypt(self):
        encryptor = AES.new(self.padding_key.encode('utf-8'), self.modo, self.iv)
        # Utilizo el metodo encrypt de AES para cifrar el texto con los requisitos anteriores ingresados
        cipher_text = encryptor.encrypt(self.padding_data.encode('utf8'))
        # Guardando el archivo cifrado en un txt como binario
        with open("archivo_cifrado.txt", "wb") as archivo_cifrado:
            archivo_cifrado.write(cipher_text)

    #Metodo para descifrar
    def decrypt(self):
        #Abriendo el archivo binario para descifrarlo
        with open("archivo_cifrado.txt", "rb") as archivo_cifrado:
            cipher_data = archivo_cifrado.read()
        # Cargo en la variable decryptor las condiciones del modo AES
        decryptor = AES.new(self.padding_key.encode('utf-8'), self.modo, self.iv)
        # Utilizo el metodo decrypt de AES para descifrar el texto con los requisitos anteriores ingresados
        data_decrypt = decryptor.decrypt(cipher_data)
        # Convierto en string el texto descifrado
        var_string = data_decrypt.decode('utf-8')
        # Escribo en otro archivo el texto descifrado
        with open("archivo_descifrado.txt", "w") as archivo_decifrado:
            # Utilizo slicing para quitar el padding del texto descifrado
            archivo_decifrado.write(var_string[:self.verify])


# Instancio a la clase para crear al objeto
execute = CifrarDescifrar(key, text, iv)

# Invoco lo metodos del objeto y capturo los errores comunes
try:
    execute.encrypt()
    execute.decrypt()

except ValueError as ve:
    print(f"ha ocurrido el siguiente error: {ve}")
