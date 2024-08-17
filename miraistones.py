''''
n stones
cost of i th stone is vi
cost array=v 
l, r -s sum of subarray


'''
n = int(input())
v = list(map(int, input().split()))
prefix_sum_original = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum_original[i] = prefix_sum_original[i - 1] + v[i - 1]

sorted_v = sorted(v)
prefix_sum_sorted = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum_sorted[i] = prefix_sum_sorted[i - 1] + sorted_v[i - 1]

m = int(input())
resultl=[]
for _ in range(m):
    query_type, l, r = map(int, input().split())
    if query_type == 1:
        result = prefix_sum_original[r] - prefix_sum_original[l - 1]
    elif query_type == 2:
        result = prefix_sum_sorted[r] - prefix_sum_sorted[l - 1]
    resultl.append(result)

for _ in resultl:
    print(_)