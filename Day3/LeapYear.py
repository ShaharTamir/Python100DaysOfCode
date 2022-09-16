'''
Write a program that works out whether if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February.

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
'''

year = int(input("Please enter year to find out leap or not: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print("Leap")
else:
  print("Not leap")
  