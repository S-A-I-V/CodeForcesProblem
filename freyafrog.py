def minimum_moves(x, y, k):
    moves_x = (x + k - 1) // k
    moves_y = (y + k - 1) // k
    
    if x == 0 and y == 0:
        return 0
    elif moves_x == moves_y:
        return 2 * moves_x
    else:
        return 2 * max(moves_x, moves_y) - 1

t = int(input())
r = []

for _ in range(t):
    x, y, k = map(int, input().split())
    r.append(minimum_moves(x, y, k))

for res in r:
    print(res)