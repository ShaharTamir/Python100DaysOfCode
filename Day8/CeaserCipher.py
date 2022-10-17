logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def calc_letters(letter, shift, shift_forward):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shift %= len(alphabet)
  if letter in alphabet:
    i = alphabet.index(letter)
    if shift_forward:
      i = (i + shift) % len(alphabet)
      return alphabet[i]
    else:
      return alphabet[i - shift]
  
  return letter

def two_choises(option_a, option_b, ability_a, ability_b):
  while True:
    choise = input(f"Type {option_a} to {ability_a}, type {option_b} to {ability_b}:\n")
    if choise == option_a:
      return True
    elif choise == option_b:
      return False
    else:
      print("I don't understand. try again.")

def app():
  encode_keyword = 'encode'
  decode_keyword = 'decode'
  run_app = True

  while run_app:
    encode = two_choises(encode_keyword, decode_keyword, 'encrypt', 'decrypt')
    msg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = ""

    for i in msg:
      result += calc_letters(i, shift, encode)

    print(\
    f"Here's the {(decode_keyword, encode_keyword)[encode]}d result: {result}")
    
    run_app = two_choises('yes', 'no', 'go again', 'finish')

print(logo)
app()
print("Goodbye.")
