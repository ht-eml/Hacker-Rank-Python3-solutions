#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    result = []
    for element in range(len(arr)):
        temp = sum(arr) - arr[element]
        result.append(temp)
    print(min(result), max(result))



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
