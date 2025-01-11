n, k= map(int, input().split())
available = 240 - k
timespent=0
probs=0
for i in range(1, n+1):
    timespent += 5*i
    if timespent <= available:
        probs += 1
    else:
        break

print(probs)