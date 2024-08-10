'''
n lines describing one goal
marked with one goal scored by that team



'''
n = int(input())
goals = {}

for _ in range(n):
    team = input().strip()
    if team in goals:
        goals[team] += 1
    else:
        goals[team] = 1
winner = max(goals, key=goals.get)
print(winner)
