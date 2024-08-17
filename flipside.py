def flipping_game(arr):
    n = len(arr)
    initial_ones = sum(arr)
    
    if initial_ones == n:
        return n - 1
    
    max_diff = float('-inf')
    current_sum = 0
    
    for i in range(n):
        val = 1 if arr[i] == 0 else -1
        current_sum += val
        
        if current_sum > max_diff:
            max_diff = current_sum
            
        if current_sum < 0:
            current_sum = 0
    
    return initial_ones + max_diff
n=int(input())
arr=list(map(int, input().split()))
print(flipping_game(arr))