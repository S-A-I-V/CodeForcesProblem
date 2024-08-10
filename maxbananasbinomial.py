def max_bananas(t, test_cases):
    results = []
    for a, b, c in test_cases:
        max_product = a * b * c
        for da in range(6):
            for db in range(6 - da):
                dc = 5 - da - db
                a1 = a + da
                b1 = b + db
                c1 = c + dc
                max_product = max(max_product, a1 * b1 * c1)
        results.append(max_product)
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = max_bananas(t, test_cases)
for result in results:
    print(result)
