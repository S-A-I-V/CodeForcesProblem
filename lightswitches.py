def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = [0] * (k * 2)
    mx = 0
    for i in a:
        mx = max(mx, i)
        cnt[i % (k * 2)] += 1

    for i in range(1, k * 2):
        cnt[i] += cnt[i - 1]

    def sum(p):
        p %= (k * 2)
        if p >= k:
            return cnt[p] - cnt[p - k]
        ans = cnt[p]
        left = k - (p + 1)
        if left:
            ans += cnt[k * 2 - 1] - cnt[k * 2 - 1 - left]
        return ans

    for i in range(mx, mx + k * 2):
        if sum(i) == n:
            print(i)
            return
    print(-1)

t = int(input())
for _ in range(t):
    solve()
