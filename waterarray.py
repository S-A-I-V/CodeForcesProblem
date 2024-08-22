def maximize_score(n, k, d, a, v):
    max_score = 0
    current_score = 0
    current_array = a[:]
    
    for day in range(1, d + 1):
        # Determine the value of bi
        bi = v[(day - 1) % k]
        
        # Apply the add operation
        for j in range(bi):
            current_array[j] += 1
        
        # Check the number of elements that are equal to their positions
        c = sum(1 for idx, val in enumerate(current_array, start=1) if idx == val)
        
        # Update the maximum score
        max_score = max(max_score, current_score + c)
        
        # If performing a count and reset operation is beneficial, do it
        if c > 0:
            current_score += c
            current_array = [0] * n
    
    return max_score

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n, k, d = map(int, input().split())
        a = list(map(int, input().split()))
        v = list(map(int, input().split()))
        results.append(maximize_score(n, k, d, a, v))
    
    # Output all results
    print("\n".join(map(str, results)))

# Run the solve function to execute the program
solve()
