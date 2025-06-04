#!/bin/python3

import math
import os
import random
import re
import sys

month_map = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def count_leap_years(y, m):
    if m <= 2:
        y -= 1
    return y // 4 - y // 100 + y // 400

days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]

def parse_time_string(s):
    parts = s.split()
    day = int(parts[1])
    month = month_map[parts[2]]
    year = int(parts[3])
    time_parts = list(map(int, parts[4].split(":")))
    hour, minute, second = time_parts
    offset = parts[5]

    total_days = year * 365 + day
    for m in range(1, month):
        total_days += days_in_month[m - 1]

    total_days += count_leap_years(year, month)

    total_sec = total_days * 24 * 3600 + hour * 3600 + minute * 60 + second

    offset_sign = 1 if offset[0] == '+' else -1
    offset_hours = int(offset[1:3])
    offset_minutes = int(offset[3:])
    offset_seconds = offset_sign * (offset_hours * 3600 + offset_minutes * 60)

    return total_sec - offset_seconds

# Complete the time_delta function below.
def time_delta(t1, t2):
    diff_sec = abs(parse_time_string(t1) - parse_time_string(t2))
    return str(diff_sec)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
