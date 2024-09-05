def solve():
    t = int(input())  
    r=[]
    for _ in range(t):
        s = input().strip()  
        
        count = {'1': 0, '2': 0, '3': 0}
        left = 0
        min_length = float('inf') 
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            while count['1'] > 0 and count['2'] > 0 and count['3'] > 0:
                min_length = min(min_length, right - left + 1)
                count[s[left]] -= 1
                left += 1
        
        if min_length == float('inf'):
            r.append(0)
        else:
            r.append(min_length)
    for i in r:
        print(i)
solve()
