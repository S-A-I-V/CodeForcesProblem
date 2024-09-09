def solve():
    t = int(input())
    r=[]
    for _ in range(t):
        n = int(input())
        valid = True
        prev_p, prev_c = 0, 0
        
        for _ in range(n):
            p, c = map(int, input().split())
            if p < prev_p or c < prev_c or c > p or (p - prev_p) < (c - prev_c):
                valid = False
            prev_p, prev_c = p, c
        
        r.append("YES" if valid else "NO")
    for i in r:
        print(i)
solve()
