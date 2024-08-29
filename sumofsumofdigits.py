def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def preprocess(max_n):
    dp = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        dp[i] = dp[i - 1] + sum_of_digits(i)
    return dp

max_n = 200000

dp = preprocess(max_n)

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    results.append(dp[n])

for result in results:
    print(result)
