'''
cards numbered 1-10
each 2 card , turn based 
'''
t = int(input())
results = []
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    suneet_wins = 0
    suneet_score = (a1 > b1) + (a2 > b2)
    slavic_score = (a1 < b1) + (a2 < b2)
    if suneet_score > slavic_score:
        suneet_wins += 1
   
    suneet_score = (a1 > b2) + (a2 > b1)
    slavic_score = (a1 < b2) + (a2 < b1)
    if suneet_score > slavic_score:
        suneet_wins += 1
    suneet_score = (a2 > b1) + (a1 > b2)
    slavic_score = (a2 < b1) + (a1 < b2)
    if suneet_score > slavic_score:
        suneet_wins += 1
    suneet_score = (a2 > b2) + (a1 > b1)
    slavic_score = (a2 < b2) + (a1 < b1)
    if suneet_score > slavic_score:
        suneet_wins += 1
    
    results.append(suneet_wins)

for result in results:
    print(result)
