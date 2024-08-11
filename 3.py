def calculate_median(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid - 1] if len(arr) % 2 == 0 else arr[mid]

def calculate_score(a, k, b):
    n = len(a)
    max_score = float('-inf')

    for i in range(n):
        if b[i] == 1:
            # Calculate score without incrementing
            a_i = a[i]
            new_a = a[:i] + a[i+1:]
            median_without_i = calculate_median(new_a)
            max_score = max(max_score, a_i + median_without_i)
            
            # Calculate score with the maximum increment
            new_a_i = a[i] + k
            new_a_with_inc = sorted(new_a + [new_a_i])
            median_with_inc = calculate_median(new_a_with_inc)
            max_score = max(max_score, new_a_i + median_with_inc)
    
    return max_score

def process_test_cases(test_cases):
    results = []
    for case in test_cases:
        n, k, a, b = case
        result = calculate_score(a, k, b)
        results.append(result)
    return results

# Input Reading
t = int(input().strip())
test_cases = []
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    test_cases.append((n, k, a, b))

# Process all test cases and output the results
results = process_test_cases(test_cases)
for result in results:
    print(result)
