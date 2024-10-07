def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        s = input().strip()
        n = len(s)
        
        if s[0] == ')' or s[-1] == '(':
            results.append("NO")
            continue
        
        open_count = 0
        for i in range(n):
            if s[i] == '(' or s[i] == '?':
                open_count += 1
            else:
                open_count -= 1
            
            if open_count < 0:
                results.append("NO")
                break
        else:
            if open_count % 2 == 0:
                results.append("YES")
            else:
                results.append("NO")
    
    print("\n".join(results))

solve()
