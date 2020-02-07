"""
This is an encryption-decryption  process where a sentence or word is given and they are encrypted based  
on the number of steps (k) required.
In doing this python has a string module that containsthe ASCII encodings of letters 
(those from the english alphabets inclusive).
Here  we are required to make the file accept a command line argument.
"""

import string, sys

def main():
    key = int(sys.argv[1])
    if len(sys.argv) != 2:
        print("Usage: ./caesar k")
        exit(1) # or sys.exit(1) or # raise IndexError ("Usage: ./caesar k")
    
    elif key < 1:
        raise ValueError ("Negative key not allowed")

    plainText = input("Plaintext: ")
    cipharText = caesar_encrypt(plainText, key)
    print(f'{plainText} : {cipharText}')

def caesar_encrypt(text, key):

    n_alphabets = len(string.ascii_lowercase) #or string.ascii_uppercase
    text = list(text)

    #in ascii integer of 'A' is 65 while that  of 'a' is 97
    for i, character in enumerate(text):
        if character.isalpha():
            if character.isupper():
                pi = ord(character) - ord("A")
                ci = (pi + key)% n_alphabets
                text[i] = chr(ci + ord("A"))
            else:
                pi = ord(character) - ord("a")
                ci = (pi + key) % n_alphabets
                text[i] = chr(ci + ord("a"))
    text = ''.join(text)

    return text

if __name__ == "__main__":
    main()


