def best_possible_ranking(N, D, Sk, Pk):
    # The astronaut we're interested in
    astronaut_points = Sk[D - 1]
    # New points after winning the next race
    new_points = astronaut_points + Pk[0]

    # Calculate new points for all astronauts if they finish at the worst possible position
    new_scores = [Sk[i] + Pk[-(i+1)] for i in range(N)]
    
    # Insert the astronaut's new score in the new_scores list
    new_scores[D - 1] = new_points
    
    # Sort in descending order to determine the rank
    new_scores.sort(reverse=True)

    # Find the best rank by checking the position of the astronaut's new points
    best_rank = new_scores.index(new_points)
    
    return best_rank

# Taking input from the user
N, D = map(int, input().split())
Sk = list(map(int, input().split()))
Pk = list(map(int, input().split()))

# Calculating the best possible ranking
result = best_possible_ranking(N, D, Sk, Pk)

# Output the result
print(result)
#re