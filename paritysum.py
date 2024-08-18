def min_operations_to_same_parity(n, a):
    odd_count = sum(1 for x in a if x % 2 == 1)
    even_count = n - odd_count
    return min(odd_count, even_count)

# Reading input and processing test cases
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(min_operations_to_same_parity(n, a))

# Output all results
print("\n".join(map(str, results)))
