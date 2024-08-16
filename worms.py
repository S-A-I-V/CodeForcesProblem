'''
n
ai
m
mi

'''
def find_worm_piles(piles, queries):
    prefix_sums = []
    current_sum = 0
    for pile in piles:
        current_sum += pile
        prefix_sums.append(current_sum)
    
    results = []
    for q in queries:
        left, right = 0, len(prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if prefix_sums[mid] >= q:
                right = mid
            else:
                left = mid + 1
        
        results.append(left + 1) 
    
    return results

n = int(input())  
piles = list(map(int, input().split()))  
m = int(input())  
queries = list(map(int, input().split()))  

results = find_worm_piles(piles, queries)
for result in results:
    print(result)
