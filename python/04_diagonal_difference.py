# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    # Values to iterate through the indexes of the values in each row of the matrix
    # right_left_count starts from the last value of the row and goes up to the value of index 0. left_right_count starts from the first value and goes up to the last value of the row.
    right_left_count = -1
    left_right_count = 0
    
    # Store the values of each diagonal.
    right_left_diagonal = []
    left_right_diagonal = []
    
    # Iterates over the length of the matrix.
    for row in range(len(arr)):
        
        # Adds the value of the current index of right_left_count to the right_left_diagonal list.
        right_left_diagonal.append(arr[row][right_left_count])
          # Adds the value of the current index of left_right_count to the left_right_diagonal list.
        left_right_diagonal.append(arr[row][left_right_count])
        
        # Subtracts 1 from the right_left_count in order to access the next index in the list in the right to left order. 
        right_left_count -= 1
        # Adds 1 to the left_right_count in order to access the next index in the list in the left to right order.
        left_right_count += 1
    
    # Returns the absolute value from the difference between each diagonal's sum.
    total = abs(sum(left_right_diagonal) - sum(right_left_diagonal))
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()