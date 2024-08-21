def same_parity_summands(t, cases):
    results = []
    for n, k in cases:
        # Check for odd parity solution
        if n >= k and (n % 2 == k % 2):
            results.append("YES")
            results.append("1 " * (k - 1) + str(n - (k - 1)))
        # Check for even parity solution
        elif n >= 2 * k:
            results.append("YES")
            results.append("2 " * (k - 1) + str(n - 2 * (k - 1)))
        else:
            results.append("NO")
    
    return results
t = int(input())
cases = []
for _ in range(t):
    n, k = map(int, input().split())
    cases.append((n, k))
results = same_parity_summands(t, cases)
for result in results:
    print(result)
