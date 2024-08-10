def get_off_order(n, m):
    left_window = []
    right_window = []
    left_non_window = []
    right_non_window = []

    for i in range(1, n + 1):
        if len(left_window) + len(right_window) < m:
            left_window.append(len(left_window) + len(right_window) + 1)
        if len(left_window) + len(right_window) < m:
            right_window.append(len(left_window) + len(right_window) + 1)

    for i in range(1, n + 1):
        if len(left_window) + len(right_window) + len(left_non_window) + len(right_non_window) < m:
            left_non_window.append(len(left_window) + len(right_window) + len(left_non_window) + len(right_non_window) + 1)
        if len(left_window) + len(right_window) + len(left_non_window) + len(right_non_window) < m:
            right_non_window.append(len(left_window) + len(right_window) + len(left_non_window) + len(right_non_window) + 1)

    off_order = []
    for i in range(n):
        if i < len(left_non_window):
            off_order.append(left_non_window[i])
        if i < len(left_window):
            off_order.append(left_window[i])
        if i < len(right_non_window):
            off_order.append(right_non_window[i])
        if i < len(right_window):
            off_order.append(right_window[i])

    return off_order

n, m = map(int, input().split())
order = get_off_order(n, m)
print(*order)
