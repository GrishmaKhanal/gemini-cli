def caesar_cipher(message, shift):

  # Define the full printable ASCII character range (32 to 127)
  ascii_range = range(32, 127)

  shifted_ascii_range = [chr(char - 32 + shift) % 95 + 32 for char in ascii_range]

  new_message = ""
  for char in message:
    if char in ascii_range:
      # Get the original character's index directly (no ord needed)
      original_index = ascii_range.index(char)
      # Use the shifted index to get the new character from the shifted range
      new_char = shifted_ascii_range[original_index]
      new_message += new_char
    else:
      # Keep non-printable characters unchanged
      new_message += char
  return new_message

initial_text = "Hey this is message!"

encrpted_text = caesar_cipher(initial_text, 3)
print(encrpted_text)

print(caesar_cipher(encrpted_text, -3))