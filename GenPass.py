import random
characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

quest=int(input("Escriba la longitud de su Cntraseña: "))

password=""

for i in range(quest):
    password+=random.choice(characters)
    
print(password)
