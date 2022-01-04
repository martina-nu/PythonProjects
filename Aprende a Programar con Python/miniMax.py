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
    # Write your code here
    arr.sort() # se ordenan los numeros
    minimo = sum(arr[0:4]) # se eligen los primeros 4 (los más altos)
    maximo = sum(arr[1:5]) # se eligen los otros cuatro menos el más alto
    
    print(minimo, maximo)
   
   
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
