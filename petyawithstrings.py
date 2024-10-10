def compare_strings():
    string1 = input().strip().lower()
    string2 = input().strip().lower()
    
    if string1 < string2:
        print("-1")
    elif string1 > string2:
        print("1")
    else:
        print("0")

compare_strings()
