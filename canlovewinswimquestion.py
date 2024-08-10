def solve():
    import sys
    input = sys.stdin.readline
 
    n, m, k = map(int, input().split())
    s = 'L' + input().strip() + 'L'  # Add 'L' to mimic the bank at start and end
 
    # Initialize the dp array with infinity, except starting position
    dp = [float('inf')] * (n + 2)
    dp[0] = 0  # Starting point on the bank, no swimming needed
 
    # DP logic to calculate the minimum swim required to reach each position
    for i in range(1, n + 2):
        for j in range(1, min(i, m) + 1):
            if s[i - j] != 'C':  # Can't land on crocodiles
                # If we land on water, increase swim count
                swim_increment = 1 if s[i] == 'W' else 0
                dp[i] = min(dp[i], dp[i - j] + swim_increment)
 
    # Check if we can reach the right bank within the allowed swim distance
    if dp[n + 1] <= k:
        print("YES")
    else:
        print("NO")
 
def main():
    import sys
    input = sys.stdin.readline
 
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
