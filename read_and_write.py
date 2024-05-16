import os

change_API = False
text_shift = 12

# very simple encryption, can change to better if necessary
def caesar_cipher(message, shift):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  new_message = ""
  for char in message.lower():
    if char.isalpha():
      index = alphabet.find(char)
      new_message += shifted_alphabet[index]
    else:
      new_message += char
  return new_message

def write_to_hidden_file():
  hidden_filename = f".store"
  
  user_api = input("Get API KEY from https://aistudio.google.com/app/apikey \n Enter your API: \n")
  content = caesar_cipher(user_api, text_shift)
  
  # clear the file before write
  with open(hidden_filename, "w") as file:
    pass
  
  # write the api
  with open(hidden_filename, "w") as file:
    file.write(content)
    print("API Added")
    change_API = False
  
  return read_from_hidden_file()

def read_from_hidden_file():
  hidden_filename = f".store"
  # if file not exists, call write
  if (not os.path.exists(hidden_filename)) or change_API:
    write_to_hidden_file()

  with open(hidden_filename, "r") as file:
    read_content = file.read()
    return caesar_cipher(read_content, -text_shift)
