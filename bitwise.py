'''


'''
t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    if m == 0:
        results.append(n)
    else:
        result = n | ((1 << m) - 1)
        results.append(result)

print("\n".join(map(str, results)))

