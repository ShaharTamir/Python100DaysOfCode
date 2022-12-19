from time import sleep


def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function


'''
This is a syntactic sugar for defining this - 
wrapped_say_hello = delay_decorator(say_hello)
wrapped_say_hello()
'''
@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def say_something():
    print("something")


def say_bye():
    print("bye!")


if __name__ == "__main__":
    say_hello()
    say_something()
    say_bye()
