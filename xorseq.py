def count_trailing_zeroes(x):
    if x == 0:
        return 32  # We assume integers are 32-bit, adjust if needed.
    count = 0
    while (x & 1) == 0:
        x >>= 1
        count += 1
    return count

def longest_common_subsegment(x, y):
    z = x ^ y
    return 1 << count_trailing_zeroes(z)

# Reading input
t = int(input())
results = []

for _ in range(t):
    x, y = map(int, input().split())
    results.append(longest_common_subsegment(x, y))

print("\n".join(map(str, results)))
