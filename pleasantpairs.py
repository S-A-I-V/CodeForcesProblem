def pleasant_pairs(t, test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        a = [(arr[i], i + 1) for i in range(n)]
        a.sort()

        cnt = 0
        for p in range(n):
            for q in range(p + 1, n):
                if a[p][0] * a[q][0] > 2 * n:
                    break
                if a[p][0] * a[q][0] == a[p][1] + a[q][1]:
                    cnt += 1

        results.append(cnt)
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

results = pleasant_pairs(t, test_cases)
for result in results:
    print(result)
