def max_expression_value(n, a):
    a.sort()
    max_val = a[-1]
    min_val = a[0]
    second_max_val = a[-2]
    second_min_val = a[1]
    
    # Calculate the maximum possible expression value
    result = max(abs(max_val - second_min_val) + abs(second_min_val - min_val) + abs(min_val - second_max_val) + abs(second_max_val - max_val),
                  abs(max_val - min_val) + abs(min_val - second_max_val) + abs(second_max_val - second_min_val) + abs(second_min_val - max_val))
    
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_expression_value(n, a))