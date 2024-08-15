'''
n steps- 1, 2 steps
total steps%m==0


'''
n, m = map(int, input().split())

min_moves = (n + 1) // 2  
if min_moves % m == 0:
    print(min_moves)
else:
    min_moves = ((min_moves + m - 1) // m) * m
    if min_moves <= n:
        print(min_moves)
    else:
        print(-1)

