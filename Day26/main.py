import pandas

# setup
phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

word = input("Enter a word: ").upper()
phonetic_list = [phonetic_df[phonetic_df.letter == letter].code.item() for letter in word]
print(phonetic_list)
