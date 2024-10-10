t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    count = 0
    
    if k == 1 or n < k:
        results.append(str(n))
        continue
    
    while n > 0:
        count += (n % k)
        n //= k
    
    results.append(str(count))

print("\n".join(results))

