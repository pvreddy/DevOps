import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHI'
password = ' '
for i in range(10):
    password += random.choice(chars)
print password
