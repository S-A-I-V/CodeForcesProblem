def find_x(n, k, a):
    a.sort()
    
    # Case when k = 0, we need x less than the smallest element in the array
    if k == 0:
        if a[0] > 1:
            return 1
        else:
            return -1
    
    # Now consider the k-th element in the sorted array
    if k > 0 and k <= n:
        left, right = 1, max(a)
        while left < right:
            mid = (left + right) // 2
            count = sum(1 for num in a if num <= mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left if sum(1 for num in a if num <= left) == k else -1
    
    return -1

# Input Parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Finding and printing the result
result = find_x(n, k, a)
print(result)