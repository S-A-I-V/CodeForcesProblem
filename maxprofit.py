def max_profit(n, m, k, planets):
    max_profit = 0

    for buy_planet in range(n):
        for sell_planet in range(n):
            if buy_planet == sell_planet:
                continue

            total_profit = 0
            items_to_buy = []

            for item_type in range(m):
                aij = planets[buy_planet][item_type][0]
                bij = planets[sell_planet][item_type][1]
                cij = planets[buy_planet][item_type][2]

                if bij > aij:
                    items_to_buy.append((bij - aij, min(cij, k)))

            items_to_buy.sort(reverse=True, key=lambda x: x[0])

            remaining_capacity = k

            for profit_per_item, quantity in items_to_buy:
                if remaining_capacity == 0:
                    break
                max_quantity = min(quantity, remaining_capacity)
                total_profit += profit_per_item * max_quantity
                remaining_capacity -= max_quantity

            max_profit = max(max_profit, total_profit)

    return max_profit

n, m, k = map(int, input().split())
planets = []

for _ in range(n):
    planet_name = input().strip()
    items = [tuple(map(int, input().split())) for _ in range(m)]
    planets.append(items)

print(max_profit(n, m, k, planets))
