#!/usr/bin/python3 

import math
from operator import itemgetter

# initally sort the list by x and y separately
# Px is L sorted by the x element in the tuple
# Py is L sorted by the y element 
def initial_sort(L):
    Px = sorted(L, key=itemgetter(0))
    Py = sorted(L, key=itemgetter(1))

    return Px, Py

# Recurse to calculate the minimum distance of the left side, right side, and the middle
# the values to check in the middle are decided by taking the minimum distance of the left and right sides
# +/- the mid point of the whole set 
def recurse(Px, Py):

    # if the size of the set is less than or equal to 3, don't recurse anymore and find the minimum of the points
    n = len(Px)
    if n <= 3:
        min_dist = 10**10
        min_tuple_list = []

        # At max, 3 operations, so O(1)
        for i in range(n):
            for j in range(i+1, n):
                cur_dist = math.dist(Px[i], Px[j])
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    min_tuple_list = [Px[i], Px[j]]

        return min_tuple_list
    
    # otherwise, we want to split up the set into left and right sections and recurse 
    ## Find the mid point on the x axis 
    xmid = Px[math.ceil(n / 2)]
    
    ## Let Q represent the left side, and R represent the right side 
    ## Define Qx as the left side of Px and Rx as the right side of Px
    ## Define Qy as the left side of Px sorted by y and Ry as the right side of Px sorted by y
    Qx = []
    Qy = []
    Rx = []
    Ry = []

    # This loop guarantees that all the sets defined above are sorted using the fact that 
    # Px and Py are sorted. This is O(n) time because we are simply looping through P and Q
    for i in range(n):
        xxval = Px[i][0]
        yxval = Py[i][0]
        # print(Px[i], Py[i])

        if xxval < xmid[0]:
            Qx.append(Px[i])
        else:
            Rx.append(Px[i])

        if yxval < xmid[0]:
            Qy.append(Py[i])
        else:
            Ry.append(Py[i])

    # Recurse on the left and right sides and get the tuples with minimum distances for both
    min_tuples_Q = recurse(Qx, Qy)
    min_tuples_R = recurse(Rx, Ry)

    min_dist_tuples = None
    if math.dist(min_tuples_Q[0], min_tuples_Q[1]) <  math.dist(min_tuples_R[0], min_tuples_R[1]):
        min_dist_tuples = min_tuples_Q
        min_dist_QR = math.dist(min_tuples_Q[0], min_tuples_Q[1]) 
    else: 
        min_dist_tuples = min_tuples_R
        min_dist_QR = math.dist(min_tuples_R[0], min_tuples_R[1])

    # Now check for distances where one element is in Q and the other is in R for 
    # elements close to the middle of the Q U R, close is determined by midpoint.x +/- min_dist_QR 
    xmidbottom = xmid[0] - min_dist_QR 
    xmidtop = xmid[0] + min_dist_QR

    # Filter the elements in Py that are not in this range
    Py_filtered = [t for t in Py if t[0] >= xmidbottom and t[0] <= xmidtop]
    
    # find the minimum distance in Py_filtered, by looping through 
    # This is also O(n) since Py_filtered is sorted 
    min_dist_Py_filtered = 10**10
    min_dist_tuples_Py = []

    for i in range(1, len(Py_filtered)):
        cur_dist = math.dist(Py_filtered[i - 1], Py_filtered[i])
        if cur_dist < min_dist_Py_filtered:
            min_dist_tuples_Py = [Py_filtered[i - 1], Py_filtered[i]]
            min_dist_Py_filtered = cur_dist

    # Finally compare the between with the left/right 
    if min_dist_Py_filtered < min_dist_QR:
        return min_dist_tuples_Py
    
    return min_dist_tuples


def solution(L):
    Px, Py = initial_sort(L)
    return recurse(Px, Py)

def main():
    L = [(1, 1), (2, 3), (4, 1), (5, -1), (8, -5), (7, 5), (-3, 2), (-5, 0)]

    min_dist_tuples = solution(L)
    print(math.dist(min_dist_tuples[0], min_dist_tuples[1]), min_dist_tuples)

if __name__ == "__main__":
    main()
