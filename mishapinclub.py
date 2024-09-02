def minimum_people(s):
    pos = 0
    MAX = 0
    MIN = 0
    
    for event in s:
        if event == '+':
            pos += 1
            MAX = max(pos, MAX)
        else:  # event == '-'
            pos -= 1
            MIN = min(pos, MIN)
    
    return MAX - MIN

s = input().strip()
print(minimum_people(s))
