r=[]
t = int(input())  
for _ in range(t):
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))  
    ds = {}
    max_time = -1
    
    for i in range(n):
        d = (k - (a[i] % k)) % k
        if d == 0:
            continue
        if d in ds:
            ds[d] += k  
        else:
            ds[d] = d
        max_time = max(max_time, ds[d])
    r.append(max_time)

for _ in r:
    print(_)