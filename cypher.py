def caesar_cipher(message, shift):
    ascii_range = [chr(char) for char in range(32, 127)]
    shifted_ascii_range = ascii_range[shift:] + ascii_range[:shift]
    new_message = ""
    for char in message:
        if(char in ascii_range):
            index = ascii_range.index(char)
            new_message += shifted_ascii_range[index]
        else:
            new_message += char
    
    return new_message

plain_text = "Hey this is a great man &*123 ✓"
encrypted = caesar_cipher(plain_text, 3)
decrypted = caesar_cipher(encrypted, -3)
print(plain_text)
print(encrypted)
print(decrypted)
