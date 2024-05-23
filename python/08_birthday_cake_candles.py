# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest. 
#
#Sample Input:

#4
#3 2 1 3

#Sample Output 

#2

#Explanation

#Candle heights are [3, 2, 1, 3]. The tallest candles are 3 units, and there are 2 of them.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    
    # Finds the maximum value in the array
    tallest_candle = max(candles)
    # Will count the number of occurrences of the maximum value in the array
    quantity = 0
    
    # Iterates through the array and adds 1 to "quantity" if a candle of maximum size is found.
    for candle in candles:
        if candle == tallest_candle:
            quantity += 1
           
    return quantity

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
