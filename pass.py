import random

print("Con este programa podras generar contraseñas de manera aleatoria (ᵔ ᗜ ᵔ)")

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

cantidad_caracteres = int(input("¿Cuantos caracteres desea tener?"))

for i in range(cantidad_caracteres):
    password += random.choice(caracteres)

print("la contraseña generada es: ", password)
