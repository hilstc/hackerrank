# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Sorts the array in a crescent order.
    sorted_array = sorted(arr)
    
    # Gets the sum of the sorted array and subtracts the last (and bigger) value
    minimum = sum(sorted_array) - sorted_array[-1]
    # Gets the sum of the sorted array and subtracts the first (and smaller) value
    maximum = sum(sorted_array) - sorted_array[0]
    
    print(minimum, maximum)
    
    

if __name__ == '__main__':

    arr = list(map(int, input("Insert integers separated by spaces: ").rstrip().split()))

    miniMaxSum(arr)