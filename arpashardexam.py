n = int(input())
cycle = [6, 8, 4, 2]
if n == 0:
    print(1)
else:
    print(cycle[n % 4])
