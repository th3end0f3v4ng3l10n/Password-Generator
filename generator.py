import random

def generate_password():
    chars = '_-abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(1,16):
        password += random.choice(chars)
    print("Generated Password: ", password)


generate_password()
