def add(*args, **kwargs):
    sum = 0
    for num in args:
        if type(num) == int:
            sum += num

    return sum

print(add(1, 2, 3, 4, soap="blah", blo=2))
