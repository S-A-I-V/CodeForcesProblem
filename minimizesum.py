def minimize_sum(n, k, arr):
    for _ in range(k):
        # Find the index of the maximum element
        max_index = 0
        for i in range(1, n):
            if arr[i] > arr[max_index]:
                max_index = i

        # Replace max element with the minimum of its neighbors
        if max_index == 0:
            arr[max_index] = arr[max_index + 1]
        elif max_index == n - 1:
            arr[max_index] = arr[max_index - 1]
        else:
            arr[max_index] = min(arr[max_index - 1], arr[max_index + 1])

    return sum(arr)

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        results.append(minimize_sum(n, k, arr))
    
    # Output all results
    print("\n".join(map(str, results)))

# Run the solve function to execute the program
solve()
