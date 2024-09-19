def solve():
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
        
        for _ in range(q):
            x, y = map(int, input().split())
            
            if x == y:
                results.append(0)
                continue
            
            direct_connection = False
            min_cost = abs(x - y)
            
            for color in portals[x - 1]:
                if color in portals[y - 1]:
                    direct_connection = True
                    break
            
            if direct_connection:
                results.append(min_cost)
            else:
                indirect_cost = float('inf')
                
                for color in portals[x - 1]:
                    for city in color_map[color]:
                        if city != x and any(color in portals[city - 1] for color in portals[y - 1]):
                            indirect_cost = min(indirect_cost, abs(x - city) + abs(city - y))
                
                if indirect_cost < float('inf'):
                    results.append(indirect_cost)
                else:
                    results.append(-1)
    
    print('\n'.join(map(str, results)))

solve()
