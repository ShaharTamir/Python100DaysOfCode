import time


def speed_calc_decorator(function):
    start_time = time.time()
    function()
    finish_time = time.time()
    print(function.__name__ + "run speed: " + str(finish_time - start_time))


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


