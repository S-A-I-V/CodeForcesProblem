def min_dig(x):
    return min(int(d) for d in str(x))
def max_dig(x):
    return max(int(d) for d in str(x))

def find_aK(a1, K):
    current = a1
    for _ in range(K-1):
        min_d = min_dig(current)
        max_d = max_dig(current)
        if min_d == 0:
            break
        current += min_d * max_d
    return current
t = int(input())
results = []
for _ in range(t):
    a1, K = map(int, input().split())
    results.append(find_aK(a1, K))

for result in results:
    print(result)
