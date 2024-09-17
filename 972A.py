def solve():
    t = int(input())
    vowels = "uoiea"  
    results = []

    for _ in range(t):
        n = int(input())
        result = ""
        
        for i in range(n):
            result += vowels[i % len(vowels)]  
        
        results.append(result)
    
    print("\n".join(results))

solve()
