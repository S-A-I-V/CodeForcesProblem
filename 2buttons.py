def min_operations(n, m):
    ops = 0
    
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        ops += 1
    
    return ops + (n - m)
n, m = map(int, input().split())
print(min_operations(n, m))
