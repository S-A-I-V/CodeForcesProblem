from collections import defaultdict

def count_right_triangles(n, points):
    count_y0 = defaultdict(int)
    count_y1 = defaultdict(int)
    
    for x, y in points:
        if y == 0:
            count_y0[x] += 1
        elif y == 1:
            count_y1[x] += 1
    
    total_triangles = 0
    for x in count_y0:
        if x in count_y1:
            total_triangles += count_y0[x] * count_y1[x]
    
    return total_triangles

t = int(input())

results = []
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    result = count_right_triangles(n, points)
    results.append(result)

for result in results:
    print(result)
