'''
score = 0
height = 1.8

print(f"your score is {score}, your height is {height}")

type(8 // 3) = int.
'''

'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

'''

age = int(input("please enter age: "))
final_age = 90
days = 365.242199
weeks = 52.177457
months = 12

days_remain = (final_age - age) * days
weeks_remain = (final_age - age) * weeks
years_remain = (final_age - age) * months

print(f"You have {days_remain:.2f} days, {weeks_remain:.2f} weeks, \
and {years_remain} months left.")