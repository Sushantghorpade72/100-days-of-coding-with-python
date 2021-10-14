'''
Project Name: Password Generator
Author: Sushant
'''
import string
import random

letters = [letter for letter in string.ascii_letters]
symbols = [symbol for symbol in string.punctuation]
numbers = [number for number in string.digits]

print("***Welcome to PyPassword Geerator***\n")
nr_letters = int(input("\nHow many letters would you like in your password? "))
nr_symbols = int(input("\nHow many symbols would you like in your password? "))
nr_numbers = int(input("\nHow many numbers would you like in your password? "))

password_list = []

for i in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
    
for j in range(1,nr_symbols+1):
    password_list += random.choice(symbols)
    
for k in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
    
password = ""

for char in password_list:
    password += char
    
print(f'\nYour password is: {password}')
