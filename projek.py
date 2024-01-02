import random

source = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Masukkan Panjang Kata Sandi:"))
password = ""

for i in range(password_length):
    password += random.choice(source)

print(password)