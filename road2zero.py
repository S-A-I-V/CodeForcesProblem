t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x > y:
        x, y = y, x

    if b >= 2 * a:
        cost = (x + y) * a
    else:
        cost = x * b + (y - x) * a

    print(cost)
