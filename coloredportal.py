from bisect import bisect_left
t = int(input())
results = []

for _ in range(t):
    n, q = map(int, input().split())
    portals = input().split()
    
    color_map = {'B': [], 'G': [], 'R': [], 'Y': []}
    for i in range(n):
        c1, c2 = portals[i][0], portals[i][1]
        color_map[c1].append(i + 1)
        color_map[c2].append(i + 1)
    
    for color in color_map:
        color_map[color].sort()
    
    for _ in range(q):
        x, y = map(int, input().split())
        
        if x == y:
            results.append(0)
            continue
        
        min_cost = abs(x - y)
        found = False
        
        for color in portals[x - 1]:
            if color in color_map:
                positions = color_map[color]
                pos = bisect_left(positions, y)
                if pos < len(positions):
                    min_cost = min(min_cost, abs(x - positions[pos]) + abs(positions[pos] - y))
                    found = True
                if pos > 0:
                    min_cost = min(min_cost, abs(x - positions[pos - 1]) + abs(positions[pos - 1] - y))
                    found = True
        
        if found:
            results.append(min_cost)
        else:
            results.append(-1)

print('\n'.join(map(str, results)))


