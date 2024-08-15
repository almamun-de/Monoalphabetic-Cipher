# monoalphabetic_cipher.py

import random
import string

def generate_substitution_key():
    """Generates a random permutation of the alphabet for the cipher."""
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    return ''.join(letters)

def encrypt(plaintext, key):
    """Encrypts the plaintext using a monoalphabetic substitution based on the provided key."""
    table = str.maketrans(string.ascii_uppercase, key)
    return plaintext.upper().translate(table)

def decrypt(ciphertext, key):
    """Decrypts the ciphertext by reversing the substitution based on the provided key."""
    reverse_table = str.maketrans(key, string.ascii_uppercase)
    return ciphertext.translate(reverse_table)

if __name__ == "__main__":
    key = generate_substitution_key()
    print("Substitution Key:", key)

    plaintext = input("Enter plaintext: ")
    ciphertext = encrypt(plaintext, key)
    print("Encrypted:", ciphertext)

    decrypted = decrypt(ciphertext, key)
    print("Decrypted:", decrypted)
