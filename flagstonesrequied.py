n,m,a= input().strip().split()
n=int(n)
m=int(m)
a=int(a)
# reqflagstones=0
# lengthwise=0
# widthwise=0
# lcounter=0
# wcounter=0
# while lengthwise<n:
#     lengthwise+=a
#     lcounter+=1
# while widthwise<m:
#     widthwise+=a
#     wcounter+=1

# reqflagstones=lcounter*wcounter
# print(reqflagstones)
lcounter = (n + a - 1) // a
wcounter = (m + a - 1) // a
reqflagstones = lcounter * wcounter
print(reqflagstones)