t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = [False] * (n + 1)
    valid = True
    occupied[a[0]] = True 
    for i in range(1, n):
        seat = a[i]
        if occupied[seat]:
            valid = False
            break
        if seat > 1 and occupied[seat - 1] or seat < n and occupied[seat + 1]:
            occupied[seat] = True
        else:
            valid = False
            break
    if valid:
        results.append("YES")
    else:
        results.append("NO")
print("\n".join(results))
