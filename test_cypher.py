def caesar_cipher(message, shift):
  """Encrypts/Decrypts a message using the Caesar cipher with a given shift value, preserving case and handling all printable ASCII characters.

  Args:
      message (str): The message to encrypt/decrypt.
      shift (int): The shift value for the cipher (positive for encryption, negative for decryption).

  Returns:
      str: The encrypted/decrypted message.
  """

  # Define the full printable ASCII character range (32 to 127)
  ascii_range = range(32, 128)

  # Create a shifted version of the ASCII range with wrapping using list comprehension
  shifted_ascii_range = [chr((ord(char) - 32 + shift) % 96 + 32) for char in ascii_range]

  new_message = ""
  for char in message:
    if char in ascii_range:
      # Get the original character's index in the ASCII range
      original_index = ascii_range.index(ord(char))
      # Use the shifted index to get the new character from the shifted range
      new_char = chr(shifted_ascii_range[original_index])
      new_message += new_char
    else:
      # Keep non-printable characters unchanged
      new_message += char
  return new_message

# Example usage
message = "This is a Secret Message! 123 @#$%^&*"
shift_value = 3

encrypted_message = caesar_cipher(message, shift_value)
decrypted_message = caesar_cipher(encrypted_message, -shift_value)  # Decrypt with negative shift

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
