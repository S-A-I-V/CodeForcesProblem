'''
one ride- a rubles
special ride offer, m rides for b rubles, 
n times req to use subway

n, m , a , b


'''
n, m, a, b = map(int, input("").split())
cost1 = n * a
cost2 = ((n + m - 1) // m) * b
cost3 = (n // m) * b + (n % m) * a
print(min(cost1, cost2, cost3))
