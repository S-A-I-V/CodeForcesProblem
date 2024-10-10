t = int(input())
for _ in range(t):
    n = int(input())
    narray = list(map(int, input().split()))

    max_value = 0
    count = 0
    
    for i in range(n):
        if (i == 0 or narray[i] >= narray[i-1]) and (i == n-1 or narray[i] >= narray[i+1]):
            count += 1
        max_value = max(max_value, narray[i])
    
    score = max_value + count
    print(score)