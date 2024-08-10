'''
s-mins to shower in m-min day

n tasks - i task ((li, ri))

n, s, m
l0, r0
l1, r1
.
.
.
'''
t = int(input())
results = []
for _ in range(t):
    n, s, m = map(int, input().split())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]
    tasks.append((m, m))
    can_shower = False
    last_end = 0
    for start, end in tasks:
        if start - last_end >= s:
            can_shower = True
            break
        last_end = end
    results.append("YES" if can_shower else "NO")
for result in results:
    print(result)
