def basil_garden_dp(test_cases):
    results = []
    for n, heights in test_cases:
        rounds = 0
        max_height = 0
        for i in range(n):
            max_height = max(max_height, heights[i] + i)
        results.append(max_height)
    return results

t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    heights = list(map(int, input().strip().split()))
    test_cases.append((n, heights))

results = basil_garden_dp(test_cases)

for result in results:
    print(result)
