'''
You need to write a function that checks 
whether if the number passed into it is a prime number or not.
'''

#Write your code below this line 👇
def prime_checker(number):
  for i in range(2, int(number ** 0.5) + 1):
    if 0 == number % i:
      print(f"{number}, is not a prime number")
      return
  print(f"{number} is a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)