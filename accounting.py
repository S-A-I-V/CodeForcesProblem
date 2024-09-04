def find_X(A, B, n):
    if A == 0:
        if B == 0:
            return 1 
        else:
            return "No solution"
    elif A != 0:
        if B==0:
            return 0
        X = round(abs(B / A) ** (1 / n))
        
        if A * (X ** n) == B:
            return X
        if A * ((-X) ** n) == B:
            return -X
    elif B == 0:
        if n == 1:
            return 0
        else:
            return "No solution"
    

    return "No solution"
A, B, n = map(int, input().split())
print(find_X(A, B, n))
