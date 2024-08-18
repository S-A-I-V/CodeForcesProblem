def find_smallest_and_largest(m, s):
    # If it's impossible to form the number
    if s == 0 and m == 1:
        return "0 0"
    if s == 0 or s > 9 * m:
        return "-1 -1"
    
    # Construct the smallest number
    smallest = [0] * m
    sum_digits = s
    
    for i in range(m - 1, -1, -1):
        if sum_digits > 9:
            smallest[i] = 9
            sum_digits -= 9
        else:
            smallest[i] = sum_digits
            sum_digits = 0
    
    # Ensure the first digit is non-zero
    if smallest[0] == 0:
        for i in range(1, m):
            if smallest[i] > 0:
                smallest[i] -= 1
                smallest[0] = 1
                break
    
    # Construct the largest number
    largest = [0] * m
    sum_digits = s
    
    for i in range(m):
        if sum_digits > 9:
            largest[i] = 9
            sum_digits -= 9
        else:
            largest[i] = sum_digits
            sum_digits = 0
    
    # Convert lists to strings
    smallest_str = ''.join(map(str, smallest))
    largest_str = ''.join(map(str, largest))
    
    return f"{smallest_str} {largest_str}"

m, s = map(int, input().split())
print(find_smallest_and_largest(m, s))
