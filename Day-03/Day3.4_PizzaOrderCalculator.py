'''
Project Name: Pizza Order
Author: Sushant

Tasks:
1. Ask customer for size of pizza
2. Do they want to add pepperoni?
3. Do they want extra cheese?

Given data:
Small piza: $15
Medium pizza: $20
Large pizza: $ 25

Pepperoni for Small Pizza: +$2
Pepperoni for medium & large pizza: +$3

Extra cheese for any size pizza: +$1
'''
print("Welcome to python pizza deliveries!!!")
size = input("What size pizza do you want? S,M or L? ")
add_pep = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Price size wise:

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_pep == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
        
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is ${bill}")