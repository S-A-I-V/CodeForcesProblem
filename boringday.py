t = int(input())
results = []
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    max_rounds = 0
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += a[end]
        while current_sum > r and start <= end:
            current_sum -= a[start]
            start += 1
        if l <= current_sum <= r:
            max_rounds += 1
            current_sum = 0
            start = end + 1

    results.append(max_rounds)

print("\n".join(map(str, results)))

