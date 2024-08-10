'''
sliding window
try to find hello substring after deletion
'''
def can_say_hello(s):
    target = "hello"
    j = 0  
    for char in s:
        if char == target[j]:
            j += 1
        if j == len(target):
            return "YES"
    
    return "NO"
s = input().strip()
print(can_say_hello(s))