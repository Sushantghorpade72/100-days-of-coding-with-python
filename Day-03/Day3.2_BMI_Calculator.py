'''
Project Name: BMI calculator
Name: Sushant
 
*Using nesting

Conditions:
1. Under 18.5 they are under weight
2. Over 18.5 and below 25 they are normal weight
3. Over 25 but below 30 are overweight
4. Over 30 but below 35 are Obse
5. Above 35 they are clinically obese
'''
height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))

bmi = round(weight/(height**2),2)

if bmi < 18.5:
    print(f'Your BMI is {bmi} and you are Under weight')
elif bmi >= 18.5 and bmi < 25:
    print(f'Your BMI is {bmi} and you are Normal weight')
elif bmi >= 25 and bmi < 30:
    print(f'Your BMI is {bmi} and you are Overweight')
elif bmi >= 30 and bmi < 35:
    print(f'Your BMI is {bmi} and you are Obese')
else:
    print(f'Your BMI is {bmi} and you are Clinically Obese')
