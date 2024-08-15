def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        result = []
        for j in range(1, n + 1):
            # Generate the array where a[j] = j * (j + 1)
            result.append(j * (j + 1))
        results.append(result)
    
    for result in results:
        print(" ".join(map(str, result)))

solve()
