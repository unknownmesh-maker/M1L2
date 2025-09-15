import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("longitud de la contraseña:"))

password = ""

for i in range(length):
    password += random.choice(characters)

print("tu contraseña es:", password)
