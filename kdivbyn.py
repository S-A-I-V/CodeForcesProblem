'''

'''
def find_kth_not_divisible(n, k):
    return k + (k - 1) // (n - 1)

t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    results.append(find_kth_not_divisible(n, k))

for result in results:
    print(result)
