import re
pattern = re.compile('[!.?]+')

#getting user input
text = input("Text:  ")
while (len(text) < 1 or text.isdigit()):
    text =  input("Text: ")


words = 0
letters = 0
sentences = 0

#number of words
for word in text.strip().split():
    words += 1


#no of letters
for i in range(len(text)):
    if text[i].isalpha():
       letters += 1


#no of sentences
for sentence in re.findall(pattern, text.strip()):
    sentences += 1

#conditionals
L = letters /words * 100
S = sentences / words * 100
cl_index = 0.0588 * L - 0.296 * S - 15.8

# L => average number of letters per 100 words in the text
# S => average number of sentences per 100 words in the text

if cl_index > 16:
    print("Grade 16+")
elif cl_index < 1:
    print("Before Grade 1")
else:
    print("Grade %s" %int(round(cl_index)))


print("Letters: %s" %letters)
print("Sentence: %s" %sentences)
print("Words: %s" %words)