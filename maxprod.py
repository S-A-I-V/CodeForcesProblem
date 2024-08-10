'''
add small multiply big
'''
a=int(input())
b=int(input())
c=int(input())
maxprod1=(a+b)*c
maxprod2=a*b*c
maxprod3=a+b+c
maxprod4=a*(b+c)
print(max(maxprod1, maxprod2, maxprod3, maxprod4))