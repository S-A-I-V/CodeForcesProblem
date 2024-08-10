'''
kiritostrength = s
ith dragon, n dragons, xi is dragon strength


if duel - s<xi (kirit dies)
if duel - s>xi (kirito wins)- s+yi

'''
s, n = map(int, input().split())
dragons = []
for _ in range(n):
    xi, yi = map(int, input().split())
    dragons.append((xi, yi))
dragons.sort()

for xi, yi in dragons:
    if s > xi:
        s += yi  
    else:
        print("NO")
        exit()

print("YES")
