t = int(input())
result=[]
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        result.append(-1)
    else:
        # For odd n, construct a symmetric permutation
        for i in range((n // 2) + 1):
            result.append(i + 1)
            if i != n // 2:
                result.append(n - i)

for i in result:
    print(i)
