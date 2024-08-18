'''



'''
def can_form_with_11_and_111(x):
    check = [False] * 1111
    for p in range(1, 1111):
        if p % 11 == 0 or p % 111 == 0:
            check[p] = True
        elif p > 11 and check[p - 11]:
            check[p] = True
        elif p > 111 and check[p - 111]:
            check[p] = True
    return check

check = can_form_with_11_and_111(1110)
t = int(input())
result=[]
for _ in range(t):
    x = int(input())
    if x >= 1111:
        result.append("YES")
    else:
        result.append("YES" if check[x] else "NO")
for i in result:
    print(i)