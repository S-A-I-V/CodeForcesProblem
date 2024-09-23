t = int(input())  
result = []  
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  

    prev = a[0]
    total = 0
    max_diff = 0

    for i in range(1, n):
        if a[i] < prev:
            diff = prev - a[i]
            total += diff
            max_diff = max(max_diff, diff)
        else:
            prev = a[i]

    result.append(total + max_diff)

for res in result:
    print(res)
