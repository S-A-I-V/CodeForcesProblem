def can_swap_arrays(a, b, n):
    # Initialize DP table
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the current elements are equal, propagate the previous state
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            
            # Check for valid swaps
            for k in range(i):
                if sorted(a[k:i]) == sorted(b[j - (i - k):j]):
                    dp[i][j] = dp[i][j] or dp[k][j - (i - k)]
    
    return dp[n][n]

def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        if can_swap_arrays(a, b, n):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

# Call the solve function to execute the program
solve()
