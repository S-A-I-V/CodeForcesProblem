def payment_without_change(q, test_cases):
    results = []
    for a, b, n, S in test_cases:
        max_n_coins = min(a, S // n)
        remaining = S - max_n_coins * n
        if remaining <= b:
            results.append("YES")
        else:
            results.append("NO")
    return results

q = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(q)]
x=payment_without_change(q, test_cases)

for i in x:
    print(i)