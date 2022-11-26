'''
#Basic Data Types

#String

#prints H
print("Hello"[0])
#prints o
print("Hello"[4])
#prints 123456
print("123"+"456")

#Integer

123456789
123_456_789 # more readable

#Float

3.14159

#Boolean

True
False


# To check what type u r using use type()
# To convert from different types use constructor functions - int(), float()...

'''

''' 
  Write a program that adds the digits in a 2 digit number. e.g. 
  If the input was 35, then the output should be 3 + 5 = 8
'''

two_digit_number = input("Type a two digit number ")

while len(two_digit_number) < 2:
  two_digit_number = input("please try again: ")

print(two_digit_number[0] + " + " + two_digit_number[1] + " = ", \
  int(two_digit_number[0])+ int(two_digit_number[1]))
  






















