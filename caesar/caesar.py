"""
This is an encryption-decryption  process where a sentence or word is given and they are encrypted based  
on the number of steps (k) required.
In doing this python has a string module that containsthe ASCII encodings of letters 
(those from the english alphabets inclusive).
Here  we are required to make the file accept a command line argument.
"""

import string, sys

def main(decrypt=False, encrypt=False):
    try:
        key = int(sys.argv[1])
        if key < 1:
            raise ValueError ("Negative key not provided")
    except (ValueError, IndexError):
        print("Usage: ./caesar k")
        sys.exit(1)

    if encrypt:
        plainText = input("Plaintext: ")
        cipharText = caesar_encrypt(plainText, key)
        print(f"{plainText}: {cipharText}")
    if decrypt:
        cipharText = input("Ciphartext: ")
        plainText = caesar_decrypt(cipharText, key)   
        print(f"{cipharText} : {plainText}")

def caesar_encrypt(text, key):
    text= list(text)
    n_alphabets = len(string.ascii_lowercase) #or string.ascii_uppercase

    #in ascii integer of 'A' is 65 while that  of 'a' is 97
    for i, character in enumerate(text):
        if character.isalpha():
            if character.isupper():
                #pi = ord(character) - ord("A") if upper or ord("a") if lower
                #ci = pi + key ci => ciphartext
                text[i] = chr((ord(character) - ord("A") + key) % n_alphabets + ord("A"))
            else:
                text[i] = chr((ord(character) - ord("a") + key) % n_alphabets + ord("a"))
        else:
            text[i] = character
    text = ''.join(text)
    return text

def caesar_decrypt(text, key):
    text = list(text)
    n_alphabets = len(string.ascii_lowercase) #or string.ascii_uppercase

    #in ascii integer of 'A' is 65 while that  of 'a' is 97
    for i, character in enumerate(text):
        if character.isalpha():
            if character.isupper():
                #pi = ord(character) - ord("A") if upper or ord("a") if lower
                #ci = pi + key ci => ciphartext
                text[i] = chr((ord(character) - ord("A") - key) % n_alphabets + ord("A"))
            else:
                text[i] = chr((ord(character) - ord("a") - key) % n_alphabets + ord("a"))
        else:
            text[i] = character
    text = ''.join(text)
    return text


if __name__ == "__main__":
    main(decrypt=True)