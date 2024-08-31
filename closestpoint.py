t = int(input())
for _ in range(t):
    n = int(input())
    points = list(map(int, input().split()))

    gaps = []
    for i in range(n - 1):
        gaps.append(points[i + 1] - points[i])
    
    max_gap = max(gaps)
    max_gap_count = gaps.count(max_gap)
    
    if max_gap_count == 1 and max_gap > 1:
        print("YES")
    else:
        print("NO")
