yr=int(input(""))
newyr=yr+1
while True:
    s_ur= str(newyr)
    s_digits = set(s_ur)
    if len(s_digits) == len(s_ur):
        print(newyr)
        break
    newyr+=1
