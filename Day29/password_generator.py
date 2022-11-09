# Password Generator Project
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password(n_letters=0, n_numbers=0, n_symbols=0):
    components = [LETTERS, NUMBERS, SYMBOLS]
    nrs = [n_letters, n_numbers, n_symbols]
    password_list = []

    for i in range(len(components)):
        for j in range(nrs[i]):
            password_list += components[i][random.randint(0, len(components[i]) - 1)]

    random.shuffle(password_list)

    password = ""
    for i in password_list:
        password += i

    return password
