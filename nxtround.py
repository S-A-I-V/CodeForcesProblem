def next_round_participants(n, k, scores):
    kth_score = scores[k-1]
    count = 0
    for score in scores:
        if score >= kth_score and score > 0:
            count += 1
    return count
n, k = map(int, input().split())
scores = list(map(int, input().split()))
result = next_round_participants(n, k, scores)
print(result)
