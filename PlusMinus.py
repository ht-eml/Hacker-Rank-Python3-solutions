import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive = []
    negative = []
    zeros = []
    for element in arr:
        if element > 0:
            positive.append(element)
        elif element < 0:
            negative.append(element)
        else:
            zeros.append(element)
    print(round(len(positive) / len(arr), 6))
    print(round(len(negative) / len(arr), 6))
    print(round(len(zeros) / len(arr), 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
