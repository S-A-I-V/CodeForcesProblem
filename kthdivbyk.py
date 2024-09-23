def solve():
    n, k = map(int, input().split())

    if n % k == 0:
        print(1)
        return

    need = k - n % k
    val = need // n
    ex = need % n
    print(val + (ex > 0) + 1)

t = int(input())
for _ in range(t):
    solve()
