import math
import os
import random
import re
import sys
from operator  import itemgetter


if __name__== 'main':
    nm = input().split()
    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    r = sorted(arr, key=itemgetter(k))
    for i in r:
        print(*i)