def fix_inventory(n, inventory):
    from collections import Counter
    count = Counter(inventory)
    missing_numbers = []
    for num in range(1, n + 1):
        if count[num] == 0:
            missing_numbers.append(num)

    result = inventory.copy()
    missing_index = 0
    expected_set = set(range(1, n + 1))

    used = set()

    for i in range(n):
        if inventory[i] in used or inventory[i] not in expected_set:
            result[i] = missing_numbers[missing_index]
            missing_index += 1
        else:
            used.add(inventory[i])
    return result
n = int(input())

inventory = list(map(int, input().split()))

result = fix_inventory(n, inventory)

print(' '.join(map(str, result)))
