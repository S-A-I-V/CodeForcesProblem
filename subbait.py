def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        min_value = min(a)
        count_min = a.count(min_value)
        
        # If all elements are the minimum, Alice loses; otherwise, she wins.
        if count_min == n:
            results.append("NO")
        else:
            results.append("YES")
    
    for result in results:
        print(result)

solve()
