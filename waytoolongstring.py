def waytoolong(string):
    if len(string)<=10:
        print(string)
    else:
        inbwletters=len(string)-2
        firstLetter=string[0]
        lastLetter=string[-1]
        print('%s%d%s'% (firstLetter,inbwletters,lastLetter))

n = int(input(""))
inputs = []
for i in range(n):
    value = input("")
    inputs.append(value)
for i in inputs:
    waytoolong(i)
    
