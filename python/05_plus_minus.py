# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    # Adds number of positive and negative values and zeros
    positive = 0
    negative = 0
    zero = 0
    
    # Checks if the value is positive, negative or zero and adds 1 to their respective variables in order to know how many of each there are in the array.
    for value in arr:
        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            zero += 1
    
    # Divides the number of positive and negative values and zeros by the number of elements in the array in order to obtain the proportion each value in it.
    proportion_positive = positive/len(arr)
    # Rounds the proportion to the 6th decimal.
    rounded_positive = round(proportion_positive, 6)
    
    proportion_negative = negative/len(arr)
    rounded_negative = round(proportion_negative, 6)
    
    proportion_zero = zero/len(arr)
    rounded_zero = round(proportion_zero, 6)
    
    print(rounded_positive)
    print(rounded_negative)
    print(rounded_zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
