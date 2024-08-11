'''
b array len(b)=m

'''
import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def check_non_decreasing(a):
    b = [gcd(a[i], a[i + 1]) for i in range(len(a) - 1)]
    return all(b[i] <= b[i + 1] for i in range(len(b) - 1))


t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 3:
        # For n = 3, just check if removing any one element solves the issue
        if check_non_decreasing(a[:2]) or check_non_decreasing(a[1:]) or check_non_decreasing([a[0], a[2]]):
            results.append("YES")
        else:
            results.append("NO")
        continue
    
    # Find first decreasing index
    first = -1
    last = -1
    for i in range(n - 2):
        if gcd(a[i], a[i+1]) > gcd(a[i+1], a[i+2]):
            if first == -1:
                first = i
            last = i
    
    if first == -1:
        # Already non-decreasing
        results.append("YES")
        continue
    
    # Check by removing elements at and around first decreasing point
    if (
        check_non_decreasing(a[:first+1] + a[first+2:]) or
        check_non_decreasing(a[:first] + a[first+1:]) or
        check_non_decreasing(a[:first+2] + a[first+3:])
    ):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))
