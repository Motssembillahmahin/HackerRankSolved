import math
import os
import random
import re
import sys
# Complete the time_delta function below.
from datetime import datetime
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    difference = datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)
    return str(int(abs(difference.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()