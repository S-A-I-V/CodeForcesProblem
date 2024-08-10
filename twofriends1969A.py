'''
n friends, atleast 2 of them o be present
ith friend in 1-n list is friend of pi.
ith friend will come to party if pi gets invitation

but pi isnt bound to come
i= 1 2 3 4 5
p= x y z a b
p= 3 1 2 5 4
dict- [3:1; 1:2; 2:3; 5:4; 4:5]
if (a,b) and (b,a) in dict then minnoofinv+=2

min invites- 2 friends can come

2 3 4 1
1 2 3 4 
'''
def min_invitations(n, p):
    """
    Calculate the minimum number of invitations Monocarp has to send so that at least 2 friends come to the party.

    Args:
        n (int): The number of friends.
        p (list): A list of integers representing the best friend of each friend.

    Returns:
        int: The minimum number of invitations Monocarp has to send.
    """
    # Create a dictionary to store the best friend of each friend
    friends = {i+1: pi for i, pi in enumerate(p)}

    # To keep track of mutual best friends
    mutual_pairs = set()
    visited = set()

    # Find all mutual best friend pairs
    for i in range(1, n+1):
        if i not in visited:
            best_friend = friends[i]
            if friends.get(best_friend) == i:
                pair = tuple(sorted((i, best_friend)))
                mutual_pairs.add(pair)
                visited.add(i)
                visited.add(best_friend)

    # Calculate the minimum number of invitations needed
    if mutual_pairs:
        # If there are mutual best friend pairs, each pair requires 2 invitations
        min_invites = 2 * len(mutual_pairs)
    else:
        min_invites = 2

    return min_invites
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(min_invitations(n, p))
