def ram_upload(n, k):
    if n == 0:
        return 0
    return (n - 1) * k + 1
result=[]
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result.append(ram_upload(n,k))
for i in result:
    print(i)