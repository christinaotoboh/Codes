import random

chars="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(><"
number=input("Insert your desired password:")
number=int(number)

length=input("What is the length of your desired password?")
length=int(length)

for p in range number:
    password=''
    for c in range length:
        password += random.choice(chars)
        print(password)
        
