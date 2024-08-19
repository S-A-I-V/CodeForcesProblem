def max_alternating_subsequence_sum(n, a):
    total_sum = 0
    current_max = a[0]
    
    for i in range(1, n):
        if (a[i] > 0 and current_max > 0) or (a[i] < 0 and current_max < 0):
            current_max = max(current_max, a[i])
        else:
            total_sum += current_max
            current_max = a[i]
    total_sum += current_max
    
    return total_sum

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        results.append(max_alternating_subsequence_sum(n, a))
    
    print("\n".join(map(str, results)))
solve()
