def min_operations(l, r):
    operations = 0
    for i in range(l, r + 1):
        count = 0
        num = i
        while num > 0:
            if num % 3 == 0:
                num //= 3
            else:
                num -= num % 3
            count += 1
        operations += count
    return operations

t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    results.append(min_operations(l, r))

for result in results:
    print(result)
