def maxmulsum(testcase):
    max_sum = 0
    optimal_x = 2  
    
    for x in range(2, testcase + 1):
        k = testcase // x
        multiple_sum = (k * (k + 1) // 2) * x
        
        if multiple_sum > max_sum:
            max_sum = multiple_sum
            optimal_x = x
    
    return (optimal_x)

t = int(input())
results=[]
for _ in range(t):
    testcase = int(input())
    results.append(maxmulsum(testcase))
for i in results:
    print(i)
