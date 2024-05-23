#
#Staircase detail

#This is a staircase of size n:

#    #
#   ##
#  ###
# ####

#Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):

    # Loops n times in other to print the right number of steps.
    for i in range(n):
        
        # The index will start at 0, when we will have one hash printed, thus we will start at i + 1 ( = 1 hash) and increase the number of hashes in each loop.
        hashes = i + 1
        
        # Prints spaces to a value lower than the current number of hashes.
        spaces = (n - hashes)
        
        # Calculates the number of spaces and hashes and adds them to the string.
        string = (" " * spaces) + ("#" * hashes)
        
        print(string)
        
        
        
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)