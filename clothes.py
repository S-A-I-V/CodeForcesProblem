n, m = map(int, input().split())
prices = list(map(int, input().split()))
matches = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    matches[u].append(v)
    matches[v].append(u)

min_cost = float('inf')

for i in range(n):
    for j in matches[i]:
        for k in matches[j]:
            if k in matches[i]:
                min_cost = min(min_cost, prices[i] + prices[j] + prices[k])

print(min_cost if min_cost != float('inf') else -1)
