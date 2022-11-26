print("Wlecome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  price = 0
  age = int(input("Please enter your age: "))
  if age < 12:
    price = 5
  elif age <= 18:
    price = 7
  elif age < 45 or age > 55:
    price = 12

  photo = int(input("Please enter 1 if you'd photos from the ride: "))
  
  if photo == 1:
    price += 3
  
  print(f"The total bill is: {price}")

else:
  print("Sorry, you are too short to ride")