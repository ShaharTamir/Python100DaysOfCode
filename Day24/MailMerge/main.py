letter_text = ""
names = []
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_text = letter_file.read()

with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.read().split()

for name in names:
    new_file = open(f"Output/ReadyToSend/{name}_invitation.txt", "w")
    new_file.write(letter_text.replace("[name]", f"{name}"))
 