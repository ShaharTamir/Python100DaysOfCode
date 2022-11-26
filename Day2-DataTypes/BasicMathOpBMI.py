'''
PEMDAS - priority of operators:
()                4
** - power        3
* - multiple      2
/ - division      2
+ - add           1
- - subtraction   1
'''

'''
Write a program that calculates the Body Mass Index (BMI) 
from a user's weight and height.
'''

weight = float(input("enter weight "))
height = float(input("enter height "))

result = weight / height ** 2

print("your BMI: ", result)