'''
Write a program that interprets the Body Mass Index (BMI) 
based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese
'''

weight = float(input("enter weight "))
height = float(input("enter height "))

BMI = weight / height ** 2
result = ""

if BMI < 18.5:
  result = "underweight"
elif BMI < 25:
  result = "normal weight"
elif BMI < 30:
  result = "slightly overweight"
elif BMI < 35:
  result = "obese"
else:
  result = "clinically obese"

print(f"Your BMI is {BMI} which means you are {result}")