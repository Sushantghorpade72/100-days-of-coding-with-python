'''
Project Name: Love Calculator
Author: Sushant
'''
print("Welcome to love calculator!!!")
name1 = input("What's your name? \n")
name2 = input("what's their name? \n")

combined_str = name1 + name2
lower_str = combined_str.lower()

t = lower_str.count('t')
r = lower_str.count('r')
u = lower_str.count('u')
e = lower_str.count('e')

true = t + r + u + e

l = lower_str.count('l')
o = lower_str.count('o')
v = lower_str.count('v')
e = lower_str.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f'Your love score is {love_score}, you go together like coke and ice cream')
elif (love_score >= 40) or (love_score <= 50):
    print(f'Your love score is {love_score}, you are altogether')
else:
    print(f'Your love score is {love_score}, peace!!')