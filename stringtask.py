'''
string-uppercase, lowercase, latin

to do- 
delete vowels
insert . before consonants
uppercaseconsonants with lowercase
'''
from array import *
t = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
t = t.lower()
result = []
for char in t:
    if char not in vowels:  
        result.append('.')
        result.append(char)
word = ''.join(result)
print(word)
