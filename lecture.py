n, m = map(int, input().split())
correspondingdict = {}

for _ in range(m):
    a, b = input().split()
    correspondingdict[a] = b

lecture = input().split()
result = []

for word in lecture:
    if len(word) <= len(correspondingdict[word]):
        result.append(word)
    else:
        result.append(correspondingdict[word])

print(' '.join(result))
