'''
array - ai
array b - bi 

only exactly 2 conditions need to be satisfied
1 2 3 2 2 3
i=0, j=1
i,j= (1, 3), (1, 4), (2,5)



'''
t = int(input()) 
results = []  

for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    
    indices = {}
    for i in range(n):
        if a[i] in indices:
            indices[a[i]].append(i)
        else:
            indices[a[i]] = [i]
    
    b = [-1] * n
    valid = False  # Flag to check if a valid b array is created
    
    for key, idxs in indices.items():
        if len(idxs) >= 2:
            # Assign 1 and 2 to the first two occurrences
            b[idxs[0]], b[idxs[1]] = 1, 2
            valid = True
            # Assign 1 to the rest of the occurrences
            for i in range(2, len(idxs)):
                b[idxs[i]] = 1
    
    # Check if array b is fully populated and valid
    if valid and -1 not in b:
        results.append(" ".join(map(str, b)))
    else:
        results.append("-1")

for result in results:
    print(result)