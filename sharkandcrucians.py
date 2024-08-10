'''
n- total amt of val teeth
m- no of rows
k- amt of cruc in dinner

r- index of the row
c- residual viability


'''
def max_crucians(n, m, k, teeth):
    rows = {}
    
    for i in range(n):
        row_index, viability = teeth[i]
        if row_index not in rows:
            rows[row_index] = []
        rows[row_index].append(viability)

    max_crucians_per_row = [min(rows[row]) for row in rows]
    total_crucians = sum(max_crucians_per_row)
    
    return min(total_crucians, k)

n, m, k = map(int, input().split())
teeth = [tuple(map(int, input().split())) for _ in range(n)]

result = max_crucians(n, m, k, teeth)
print(result)
