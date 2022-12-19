'''
Create a logging_decorator() which is going to log the name of the function that was called,
the arguments it was given and finally the returned output.
'''


# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        log_string = f"You called {function.__name__}("
        for i in range(len(args)):
            if i + 1 == len(args):
                log_string += f"{args[i]}"
            else:
                log_string += f"{args[i]}, "
        log_string += ")"
        print(log_string)
        return_val = function(args)
        print("It returned: ", return_val)
    return wrapper


# Use the decorator 👇
@logging_decorator
def foo(*args):
    result = 0
    for i in args[0]:
        result += i
    return result


foo(1, 2, 3)
foo(12, 2)
