def solve():
    n, m = map(int, input().split())
    s = list(input())
    indices = set(int(x) - 1 for x in input().split())
    c = sorted(input())
    
    i = 0
    for x in sorted(indices):
        s[x] = c[i]
        i += 1
    
    print(''.join(s))

tcs = int(input())
for _ in range(tcs):
    solve()
