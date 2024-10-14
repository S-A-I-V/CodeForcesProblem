s = input()
uniq_chars = set(s)  
if len(uniq_chars) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")