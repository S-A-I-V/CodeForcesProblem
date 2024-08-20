from collections import Counter
resultl=[]
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        if n == 1:
            resultl.append(0)
            continue
        
        if len(set(a)) == 1:
            resultl.append(0)
            continue
        
        frequency = Counter(a)
        max_freq = max(frequency.values())
        result = n - max_freq  
        resultl.append(result)

solve()
for i in resultl:
    print(i)