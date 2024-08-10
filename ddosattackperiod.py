# def longest_ddos_period(n, requests):
#     max_ddos_time = 0  
#     for t in range(n):
#         current_sum = 0  
#         for i in range(t, n):
#             current_sum += requests[i]  
#             sec = i - t + 1    
#             if current_sum > 100 * sec:
#                 max_ddos_time = max(max_ddos_time, sec)  

#     print(max_ddos_time)  

# n = int(input().strip())  
# requests = list(map(int, input().strip().split())) 
# longest_ddos_period(n, requests)


# def longest_ddos_period(n, requests):
#     max_ddos_time = 0
#     current_sum = 0
#     start = 0
#     for end in range(n):
#         current_sum += requests[end]
#         while current_sum > 100 * (end - start + 1):
#             max_ddos_time = max(max_ddos_time, end - start + 1)    
#             current_sum -= requests[start]
#             start += 1
#     print(max_ddos_time)

# n = int(input().strip())  
# requests = list(map(int, input().strip().split())) 
# longest_ddos_period(n, requests)

def longest_ddos_period(n, requests):
    max_ddos_time = 0

    # Compute prefix sums
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + requests[i - 1]

    # Check all possible subarrays using prefix sums
    for start in range(n):
        for end in range(start + 1, n + 1):
            current_sum = prefix_sums[end] - prefix_sums[start]
            period_length = end - start
            if current_sum > 100 * period_length:
                max_ddos_time = max(max_ddos_time, period_length)

    print(max_ddos_time)

n = int(input().strip())
requests = list(map(int, input().strip().split()))
longest_ddos_period(n, requests)
