def count_good_pairs(n, a, b):
    diffs = [a[i] - b[i] for i in range(n)]
    diffs.sort()
    
    count = 0
    j = n - 1
    
    for i in range(n):
        while j > i and diffs[i] + diffs[j] > 0:
            j -= 1
        count += (n - j - 1)
    
    return count

# Input reading
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and print the result
print(count_good_pairs(n, a, b))
