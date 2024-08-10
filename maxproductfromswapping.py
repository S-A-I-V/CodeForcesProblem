def maximize_product(x, y):
    x = list(str(x))
    y = list(str(y))
    n = len(x)
    prod=x*y
    
    for i in range(n):
        if x[i] > y[i]:
            x[i], y[i] = y[i], x[i]
            if x*y>prod:
                

    
    x = int(''.join(x))
    y = int(''.join(y))
    
    return x, y

t = int(input())

for _ in range(t):
    x = int(input())
    y = int(input())
    x, y = maximize_product(x, y)
    print(x)
    print(y)