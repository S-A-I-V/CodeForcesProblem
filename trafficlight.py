t = int(input()) 
r = []
for _ in range(t):
    n, c = input().split()  
    n = int(n)
    s = input()  
    if c == 'g':
        r.append(0)
        continue
    max_wait = 0
    g_positions = [i for i in range(n) if s[i] == 'g']
    for i in range(n):
        if s[i] == c:
            min_time = min((g - i + n) % n for g in g_positions)
            max_wait = max(max_wait, min_time)
    r.append(max_wait)
for i in r:
    print(i)
