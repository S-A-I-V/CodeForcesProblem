def can_select_odd_sum(n, x, arr):
    odd_count = sum(1 for num in arr if num % 2 != 0)
    even_count = n - odd_count

    # Case 1: If all numbers are even, we can't get an odd sum
    if odd_count == 0:
        return False
    
    # Case 2: If x == n, we must consider the sum of the entire array
    if x == n:
        return sum(arr) % 2 != 0
    
    # Case 3: We want to select x elements, ensuring at least one odd element
    # x must be odd, or if x is even, we must ensure we have a combination that yields an odd sum.
    
    if x % 2 == 1:
        # We need at least 1 odd number, and the rest can be even or odd
        return odd_count >= 1 and (odd_count + even_count >= x)
    else:
        # We need an odd count of odd numbers, and at least one even number to pair
        return odd_count >= 1 and even_count >= 1 and (odd_count + even_count >= x)

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        if can_select_odd_sum(n, x, arr):
            results.append("Yes")
        else:
            results.append("No")
    
    print("\n".join(results))

# Run the solve function to execute the program
solve()
