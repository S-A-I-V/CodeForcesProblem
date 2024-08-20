t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # This dictionary will store the first occurrence of each unique element
    first_occurrence = {}
    unique_subsequence = []
    
    for num in a:
        if num not in first_occurrence:
            first_occurrence[num] = True
            unique_subsequence.append(num)
    
    # The unique_subsequence will now contain the longest subsequence without duplicates
    # in the order of their first appearance in the array.
    
    # Prepare the result for this test case
    results.append(f"{len(unique_subsequence)}")
    results.append(" ".join(map(str, unique_subsequence)))

# Print all results at once
print("\n".join(results))

