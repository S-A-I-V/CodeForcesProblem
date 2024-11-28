'''
distinct split

'''
def max_distinct_split(t, test_cases):
    results = []
    for n, s in test_cases:
        left = [0] * 26 
        right = [0] * 26  
        
        for char in s:
            right[ord(char) - ord('a')] += 1
        
        distinct_a = 0
        distinct_b = sum(1 for x in right if x > 0)
        max_sum = distinct_a + distinct_b
        
        for char in s:
            idx = ord(char) - ord('a')
            if right[idx] == 1:
                distinct_b -= 1
            right[idx] -= 1
            
            if left[idx] == 0:
                distinct_a += 1
            left[idx] += 1
            max_sum = max(max_sum, distinct_a + distinct_b)
        
        results.append(max_sum)
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append((n, s))

results = max_distinct_split(t, test_cases)
print("\n".join(map(str, results)))
