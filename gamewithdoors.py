t=int(input())
for i in range(t):
    la,ra=map(int, input().split())
    lb,rb=map(int, input().split())
    if ra < lb:
        print(1)
    elif rb < la:
        print(1)
    elif ra==rb and la==lb:
        print(ra-la)
    else:
        print(min(ra, rb)-max(la, lb)+1)