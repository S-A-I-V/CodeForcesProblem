def solve():
    t = int(input())  
    results = []  
    
    for _ in range(t):
        x = input().strip()  
        y = input().strip()  
        
        s1, s2 = "", ""
        tgt = 0
        
        for i in range(len(x)):
            if tgt == 0:
                if x[i] == y[i]:
                    s1 += x[i]
                    s2 += x[i]
                elif x[i] > y[i]:
                    tgt = 1
                    s1 += x[i]
                    s2 += y[i]
                else:
                    tgt = 1
                    s1 += y[i]
                    s2 += x[i]
            else:
                if x[i] > y[i]:
                    s2 += x[i]
                    s1 += y[i]
                else:
                    s2 += y[i]
                    s1 += x[i]
        
        results.append(s1)
        results.append(s2)
    
    print("\n".join(results))
solve()
