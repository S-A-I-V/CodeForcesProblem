def solve():
    t = int(input()) 
    r=[] 
    for _ in range(t):
        n = int(input())  
        b = list(map(int, input().split()))  
        
        b.sort(reverse=True)
        
        a = []
        seen = set()
        for value in b:
            if len(a) < n and value not in seen:
                a.append(value)
                seen.add(value)
        
        r.append(" ".join(map(str, a)))
        for i in r:
            print(i)

solve()
