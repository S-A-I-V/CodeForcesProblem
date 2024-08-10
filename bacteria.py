'''
min number of bacteria



'''
req=1
n=int(input())
req = 0
while n > 0:
    if n % 2 == 1:  
        req += 1
    n //= 2  
print(req)


