'''
Project Name: Bank roulette
Author: Sushant
'''
import random

name_str = input("Give me everybody's name, seprated by a comma. ")

names = name_str.split(",")

person_who_pays = random.choice(names)

print(f'{person_who_pays} is going to pay for everyone')

 