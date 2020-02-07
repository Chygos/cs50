import string, sys, re, math

pattern = re.compile(r'([^A-za-z])+')


#checking argument
if len(sys.argv) != 2:
    print('Usage: ./substitution  key')
    exit(1)
elif pattern.search(sys.argv[1]):
    print('Usage: ./substitution key')
    exit(1)

#checking for repeated letters
key = sys.argv[1]

if len(key) != 26:
    print('key must contain 26 characters')
    exit(1)
else:
    for char in list(key):
        if key.count(char) > 1 or len(key) != 26:
            print('Key must not have repeated letters')
            exit(0)

#Get user input
plainText = list(input('PlainText: '))
cipharText = list()
for i in range(len(plainText)):
    if plainText[i].isalpha():
        if plainText[i].islower():
            pi = ord(plainText[i]) - ord('a')
            ci = key[pi]
            cipharText.append(ci.lower())
        elif plainText[i].isupper():
            pi = ord(plainText[i]) - ord('A')
            ci = key[pi]
            cipharText.append(ci.upper())
    else:
        cipharText.append(plainText[i])

print(f"CipharText : {''.join(cipharText)}")