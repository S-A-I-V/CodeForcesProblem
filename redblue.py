def max_partial_sum(sequence):
    max_sum = 0
    current_sum = 0
    for num in sequence:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
rres=[]

def solve():
    t = int(input())  
    for _ in range(t):
        n = int(input())  
        r = list(map(int, input().split()))  
        m = int(input())  
        b = list(map(int, input().split()))  
        max_r_sum = max_partial_sum(r)
        max_b_sum = max_partial_sum(b)
        
        rres.append(max_r_sum + max_b_sum)
    for i in rres:
        print(i)
solve()
