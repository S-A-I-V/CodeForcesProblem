def minimize_sum(t, test_cases):
    results = []
    for case in test_cases:
        n, k = case[0]
        a = case[1]
        
        min_value = min(a)
        total_sum = sum(a)
        
        if k >= n:
            total_sum = n * min_value
        elif k > 0:
            # Start replacing from the first element
            for i in range(1, n):
                if k == 0:
                    break
                if a[i] > a[i-1]:
                    # Perform an operation by replacing a[i] with the minimum of a[i-1] and a[i]
                    total_sum -= (a[i] - a[i-1])
                    k -= 1
                    a[i] = a[i-1]
                if a[i] > min_value:
                    total_sum -= (a[i] - min_value)
                    a[i] = min_value
                    k -= 1
        
        results.append(total_sum)
    
    return results

# Input Parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append(((n, k), a))

# Process each test case
results = minimize_sum(t, test_cases)

# Output results
for result in results:
    print(result)