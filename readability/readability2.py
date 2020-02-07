text = input("Text:  ")

while (len(text) < 1 or text.isdigit()):
    text =  input("Text: ")

words = 0
letters = 0
sentence = 0

#no of letters
for i in range(len(text)):
    if text[i].isalpha():
        letters += 1

#no of sentences
for i in range(len(text)):
    if (text[i] == '!' or text[i] == '.' or text[i] == '?'):
        sentence+=1

#no of words
for i in range(len(text)):
    if (text[i].isspace()):
        words += 1

L = letters/words*100
S = sentence/words*100
cl_index = 0.0588 * L - 0.296 * S - 15.8

if cl_index > 16:
    print("Grade 16+")
elif cl_index < 1:
    print("Before Grade 1")
else:
    print("Grade %s" %int(round(cl_index)))


print("Letters: %s" %letters)
print("Sentence: %s" %sentence)
print("Words: %s" %words)
