t = int(input())
result=[]
for _ in range(t):
    a, b = map(int, input().split())
    result.append(b - a)
for i in result:
    print(i)