def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        if len(set(a)) == 1:
            results.append("0")
            continue
        
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        target = max(freq, key=freq.get)
        min_cost = float('inf')
        
        left, right = 0, n - 1
        
        while left < n and a[left] == target:
            left += 1
        while right >= 0 and a[right] == target:
            right -= 1
        
        min_cost = right - left + 1 
        
        results.append(str(min_cost))
    
    print("\n".join(results))

solve()
