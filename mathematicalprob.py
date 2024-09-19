def solve():
    n = int(input())
    s = input()
    
    if n < 3:
        print(int(s))
        return
    
    if s[0] == '0' or s[n - 1] == '0':
        print(0)
        return
    
    mn = float('inf')
    
    if n == 3:
        x = int(s[0])
        y = int(s[2])
        a = int(s[:2])
        b = int(s[1:])
        mn = min(mn, x + b)
        mn = min(mn, x * b)
        mn = min(mn, y + a)
        mn = min(mn, y * a)
        print(mn)
        return
    
    for i in range(n - 1):
        if s[i] == '0':
            print(0)
            return
        
        sum_value = 0
        ct = 0
        for j in range(i):
            sum_value += int(s[j])
            if s[j] == '1':
                ct += 1
        
        num = int(s[i:i+2])
        sum_value += num
        
        for k in range(i + 2, n):
            sum_value += int(s[k])
            if s[k] == '1':
                ct += 1
        
        mn = min(mn, sum_value - ct)
    
    print(mn)

tcs = int(input())
for _ in range(tcs):
    solve()
