t = int(input())
numbers = [int(input()) for _ in range(t)]
sums = [(n // 10) + (n % 10) for n in numbers]
for s in sums:
    print(s)
