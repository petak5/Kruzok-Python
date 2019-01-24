#!/bin/python3

# NOT WORKING PROPERLY

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/picking-numbers/problem
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    my_dict = {0: [a[0]]}
    counter = 0
    for i in range(1, len(a)):
        if abs(a[i-1] - a[i]) <= 1:
            my_dict[counter].append(a[i])
        else:
            counter = counter + 1
            if counter not in my_dict:
                my_dict[counter] = [a[i]]
            else:
                my_dict[counter].append(a[i])
    maximum = 0
    for i in range(len(my_dict)):
        if len(my_dict[i]) > maximum:
            maximum = len(my_dict[i])
    print(my_dict)
    return maximum


n = int(input().strip())
a = list(map(int, input().rstrip().split()))

result = pickingNumbers(a)

print(result)