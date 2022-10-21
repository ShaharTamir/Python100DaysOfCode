def add(num_a, num_b):
    return num_a + num_b

def sub(num_a, num_b):
    return num_a - num_b

def multi(num_a, num_b):
    return num_a * num_b

def div(num_a, num_b):
    return num_a / num_b

def calculator():
  """
  Calc two numbers and an operation.
  May use result to continue calculating according to user input.

  :return: (float) result of calculation
  """
  operators = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
  }

  first_number = float(input("What's the first number?: "))
  finish = False
  result = 0

  for i in operators:
      print(i)

  while not finish:
    oper = input("Pick an operation: ") # assume valid
    sec_number = float(input("What's the next number?: "))

    for op_key in operators:
        if oper == op_key:
            result = operators[op_key](first_number, sec_number)

    print(f"{first_number} {oper} {sec_number} = {result}")
    finish = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'n'
    first_number = result

if __name__ == "__main__":
    calculator()