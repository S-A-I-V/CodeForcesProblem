def max_aesthetic_appeal(n, appeals):
    appeal_dict = {}
    
    for i, appeal in enumerate(appeals):
        if appeal in appeal_dict:
            appeal_dict[appeal].append(i)
        else:
            appeal_dict[appeal] = [i]
    
    max_appeal_sum = float('-inf')
    best_pair = (0, 1)

    for indices in appeal_dict.values():
        if len(indices) < 2:
            continue

        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                l, r = min(indices[i], indices[j]), max(indices[i], indices[j])
                current_sum = sum(appeals[l:r + 1])
                
                if current_sum > max_appeal_sum:
                    max_appeal_sum = current_sum
                    best_pair = (l, r)
    
    # Consider cutting down trees from both ends
    left_sum = sum(appeals[:best_pair[0]])
    right_sum = sum(appeals[best_pair[1]+1:])
    if left_sum > max_appeal_sum:
        max_appeal_sum = left_sum
        total_cut = [i + 1 for i in range(n) if i >= best_pair[0]]
    elif right_sum > max_appeal_sum:
        max_appeal_sum = right_sum
        total_cut = [i + 1 for i in range(n) if i <= best_pair[1]]
    else:
        l, r = best_pair
        total_cut = [i + 1 for i in range(n) if i < l or i > r]
    
    return max_appeal_sum, len(total_cut), total_cut

n = int(input())
appeals = list(map(int, input().split()))
max_sum, cuts_count, cuts = max_aesthetic_appeal(n, appeals)
print(max_sum, cuts_count)
print(' '.join(map(str, cuts)))