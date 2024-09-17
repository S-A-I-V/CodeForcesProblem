def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n, m, q = map(int, input().split())
        teacher1, teacher2 = map(int, input().split())
        david = int(input())
        
        if teacher1 > teacher2:
            teacher1, teacher2 = teacher2, teacher1

        if teacher1 <= david <= teacher2:
            min_moves = min(david - teacher1, teacher2 - david)
        else:
            min_moves = min(abs(david - teacher1), abs(david - teacher2))
        
        results.append(str(min_moves))
    
    print("\n".join(results))

solve()
