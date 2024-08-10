'''
easy vector sum
'''
xsum=0
ysum=0
zsum=0
n=int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    xsum += x
    ysum += y
    zsum += z
if xsum==ysum==zsum==0:
    print('YES')
else:
    print('NO')
i+=1