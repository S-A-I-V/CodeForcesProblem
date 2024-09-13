'''
ith price is i+1



'''
import sys
import math

def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False

    for i in range(4, limit + 1, 2):
        prime[i] = False

    for i in range(3, int(math.sqrt(limit)) + 1, 2):
        if prime[i]:
            for j in range(i * 2, limit + 1, i):
                prime[j] = False

    return prime

n = int(input())
prime = sieve(n + 1)

pr, npr = 0, 0
for i in range(2, n + 2):
    if prime[i]:
        pr += 1
    else:
        npr += 1

if npr == 0:
    print(1)
else:
    print(2)

for i in range(2, n + 2):
    if prime[i]:
        print(1, end=' ')
    else:
        print(2, end=' ')
