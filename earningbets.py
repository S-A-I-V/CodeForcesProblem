'''
n possible outcomes
for every n, bet certain amt of coins, if i th event win, we get = total bet coins*ki

only 1 out of n is winning, 
t=testcases, 
n- 1-50, number of outcomes
ki in n:
'''
t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    x = [0] * n  
    total_bets = 0
    
    possible = True
    for i in range(n):
        x[i] = 1  
        total_bets += x[i]
    
    for i in range(n):
        while total_bets >= k[i] * x[i]:
            x[i] += 1
            total_bets = sum(x)
        
        if total_bets >= k[i] * x[i]:
            possible = False
            break
    
    if possible:
        print(' '.join(map(str, x)))
    else:
        print(-1)