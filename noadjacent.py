def generate_matrix(n):
    if n == 2:
        return -1  
    matrix = [[0] * n for _ in range(n)]
    numbers = []
    
    for i in range(1, n * n + 1):
        if i % 2 != 0:
            numbers.append(i)
    
    for i in range(1, n * n + 1):
        if i % 2 == 0:
            numbers.append(i)
    index = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = numbers[index]
            index += 1
    
    return matrix

def print_matrix(matrix):
    if matrix == -1:
        print(-1)
    else:
        for row in matrix:
            print(" ".join(map(str, row)))

t = int(input()) 
for _ in range(t):
    n = int(input())
    result = generate_matrix(n)
    print_matrix(result)
