import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_script = ""

for i in range(m):
    for j in range(n):
        decoded_script += matrix[j][i]

pattern = r'(\w)\W+(\w)'
result = re.sub(pattern, r'\1 \2', decoded_script)

print(result)


