'''


'''
# def minimize_equal_sum_subarrays(t, test_cases):
#     results = []
#     for n, p in test_cases:
#         sorted_p = sorted(p)
#         q = []
#         left = 0
#         right = n - 1
#         toggle = True
#         while left <= right:
#             if toggle:
#                 q.append(sorted_p[right])
#                 right -= 1
#             else:
#                 q.append(sorted_p[left])
#                 left += 1
#             toggle = not toggle
#         results.append(q)
#     return results
# t = int(input())
# test_cases = []
# for _ in range(t):
#     n = int(input())
#     p = list(map(int, input().split()))
#     test_cases.append((n, p))

# results = minimize_equal_sum_subarrays(t, test_cases)
# for result in results:
#     print(' '.join(map(str, result)))
def minimize_equal_sum_subarrays(t, test_cases):
    results = []
    for n, p in test_cases:
        sorted_p = sorted(p)
        q = [0] * n  
        
        middle_index = (n - 1) // 2
        q[middle_index] = sorted_p.pop()  

        left = middle_index - 1
        right = middle_index + 1
        
        while sorted_p:
            if left >= 0:
                q[left] = sorted_p.pop()
                left -= 1
            if right < n and sorted_p:
                q[right] = sorted_p.pop()
                right += 1
        
        q = [(x % n) + 1 for x in q]
        results.append(q)
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

results = minimize_equal_sum_subarrays(t, test_cases)
for result in results:
    print(' '.join(map(str, result)))
