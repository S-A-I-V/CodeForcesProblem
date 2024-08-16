'''
array of n intergers
such that aj-ai=j-i


'''
from collections import defaultdict

def count_pairs(n, a):
    count = defaultdict(int)
    pairs = 0
    
    for i in range(n):
        key = a[i] - i
        pairs += count[key]
        count[key] += 1
    return pairs
t = int(input()) 

results = []
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split())) 
    result = count_pairs(n, a)
    results.append(result)

for result in results:
    print(result)
