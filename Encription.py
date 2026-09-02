import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("Original message:", plain_text)
print("Encrypted message:", cipher_text)

# DECRYPT
decrypted_text = ""

for letter in cipher_text:
    index = key.index(letter)
    decrypted_text += chars[index]

print("Decrypted message:", decrypted_text)