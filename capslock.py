'''
caps lock

word is mistyped when
- only upercase
- first lowercase rest uppercase

'''
word = input()
if (word[0].islower() and word[1:].isupper()):
    word = word.capitalize()
elif word.isupper():
    word=word.lower()
elif len(word)==1 and word.islower():
    word=word.upper()
else:
    word = word
print(word)
