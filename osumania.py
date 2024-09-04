t = int(input())
result=[]
for _ in range(t):
    n = int(input())
    columns = []
    
    for i in range(n):
        row = input().strip()
        for j in range(4):
            if row[j] == '#':
                columns.append(j + 1)
                break
    
    result.append(" ".join(map(str, columns[::-1])))
for i in result:
    print(i)