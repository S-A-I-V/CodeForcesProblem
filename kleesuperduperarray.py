def min_value_x(n, k):
    if n % 2 == 0:
        return 0
    else:
        return 1

t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    results.append(min_value_x(n, k))

print("\n".join(map(str, results)))
