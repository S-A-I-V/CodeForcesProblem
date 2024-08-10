'''
new yr transport problem

'''
n, t = map(int, input().split())  
a = list(map(int, input().split()))  
currcell = 1  
while currcell < t: 
    currcell += a[currcell - 1]  
if currcell == t: 
    print("YES")
else:
    print("NO")
