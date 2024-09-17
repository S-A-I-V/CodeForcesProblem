import math
from functools import reduce
from math import gcd

def solve():
    def compute_gcd_list(arr):
        return reduce(gcd, arr)
    
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        gcdA = compute_gcd_list(a)
        gcdB = compute_gcd_list(b)
        
        max_gcd_sum = gcdA + gcdB
        ways = 0
        
        # Iterate through each possible swap
        for i in range(n):
            # Swap a[i] with b[i] and compute new GCDs
            a_with_swap = a[:]
            b_with_swap = b[:]
            a_with_swap[i], b_with_swap[i] = b[i], a[i]
            
            new_gcdA = compute_gcd_list(a_with_swap)
            new_gcdB = compute_gcd_list(b_with_swap)
            
            new_gcd_sum = new_gcdA + new_gcdB
            
            if new_gcd_sum > max_gcd_sum:
                max_gcd_sum = new_gcd_sum
                ways = 1
            elif new_gcd_sum == max_gcd_sum:
                ways += 1
        
        results.append(f"{max_gcd_sum} {ways}")
    
    print("\n".join(results))

solve()
