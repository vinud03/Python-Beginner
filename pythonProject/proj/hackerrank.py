'''

Sub array sum

'''




#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    print(numbers)
    j = len(queries)
    ls1 = queries[0]

    if j > 2:
        ls2 = queries[1]

    for i in range(0, j):

        if i == 0:
            m = ls1[0] - 1
            n = ls1[1] - 1
            sum1 = numbers[m] + numbers[n]
            if n == 0 or m == 0:
                sum1 += 10
            return ({sum1})
        if i == 1:
            m = ls2[0] - 1
            n = ls2[1] - 1
            sum2 = numbers[m] + numbers[n]
            if numn == 0 or m == 0:
                sum2 += 10
            return ('%d', sum2)

    # return ('{sum1}{sum2}')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
