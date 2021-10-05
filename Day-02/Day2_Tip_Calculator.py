'''
Project Name: Tip calculator
Author: Sushant

Tasks:
1. Greeting for program
2. What is the total bill? 124.54
3. How many people to split the bill? 5
4. What percentage tip would you like to give?10,12 or 15?
5. Each person should pay?
'''
print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip  = int(input("How much tip you would like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill?"))

bill_with_tip = round(bill*(1 + tip/100),2)

split = round(bill_with_tip/people,2)

print(f"Total bill is ${bill_with_tip} and split for each person will be ${split}")
