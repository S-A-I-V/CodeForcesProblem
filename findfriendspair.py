'''
user a sends message to b at t1
user b sends message to a at t2
0<=t2-t1<=d - then a and b are friends
 
atleast one asnwere from a to b then friends
 
approach- 
n = logs of total messages
(a, b):time
'''
def find_friends(n, d, messages):
    timedict = {}
    friends = set()
    
    for a, b, time in messages:
        if (b, a) in timedict:
            last_times = timedict[(b, a)]
            for last_time in last_times:
                if 0 < time - last_time <= d:
                    friends.add(tuple(sorted((a, b))))
                    break  
        
        if (a, b) not in timedict:
            timedict[(a, b)] = []
        timedict[(a, b)].append(time)

    friend_list = sorted(friends)
    return friend_list

n, d = map(int, input().split())
messages = [input().split() for _ in range(n)]
messages = [(a, b, int(time)) for a, b, time in messages]
friend_pairs = find_friends(n, d, messages)

print(len(friend_pairs))
for pair in friend_pairs:
    print(pair[0], pair[1])
