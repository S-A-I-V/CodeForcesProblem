def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k == 0:
            results.append(0)
        else:
            # Calculate number of diagonals needed
            if k <= n:
                results.append(1)
            else:
                results.append(min(k, 2*n - 1))
    
    for result in results:
        print(result)

solve()