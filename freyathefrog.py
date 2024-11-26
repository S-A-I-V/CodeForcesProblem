import math

t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())

    xd = 2 * math.ceil(x / k) - 1
    yd = 2 * math.ceil(y / k)

    print(max(xd, yd))
