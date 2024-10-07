t=int(input())
r=[]
for i in range(t):
    n=int(input())
    if n==1:
        r.append(-1)
    else:
        r.append("5" + "7" * (n - 1))

for i in r:
    print(i)