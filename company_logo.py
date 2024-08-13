import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    my_list = [(s.count(char), char) for char in set(s)]
    sorted_list = sorted(my_list, key=lambda x:(-x[0], x[1]))
    for count, char in sorted_list[:3]:
        print(f"{char} {count}")

    

