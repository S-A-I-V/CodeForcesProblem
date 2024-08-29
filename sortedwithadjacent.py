def sorted_adjacent_differences(n, arr):
    arr.sort()
    result = []
    left, right = 0, n - 1
    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1
    return result[::-1]

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    rearranged = sorted_adjacent_differences(n, arr)
    results.append(rearranged)

for result in results:
    print(" ".join(map(str, result)))
