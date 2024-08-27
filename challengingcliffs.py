def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))
        h.sort()

        min_diff = float('inf')
        min_index = 0
        for i in range(1, n):
            if h[i] - h[i-1] < min_diff:
                min_diff = h[i] - h[i-1]
                min_index = i
        left_part = h[:min_index-1]
        right_part = h[min_index+1:]
        result = [h[min_index-1]] + right_part + left_part + [h[min_index]]

        print(" ".join(map(str, result)))
solve()
