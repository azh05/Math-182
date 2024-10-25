#!/usr/bin/python3 
from itertools import combinations
import math

# get all subsets size k of the set of tuples size n
# returns a list of subsets (lists with tuples)
# The runtime is O(n^k), because we need k for loops that each run n times to get the combinations
def get_combinations(L, k):
    return list(combinations(L, k))

def solution(L, k):
    k_subsets = get_combinations(L, k)
    # minimize the maximum minimum distance of a point to any center

    min_max_min_dist = 10*10
    optimal_subset = None

    for centers in k_subsets:
        max_min_dist = -1
        for p in L:
            # find the minimum distance of point p in P to a c in centers
            min_dist = 10**10
            
            for c in centers:
                min_dist = min(math.dist(p, c), min_dist)

            max_min_dist = max(max_min_dist, min_dist)

        if(min_max_min_dist > max_min_dist):
            min_max_min_dist = max_min_dist 
            optimal_centers = centers

    return min_max_min_dist, optimal_centers

            
def main():
    input_list = [(1, 2), (2, 3), (4, 1), (2, 1), (4, 5), (7, 2)]
    k = 3

    print(solution(input_list, k))



if __name__ == '__main__':
    main()
