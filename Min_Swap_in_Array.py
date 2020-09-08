# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:08:29 2020

@author: siva
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    #create a dictionary which holds value, index pairs of our array
    #[4,3,1,2] --> {4: 1, 3: 2, 1: 3, 2: 4}
    getIndex = dict(zip(arr,range(1,len(arr)+1)))
    for i in range(1,len(arr)+1):
        #swap only if value is not equal to index
        if getIndex[i]!=i: 
            """
            Example of a proper swap when i=1
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 1, 2: 4}
            [4,3,1,2] --> [1,3,4,2]
            Full swap is not required i.e. we don't have to set 1:1 or arr[0]=1(i:i or arr[i-1]=i) because we will never use these two values again. Therefore we can keep these two values as it is. And thus our swap looks as follows.
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 3, 2: 4}
            [4,3,1,2] --> [4,3,4,2]
            """
            getIndex[arr[i-1]]=getIndex[i]
            #print(getIndex)
            arr[getIndex[i]-1]=arr[i-1]
            
            swaps+=1
    print(getIndex)
    return swaps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(f'answer is {res}')

    #fptr.write(str(res) + '\n')

   # fptr.close()
