'''
Project Name: Add even numbers between 0 to 100
Author: Sushant
'''
even = []

for i in range(0,100):
    if i%2 == 0:
        even.append(i)

print(sum(even))