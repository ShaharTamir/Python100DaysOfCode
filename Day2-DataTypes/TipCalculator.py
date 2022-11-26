print("Welcome to the tip calculator")
total = input("What was the total bill? ")
if not (total[0] in str(range(10))):
  total = float(total[1:])
else:
  total = float(total)

tip_precentage = int(input("What precentage tip would you \
like to give? 10, 12, or 15? "))
split = int(input("How many people split the bill? "))
result = (total + total * tip_precentage / 100) / split
print(f"Each person should pay: ${result:.2f}")
