import random

length = input("How many characters does your password need : ")

letters = "ABCEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"

password = "".join(random.sample(letters, int(length)))
print(password)
