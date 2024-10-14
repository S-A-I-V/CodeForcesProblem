s=str(input())
lcase=0
ucase=0
for i in s:
    if i.isupper():
        ucase+=1
    else:
        lcase+=1
if lcase>ucase:
    print(s.lower())
elif lcase<ucase:
    print(s.upper())
else:
    print(s.lower())
    