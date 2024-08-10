t = int(input())
result=[]
for _ in range(t):
    x, y = map(int, input().split())
    result.append((min(x, y), max(x, y)))
for i in result:
    print(i[0], i[1])
