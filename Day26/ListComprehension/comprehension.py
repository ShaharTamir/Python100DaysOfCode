# regular comprehension: [ new_item for item in list ]
# conditional comprehension: [ new_item for item in list if test ]

# simple comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

# using strings
word = "something"
word_letters = [letter for letter in word]

# using range
range_list = [num * 2 for num in range(1, 5)]

# conditional
four_doubles = [i * 2 for i in range(1, 5) if (i * 2) % 4 == 0]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_case_long_names = [name.upper() for name in names if len(name) > 4]
