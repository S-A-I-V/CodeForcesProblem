'''


'''
def min_rest_days(n, a):
    # dp[i][0] -> rest on day i
    # dp[i][1] -> contest on day i
    # dp[i][2] -> gym on day i
    dp = [[float('inf')] * 3 for _ in range(n)] 
 # Initialization based on the first day
    dp[0][0] = 1  # If we rest on the first day
    if a[0] == 1 or a[0] == 3:
        dp[0][1] = 0  # If we do a contest on the first day
    if a[0] == 2 or a[0] == 3:
        dp[0][2] = 0  # If we go to the gym on the first day
    
    # Fill the dp array
    for i in range(1, n):
        # Rest on day i
        dp[i][0] = min(dp[i-1]) + 1
        
        # Contest on day i
        if a[i] == 1 or a[i] == 3:
            dp[i][1] = min(dp[i-1][0], dp[i-1][2])
        
        # Gym on day i
        if a[i] == 2 or a[i] == 3:
            dp[i][2] = min(dp[i-1][0], dp[i-1][1])
    
    return min(dp[n-1])
n = int(input())
a = list(map(int, input().split()))
print(min_rest_days(n, a))
