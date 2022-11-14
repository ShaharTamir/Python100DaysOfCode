import pandas

# setup
phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")


def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        phonetic_list = [phonetic_df[phonetic_df.letter == letter].code.item() for letter in word]
    except (KeyError, ValueError):
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
