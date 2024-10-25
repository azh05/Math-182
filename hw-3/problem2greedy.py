#!/usr/bin/python3

import math
import random

def solution(L, k):
    # Choose a random starting point
    random.seed(10)

    n = len(L)
    startIdx = random.randint(0, n - 1)
    start = L[startIdx]
    
    centers = [start]


    # until we have k centers, loop and find the point furthest from all the points in centers
    while(len(centers) < k):
        max_min_dist = -1
        new_center = None

        for point in L:
            min_dist_to_c = 10**10

            # loop through all the centers currently in our list
            for c in centers:
                # print(c, point)
                # calculate the distance of the point to the center
                min_dist_to_c = min(min_dist_to_c, math.dist(c, point))
           
            # print(min_dist_to_c, max_min_dist)
            if(max_min_dist < min_dist_to_c):
                max_min_dist = min_dist_to_c
                new_center = point

        # print(new_center)
        # print(max_min_dist)
        centers.append(new_center)
        # min_max_min_dist = min(min_max_min_dist, max_min_dist)

    # Calculating the maximum of the distance between a point and its closest center 
    max_min = 0

    for point in L:
        min_dist = 10**10
        for center in centers:
            min_dist = min(min_dist, math.dist(point, center))

        max_min = max(min_dist, max_min)

    return max_min, centers




def main():
    input_list = [(1, 2), (2, 3), (4, 1), (2, 1), (4, 5), (7, 2)]
    k = 3

    print(solution(input_list, 3))

if __name__ == '__main__':
    main()
