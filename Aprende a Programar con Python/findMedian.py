

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()
    
    medianIndex = int((len(arr)/2) - 0.5)
    
    return arr[medianIndex]

    
    

if __name__ == '__main__':
    

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(result)