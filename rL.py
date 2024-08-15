def max_score(t, test_cases):
    results = []
    for _ in range(t):
        n = test_cases[_][0]
        a = test_cases[_][1]
        s = test_cases[_][2]
        
        max_points = 0
        current_sum = 0
        left_index = -1
        
        for i in range(n):
            if s[i] == 'L':
                left_index = i  # Start a new window when 'L' is found
                current_sum = a[i]  # Initialize sum with the value at 'L'
            elif s[i] == 'R' and left_index != -1:
                # If 'R' is found after an 'L', sum the values in this window
                current_sum += a[i]
                max_points += current_sum
                current_sum = 0  # Reset for the next potential window
                left_index = -1  # Reset left_index to indicate the window is closed

        results.append(max_points)
    
    return results
# Input from the user
t = int(input(""))

test_cases = []
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    s = input("")
    test_cases.append((n, a, s))

# Get the results
output = max_score(t, test_cases)

# Output the results
for result in output:
    print(result)
