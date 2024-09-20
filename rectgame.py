def max_game_result(n):
    result = 0
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result += n
                n = n // i
                break
    return result + 1

n=int(input())
result=max_game_result(n)
print(result)