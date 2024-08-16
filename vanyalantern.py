'''
n lanterns, length of street

array len=n
array=[ai]


'''
n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
max_gap = 0
for i in range(1, len(a)):
    gap = a[i] - a[i - 1]
    max_gap = max(max_gap, gap)
d_from_start = a[0]
d_from_end = l - a[-1]
d_min = max(max_gap / 2, d_from_start, d_from_end)

print(f"{d_min:.10f}")

