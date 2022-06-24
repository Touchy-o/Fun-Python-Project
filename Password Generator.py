import random

length = input("How long is your password : ")

letters = "ABCEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"

password = "".join(random.sample(letters, int(length)))
print(password)