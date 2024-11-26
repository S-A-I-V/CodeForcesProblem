def soldbanana(k, n, w):
    cost = k * (w * (w + 1)) // 2
    borrowed = max(0, cost - n)
    return borrowed

k, n, w = map(int, input().split())

print(soldbanana(k, n, w))
