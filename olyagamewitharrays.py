def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        
        min_vals = []
        second_min_vals = []
        global_min = float('inf')
        
        for _ in range(n):
            mi = int(input())
            array = list(map(int, input().split()))
            
            sorted_array = sorted(array)
            min_val = sorted_array[0]
            second_min_val = sorted_array[1]
            
            min_vals.append(min_val)
            second_min_vals.append(second_min_val)
            global_min = min(global_min, min_val)
        
        total_beauty = sum(min_vals)
        max_beauty = float('-inf')
        
        for i in range(n):
            if min_vals[i] == global_min:
                alternative = total_beauty - min_vals[i] + second_min_vals[i]
            else:
                alternative = total_beauty - min_vals[i] + global_min
            max_beauty = max(max_beauty, alternative)
        
        results.append(str(max_beauty))
    
    print("\n".join(results))

solve()