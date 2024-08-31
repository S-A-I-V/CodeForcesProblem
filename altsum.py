t = int(input())
result = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    alt_sum = 0
    for i in range(n):
        if i % 2 == 0:
            alt_sum += arr[i] 
        else:
            alt_sum -= arr[i]  
    
    result.append(alt_sum)
for _ in result:
    print(_)
