for i in range(1, 101):
  if 0 == i % 15:
    print("FizzBuzz")
  elif 0 == i % 3:
    print("Fizz")
  elif 0 == i % 5:
    print("Buzz")
  else:
    print(i)