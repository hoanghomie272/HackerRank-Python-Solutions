#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)
    time_difference = time1 - time2
    return abs(int(time_difference.total_seconds()))


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)


