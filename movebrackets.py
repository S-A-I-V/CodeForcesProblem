'''
logic- 
balance variable tracking the number of brackets. 
balance+= for (
balance-= for )
'''
def movebrackets(n: int, s: str) -> int:
    balance = 0
    minbal = 0 
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        minbal = min(minbal, balance)
    return abs(minbal)
result=[]
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    result.append((movebrackets(n, s)))
for _ in result:
    print(_)