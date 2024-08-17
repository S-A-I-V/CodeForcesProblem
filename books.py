'''
t free mins to read
n books

prefix sum

'''
n, t = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]

max_books = 0

j = 0
for i in range(1, n + 1):
    while j < n and prefix[j + 1] - prefix[i - 1] <= t:
        j += 1
    max_books = max(max_books, j - (i - 1))
print(max_books)
