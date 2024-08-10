'''
l to r inclusive

x and y randomly selected, changed to 3x and y//3
to make all numbers zero, we need to get most numbers in pair of x and y

'''
def calculate_operations(l, r):
    n = r - l + 1
    operations = 0
    while n > 0:
        operations += 1
        n -= (n + 1) // 2 

    return operations

def minimum_operations(t, cases):
    results = []
    for l, r in cases:
        operations = calculate_operations(l, r)
        results.append(operations)
    return results

t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]
results = minimum_operations(t, cases)

for result in results:
    print(result)

