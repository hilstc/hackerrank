#Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

#    If a[i] > b[i], then Alice is awarded 1 point.
#    If a[i] < b[i], then Bob is awarded 1 point.
#    If a[i] = b[i], then neither person receives a point.

# Comparison points is the total points a person earned.

# Given a and b, determine their respective comparison points. 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
        
    def check_points(array):
        # Initialize both players with 0 points.
        alice_points = 0
        bob_points = 0
        
        for i in range(len(array)):
            # If both have the same score, neither receives a point.
            if a[i] == b[i]:
                pass
                
            # If Alice has a bigger value, she receives a point
            elif a[i] > b[i]:
                alice_points += 1
                
            # If the values are not equal and Alice's value is not bigger, then Bob's value is bigger and he receives a point.
            else:
                bob_points += 1
                
        return alice_points, bob_points
        
# Checks if the arrays have the same length in order to verify how long the iteration should be. If they are the same length or if "a" is shorter, "a"'s length is used; "b"'s is used otherwise.
    if len(a) <= len(b):
        alice, bob = check_points(a)
        
    else:
        alice, bob = check_points(b)
            
    # Creates an array to add Alice's and Bob's scores, respectively.
    final_score = []
    
    final_score.append(alice)
    final_score.append(bob)
    
    return final_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()