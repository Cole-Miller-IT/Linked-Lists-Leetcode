#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER x as parameter.
#

def calculate(x):
    if x < 1 or x > 1000:
        print("outside range")
        return 0
        
    else:
        #Calculate
        print(x)
        result = (x % 11)
        
        print(result)
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    result = calculate(x)

    fptr.write(str(result) + '\n')

    fptr.close()
