#!/usr/bin/python3

import math

def solution(L):
    n = len(L)
    min_dist = 10**10
    min_tuple_list = []
    for i in range(n):
        for j in range(i+1, n):
            if min_dist > math.dist(L[i], L[j]):
                min_dist = math.dist(L[i], L[j])
                min_tuple_list = [L[i], L[j]]

    return min_dist, min_tuple_list

def main():
    L = [(1, 1), (2, 3), (4, 1), (5, -1), (8, -5), (7, 5), (-3, 2), (-5, 0)]

    print(solution(L))

if __name__ == "__main__":
    main()
